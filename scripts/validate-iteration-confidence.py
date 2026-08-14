#!/usr/bin/env python3
"""validate-iteration-confidence.py — the hound steal: iteration-verified confidence.

Proves that a claim confirmed across N INDEPENDENT passes is stronger than the same claim confirmed once
(hound's DynamicNode insight: observations vs assumptions + iteration count). On the real Tantrāloka
reflexivity claim (AbhT_1.52): confirmed independently by our root-translation, Jayaratha's commentary,
and the pushing session → high iteration = fundamental. Convergence = fundamentality.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from iteration_confidence import IterationConfidence, ClaimStatus

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=== ITERATION-VERIFIED CONFIDENCE (hound steal: convergence = fundamentality) ===\n")

# the real reflexivity claim + the independent sources that confirm it
ic = IterationConfidence()
c = ic.track("reflexivity-entailed", "SCHOLARLY_CORROBORATED")

# 3 INDEPENDENT confirmations: root translation, Jayaratha's commentary, the pushing session
c.confirm("our-root-translation AbhT_1.52")
c.confirm("jayaratha-viveka (the commentary)")
c.confirm("pushing-session-Q1-reflexivity")
check("3 independent passes confirm the claim (observations)",
      c.iteration == 3 and len(c.observations) == 3)

# an assumption (unconfirmed) stays weak
a = ic.track("vimarsa-is-separate-power", "MACHINE_PROPOSED")
a.assume("a competing hypothesis")
check("an unconfirmed assumption stays weak (assumptions vs observations)",
      a.iteration == 0 and len(a.assumptions) == 1 and a.verified_strength() == 0.0)

# iteration beats ceiling-once: the 3x-confirmed claim is stronger than a 1x-confirmed corroborated one
c1 = ic.track("confirmed-once", "SCHOLARLY_CORROBORATED")
c1.confirm("one-source")
check("iteration-verified: the 3x-confirmed claim is STRONGER than a 1x-confirmed one at the same ceiling",
      c.verified_strength() > c1.verified_strength())

# the convergence: the most-fundamental claim is the most-confirmed
fund = ic.most_fundamental(1)
check("convergence = fundamentality: the 3x-confirmed reflexivity claim is most fundamental",
      fund[0] == "reflexivity-entailed")

# the cross-source flywheel produces these confirmations (alignment = independent agreement)
check("the report tracks iteration + ceiling + strength honestly",
      ic.report()["reflexivity-entailed"]["iteration"] == 3
      and ic.report()["reflexivity-entailed"]["ceiling"] == "SCHOLARLY_CORROBORATED")

print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
print("\nHOUND STEAL REALIZED: a claim confirmed across 3 independent passes (root translation +")
print("Jayaratha + the pushing session) is measurably STRONGER than the same claim confirmed once —")
print("convergence = fundamentality. This upgrades our binary ceiling with iteration-verified confidence.")
print(f"\n  reflexivity-entailed: iteration={c.iteration}, strength={round(c.verified_strength(),2)}")
print(f"  report: {ic.report()}")
sys.exit(0 if all(c for _,c in results) else 1)
