"""lib/certificate.py — Certification Weight (Verified-Statement-Marketplace mechanism).

The compounding verification metric: a claim's certification weight rises with verifier strength,
independent consensus, downstream load-bearing, and time survived. The network-effect moat encoded in
the data — the unit of value in a Verified-Statement-Marketplace.

  CW = kill_rate × consensus × (1 + downstream_load) × (1 + time_signed)

Each factor comes from a VALIDATED subsystem:
  verifier_kill_rate    <- mutation-testing (0..1)
  consensus_multiplicity <- cross-review (how many independent reviewers confirmed)
  downstream_load       <- counterfactual engine (how much collapses if it's wrong)
  time_signed           <- temporal validity / signed-root survival
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Certification:
    claim_id: str
    verifier_kill_rate: float = 1.0
    consensus_multiplicity: int = 1
    downstream_load: int = 1
    time_signed_years: float = 1.0

    def weight(self) -> float:
        """Monotonic + compounding certification weight."""
        return (self.verifier_kill_rate * self.consensus_multiplicity
                * (1 + self.downstream_load) * (1 + self.time_signed_years))

    def to_dict(self) -> dict:
        return {"claim_id": self.claim_id, "certification_weight": round(self.weight(), 3),
                "verifier_kill_rate": self.verifier_kill_rate,
                "consensus_multiplicity": self.consensus_multiplicity,
                "downstream_load": self.downstream_load,
                "time_signed_years": self.time_signed_years}


def project_weight(cert: Certification, years: float) -> float:
    """Project CW forward in time, compounding downstream_load as use accumulates."""
    c = Certification(cert.claim_id, cert.verifier_kill_rate, cert.consensus_multiplicity,
                      int(cert.downstream_load * years), cert.time_signed_years + years)
    return c.weight()


def value_of_consensus(cert: Certification, n: int) -> float:
    """CW if the claim had n independent confirmations (bias-robust verification is worth more)."""
    c = Certification(cert.claim_id, cert.verifier_kill_rate, n,
                      cert.downstream_load, cert.time_signed_years)
    return c.weight()
