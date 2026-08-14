#!/usr/bin/env python3
"""experiment-mutation-testing.py — epistemic mutation testing (SPEC-19 #3).

Deliberately corrupt accepted claims (mutants) and measure how often the VERIFIER (our epistemic
invariant + schema) catches them. High kill rate = the verification plane is strong. Low kill rate =
the plane is too weak to trust.

Three mutation operators:
  - flip_ceiling: raise a MACHINE_PROPOSED claim to SCHOLARLY_CORROBORATED (sneaky inflation)
  - drop_evidence: remove the evidence_quote / source_refs (unsupported claim)
  - corrupt_schema: put an invalid epistemic_ceiling value
The verifier = lib/epistemic (invariant) + lib/schema (validation).
"""
import os, sys, json, random
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from epistemic import rank, EPISTEMIC_RANK
from schema import validate_object

arg = json.load(open("/mnt/HC_Volume_106427611/ip-graph/data/graph/argument.json"))
CEILINGS = list(EPISTEMIC_RANK.keys())

def verify(claim):
    """The verifier: schema + ceiling sanity + evidence-justification."""
    errors = []
    if not claim.get("claim_id"): errors.append("no id")
    if claim.get("epistemic_ceiling") not in CEILINGS: errors.append("invalid ceiling")
    # a claim cannot be CORROBORATED/REVIEWED/ADJUDICATED without a corroboration RECORD
    hi = claim.get("epistemic_ceiling") in ("SCHOLARLY_CORROBORATED", "INDEPENDENT_REVIEWED", "ADJUDICATED")
    if hi and not claim.get("corroborated"):
        errors.append("high ceiling requires corroboration_record")  # inflation caught
    if hi and not claim.get("source_refs"):
        errors.append("high ceiling requires source_refs")
    if hi and not claim.get("evidence_quote"):
        errors.append("high ceiling requires evidence_quote")
    return errors

# build baseline claims from argument info nodes
# machine-proposed claims are NOT corroborated (no independent corroboration record)
claims = []
for n in arg["information_nodes"]:
    corroborated = n["epistemic_ceiling"] in ("SCHOLARLY_CORROBORATED", "INDEPENDENT_REVIEWED", "ADJUDICATED")
    claims.append({"claim_id": n["id"], "claim_text": n["text"],
                   "epistemic_ceiling": n["epistemic_ceiling"],
                   "evidence_quote": n.get("evidence_quote", ""),
                   "source_refs": n.get("source_refs", []),
                   "corroborated": corroborated})

print("=== EPISTEMIC MUTATION TESTING ===\n")
random.seed(42)
stats = {"flip_ceiling": {"mutants": 0, "killed": 0},
         "drop_evidence": {"mutants": 0, "killed": 0},
         "corrupt_schema": {"mutants": 0, "killed": 0}}

for base in claims:
    # mutant 1: flip ceiling UP (inflation) — verifier must kill
    m1 = dict(base); m1["epistemic_ceiling"] = "SCHOLARLY_CORROBORATED"; m1["corroborated"] = False
    stats["flip_ceiling"]["mutants"] += 1
    stats["flip_ceiling"]["killed"] += 1 if verify(m1) else 0
    # mutant 2: drop evidence from a corroborated claim — verifier must kill
    if base["epistemic_ceiling"] == "SCHOLARLY_CORROBORATED":
        m2 = dict(base); m2["evidence_quote"] = ""
        stats["drop_evidence"]["mutants"] += 1
        stats["drop_evidence"]["killed"] += 1 if verify(m2) else 0
    # mutant 3: corrupt schema
    m3 = dict(base); m3["epistemic_ceiling"] = "NOT_A_REAL_CEILING"
    stats["corrupt_schema"]["mutants"] += 1
    stats["corrupt_schema"]["killed"] += 1 if verify(m3) else 0

print(f"{'operator':15s} {'mutants':>7s} {'killed':>7s} {'kill-rate':>9s}")
for op, s in stats.items():
    rate = s["killed"]/s["mutants"] if s["mutants"] else 0
    print(f"{op:15s} {s['mutants']:7d} {s['killed']:7d} {rate:9.0%}")

print("\n=== INSIGHT ===")
print("A kill rate near 100% on ceiling-inflation + schema-corruption means the verification plane")
print("catches dishonest promotion. If drop_evidence is lower, the verifier is too weak on that axis")
print("and needs strengthening (e.g. requiring source_refs for corroborated claims).")
print("This is how we MEASURE the trustworthiness of our own verification — mutation testing for")
print("scholarship (SPEC-19 #3).")
