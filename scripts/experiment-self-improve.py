#!/usr/bin/env python3
"""experiment-self-improve.py — self-improvement as PR (not mutation) applied to our epistemic engine.

Borrowed from BerriAI/self-improving-agent (cloned): the agent proposes a MINIMAL DIFF, a human
approves, a PR opens. We apply this to epistemic objects — an agent proposes a claim/ceiling change,
it's wrapped as a Proposal with a diff + reason, and our herdr human-gate decides. Self-improvement
never mutates in place; it's a reviewed, versioned, atomic change (SPEC-12: PR not mutation).
"""
import os, sys, json, hashlib
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from review import reducer, ReviewState, ReviewPhase

# ---- a Proposal (self-improving-agent's core object) ----
class Proposal:
    """Minimal diff + reason; requires human approval to apply."""
    def __init__(self, object_id, field, old, new, reason):
        self.object_id = object_id
        self.field = field
        self.old = old
        self.new = new
        self.reason = reason
        self.approved = False
    def diff(self):
        return f"- {self.field}: {self.old}\n+ {self.field}: {self.new}\n  reason: {self.reason}"
    def apply(self):
        if not self.approved:
            raise RuntimeError("cannot apply unapproved proposal")
        return {"id": self.object_id, self.field: self.new}

# ---- the epistemic object being improved ----
claim = {"id": "C1", "text": "Free will requires indeterminism", "ceiling": "MACHINE_PROPOSED"}

print("=== SELF-IMPROVEMENT AS PR (not mutation) ===\n")

# Agent proposes: this claim should be corroborated (it found supporting evidence)
prop = Proposal("C1", "ceiling", "MACHINE_PROPOSED", "SCHOLARLY_CORROBORATED",
                reason="2 independent sources now support the indeterminism requirement")
print(f"agent PROPOSES a diff:")
print(f"{prop.diff()}")

# ---- the herdr human-gate decides (self-improving-agent's approval = our reducer gate) ----
st = ReviewState("C1")
# the proposal goes through review: evidence present, but is it corroborated?
# our reducer: a MACHINE_PROPOSED claim proposing to jump to CORROBORATED needs the review to confirm
reducer(st, evidence_ok=True)   # AWAITING -> REVIEWING
# blocking finding: the 2 sources are the same author (not independent) -> challenge the proposal
from scholar_review import Finding
st.findings.append(Finding("f1", "reviewer", severity="BLOCKING", category="evidence",
                           evidence="sources not independent"))
reducer(st, evidence_ok=True)   # REVIEWING -> CORRECTION
print(f"\nherdr gate: {st.phase} — the proposal is CHALLENGED (sources not independent)")

if st.phase == ReviewPhase.CORRECTION:
    print("=> proposal NOT auto-applied. It returns to the agent for a better diff.")
    print("   Self-improvement never mutates in place; a weak proposal is rejected, not force-applied.")
else:
    prop.approved = True
    applied = prop.apply()
    print(f"proposal approved and applied: {applied}")

print("\n=== INSIGHT ===")
print("self-improving-agent's 'propose minimal diff -> human approves -> PR' maps onto our herdr gate:")
print("an agent's self-improvement proposal is a REVIEWED, VERSIONED, ATOMIC change — never a silent")
print("mutation. The reducer gates it; only a strong, independently-evidenced proposal survives to")
print("application. This is safe self-improvement for the epistemic engine (SPEC-12: PR not mutation).")
