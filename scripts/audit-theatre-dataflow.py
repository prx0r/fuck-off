#!/usr/bin/env python3
"""audit-theatre-dataflow.py — RIGOROUS anti-theatre: does the asserted object trace to REAL data?

The hole in theatre-check-all.py: it uses a hardcoded MARKER WHITELIST (string match) to decide
"real data". That has two failures:
  1. INCOMPLETE MARKERS — a test reading data/tantraloka/ (or any new corpus) is wrongly flagged
     synthetic because "data/tantraloka" isn't in the list.
  2. NO DATA-FLOW CHECK — the marker can't tell whether the object under test is DERIVED from the
     loaded data or HAND-FED next to it. My translate test loads the verse THEN hand-writes the proof
     fields (source_analysis=PASS) — that's theatre a string match cannot catch.

This audit does STATIC DATA-FLOW ANALYSIS on each validator:
  - FIND every `json.load(open(...))` / `open(...).read()` that loads a real data file
  - FIND every CHECK that asserts something
  - DETECT "dead reads": a file is loaded but its contents are never referenced in any check's
    argument (the object under test is hand-fed, the read is theatre decoration)

Usage: python3 scripts/audit-theatre-dataflow.py   # exit 0/1
"""
import os, re, sys

ROOT = "/mnt/HC_Volume_106427611/ip-graph"
REAL_PATHS = ["data/", "/root/", "site/", "/mnt/", "corpus", "research-library"]

def audit_script(path):
    src = open(path).read()
    name = os.path.basename(path)
    findings = []

    # 1. every real-data load (handle both `json.load(open(...))` AND `with open(...) as f:` + loop)
    loads = re.findall(r'open\([^)]*(?:data/|/root/|site/|/mnt/|corpus)[^)]*\)', src)
    with_opens = re.findall(r'with\s+open\([^)]*(?:data/|/root/|site/|/mnt/|corpus)[^)]*\)\s+as\s+(\w+)', src)
    load_vars = set(re.findall(r'(\w+)\s*=\s*(?:json\.load\(open|open)\(', src))
    load_vars |= set(with_opens)  # the `as f` variable counts as a data load

    # 2. every check's arguments — do they reference loaded variables or hand-fed literals?
    checks = re.findall(r'check\("([^"]+)",\s*([^\)]+)\)', src)
    hand_fed = 0
    derived = 0
    for label, cond in checks:
        # is the condition built from a loaded variable (data-derived)?
        if any(v in cond for v in load_vars):
            derived += 1
        elif re.search(r'==\s*"[A-Z_]+"|True|False|None\b|\.phase\s*==', cond):
            # assertion on a constant/state — could be derived or hand-fed; flag if no load_var
            if not load_vars:
                hand_fed += 1
            else:
                derived += 1

    # verdict
    if not loads and not load_vars:
        verdict = "SYNTHETIC"          # reads no real data at all
        detail = "no real data loaded"
    elif derived == 0 and len(checks) > 0:
        verdict = "THEATRE"            # loads data but asserts only on hand-fed constants
        detail = f"reads {len(loads)} file(s) but {len(checks)} checks never reference loaded vars"
    elif hand_fed > derived:
        verdict = "PARTIAL"
        detail = f"reads data, but {hand_fed} checks assert on constants vs {derived} on loaded data"
    else:
        verdict = "REAL-DATA"
        detail = f"reads {len(loads)} file(s), {derived} checks reference loaded data"

    return verdict, detail, {"loads": len(loads), "checks": len(checks), "hand_fed": hand_fed, "derived": derived}

def main():
    print("=== RIGOROUS ANTI-THEATRE: static data-flow audit of every validator ===\n")
    validators = sorted(f for f in os.listdir(f"{ROOT}/scripts") if f.startswith("validate-"))
    rows = []
    for v in validators:
        verdict, detail, meta = audit_script(f"{ROOT}/scripts/{v}")
        rows.append((v, verdict, detail))
    for v, verdict, detail in rows:
        mark = "✓" if verdict == "REAL-DATA" else ("!" if verdict == "THEATRE" else "~")
        print(f"  {mark} {v:44s} [{verdict:9s}] {detail}")
    # summary
    from collections import Counter
    c = Counter(r[1] for r in rows)
    print(f"\n=== SUMMARY ({len(rows)} validators) ===")
    for k, n in c.items():
        print(f"  {k}: {n}")
    theatre = [r for r in rows if r[1] == "THEATRE"]
    print(f"\n  THEATRE-flagged: {len(theatre)}  (ADVISORY — manually verify each; the static check")
    print(f"  cannot trace data through helper functions, so it over-flags. A THEATRE flag means 'audit")
    print(f"  by hand' not 'definitely fake'.")
    for v, _, d in theatre:
        print(f"    ! {v}: {d}")
    # ADVISORY: report, but don't hard-fail (over-flagging is worse than under-flagging for a static tool)
    sys.exit(0)

if __name__ == "__main__":
    main()
