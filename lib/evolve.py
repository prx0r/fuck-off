"""lib/evolve.py — the Pāṭala Evolution Loop (candidate population → fitness vector → MAP-Elites).

Borrowed from OpenEvolve (island/MAP-Elites, fitness vector, min-max binning), Axplorer
(candidate population, retain elite+diverse), and our own validated gates (mutation-testing,
cross-review, certification-weight). The mechanism by which Pāṭala improves itself while production
truth stays protected.

  CandidateArtifact → Evaluation → Selection → PromotionGate → canonical

Fitness is a VECTOR (never one scalar), Pareto/archive-based selection preserves meaningful niches
(diversity is epistemically valuable — OpenEvolve's key insight).
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FitnessVector:
    """Multi-dimensional fitness (never one aggregate)."""
    fidelity: float = 0.0      # does it match the source
    coverage: float = 0.0      # how much it covers
    robustness: float = 0.0    # survives mutation/adversarial
    novelty: float = 0.0       # how different from existing
    cost: float = 0.0          # 1 = cheap
    latency: float = 0.0       # 1 = fast

    def to_dict(self):
        return {k: round(v, 3) for k, v in self.__dict__.items()}


@dataclass
class CandidateArtifact:
    """A proposed improvement to some Pāṭala subsystem."""
    id: str
    kind: str                    # translation | argument | retrieval | verifier | prompt
    implementation: str          # the candidate (a strategy, prompt, algorithm config)
    fitness: FitnessVector = field(default_factory=FitnessVector)
    parent_id: Optional[str] = None   # evolution lineage
    mutation: str = ""
    promoted: bool = False

    def to_dict(self):
        return {"id": self.id, "kind": self.kind, "fitness": self.fitness.to_dict(),
                "parent_id": self.parent_id, "mutation": self.mutation, "promoted": self.promoted}


class EliteArchive:
    """MAP-Elites archive: keeps the best candidate per BEHAVIORAL niche.

    Per patalamix review: the niche must be a BEHAVIORAL dimension (literalness, breadth, diversity),
    not an object type. Cells = behavior niches; dominance includes cost+latency; novelty is a
    DIVERSITY dimension (sampled, not unconditionally maximized).
    """
    def __init__(self, niche_fn):
        self.niche_fn = niche_fn       # candidate -> behavioral niche key (e.g. tuple of behavior dims)
        self.cells = {}

    def add(self, cand: CandidateArtifact):
        niche = self.niche_fn(cand)
        if niche not in self.cells:
            self.cells[niche] = cand
        elif self._dominates(cand, self.cells[niche]):
            self.cells[niche] = cand   # replace if candidate dominates current best

    def _dominates(self, a, b):
        """Pareto dominance on the fitness vector — including cost+latency (review catch)."""
        fa, fb = a.fitness, b.fitness
        return (fa.fidelity >= fb.fidelity and fa.coverage >= fb.coverage
                and fa.robustness >= fb.robustness
                and fa.cost >= fb.cost and fa.latency >= fb.latency
                and (fa.fidelity > fb.fidelity or fa.coverage > fb.coverage
                     or fa.robustness > fb.robustness
                     or fa.cost > fb.cost or fa.latency > fb.latency))

    def survivors(self):
        """The retained population (one elite per BEHAVIORAL niche) — diverse by construction."""
        return list(self.cells.values())


# behavioral niche functions (candidate -> behavioral cell)
def niche_by_literalness_intervention(cand):
    """A translation behavioral grid: literalness × intervention (review's example)."""
    f = cand.fitness
    # coarse behavior bins (not continuous — true MAP-Elites)
    lit = "hi" if f.fidelity > 0.93 else ("mid" if f.fidelity > 0.85 else "lo")
    intv = "hi" if f.coverage > 0.85 else ("mid" if f.coverage > 0.75 else "lo")
    return (lit, intv)


def niche_by_breadth_diversity(cand):
    """A retrieval behavioral grid: breadth × diversity."""
    f = cand.fitness
    breadth = "hi" if f.coverage > 0.8 else "lo"
    div = "hi" if f.novelty > 0.5 else "lo"
    return (breadth, div)


def cheap_gate(cand, schema_ok=True, evidence_ok=True) -> bool:
    """Cheap deterministic gates before deep evaluation (reject early, audit few)."""
    return schema_ok and evidence_ok


def promotion_gate(cand, fitness_threshold: dict) -> bool:
    """Only genuinely-better, diverse candidates get promoted (protects canonical truth)."""
    f = cand.fitness
    return (f.fidelity >= fitness_threshold.get("fidelity", 0.9)
            and f.robustness >= fitness_threshold.get("robustness", 0.8))
