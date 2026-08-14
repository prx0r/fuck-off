"""lib/evidence_ledger.py — typed evidence events + kind-aware confidence (GEM 6.5 + fojin).

GEM 6.5 (migration/v2/GEMS.md): "`evidence_ok: bool` is too lossy. Use typed events (EvidenceAttached,
ContradictionRaised, FindingResolved, AdjudicationRecorded). The reducer decides what events imply;
agents submit claims, not state."

fojin (migration/v2/EXTERNAL-REPOS.md): "`confidence_kind` discipline — every confidence value is only
meaningful alongside its kind (llm/import_flag/catalog). Never compare incomparable confidence numbers."

This kernel fuses both: an evidence LEDGER of TYPED events (not a bool), where every confidence carries
its KIND. The reducer consumes typed events, not a lossy bool. Two numbers with different kinds are
never summed/compared without their kind. This is the correctness win for multi-source verification.
"""
from __future__ import annotations
import enum, hashlib


class EventType(enum.Enum):
    EVIDENCE_ATTACHED = "EvidenceAttached"
    CONTRADICTION_RAISED = "ContradictionRaised"
    FINDING_RESOLVED = "FindingResolved"
    ADJUDICATION_RECORDED = "AdjudicationRecorded"
    CITATION_VERIFIED = "CitationVerified"
    CITATION_PHANTOM = "CitationPhantom"


class ConfidenceKind(enum.Enum):
    LLM = "llm"                # model-generated (weakest, needs review)
    CATALOG = "catalog"        # authoritative catalog/curated (strong)
    IMPORT_FLAG = "import_flag"  # imported, a flag not a real confidence (NOT comparable)
    EXPERT = "expert"          # human-adjudicated (strongest)
    FLYWHEEL_VERIFIED = "flywheel-verified"  # promoted through human-in-the-loop


class EvidenceEvent:
    """A typed evidence event (never a lossy bool). Agents submit events, not state."""
    def __init__(self, etype, target, confidence=None, kind=None, source=None, note=""):
        self.type = etype
        self.target = target
        self.confidence = confidence
        self.kind = kind                      # ConfidenceKind (fojin discipline)
        self.source = source
        self.note = note
        self.id = hashlib.sha256(f"{etype.value}:{target}:{source}".encode()).hexdigest()[:12]


class EvidenceLedger:
    """The append-only evidence event ledger. Reducers consume typed events, not bools."""

    def __init__(self):
        self.events = []
        self._confidence_by_target = {}

    def attach(self, target, confidence, kind, source, note=""):
        ev = EvidenceEvent(EventType.EVIDENCE_ATTACHED, target, confidence, kind, source, note)
        self.events.append(ev)
        self._confidence_by_target.setdefault(target, []).append((confidence, kind))
        return ev

    def contradict(self, target, source, note=""):
        ev = EvidenceEvent(EventType.CONTRADICTION_RAISED, target, None, None, source, note)
        self.events.append(ev)
        return ev

    def resolve_finding(self, target, source, note=""):
        ev = EvidenceEvent(EventType.FINDING_RESOLVED, target, None, None, source, note)
        self.events.append(ev)
        return ev

    def adjudicate(self, target, verdict, kind=ConfidenceKind.EXPERT, source="scholar"):
        ev = EvidenceEvent(EventType.ADJUDICATION_RECORDED, target, 1.0, kind, source,
                           f"verdict={verdict}")
        self.events.append(ev)
        return ev

    def verify_citation(self, target, source, phantom=False):
        etype = EventType.CITATION_PHANTOM if phantom else EventType.CITATION_VERIFIED
        ev = EvidenceEvent(etype, target, None, None, source, "phantom" if phantom else "verified")
        self.events.append(ev)
        return ev

    # ---- kind-aware confidence: NEVER compare incomparable kinds ----
    def kind_rank(self, kind):
        return {ConfidenceKind.IMPORT_FLAG: 0, ConfidenceKind.LLM: 1, ConfidenceKind.CATALOG: 2,
                ConfidenceKind.FLYWHEEL_VERIFIED: 3, ConfidenceKind.EXPERT: 4}.get(kind, 0)

    def best_supported(self, target, min_kind=ConfidenceKind.CATALOG):
        """The strongest (kind, confidence) for a target, honest about its kind."""
        entries = self._confidence_by_target.get(target, [])
        if not entries:
            return None
        entries.sort(key=lambda ck: self.kind_rank(ck[1]), reverse=True)
        conf, kind = entries[0]
        if self.kind_rank(kind) < self.kind_rank(min_kind):
            return None                      # not yet supported at the required strength
        return {"confidence": conf, "kind": kind.value}

    def state_of(self, target):
        """The reducer's derived state from typed events (agents submit events, not state)."""
        contradicted = any(e.type == EventType.CONTRADICTION_RAISED and e.target == target
                           for e in self.events)
        adjudicated = [e for e in self.events
                       if e.type == EventType.ADJUDICATION_RECORDED and e.target == target]
        supported = self.best_supported(target)
        if adjudicated:
            return {"target": target, "phase": "ADJUDICATED", "verdict": adjudicated[-1].note}
        if contradicted:
            return {"target": target, "phase": "CONTRADICTED", "support": supported}
        if supported:
            return {"target": target, "phase": "EVIDENCED", "support": supported}
        return {"target": target, "phase": "UNSUPPORTED", "support": None}
