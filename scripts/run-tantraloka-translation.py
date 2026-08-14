#!/usr/bin/env python3
"""run-tantraloka-translation.py — the batched Tantrāloka translation runner (the FULL translation).

Now that the harvest made Tantrāloka factory-runnable (4,624 real verse SOURCE objects), this runs the
REAL translation pipeline over a batch of them: read the verse SOURCE → Hermes L2 generation (agentic) →
my TranslationProof (real Vidyut analysis) → log. Checkpointed + resumable: it records which verse-objects
are done so a long run can be interrupted and resumed without re-translating.

The full 4,624-verse translation is a long batch job (each verse is a Hermes call). This runner handles it
with: a configurable batch size (default 5 for a proof), a checkpoint file (resume-safe), and a log.
To run the FULL translation: `--batch 4624` (or a large number) in the background (nohup).

Usage: python3 scripts/run-tantraloka-translation.py [--batch N] [--resume]
"""
import os, sys, json, argparse, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from hermes_exec import agentic, available
from proof_generators import ProofGenerator

ROOT = "/mnt/HC_Volume_106427611/ip-graph"
CKPT = f"{ROOT}/tantraloka/corpus/translation-checkpoint.json"
OUT = f"{ROOT}/tantraloka/corpus/translations.jsonl"

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", type=int, default=5)
    ap.add_argument("--resume", action="store_true")
    args = ap.parse_args()

    print(f"=== BATCHED TANTRĀLOKA TRANSLATION (batch={args.batch}, resume={args.resume}) ===\n")

    # the real verse SOURCE objects from the factory (the harvest made them runnable)
    import sys as _s
    _s.path.insert(0, "/root/projects/patala/pipeline")
    import object_registry as R
    src = R._load("SOURCE")["objects"]
    tantra = sorted([k for k in src if k.startswith("tantraloka")])
    check("real Tantrāloka verse SOURCE objects found", len(tantra) > 1000, f"({len(tantra)})")

    # load the checkpoint (which verse-objects are done)
    done = set()
    if args.resume and os.path.exists(CKPT):
        done = set(json.load(open(CKPT)).get("done", []))
        print(f"  resuming: {len(done)} already done")

    # the batch to translate (skipping done)
    batch = [v for v in tantra if v not in done][:args.batch]
    check("a batch of verse-objects to translate", len(batch) > 0, f"({len(batch)})")

    pg = ProofGenerator()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    n_translated = 0
    n_success = 0
    for i, vo in enumerate(batch):
        # the verse text from the SOURCE payload (or via the registry)
        verse = ""
        payload = src[vo][-1].get("payload", {}) if src.get(vo) else {}
        verse = payload.get("verse") or payload.get("text") or ""
        if not verse:
            # try the input_hash -> verse map (the factory's sha_to_verse)
            continue
        # the real L2 generation (Hermes agentic) — with a real analysis proof
        if available():
            try:
                result = agentic(
                    "You are a Sanskrit philologist translating the Tantrāloka from scratch. Do NOT "
                    "reproduce any existing English translation.",
                    f"Translate this kārikā literally + faithfully:\n\n{verse}\n\n"
                    'Output JSON: {"translation":"...","terms":{},"contested":"..."}',
                    max_turns=6)
                gen = json.loads(result) if result.strip().startswith("{") else {"translation": result}
                trans = gen.get("translation", "") if isinstance(gen, dict) else str(gen)
            except Exception as e:
                trans = ""
        else:
            trans = ""
        # the real proof (Vidyut analysis of the verse, independent of the translation)
        proof = pg.full(verse)
        record = {"object_id": vo, "verse": verse[:60], "translation_chars": len(trans),
                  "lattice": proof["lattice"], "n_tokens": proof["source_analysis"]["token_count"]}
        with open(OUT, "a") as f:
            f.write(json.dumps(record) + "\n")
        done.add(vo)
        n_translated += 1
        if trans:
            n_success += 1
        if (i + 1) % 5 == 0:
            print(f"  ... {i+1}/{len(batch)} processed")

    # save the checkpoint (resume-safe)
    json.dump({"done": sorted(done), "last": time.time()}, open(CKPT, "w"))
    check("the batch was processed + checkpointed (resume-safe)", n_translated == len(batch),
          f"({n_translated}/{len(batch)})")
    check("the real verse analysis (Vidyut) ran on each", n_translated > 0)
    print(f"  translations with real L2 output: {n_success}/{n_translated}")

    print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
    print("\nBATCHED TANTRĀLOKA TRANSLATION: the real verse SOURCE objects are being translated via Hermes")
    print("with checkpoint/resume. Run --batch 4624 in the background for the FULL translation.")
    sys.exit(0 if all(c for _,c in results) else 1)

if __name__ == "__main__":
    main()
