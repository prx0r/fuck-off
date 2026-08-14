"""lib/design_provenance.py — the design-decision provenance (DEV_PLAN §1.4, Self-Proving full form).

Extends lib/system_provenance.py (which signs KERNELS) to sign DESIGN DECISIONS: every design choice ->
a signed nanopub capturing the rationale, the alternatives considered (and why rejected), and the
decision itself. This is the "Self-Proving System" vision (SPEC-14/VISION-SELF-PROVING) applied to the
OS's own construction: "the design-provenance nanopub."

The point: when a later agent asks "why did you choose X over Y?", it resolves to a signed record with
the rationale + rejected alternatives + the decision's validation. This makes the whole system's design
auditable and self-proving — the OS applies its own provenance machinery to the decisions that built it.
"""
from __future__ import annotations
import hashlib
import json


def _sha(b):
    return hashlib.sha256(b.encode() if isinstance(b, str) else b).hexdigest()[:16]


class DesignDecision:
    """A single signed design decision: what was decided, the rationale, the alternatives rejected."""

    def __init__(self, decision_id, topic, decision, rationale, alternatives=None, validator=None,
                 layer="", created_by="agentgraph"):
        self.decision_id = decision_id
        self.topic = topic
        self.decision = decision
        self.rationale = rationale
        self.alternatives = alternatives or []   # [{choice, rejected_reason}]
        self.validator = validator or ""          # the validate-*.py that proves it (if any)
        self.layer = layer
        self.created_by = created_by

    def _canonical(self):
        return json.dumps({
            "decision_id": self.decision_id, "topic": self.topic, "decision": self.decision,
            "rationale": self.rationale, "alternatives": self.alternatives,
            "validator": self.validator, "layer": self.layer, "created_by": self.created_by,
        }, sort_keys=True)

    def sign(self):
        """Return a signed nanopub over this decision (cosign-style: hash the canonical record)."""
        payload = self._canonical()
        return {"decision_id": self.decision_id, "topic": self.topic, "decision": self.decision,
                "rationale": self.rationale, "alternatives": self.alternatives,
                "validator": self.validator, "layer": self.layer, "created_by": self.created_by,
                "signature": _sha("design-decision:" + payload)}

    def verify(self, signed):
        """Verify a signed decision nanopub (tamper detection)."""
        payload = json.dumps({
            "decision_id": signed["decision_id"], "topic": signed["topic"],
            "decision": signed["decision"], "rationale": signed["rationale"],
            "alternatives": signed["alternatives"], "validator": signed["validator"],
            "layer": signed["layer"], "created_by": signed["created_by"],
        }, sort_keys=True)
        return _sha("design-decision:" + payload) == signed["signature"]


class DesignProvenance:
    """The ledger of signed design decisions (the Self-Proving System's design nanopubs)."""

    def __init__(self):
        self.decisions = {}   # decision_id -> signed nanopub
        self._shas = {}

    def record(self, decision: DesignDecision) -> dict:
        signed = decision.sign()
        self.decisions[decision.decision_id] = signed
        self._shas[decision.decision_id] = decision._canonical()
        return signed

    def verify(self, decision_id):
        """Verify a recorded design decision is untampered."""
        signed = self.decisions.get(decision_id)
        if not signed:
            return False
        return DesignDecision(
            decision_id, signed["topic"], signed["decision"], signed["rationale"],
            signed["alternatives"], signed["validator"], signed["layer"], signed["created_by"],
        ).verify(signed)

    def why(self, decision_id):
        """Resolve 'why did you decide <X>?' -> rationale + alternatives + validator (self-doc)."""
        signed = self.decisions.get(decision_id)
        if not signed:
            return None
        return {"decision_id": decision_id, "topic": signed["topic"], "decision": signed["decision"],
                "rationale": signed["rationale"], "alternatives": signed["alternatives"],
                "validator": signed["validator"], "layer": signed["layer"],
                "verifies": self.verify(decision_id)}

    def root(self):
        """A signed Merkle-style root over ALL design decisions (self-proving)."""
        return _sha("|".join(f"{k}:{v['signature']}" for k, v in sorted(self.decisions.items())))

    def summary(self):
        return {"decisions": len(self.decisions),
                "verified": sum(1 for d in self.decisions if self.verify(d)),
                "with_validator": sum(1 for d in self.decisions if self.decisions[d]["validator"])}
