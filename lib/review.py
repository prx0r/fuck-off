"""lib/review.py — the herdr-style adversarial review state machine (Layer 05/08).

Borrowed from herdr-workflow (`adversarial_review.rs`), simplified + integrated with our epistemic
envelope. Deterministic reducer: nothing promotes without evidence; only a human reaches ADJUDICATED.
Maps to our SPEC-02 epistemic_ceiling ladder.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional


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


class FindingSeverity:
    BLOCKING = "BLOCKING"
    NON_BLOCKING = "NON_BLOCKING"


@dataclass
class ReviewFinding:
    finding_id: str
    owner: str
    severity: str = FindingSeverity.BLOCKING
    evidence: str = ""
    status: str = FindingStatus.OPEN
    version: int = 1


@dataclass
class ReviewState:
    object_id: str
    phase: str = ReviewPhase.AWAITING
    findings: list = field(default_factory=list)

    def blocking_findings(self):
        return [f for f in self.findings if f.severity == FindingSeverity.BLOCKING
                and f.status in (FindingStatus.OPEN, FindingStatus.FIXED_PENDING)]


def reducer(state: ReviewState, *, evidence_ok: bool, human_approves: bool = False,
            new_finding: Optional[ReviewFinding] = None) -> str:
    """Pure deterministic transition (herdr-style). Returns the next phase."""
    if new_finding:
        state.findings.append(new_finding)
    if human_approves:
        state.phase = ReviewPhase.HUMAN_OVERRIDE
        return state.phase
    if state.phase == ReviewPhase.AWAITING:
        state.phase = ReviewPhase.REVIEWING if evidence_ok else ReviewPhase.CORRECTION
    elif state.phase == ReviewPhase.REVIEWING:
        state.phase = ReviewPhase.CORRECTION if state.blocking_findings() else ReviewPhase.ALIGNED
    elif state.phase == ReviewPhase.CORRECTION:
        state.phase = ReviewPhase.REVIEWING if evidence_ok else ReviewPhase.CORRECTION
    return state.phase


# ---- map epistemic_ceiling -> review phase (our SPEC-02 integration) ----
CEILING_TO_PHASE = {
    "MACHINE_PROPOSED": ReviewPhase.CORRECTION,                # needs evidence to promote
    "SCHOLARLY_CORROBORATED_PRELIMINARY": ReviewPhase.REVIEWING,
    "SCHOLARLY_CORROBORATED": ReviewPhase.ALIGNED,
    "INDEPENDENT_REVIEWED": ReviewPhase.ALIGNED,
    "ADJUDICATED": ReviewPhase.HUMAN_OVERRIDE,
}


def phase_from_ceiling(ceiling: str) -> str:
    return CEILING_TO_PHASE.get(ceiling, ReviewPhase.AWAITING)


def promote(state: ReviewState, target_ceiling: str) -> bool:
    """Can this object reach target_ceiling? Only human override reaches ADJUDICATED."""
    if target_ceiling == "ADJUDICATED":
        return state.phase == ReviewPhase.HUMAN_OVERRIDE
    if target_ceiling in ("SCHOLARLY_CORROBORATED", "INDEPENDENT_REVIEWED"):
        return state.phase == ReviewPhase.ALIGNED
    return True
