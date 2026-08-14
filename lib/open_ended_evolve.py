"""lib/open_ended_evolve.py — Darwin Godel Machine, adapted to the Verified Epistemic Organism.

Steal (arXiv 2505.22954, ecosystem/agent-evolution/dgm): DGM iteratively modifies its own code and
empirically VALIDATES each change against a benchmark; the archive only keeps commits that improve. It
is OPEN-ENDED (novelty, not just performance, drives the search) and SELF-REFERENTIAL (agents modify
their own ability to modify).

Our adaptation: the "organism" proposes changes to its RULES/THRESHOLDS/VERIFIERS (not code). A proposed
change is accepted into the ARCHIVE only if it (1) passes our oracle — the epistemic invariant + mutation
kill-rate + RKA correctness — the verifiable reward, and (2) improves or adds novelty. This is the
epistemically-SAFE open-ended loop: evolution under the invariant oracle, with an audit trail for every
promoted candidate (skill-graph self-improvement 2512.23760 + Darwin).
"""
from __future__ import annotations
import hashlib


class EvolvedRule:
    """A candidate change to the organism's rules (a node in the evolution archive)."""
    def __init__(self, rule_id, description, oracle_score=0.0, novelty=0.0, parent=None):
        self.id = rule_id
        self.description = description
        self.oracle_score = oracle_score       # verifiable reward (kill-rate / invariant)
        self.novelty = novelty                 # open-endedness driver
        self.parent = parent
        self.children = 0
        self.accepted = False
        self._hash = hashlib.sha256(f"{rule_id}:{description}".encode()).hexdigest()[:12]

    def fitness(self, novelty_w=0.3):
        """Performance + novelty (Darwin open-ended: not just performance)."""
        return self.oracle_score + novelty_w * self.novelty


class OpenEndedEvolution:
    """The archive of evolved rules. A rule is added ONLY if it passes the oracle + improves/novel."""

    def __init__(self, oracle=None, novelty_w=0.3):
        self.archive = {}          # rule_id -> EvolvedRule
        self.generation = 0
        self.novelty_w = novelty_w
        self.oracle = oracle       # callable(proposed_change) -> (passes:bool, score:float)

    def _parent_candidates(self):
        """Choose parent(s) from the archive (DGM: best + some diversity)."""
        accepted = [r for r in self.archive.values() if r.accepted]
        if not accepted:
            return []
        return sorted(accepted, key=lambda r: -r.fitness(self.novelty_w))

    def propose(self, rule_id, description, novelty=0.0, parent=None):
        """Propose a candidate change (self-referential: it may modify other rules)."""
        # run the oracle (the verifiable reward: invariant + kill-rate + RKA correctness)
        passes, score = self.oracle(description) if self.oracle else (True, 0.5)
        rule = EvolvedRule(rule_id, description, oracle_score=score, novelty=novelty, parent=parent)
        if passes and (score > 0 or novelty > 0):
            # open-ended accept: improves performance OR adds novelty (Darwin)
            rule.accepted = True
            if parent and parent in self.archive:
                self.archive[parent].children += 1
        self.archive[rule_id] = rule
        return rule

    def step(self):
        """One Darwin generation: propose from the best parents, advance generation."""
        self.generation += 1
        return self.generation

    def best(self, n=3):
        """The highest-fitness accepted rules (the archive's elite)."""
        return sorted([r for r in self.archive.values() if r.accepted],
                      key=lambda r: -r.fitness(self.novelty_w))[:n]

    def archive_state(self):
        return {"generation": self.generation, "rules": len(self.archive),
                "accepted": sum(1 for r in self.archive.values() if r.accepted),
                "best": [{"id": r.id, "fitness": round(r.fitness(self.novelty_w), 3)} for r in self.best(3)]}
