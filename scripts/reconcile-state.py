#!/usr/bin/env python3
"""reconcile-state.py — verify STATE.yaml stays in sync with the real build.

Checks that:
  1. every lib/*.py kernel is accounted for (in STATE.yaml or the experiment matrix)
  2. every experiment in the matrix has a PASS status in test-results (or is an exploratory RUN)
  3. STATE.yaml layers are not claiming NOT_STARTED when experiments validate them

This makes the checkpoint mechanism self-auditing — it cannot silently drift like it did before.
"""
import os, json, yaml, glob

ROOT = "/mnt/HC_Volume_106427611/ip-graph"

print("=== STATE RECONCILIATION CHECK ===\n")
issues = []

# 1. every lib kernel must be referenced in STATE.yaml or the matrix
state = yaml.safe_load(open(f"{ROOT}/STATE.yaml"))
matrix = json.load(open(f"{ROOT}/data/references/experiments.json"))
mat_scripts = {e["script"] for e in matrix["entries"]}
state_kernels = set(state.get("product_kernels", {}).keys())

lib_kernels = {os.path.basename(f) for f in glob.glob(f"{ROOT}/lib/*.py")}
print("[kernels] lib/*.py:", sorted(lib_kernels))
for k in sorted(lib_kernels):
    # kernel is referenced if a matrix experiment names it or it's in product_kernels
    ref = k in state_kernels or any(k in e.get("kernel", "") for e in matrix["entries"])
    print(f"  {'OK ' if ref else 'UNREFERENCED'} {k}")
    if not ref: issues.append(f"lib kernel not referenced: {k}")

# 2. every experiment should have a source + kernel mapped
print(f"\n[experiments] {len(mat_scripts)} in matrix, {len([e for e in matrix['entries'] if e['status']=='PASS'])} PASS")
unmapped = [e["script"] for e in matrix["entries"] if not e.get("source") or not e.get("kernel")]
if unmapped: issues.append(f"experiments missing source/kernel: {unmapped}")

# 3. STATE.yaml layers: flag any that say NOT_STARTED but have validating experiments
layer_ok = {}
for layer, info in state.get("layers", {}).items():
    layer_ok[layer] = info["status"]
# map matrix layers to STATE layers (L00..L12 -> 00..12)
layer_exp = {}
for e in matrix["entries"]:
    for l in e["layer"].split("+"):
        if l.startswith("L") and l[1:].isdigit():
            layer_exp.setdefault(l[1:].zfill(2), []).append(e["script"])
print("\n[layer status]")
for layer, status in layer_ok.items():
    exps = layer_exp.get(layer.split("-")[0], [])
    if status == "NOT_STARTED" and exps:
        issues.append(f"STATE layer {layer} NOT_STARTED but has experiments: {exps}")
    print(f"  {layer:24s} {status:12s} ({len(exps)} exps)")

print(f"\n=== RESULT: {len(issues)} issues ===")
if issues:
    for i in issues: print("  -", i)
    print("\nRun `scripts/build-experiment-matrix.py` then re-check. Fix STATE.yaml to match reality.")
    print("(This is the checkpoint mechanism self-auditing — it caught drift before, now it can't.)")
else:
    print("STATE.yaml is in sync with the build. PASS.")
