#!/usr/bin/env python3
"""experiment-certification-weight.py — the compounding certification-weight mechanism (VISION).

From VISION-Verified-Statement-Marketplace: a claim's certification weight compounds:
  CW = verifier_kill_rate × consensus_multiplicity × downstream_load × time_signed

Each factor is from a VALIDATED subsystem:
  verifier_kill_rate   <- mutation-testing (0..1)
  consensus_multiplicity <- cross-review (how many independent reviewers confirmed)
  downstream_load      <- counterfactual engine (how much collapses if it's wrong)
  time_signed          <- how long it's survived unchanged (temporal validity + signed root)

The flywheel: a claim that survives verified + accumulates downstream use + holds over time has
compounding weight — a network-effect moat encoded in the data.
"""
import os, sys, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))

# validated inputs (from our experiments) for the two-stage free-will claims
claims = [
    {"id": "I1", "text": "Quantum events are genuinely indeterministic",
     "verifier_kill_rate": 1.0, "consensus_multiplicity": 3, "downstream_load": 5, "time_signed_years": 1.0},
    {"id": "I2", "text": "Indeterminism provides the random chance stage",
     "verifier_kill_rate": 1.0, "consensus_multiplicity": 2, "downstream_load": 4, "time_signed_years": 0.6},
    {"id": "I5", "text": "The two-stage model explains free will as chance + choice",
     "verifier_kill_rate": 0.9, "consensus_multiplicity": 2, "downstream_load": 4, "time_signed_years": 0.8},
    {"id": "I4", "text": "Biological variability mirrors the chance stage",
     "verifier_kill_rate": 1.0, "consensus_multiplicity": 1, "downstream_load": 3, "time_signed_years": 0.5},
]

def certification_weight(c):
    """CW = kill_rate × consensus × (1 + downstream) × (1 + time) — compounding, monotonic."""
    return (c["verifier_kill_rate"] * c["consensus_multiplicity"]
            * (1 + c["downstream_load"]) * (1 + c["time_signed_years"]))

print("=== CERTIFICATION WEIGHT: the compounding verification asset ===\n")
print(f"{'claim':12s} {'kill':>4s} {'cons':>4s} {'load':>4s} {'time':>5s}  {'CW':>7s}")
for c in claims:
    cw = certification_weight(c)
    print(f"{c['id']:12s} {c['verifier_kill_rate']:4.1f} {c['consensus_multiplicity']:4d} "
          f"{c['downstream_load']:4d} {c['time_signed_years']:5.1f}  {cw:7.2f}")

# ---- the compounding property: time + downstream accumulation raise CW ----
print("\n-- compounding over time (I1 accumulates downstream use + stays verified) --")
base = dict(claims[0])
for t in [1.0, 2.0, 5.0, 10.0]:
    c = dict(base); c["time_signed_years"] = t; c["downstream_load"] = int(5 * t/1.0)
    print(f"  year {t:4.0f}: downstream_load={c['downstream_load']:2d} -> CW={certification_weight(c):8.2f}")

# ---- the marketplace property: more consensus raises CW (bias-robust) ----
print("\n-- consensus raises weight (bias-robust verification is worth more) --")
c = dict(claims[1])
for cons in [1, 2, 3, 5, 8]:
    c["consensus_multiplicity"] = cons
    print(f"  {cons} independent confirmations -> CW={certification_weight(c):6.2f}")

print("\n=== INSIGHT ===")
print("Certification Weight is MONOTONIC + COMPOUNDING: it rises with (a) verifier strength,")
print("(b) independent consensus, (c) downstream load-bearing, and (d) time survived. The flywheel:")
print("a claim that survives verified accumulates downstream use -> higher CW -> more valuable to build")
print("on -> more downstream use. This is a network-effect moat encoded in the data itself — the")
print("unit of value in a Verified-Statement-Marketplace, and it gets stronger as AI content floods")
print("the world (verified knowledge becomes the scarce asset).")
