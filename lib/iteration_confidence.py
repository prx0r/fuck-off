"""lib/iteration_confidence.py — iteration-verified confidence (stolen from hound, scabench-org).

Hound's DynamicNode carries observations (verified) vs assumptions (unverified) + `iteration: int`
(how many independent passes confirmed a claim). The insight: a claim confirmed across N independent
passes is STRONGER than the same claim confirmed once, even at the same epistemic ceiling.

This kernel adds that signal to our organism:
  - each independent confirmation of a claim increments its iteration count
  - the "verified strength" of a claim = f(ceiling, iteration, corroborations)
  - a claim with higher iteration is preferred at the same ceiling (convergence = fundamentality)

This composes with evidence_ledger (ConfidenceKind) and epistemic.py (ceiling). The three-version method
(translation_variant) and the cross-source flywheel (alignment_flywheel) both naturally produce
independent confirmations — this kernel makes that convergence measurable.
"""
from __future__ import annotations
from evidence_ledger import ConfidenceKind, EvidenceLedger


class ClaimStatus:
    """The iteration-verified state of a claim (how many independent passes confirmed it)."""
    def __init__(self, claim_id, ceiling, kind=ConfidenceKind.LLM):
        self.claim_id = claim_id
        self.ceiling = ceiling                 # the epistemic ceiling (MACHINE_PROPOSED..ADJUDICATED)
        self.kind = kind
        self.observations = []                 # verified confirmations (source, iteration)
        self.assumptions = []                  # unverified claims (not yet confirmed)
        self.iteration = 0                     # how many INDEPENDENT passes confirmed it

    def confirm(self, source, ceiling_override=None):
        """An independent confirmation (a second/third source or pass reaches the same claim)."""
        if ceiling_override:
            self.ceiling = max(self.ceiling, ceiling_override, key=lambda c: _rank(c))
        self.observations.append({"source": source, "iteration": self.iteration + 1})
        self.iteration += 1
        return self.iteration

    def assume(self, source):
        """An unverified assumption (recorded, not confirmed)."""
        self.assumptions.append({"source": source})
        return len(self.assumptions)

    def verified_strength(self):
        """f(ceiling, iteration): how strong the confirmation is. Higher iteration = stronger."""
        return self.iteration + (0.0 if self.iteration == 0 else _rank(self.ceiling) / 10.0)


def _rank(ceiling):
    return {"MACHINE_PROPOSED": 1, "SCHOLARLY_CORROBORATED_PRELIMINARY": 2,
            "SCHOLARLY_CORROBORATED": 3, "INDEPENDENT_REVIEWED": 4, "ADJUDICATED": 5}.get(ceiling, 0)


class IterationConfidence:
    """The belief-evolution ledger: iteration-verified claims, convergence-detection."""

    def __init__(self):
        self.claims = {}

    def track(self, claim_id, ceiling, kind=ConfidenceKind.LLM):
        c = self.claims.setdefault(claim_id, ClaimStatus(claim_id, ceiling, kind))
        return c

    def confirm(self, claim_id, source, ceiling_override=None):
        return self.track(claim_id, self._ceiling_of(claim_id)).confirm(source, ceiling_override)

    def _ceiling_of(self, claim_id):
        return self.claims.get(claim_id).ceiling if claim_id in self.claims else "MACHINE_PROPOSED"

    def convergence(self):
        """The claims with the HIGHEST iteration (confirmed by the most independent passes) =
        the most fundamental (convergence = fundamentality, the PrimitiveRobustness idea)."""
        return sorted(self.claims.values(), key=lambda c: -c.verified_strength())

    def most_fundamental(self, n=3):
        return [c.claim_id for c in self.convergence()[:n]]

    def report(self):
        return {cid: {"iteration": c.iteration, "ceiling": c.ceiling,
                      "strength": round(c.verified_strength(), 2),
                      "observations": len(c.observations), "assumptions": len(c.assumptions)}
                for cid, c in self.claims.items()}
