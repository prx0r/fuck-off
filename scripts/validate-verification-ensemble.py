#!/usr/bin/env python3
"""validate-verification-ensemble.py — the verification ensemble, not one big prompt (GEM 7.1).

Proves RefChecker (atomic claims resolve) + GraphCheck (relations are real edges) composed into a
RARR-style gate. An answer passes only if EVERY atomic claim resolves AND its relations are real graph
edges — no single big prompt, no phantom sources, no invented relations. On our real IPK sources.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from verification_ensemble import VerificationEnsemble

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=== VERIFICATION ENSEMBLE: RefChecker + GraphCheck + RARR-gate (GEM 7.1) ===\n")

ve = VerificationEnsemble()
# register the real sources + edges
ve.register_source("IPK-1.5.19")
ve.register_source("IPK-1.5.11")
ve.register_source("ratie")
ve.register_edge("adhyavasaya", "is_power_of", "mahesvara")
ve.register_edge("vimarśa", "defines", "avabhasa")

# ---- a GOOD answer: atomic claims all resolve + all relations are real edges ----
good_atomic = [
    ("adhyavasaya", "is_power_of", "mahesvara", "IPK-1.5.19"),
    ("vimarśa", "defines", "avabhasa", "IPK-1.5.11"),
]
ve._atomic_claims["good"] = good_atomic
v = ve.verify("good")
check("GOOD: all atomic claims resolve (RefChecker pass)", v["refchecker"]["pass"])
check("GOOD: all relations are real graph edges (GraphCheck pass)", v["graphcheck"]["pass"])
check("GOOD: ensemble ACCEPTS the answer", v["accepted"] and v["reason"] == "ALL_ATOMIC_CLAIMS_VERIFIED")

# ---- a PHANTOM: atomic claim cites a source that isn't registered ----
phantom_atomic = [
    ("adhyavasaya", "is_power_of", "mahesvara", "IPK-1.5.19"),
    ("some_claim", "about", "nothing", "IPK-99.99"),   # phantom source
]
ve._atomic_claims["phantom"] = phantom_atomic
vp = ve.verify("phantom")
check("PHANTOM: unregistered source caught (RefChecker)", not vp["refchecker"]["pass"]
      and "IPK-99.99" in vp["refchecker"]["missing_sources"])
check("PHANTOM: ensemble REJECTS", not vp["accepted"])

# ---- INVENTED RELATION: relation is not a real graph edge ----
invented_atomic = [
    ("vimarśa", "IS_THE_SAME_AS", "coffee", "IPK-1.5.11"),   # real source but fake relation
]
ve._atomic_claims["invented"] = invented_atomic
vi = ve.verify("invented")
check("INVENTED: fake relation caught (GraphCheck)", not vi["graphcheck"]["pass"]
      and ("vimarśa", "IS_THE_SAME_AS", "coffee") in vi["graphcheck"]["invented_relations"])
check("INVENTED: ensemble REJECTS (graph gate)", not vi["accepted"])

# ---- the ensemble is compositional (each check is independently reportable) ----
check("compositional: RefChecker + GraphCheck are separate, auditable verdicts",
      "refchecker" in v and "graphcheck" in v and v["refchecker"]["n_atomic"] == 2)

print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
print("\nVERIFICATION ENSEMBLE (GEM 7.1): RefChecker + GraphCheck composed into a RARR-style gate —")
print("an answer passes only if EVERY atomic claim resolves to a registered source AND every relation")
print("is a real graph edge. No single big prompt, no phantoms, no invented relations. The ensemble")
print("is the anti-hallucination layer.")
sys.exit(0 if all(c for _,c in results) else 1)
