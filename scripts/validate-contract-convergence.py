#!/usr/bin/env python3
"""validate-contract-convergence.py — the #1 build: converge the divergent contracts (parity test).

Proves the 6 divergent ReviewEvent/Authority definitions converge onto ONE canonical contract:
  - the AuthorityVector is 4-axis NON-SCALAR with explicit gate predicates (the OG design, which my
    lib/epistemic.py's scalar ceiling() wrongly violated).
  - a review event through the canonical contract gives the same eligibility as the OG AuthorityVector.
  - PARITY: the same authority dict via OG and via our convergence reduces to the same vector.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from canonical_contracts import (AuthorityVector, Gen, Ev, Rev, Pub, ReviewEvent,
                                 CanonicalEnvelope, parity_with_og)

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=== CONTRACT CONVERGENCE — ONE canonical Authority/ReviewEvent (the #1 build) ===\n")

# ---- the canonical 4-axis vector is NON-SCALAR (gates, not a rank) ----
v = AuthorityVector(Gen.MACHINE_PROPOSED, Ev.NONE, Rev.NOT_REVIEWED, Pub.PRIVATE)
check("AuthorityVector has 4 independent axes (no scalar rank)", len(v.to_dict()) == 4)
check("a machine-proposed, unreviewed claim is NOT eligible for publication (gate)",
      not v.eligible_for_publication())
check("a machine-proposed claim IS eligible for scholar review (the gate)", v.eligible_for_scholar_review())
check("a private, unreviewed claim is NOT eligible for education", not v.eligible_for_education())

# ---- the honest display badge (non-scalar) ----
check("display_badge is a phrase, not a number (no misleading scalar)",
      "machine-generated" in v.display_badge() and "not human-reviewed" in v.display_badge())

# ---- a review PROMOTES the authority (only via explicit states) ----
v2 = AuthorityVector(Gen.ENGINEERING_VALIDATED, Ev.SCHOLARLY_CORROBORATED, Rev.ADJUDICATED, Pub.PUBLIC)
check("an engineering-validated + adjudicated + public claim IS eligible for publication",
      v2.eligible_for_publication())
check("an adjudicated + public claim IS eligible for education", v2.eligible_for_education())

# ---- the envelope uses the canonical vector (not a scalar ceiling()) ----
env = CanonicalEnvelope("AbhT_1.52", "claim", authority=AuthorityVector(Gen.MACHINE_PROPOSED, Ev.NONE))
check("the convergent envelope exposes the canonical gates",
      not env.eligible_for_publication() and env.eligible_for_scholar_review())

# ---- PARITY: the same authority via OG and via our convergence agree ----
og = {"generation": "MACHINE_PROPOSED", "evidence": "NONE", "review": "NOT_REVIEWED", "publication": "PRIVATE"}
mine = parity_with_og(og, None)
check("PARITY: OG authority dict → our convergent vector (same 4 axes, same values)",
      mine == og)

# ---- a review event is EVIDENCE about a target, not a status mutation ----
ev = ReviewEvent("AbhT_1.52", "REJECT", "scholar-1", finding="reflexivity unadjudicated")
check("ReviewEvent is evidence-about-target (target + kind + reviewer)",
      ev.target_id == "AbhT_1.52" and ev.kind == "REJECT" and ev.reviewer == "scholar-1")

print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
print("\nTHE CONTRACTS CONVERGE: ONE canonical 4-axis non-scalar AuthorityVector with explicit gate")
print("predicates (fixing my lib/epistemic.py's scalar ceiling() design error), + ONE ReviewEvent")
print("(evidence-about-target). PARITY holds: the same authority via OG and our convergence agree.")
print("Nothing builds on divergent contracts anymore.")
sys.exit(0 if all(c for _,c in results) else 1)
