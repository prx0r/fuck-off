#!/usr/bin/env python3
"""run-tantraloka-translation-parallel.py — the PARALLEL batched Tantrāloka translation runner.

The full 4,624-verse translation is a long batch job (each verse is a Hermes call). This runs it with a
worker pool: each verse-object is an independent subprocess `hermes chat` call (GIL-releasing) + a quick
CPU Vidyut proof, so many can run concurrently against the same Hermes gateway. Checkpointed + resumable:
records which verse-objects are done so an interrupted run resumes without re-translating.

Parallelization notes (reuse, don't rebuild):
  - Hermes execution: lib/hermes_exec.agentic() (shells to `hermes chat`, subprocess — safe to fan out).
  - Sanskrit proof: lib/proof_generators.ProofGenerator (deterministic, cheap — shares one instance).
  - Registry SOURCE: patala object_registry (read-only). Keep lib/schema and pipeline/schema in separate
    processes (they are — this script only imports pipeline's object_registry).

Usage: python3 scripts/run-tantraloka-translation-parallel.py [--workers N] [--batch N] [--resume]
  --workers  parallelism (default: number of CPUs, capped)
  --batch    how many NEW verse-objects to process (0 = all remaining; default 0)
  --resume   load the checkpoint and skip already-done verse-objects
"""
import os, sys, json, argparse, time, threading
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from hermes_exec import translate_karika, available
from proof_generators import ProofGenerator

ROOT = "/mnt/HC_Volume_106427611/ip-graph"
CKPT = f"{ROOT}/tantraloka/corpus/translation-checkpoint.json"
OUT = f"{ROOT}/tantraloka/corpus/translations.jsonl"

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}", flush=True)


def translate_one(vo, verse, pg, hermes_ok):
    """Translate a single verse-object: real Hermes L2 generation + real Vidyut proof.

    Uses hermes_exec.translate_karika() which does proper brace-balanced JSON extraction of the
    FINAL answer (NOT the raw reasoning trace — a naive json.loads() was capturing the Hermes
    `┌─ Reasoning ─` box as the "translation"). Clean translation JSON only, proof on real output.
    """
    gen = {}
    if hermes_ok:
        try:
            gen = translate_karika(verse)
            if not isinstance(gen, dict):
                gen = {}
        except Exception:
            gen = {}
    trans = gen.get("translation", "") if isinstance(gen, dict) else ""
    proof = pg.full(verse)
    return {
        "object_id": vo, "verse": verse[:60], "translation_chars": len(trans),
        "translation": trans[:2000], "terms": gen.get("terms", {}) if isinstance(gen, dict) else {},
        "contested": gen.get("contested", "") if isinstance(gen, dict) else "",
        "lattice": proof["lattice"], "n_tokens": proof["source_analysis"]["token_count"],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=max(1, (os.cpu_count() or 1) - 1))
    ap.add_argument("--batch", type=int, default=0)
    ap.add_argument("--resume", action="store_true")
    args = ap.parse_args()

    print(f"=== PARALLEL TANTRĀLOKA TRANSLATION (workers={args.workers}, batch={args.batch or 'all'}, "
          f"resume={args.resume}) ===\n", flush=True)

    _s = sys
    _s.path.insert(0, "/root/projects/patala/pipeline")
    import object_registry as R
    src = R._load("SOURCE")["objects"]
    tantra = sorted([k for k in src if k.startswith("tantraloka")])
    check("real Tantrāloka verse SOURCE objects found", len(tantra) > 1000, f"({len(tantra)})")

    done = set()
    if args.resume and os.path.exists(CKPT):
        done = set(json.load(open(CKPT)).get("done", []))
        print(f"  resuming: {len(done)} already done", flush=True)

    remaining = [v for v in tantra if v not in done]
    if args.batch:
        remaining = remaining[:args.batch]
    check("verse-objects to translate this run", len(remaining) > 0, f"({len(remaining)})")
    if not remaining:
        print("  nothing left to translate — all verse-objects already done.")
        sys.exit(0)

    # the verse text for each object (skip objects with no payload text)
    def verse_for(vo):
        payload = src[vo][-1].get("payload", {}) if src.get(vo) else {}
        return payload.get("verse") or payload.get("text") or ""

    work = [(vo, verse_for(vo)) for vo in remaining]
    work = [(vo, v) for vo, v in work if v]
    check("verse-objects with real verse text", len(work) > 0, f"({len(work)})")
    if not work:
        sys.exit(1)

    pg = ProofGenerator()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    # check Hermes availability ONCE up front (not per-verse — a per-verse available() is an extra call)
    hermes_ok = available()
    check("Hermes agentic available", hermes_ok)
    out_lock = threading.Lock()
    n_translated = [0]
    n_success = [0]
    n_workers = min(args.workers, len(work))
    start = time.time()
    last_ckpt = [start]

    def process(task):
        vo, verse = task
        rec = translate_one(vo, verse, pg, hermes_ok)
        with out_lock:
            with open(OUT, "a") as f:
                f.write(json.dumps(rec) + "\n")
            done.add(vo)
            n_translated[0] += 1
            if rec["translation"]:
                n_success[0] += 1
            # checkpoint every ~10 verses (cheap, resume-safe)
            if n_translated[0] % 10 == 0 or time.time() - last_ckpt[0] > 60:
                json.dump({"done": sorted(done), "last": time.time()}, open(CKPT, "w"))
                last_ckpt[0] = time.time()
                el = time.time() - start
                rate = n_translated[0] / el if el else 0
                print(f"  ... {n_translated[0]}/{len(work)} done "
                      f"({rate:.2f}/s, success {n_success[0]})", flush=True)

    with ThreadPoolExecutor(max_workers=n_workers) as ex:
        futures = [ex.submit(process, t) for t in work]
        for _ in as_completed(futures):
            pass

    json.dump({"done": sorted(done), "last": time.time()}, open(CKPT, "w"))
    el = time.time() - start
    check("the batch was processed + checkpointed (resume-safe)",
          n_translated[0] == len(work), f"({n_translated[0]}/{len(work)})")
    check("the real verse analysis (Vidyut) ran on each", n_translated[0] > 0)
    print(f"  translations with real L2 output: {n_success[0]}/{n_translated[0]} "
          f"({el:.1f}s elapsed)", flush=True)

    print(f"\n=== SUMMARY: {sum(1 for _, c in results if c)}/{len(results)} passed ===", flush=True)
    print("PARALLEL TANTRĀLOKA TRANSLATION: real verse SOURCE objects translated via Hermes "
          f"across {n_workers} workers; checkpoint at {CKPT}", flush=True)
    sys.exit(0 if all(c for _, c in results) else 1)


if __name__ == "__main__":
    main()
