"""lib/discovery.py — Research Value Score (What-If Machine mechanism).

Prioritizes research by expected value: claims that are load-bearing, weakly verified, and contested
are the highest-value research targets. Turns the epistemic OS from a record into a research strategist.

  ResearchValue = load_bearing × (1 − verifier_strength) × crux_pressure

Factors from VALIDATED subsystems:
  load_bearing       <- counterfactual engine (downstream collapse if wrong)
  verifier_strength  <- mutation-testing kill-rate (1 − strength = how unverified it is)
  crux_pressure      <- crux-compiler (how much separates rival positions)
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ResearchTarget:
    claim_id: str
    load_bearing: int = 1            # downstream claims that collapse if wrong
    verifier_strength: float = 0.5   # mutation kill-rate (0..1)
    crux_pressure: float = 0.5       # how contested / how much separates rivals (0..1)

    def research_value(self) -> float:
        """Higher = more valuable to research (load-bearing + unverified + contested)."""
        return self.load_bearing * (1 - self.verifier_strength) * (1 + self.crux_pressure)

    def to_dict(self) -> dict:
        return {"claim_id": self.claim_id, "research_value": round(self.research_value(), 3),
                "load_bearing": self.load_bearing,
                "unverified": round(1 - self.verifier_strength, 3),
                "crux_pressure": self.crux_pressure}


def prioritize(targets: list) -> list:
    """Rank research targets by ResearchValue (highest first)."""
    return sorted(targets, key=lambda t: -t.research_value())


def proposed_research_queue(targets: list, min_value: float = 0.0) -> list:
    """The proposed-research queue: targets worth attacking (above a value threshold)."""
    return [t for t in targets if t.research_value() >= min_value]
