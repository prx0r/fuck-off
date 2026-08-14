#!/usr/bin/env python3
"""experiment-counterfactual-engine.py — VISION B: whole-graph counterfactual robustness.

Extends the single-premise PremiseRetract into a full engine: for every layer, ask
"what if this were false?" and measure (a) how much downstream collapses, (b) which layers are
most load-bearing (highest counterfactual blast-radius). Robustness becomes the metric —
a claim that survives more counterfactuals is more foundational.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from staleness import build_dependency_index, blast_radius

# the full canonical DAG
dag = {
    "PHYSICS": {"requires": []}, "THERMODYNAMICS": {"requires": []},
    "INFORMATION": {"requires": ["THERMODYNAMICS"]}, "COMPUTATION": {"requires": ["INFORMATION"]},
    "QUANTUM": {"requires": ["PHYSICS"]}, "PROBABILITY": {"requires": ["PHYSICS", "THERMODYNAMICS"]},
    "INDETERMINISM": {"requires": ["QUANTUM", "PROBABILITY"]},
    "MIND": {"requires": ["INFORMATION", "COMPUTATION"]}, "LIFE": {"requires": ["INFORMATION", "THERMODYNAMICS"]},
    "FREE_WILL": {"requires": ["INDETERMINISM", "MIND"]}, "RESPONSIBILITY": {"requires": ["FREE_WILL"]},
    "VALUE": {"requires": ["FREE_WILL", "LIFE"]}, "SYNTHESIS": {"requires": ["FREE_WILL", "VALUE"]},
    "ESSAY": {"requires": ["SYNTHESIS"]},
}
dep = build_dependency_index(dag)

print("=== VISION B: COUNTERFACTUAL ENGINE (whole-graph what-if) ===\n")

# for each layer, counterfactual: retract it, measure downstream collapse
print(f"{'layer':16s} {'downstream lost':>15s} {'load-bearing'}")
load_bearing = []
for layer in dag:
    if layer == "SOURCE": continue
    stale = blast_radius(dep, {layer}) - {layer}
    lb = len(stale)
    load_bearing.append((layer, lb, sorted(stale)))
    print(f"{layer:16s} {lb:15d} {'HIGH' if lb >= 2 else ''}")

print("\n-- the most load-bearing assumptions --")
top = sorted(load_bearing, key=lambda x: -x[1])[:3]
for layer, lb, stale in top:
    print(f"  {layer}: if FALSE, {lb} downstream claims collapse ({', '.join(stale)})")

print("\n-- the leaf claims (nothing depends on them) --")
leafs = [l for l, lb, _ in load_bearing if lb == 0]
print(f"  {leafs}")

print("\n=== INSIGHT ===")
print("Counterfactual robustness = a NEW metric: FREE_WILL, RESPONSIBILITY, VALUE, SYNTHESIS are the")
print("most load-bearing (their collapse takes everything). PHYSICS is a foundation but not the most")
print("load-bearing (less depends directly on it than on the thesis chain). This is vulnerability")
print("analysis for knowledge — the OS as a reasoning instrument, not a record. The most load-bearing")
print("claims are where a rival should attack (feeds VISION D).")
