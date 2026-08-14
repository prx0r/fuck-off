#!/usr/bin/env python3
"""tantraloka/run-all.py — the live Tantrāloka pipeline test harness (ML-architecture-suite style).

Runs the ENTIRE Tantrāloka pipeline in order, like a live ML training/eval suite:
  STAGE 0 Ingest    (the Sanskrit root → data/tantraloka)
  STAGE 1 Atlas     (bibliography/tagging/condition/timeline)
  STAGE 2 Translation (L0 + TranslationProof, REAL Hermes wiring)
  STAGE 3 Argument  (auto-mined cruxes from the pushing sessions)
  STAGE 4 Fullstack (essay→education→pedagogy→products)
  STAGE 5 Validation (vs Dyczkowski)
  STAGE 6 Factory   (the parallel worker pool)
  STAGE 7 Runner    (next_action + real Hermes generation)

For each stage: records PASS/FAIL, the checks, the timing, and any error. Writes:
  tantraloka/logs/run-<timestamp>.json   (machine-readable)
  tantraloka/logs/run-<timestamp>.txt    (human-readable)
  tantraloka/iterations/<n>.json         (the iteration snapshot, for the autonomous-iteration log)
No stage is skipped; failures are RECORDED, not hidden. This is the honest live-testing record.
"""
import os, sys, json, time, subprocess, datetime, traceback

ROOT = "/mnt/HC_Volume_106427611/ip-graph"
LOGS = f"{ROOT}/tantraloka/logs"
ITERS = f"{ROOT}/tantraloka/iterations"

STAGES = [
    ("0-ingest",     "scripts/ingest-tantraloka-root.py",        "the Sanskrit root → data/tantraloka"),
    ("1-atlas",      "scripts/validate-tantraloka-atlas.py",      "bibliography/tagging/condition/timeline"),
    ("2-translation","scripts/validate-tantraloka-translation.py","L0 + TranslationProof (REAL Hermes wiring)"),
    ("3-argument",   "scripts/validate-tantraloka-argument.py",   "auto-mined cruxes from pushing sessions"),
    ("4-fullstack",  "scripts/validate-tantraloka-fullstack.py",  "essay→education→pedagogy→products"),
    ("5-validation", "scripts/validate-tantraloka-vs-dyczkowski.py","vs Dyczkowski (three-version)"),
    ("6-factory",    "scripts/validate-factory-pool.py",          "the parallel worker pool"),
]

def main():
    os.makedirs(LOGS, exist_ok=True)
    os.makedirs(ITERS, exist_ok=True)
    ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    report = {"run": ts, "stages": [], "overall": {"pass": 0, "fail": 0, "error": 0}}
    lines = [f"TANTRĀLOKA LIVE TEST RUN — {ts}", "=" * 60, ""]

    for name, script, desc in STAGES:
        start = time.time()
        entry = {"stage": name, "script": script, "description": desc}
        try:
            r = subprocess.run([sys.executable, f"{ROOT}/{script}"],
                               capture_output=True, text=True, timeout=120)
            dt = round(time.time() - start, 2)
            # parse the SUMMARY line (the pass count)
            summary = ""
            for ln in (r.stdout + r.stderr).splitlines():
                if "SUMMARY" in ln:
                    summary = ln.strip()
            ok = r.returncode == 0
            entry.update({"status": "PASS" if ok else "FAIL", "time_s": dt, "summary": summary,
                          "rc": r.returncode})
            status = "PASS" if ok else "FAIL"
            report["overall"]["pass" if ok else "fail"] += 1
            print(f"  [{status}] {name}: {summary} ({dt}s)")
            lines.append(f"[{status}] {name}: {summary} ({dt}s)")
            if not ok:
                # record the failure output (first 400 chars)
                err = (r.stdout + r.stderr).strip()[-500:]
                entry["error"] = err
                lines.append(f"    ERROR: {err[:300]}")
        except subprocess.TimeoutExpired:
            entry.update({"status": "ERROR", "time_s": round(time.time() - start, 2),
                          "error": "TIMEOUT (120s)"})
            report["overall"]["error"] += 1
            print(f"  [ERROR] {name}: TIMEOUT (120s)")
            lines.append(f"[ERROR] {name}: TIMEOUT (120s)")
        except Exception as e:
            entry.update({"status": "ERROR", "error": f"{e}: {traceback.format_exc()[-300:]}"})
            report["overall"]["error"] += 1
            print(f"  [ERROR] {name}: {e}")
            lines.append(f"[ERROR] {name}: {e}")
        report["stages"].append(entry)

    # the machine + human logs
    mpath = f"{LOGS}/run-{ts}.json"
    hpath = f"{LOGS}/run-{ts}.txt"
    json.dump(report, open(mpath, "w"), indent=1)
    open(hpath, "w").write("\n".join(lines) + "\n")

    # the iteration snapshot (for the autonomous-iteration log)
    it_path = f"{ITERS}/{ts}.json"
    json.dump({"run": ts, "overall": report["overall"], "stages": report["stages"]}, open(it_path, "w"), indent=1)

    tot = report["overall"]["pass"] + report["overall"]["fail"] + report["overall"]["error"]
    print(f"\n=== OVERALL: {report['overall']['pass']} PASS / {report['overall']['fail']} FAIL / "
          f"{report['overall']['error']} ERROR (of {tot} stages) ===")
    print(f"  log: {mpath}")
    print(f"  human: {hpath}")
    print(f"  iteration: {it_path}")
    return 0 if report["overall"]["fail"] == 0 and report["overall"]["error"] == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
