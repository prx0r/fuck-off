#!/usr/bin/env python3
"""experiment-unified-epistemic.py — synthesize herdr + RKA + Kappa into one epistemic pipeline.

Combines three cloned-repo patterns, applied to our REAL data:
  1. Kappa  : evidence grounding (support vs contradiction) per concept  [from our evidence-weights]
  2. herdr  : adversarial review state machine per claim                  [SPEC-12]
  3. RKA    : blast-radius staleness on the canonical DAG                 [SPEC-07]
The result: an executable, honest promotion path agent-output -> evidence -> review -> canonical.
"""
import json, yaml

ROOT = "/mnt/HC_Volume_106427611/ip-graph"
weights = json.load(open(f"{ROOT}/data/graph/evidence-weights.json"))["concepts"]
arg = json.load(open(f"{ROOT}/data/graph/argument.json"))
dag = yaml.safe_load(open(f"{ROOT}/data/graph/canonical-dag.yaml"))["dependencies"]

# ---- 1. KAPPA: grounding/support/contradiction per concept ----
def kappa_signal(concept):
    w = weights.get(concept, {})
    support = w.get("support_weight", 0); contra = w.get("contradiction_weight", 0)
    grounding = w.get("grounding", 0)
    if support == 0 and contra == 0: return "NO_DATA"
    ratio = support / (support + contra) if (support+contra) else 0
    return "CORROBORATED" if ratio > 0.7 else ("CONTESTED" if 0.3 <= ratio <= 0.7 else "CONTRADICTED")

# ---- 2. HERDR: review phase from kappa signal ----
def herdr_phase(signal):
    return {"CORROBORATED": "ALIGNED", "CONTESTED": "REVIEWING", "CONTRADICTED": "CORRECTION_REQUIRED"}.get(signal, "AWAITING_CANDIDATE")

# ---- 3. RKA: staleness blast-radius ----
depends_on = {l: set() for l in dag}
for layer, d in dag.items():
    for req in d.get("requires", []):
        if req in dag: depends_on[req].add(layer)
def blast(changed):
    stale = set(changed); frontier = set(changed)
    while frontier:
        nxt = set()
        for f in frontier:
            for dep in depends_on.get(f, set()):
                if dep not in stale: stale.add(dep); nxt.add(dep)
        frontier = nxt
    return stale

print("=== UNIFIED EPISTEMIC PIPELINE (kappa+herdr+rka) ===")
print("\n-- Claims (kappa grounding -> herdr review) --")
for n in arg["information_nodes"]:
    cid = n["id"]; text = n["text"][:40]
    signal = kappa_signal(cid.replace("I", ""))  # concept-by-id fallback
    # map claim id to a concept
    concept = {"I1":"quantum_mechanics","I2":"indeterminism","I3":"mind","I4":"chance","I5":"free_will","I6":"mind"}.get(cid)
    signal = kappa_signal(concept) if concept else signal
    phase = herdr_phase(signal)
    print(f"  {cid} [{signal:14s} -> {phase:22s}] {text}")

print("\n-- Staleness (RKA blast-radius) --")
for changed in ["PHYSICS", "INDETERMINISM"]:
    stale = blast({changed})
    print(f"  {changed} changed -> {len(stale)-1} downstream stale: {sorted(stale - {changed})[:8]}")

print("\n=== SYNTHESIS ===")
print("kappa scores a concept (CORROBORATED/CONTESTED/CONTRADICTED), herdr's state machine")
print("maps that to a review phase, and RKA propagates any change downstream as stale. Together:")
print("  physics floor (CORROBORATED) -> ALIGNED\n  free-will thesis (CONTESTED/CONTRADICTED) -> REVIEWING/CORRECTION\n  any physics retraction -> FREE_WILL/VALUE flagged stale -> review_queue\n")
print("This is the executable epistemic-promotion engine our vision calls for, built from the")
print("best patterns in herdr (SPEC-12), RKA (SPEC-07), and kappa (SPEC-07).")
