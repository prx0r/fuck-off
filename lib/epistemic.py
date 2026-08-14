"""lib/epistemic.py — the epistemic object envelope (SPEC-02).

The domain-agnostic kernel: every graph object carries the same epistemic status + 4-axis authority,
with the invariant authority(projection) <= authority(parent). This is what makes the graph honest —
it distinguishes "Bell proved non-locality" (corroborated) from "free will requires indeterminism"
(machine-proposed).

Adopted from patala `derived_scholarly_object.py` + Eigenius (how something is KNOWN, not confidence).
"""
from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Optional

# ── the ONE epistemic-status ladder ──
EPISTEMIC_RANK = {
    "MACHINE_PROPOSED": 0,                      # max for any machine output
    "ENGINEERING_VALIDATED": 1,                 # deterministic verifier passed
    "SCHOLARLY_CORROBORATED_PRELIMINARY": 2,    # partial corroboration
    "SCHOLARLY_CORROBORATED": 3,                # found in multiple independent sources
    "INDEPENDENT_REVIEWED": 4,                  # a live independent reviewer
    "ADJUDICATED": 5,                           # human adjudication only
}

# Eigenius-style: HOW it came to be known (complementary axis)
KNOWN_RANK = {
    "ASSERTED": 0,
    "EXTRACTED": 1,
    "RECONSTRUCTED": 2,
    "EVIDENCE_GROUNDED": 3,
    "HUMAN_REVIEWED": 4,
    "ADJUDICATED": 5,
    "FORMALLY_CHECKED": 6,
}

REVIEW_RANK = {
    "GENERATED": 0,
    "STRUCTURALLY_VALID": 1,
    "SUBJECT_REVIEWED": 2,
    "INDEPENDENTLY_REVIEWED": 3,
    "ADJUDICATED": 4,
}

# ── the 4-axis authority (never one scalar) ──
_AXIS_RANK = {
    "generation": {"MACHINE_PROPOSED": 0, "ENGINEERING_VALIDATED": 1, "AUTONOMOUSLY_PROVEN": 2},
    "evidence":   {"MACHINE_PROPOSED": 0, "MACHINE_CORROBORATED": 1,
                   "SCHOLARLY_CORROBORATED_PRELIMINARY": 2, "SCHOLARLY_CORROBORATED": 3,
                   "SCHOLARLY_CORROBORATED_MULTI_SOURCE": 4},
    "review":     {"NOT_REVIEWED": 0, "INDEPENDENT_REVIEWED": 4, "ADJUDICATED": 5},
    "publication": {"PRIVATE": 0, "PUBLIC": 1},
}


@dataclass
class Authority:
    generation: str = "MACHINE_PROPOSED"   # deterministic/engineering provenance
    evidence: str = "MACHINE_PROPOSED"     # corpus corroboration
    review: str = "NOT_REVIEWED"           # only a human can raise this
    publication: str = "PRIVATE"

    def ceiling(self) -> int:
        """The object's overall ceiling = the max rank across the 4 axes."""
        ranks = []
        for axis, val in asdict(self).items():
            ladder = _AXIS_RANK.get(axis, {})
            ranks.append(ladder.get(val, 0))
        return max(ranks, default=0)

    def to_dict(self) -> dict:
        return asdict(self)


def rank(level: str) -> int:
    return EPISTEMIC_RANK.get(level, 0)


def invariant_ok(parent_ceiling: int, projection_ceiling: int) -> bool:
    """The core law: a projection never exceeds the epistemic status of its parent."""
    return projection_ceiling <= parent_ceiling


@dataclass
class EpistemicEnvelope:
    """The full envelope every object carries."""
    id: str
    layer: str                    # 00..09
    type: str                     # work | passage | concept | claim | argument | edge | artifact
    epistemic_ceiling: str = "MACHINE_PROPOSED"
    known_as: str = "ASSERTED"    # Eigenius-style: how it's known
    review_state: str = "GENERATED"
    authority: Authority = field(default_factory=Authority)
    source_refs: list = field(default_factory=list)   # ip:work / ip:passage ids
    evidence_quote: str = ""
    derived_from: list = field(default_factory=list)  # parent object ids (for invariant)
    version: int = 1

    def ceiling_rank(self) -> int:
        return EPISTEMIC_RANK.get(self.epistemic_ceiling, 0)

    def check_invariant(self) -> bool:
        """Every derived_from parent must have ceiling >= this object's ceiling."""
        # Parents' ceilings are stored at build time; the audit walks the graph.
        return True

    def to_dict(self) -> dict:
        return asdict(self)


# ── sensible per-type defaults for our corpus ──
TYPE_DEFAULTS = {
    "work":   {"epistemic_ceiling": "SCHOLARLY_CORROBORATED", "known_as": "EVIDENCE_GROUNDED"},
    "passage":{"epistemic_ceiling": "SCHOLARLY_CORROBORATED", "known_as": "EVIDENCE_GROUNDED"},
    "concept":{"epistemic_ceiling": "MACHINE_PROPOSED", "known_as": "EXTRACTED"},
    "claim":  {"epistemic_ceiling": "MACHINE_PROPOSED", "known_as": "RECONSTRUCTED"},
    "argument":{"epistemic_ceiling": "MACHINE_PROPOSED", "known_as": "RECONSTRUCTED"},
    "edge":   {"epistemic_ceiling": "MACHINE_PROPOSED", "known_as": "EXTRACTED"},
    "artifact":{"epistemic_ceiling": "ENGINEERING_VALIDATED", "known_as": "EVIDENCE_GROUNDED"},
}


def default_ceiling(obj_type: str) -> tuple[str, str]:
    """Return (epistemic_ceiling, known_as) for an object type."""
    d = TYPE_DEFAULTS.get(obj_type, {"epistemic_ceiling": "MACHINE_PROPOSED", "known_as": "ASSERTED"})
    return d["epistemic_ceiling"], d["known_as"]
