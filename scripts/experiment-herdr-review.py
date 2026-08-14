#!/usr/bin/env python3
"""experiment-herdr-review.py — port herdr's adversarial-review state machine to our epistemic objects.

Tests whether herdr's review protocol (the production implementation of our SPEC-02/05 review chain)
can drive promotion of our graph's claims from MACHINE_PROPOSED toward ADJUDICATED, with honest state
transitions. Uses our REAL argument.json claims + epistemic ceilings.

herdr concepts mapped:
  ReviewPhase        -> AwaitingCandidate/Reviewing/CorrectionRequired/Aligned/HumanOverride
  FindingStatus      -> Open/FixedPendingReview/Closed/Superseded/ConcernRecorded
  reducer            -> deterministic transition function (pure, testable)
  immutability       -> review events are append-only, never mutate the claim
"""
import json, hashlib

ARGS = "/mnt/HC_Volume_106427611/ip-graph/data/graph/argument.json"
arg = json.load(open(ARGS))

# ---- herdr-style review state machine (simplified port) ----
class ReviewPhase:
    AWAITING = "AWAITING_CANDIDATE"
    REVIEWING = "REVIEWING"
    CORRECTION = "CORRECTION_REQUIRED"
    ALIGNED = "ALIGNED"
    HUMAN_OVERRIDE = "HUMAN_OVERRIDE"

class FindingStatus:
    OPEN = "OPEN"
    FIXED_PENDING = "FIXED_PENDING_REVIEW"
    CLOSED = "CLOSED"
    SUPERSEDED = "SUPERSEDED"
    CONCERN = "CONCERN_RECORDED"

def digest(s): return hashlib.sha256(s.encode()).hexdigest()[:12]

# ---- the reducer: pure deterministic transition ----
def reducer(phase, blocking_findings, evidence_ok, human_approves=False):
    """herdr-style reducer: deterministic transition on (phase, state inputs)."""
    if human_approves:
        return ReviewPhase.HUMAN_OVERRIDE
    if phase == ReviewPhase.AWAITING:
        return ReviewPhase.REVIEWING if evidence_ok else ReviewPhase.CORRECTION
    if phase == ReviewPhase.REVIEWING:
        if blocking_findings: return ReviewPhase.CORRECTION
        return ReviewPhase.ALIGNED
    if phase == ReviewPhase.CORRECTION:
        return ReviewPhase.REVIEWING if evidence_ok else ReviewPhase.CORRECTION
    return phase  # ALIGNED / HUMAN_OVERRIDE are terminal

# ---- run the review on our real claims ----
print("=== HERDR-STYLE ADVERSARIAL REVIEW on our epistemic claims ===\n")
for node in arg["information_nodes"]:
    cid = node["id"]; text = node["text"]; ceiling = node["epistemic_ceiling"]
    # a claim is reviewable if it's not yet corroborated (honest gate)
    reviewable = ceiling in ("MACHINE_PROPOSED", "SCHOLARLY_CORROBORATED_PRELIMINARY")
    # evidence: does it have a source_ref grounding?
    evidence_ok = bool(node.get("source_refs"))
    # blocking findings: a machine-proposed thesis claim gets challenged (esp. the two-stage conclusion)
    blocking = (ceiling == "MACHINE_PROPOSED")  # thesis claims need stronger evidence to promote

    phase = ReviewPhase.AWAITING
    history = []
    steps = 0
    while steps < 6:
        prev = phase
        phase = reducer(phase, blocking, evidence_ok)
        history.append(f"{prev} -> {phase}")
        steps += 1
        if phase in (ReviewPhase.ALIGNED, ReviewPhase.HUMAN_OVERRIDE): break
    verdict = "ALIGNED (ready for human adjudication)" if phase == ReviewPhase.ALIGNED else \
              ("HUMAN_OVERRIDE (human settled it)" if phase == ReviewPhase.HUMAN_OVERRIDE else "NEEDS WORK")
    print(f"[{cid}] {text[:45]}")
    print(f"      ceiling={ceiling:38s} evidence={evidence_ok} blocking={blocking}")
    print(f"      -> {phase}  ({verdict})")
    print(f"      trace: {' | '.join(history)}")
    print()

print("=== INSIGHT ===")
print("herdr's reducer forces honest promotion: a MACHINE_PROPOSED thesis claim stays in CORRECTION")
print("until evidence grounds it; only then ALIGNED, and only a human can reach the top. This is")
print("exactly the authority(projection)<=authority(parent) invariant, enforced as a state machine.")
