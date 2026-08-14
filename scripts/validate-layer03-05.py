#!/usr/bin/env python3
"""validate-layer03-05.py — verifiable tests for the Factory (DAG=staleness) + Research (reducer) kernels.

Layer 03 (Factory): RKA blast-radius on our canonical DAG -> retraction flags downstream stale,
files review_queue, and computes incremental rebuild order.
Layer 05 (Research): herdr reducer on our argument claims -> honest promotion gating.

Prints a PASS/FAIL validation summary. Exit 0 if all pass.
"""
import os, sys, yaml, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from review import reducer, ReviewState, ReviewFinding, FindingSeverity, phase_from_ceiling, promote, ReviewPhase
from staleness import blast_radius, build_dependency_index, file_review_queue, incremental_rebuild_order

ROOT = "/mnt/HC_Volume_106427611/ip-graph"
dag = yaml.safe_load(open(f"{ROOT}/data/graph/canonical-dag.yaml"))["dependencies"]
arg = json.load(open(f"{ROOT}/data/graph/argument.json"))

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=== LAYER 03 — FACTORY (DAG = staleness engine) ===\n")
depends_on = build_dependency_index(dag)
# 1. blast radius from PHYSICS retraction
stale = blast_radius(depends_on, {"PHYSICS"})
check("PHYSICS retraction reaches FREE_WILL", "FREE_WILL" in stale)
check("PHYSICS retraction reaches VALUE", "VALUE" in stale)
check("PHYSICS retraction does NOT reach THERMODYNAMICS (not downstream)", "THERMODYNAMICS" not in stale)
# 2. review queue filed
q = file_review_queue(dag, {"PHYSICS"}, flag="stale_dependency")
check("review_queue filed for downstream", len(q) > 5, f"({len(q)} entries)")
check("review_queue flag is stale_dependency", all(i.flag == "stale_dependency" for i in q))
# 3. incremental rebuild order (topological, dependencies first)
order = incremental_rebuild_order(dag, {"PHYSICS"})
pos = {l: i for i, l in enumerate(order)}
check("rebuild order has FREE_WILL after INDETERMINISM", "INDETERMINISM" in pos and "FREE_WILL" in pos
      and pos["INDETERMINISM"] < pos["FREE_WILL"], f"order={order}")

print("\n=== LAYER 05 — RESEARCH (herdr reducer promotion gate) ===\n")
# 4. reducer: corroborated physics claim -> ALIGNED (AWAITING->REVIEWING->ALIGNED)
st = ReviewState("I1")
reducer(st, evidence_ok=True)      # AWAITING -> REVIEWING
check("corroborated claim reaches ALIGNED",
      reducer(st, evidence_ok=True) == ReviewPhase.ALIGNED)
# 5. reducer: machine-proposed thesis -> CORRECTION (blocked)
st2 = ReviewState("I5")
reducer(st2, evidence_ok=True)  # AWAITING -> REVIEWING
st2.findings.append(ReviewFinding("f1", "reviewer", FindingSeverity.BLOCKING))
check("machine-proposed thesis blocked in CORRECTION",
      reducer(st2, evidence_ok=True) == ReviewPhase.CORRECTION)
# 6. phase_from_ceiling mapping
check("phase_from_ceiling(CORROBORATED)=ALIGNED", phase_from_ceiling("SCHOLARLY_CORROBORATED") == ReviewPhase.ALIGNED)
check("phase_from_ceiling(MACHINE_PROPOSED)=CORRECTION", phase_from_ceiling("MACHINE_PROPOSED") == ReviewPhase.CORRECTION)
# 7. promotion: only human reaches ADJUDICATED
st3 = ReviewState("I5", phase=ReviewPhase.ALIGNED)
check("ALIGNED cannot reach ADJUDICATED without human", not promote(st3, "ADJUDICATED"))
reducer(st3, evidence_ok=True, human_approves=True)
check("human override reaches ADJUDICATED", promote(st3, "ADJUDICATED"))

# ---- summary ----
npass = sum(1 for _, c, _ in results if c)
print(f"\n=== SUMMARY: {npass}/{len(results)} passed ===")
sys.exit(0 if npass == len(results) else 1)
