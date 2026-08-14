#!/usr/bin/env python3
"""audit-state.py — machine-gate that state.json is VALID, consistent, and resolvable.

The clean-structure fix: state.json is the machine-readable current-state file. It must (1) parse as
valid JSON (it previously had comments that broke parsing), (2) have counts that MATCH the actual
ground truth (lib/, experiments.json, tests), and (3) reference only resolvable paths. This is the
"compute-on-write, no drift" gate for the project state — a human + machine can't silently disagree.

Usage:
  python3 scripts/audit-state.py     # exit 0/1
"""
import os, sys, json

ROOT = "/mnt/HC_Volume_106427611/ip-graph"

def main():
    errors = []
    # 1. state.json must be valid JSON
    try:
        state = json.load(open(f"{ROOT}/state.json"))
    except Exception as e:
        print(f"FAIL: state.json is not valid JSON: {e}")
        sys.exit(1)
    print("state.json parses as valid JSON")
    # 2. counts must match ground truth
    n_kernels = len([f for f in os.listdir(f"{ROOT}/lib") if f.endswith(".py")])
    exp = json.load(open(f"{ROOT}/data/references/experiments.json"))
    n_exp = len(exp["entries"])
    got = state["counts"]
    if got["kernels"] != n_kernels:
        errors.append(f"kernels: state says {got['kernels']}, actual {n_kernels}")
    if got["experiments"] != n_exp:
        errors.append(f"experiments: state says {got['experiments']}, actual {n_exp}")
    # 3. referenced test scripts must exist
    for k, v in state.get("read_plane_built", {}).items():
        t = v.get("test")
        if t and not os.path.exists(f"{ROOT}/scripts/{t}.py"):
            errors.append(f"read_plane {k}: test {t}.py missing")
    if errors:
        print("FAIL — state.json is out of sync with ground truth:")
        for e in errors:
            print(f"  ✗ {e}")
        sys.exit(1)
    print(f"state.json consistent with ground truth ({n_kernels} kernels, {n_exp} experiments, "
          f"{len(state.get('next_dev_steps', []))} next steps)")
    sys.exit(0)

if __name__ == "__main__":
    main()
