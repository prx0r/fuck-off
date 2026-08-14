"""lib/canonical_contracts.py — THE CONTRACT CONVERGENCE (BUILD-CONTRACTS-CONVERGENCE, the #1 build).

The audit + the shared BUILD directives found the schema-drift at the CONTRACT level: ~6 divergent
ReviewEvent/Authority definitions across the two repos (my lib/review + lib/epistemic vs OG patala's
source-evidence/schema + patala_core/objects + authority + pipeline/review_engine).

This is the convergence: ONE canonical AuthorityVector + ReviewEvent, adopted from the OG design
(python/patala_core/authority.py — the 4-axis, NON-SCALAR, gate-predicate form) and unified with my
epistemic envelope + review reducer. The anti-theatre rule: nothing builds on divergent contracts.

KEY FIX vs my lib/epistemic.py: my Authority.ceiling() = max rank (a SCALAR). The OG design explicitly
rejects that — authority is a 4-axis VECTOR with explicit gate predicates, never a single rank. This
converges to the correct design.
"""
from __future__ import annotations
from enum import Enum


# ---- the canonical 4-axis Authority (non-scalar, from OG patala_core/authority.py) ----
class Gen(Enum):
    MACHINE_PROPOSED = "MACHINE_PROPOSED"
    ENGINEERING_VALIDATED = "ENGINEERING_VALIDATED"
    EDITORIAL = "EDITORIAL"

class Ev(Enum):
    NONE = "NONE"
    SCHOLARLY_CORROBORATED = "SCHOLARLY_CORROBORATED"
    DISPUTED = "DISPUTED"
    CORROBORATION_OPEN = "CORROBORATION_OPEN"

class Rev(Enum):
    NOT_REVIEWED = "NOT_REVIEWED"
    SINGLE_REVIEWED = "SINGLE_REVIEWED"
    ADJUDICATED = "ADJUDICATED"

class Pub(Enum):
    PRIVATE = "PRIVATE"
    INTERNAL = "INTERNAL"
    PUBLIC = "PUBLIC"


class AuthorityVector:
    """Four independent axes. NO total order across them — gates are explicit predicates."""
    def __init__(self, generation=Gen.MACHINE_PROPOSED, evidence=Ev.NONE,
                 review=Rev.NOT_REVIEWED, publication=Pub.PRIVATE):
        self.generation = generation if isinstance(generation, Gen) else Gen(generation)
        self.evidence = evidence if isinstance(evidence, Ev) else Ev(evidence)
        self.review = review if isinstance(review, Rev) else Rev(review)
        self.publication = publication if isinstance(publication, Pub) else Pub(publication)

    def eligible_for_publication(self) -> bool:
        return (self.review in (Rev.ADJUDICATED, Rev.SINGLE_REVIEWED)
                and self.generation in (Gen.ENGINEERING_VALIDATED, Gen.EDITORIAL))

    def eligible_for_scholar_review(self) -> bool:
        return self.generation in (Gen.MACHINE_PROPOSED, Gen.ENGINEERING_VALIDATED)

    def eligible_for_education(self) -> bool:
        return self.publication == Pub.PUBLIC and self.review != Rev.NOT_REVIEWED

    def display_badge(self) -> str:
        parts = []
        if self.generation == Gen.ENGINEERING_VALIDATED: parts.append("machine-validated")
        elif self.generation == Gen.MACHINE_PROPOSED: parts.append("machine-generated")
        if self.evidence == Ev.SCHOLARLY_CORROBORATED: parts.append("scholarly evidence")
        if self.review == Rev.ADJUDICATED: parts.append("adjudicated")
        elif self.review == Rev.SINGLE_REVIEWED: parts.append("single-reviewed")
        else: parts.append("not human-reviewed")
        if self.publication == Pub.PUBLIC: parts.append("public")
        return " · ".join(parts) or "no authority recorded"

    def to_dict(self) -> dict:
        return {"generation": self.generation.value, "evidence": self.evidence.value,
                "review": self.review.value, "publication": self.publication.value}


# ---- the canonical ReviewEvent (evidence ABOUT a target, never a status mutation) ----
class ReviewEvent:
    def __init__(self, target_id, kind, reviewer, finding=None, verdict=None):
        self.target_id = target_id
        self.kind = kind            # REJECT | REVISE | ACCEPT | ABSTAIN | EVIDENCE_ATTACHED
        self.reviewer = reviewer
        self.finding = finding
        self.verdict = verdict


# ---- the convergence: my envelope uses the canonical 4-axis vector (not a scalar rank) ----
class CanonicalEnvelope:
    """The unified envelope: canonical AuthorityVector + honest ceiling + review state."""
    def __init__(self, object_id, obj_type, ceiling="MACHINE_PROPOSED",
                 authority=None, source_refs=None):
        self.id = object_id
        self.type = obj_type
        self.epistemic_ceiling = ceiling
        self.authority = authority or AuthorityVector()   # the 4-axis canonical vector
        self.source_refs = source_refs or []
        self.review_state = "GENERATED"

    def eligible_for_publication(self): return self.authority.eligible_for_publication()
    def eligible_for_scholar_review(self): return self.authority.eligible_for_scholar_review()
    def eligible_for_education(self): return self.authority.eligible_for_education()


def parity_with_og(og_authority_dict, my_envelope_authority):
    """PARITY: the same authority, represented via OG and via our convergence, must agree."""
    # OG: {generation, evidence, review, publication}  -> our AuthorityVector
    v = AuthorityVector(**og_authority_dict)
    return v.to_dict()
