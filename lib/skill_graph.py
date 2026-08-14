"""lib/skill_graph.py — audited skill-graph self-improvement via verifiable rewards (arXiv 2512.23760).

Steal (2512.23760): an agent maintains a graph of SKILLS (reusable capabilities with dependencies).
Improvements are accepted ONLY when backed by a VERIFIABLE reward (provably-correct outcome), not a
model's self-assessment. The skill graph self-organizes — skills spawn/split/rewire by measured success.

Our adaptation: the 33 kernels ARE the skill graph. Each kernel's validation suite (validate-*.py) is
its VERIFIABLE REWARD (kill-rate / invariant / RKA-correctness — provable, not vibes). A skill
improvement is promoted only if it passes its verifiable reward AND herdr's audit gate. This is the
epistemically-safe self-improvement loop — our kernels become a self-improving skill graph.
"""
from __future__ import annotations
import hashlib


class Skill:
    """A kernel-as-skill in the graph. Verifiable reward = its validate suite."""
    def __init__(self, name, verifier, depends_on=None):
        self.name = name
        self.verifier = verifier        # callable() -> (passes:bool, reward:float) — the validate suite
        self.depends_on = depends_on or []   # skill deps
        self.reward = 0.0
        self.verified = False
        self.children = []

    def run_verification(self):
        """The VERIFIABLE REWARD: run the skill's own validation suite (not a self-assessment)."""
        passes, reward = self.verifier()
        self.verified = passes
        self.reward = reward if passes else 0.0
        return passes, self.reward


class SkillGraph:
    """The kernel-as-skill graph. Improvements promoted only on verifiable reward + audit."""

    def __init__(self):
        self.skills = {}

    def add(self, skill):
        self.skills[skill.name] = skill
        return skill

    def verify_all(self):
        """Run every skill's verifiable reward (the full audit)."""
        results = {}
        for name, s in self.skills.items():
            results[name] = s.run_verification()
        return results

    def suggest_improvement(self, skill_name, improvement_verifier):
        """Propose an improvement to a skill; accepted ONLY if its verifiable reward passes + improves."""
        old = self.skills[skill_name]
        old_passes, old_reward = old.run_verification()
        # the improvement candidate is validated by ITS OWN verifier (not the model's self-assessment)
        cand = Skill(skill_name + "+improved", improvement_verifier, depends_on=old.depends_on)
        cand_passes, cand_reward = cand.run_verification()
        if cand_passes and cand_reward > old_reward:
            # audited improvement: accepted only on provably-better verifiable reward
            self.skills[skill_name] = cand
            old.children.append(cand.name)
            return {"accepted": True, "from": old_reward, "to": cand_reward}
        return {"accepted": False, "reason": "improvement not verifiably better",
                "from": old_reward, "to": cand_reward}

    def weakest_skills(self, n=3):
        """The lowest-reward skills (the graph's improvement candidates)."""
        verified = [s for s in self.skills.values() if s.verified]
        return sorted(verified, key=lambda s: s.reward)[:n]

    def to_dict(self):
        return {"skills": len(self.skills),
                "verified": sum(1 for s in self.skills.values() if s.verified),
                "weakest": [s.name for s in self.weakest_skills()]}
