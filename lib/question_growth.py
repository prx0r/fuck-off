"""lib/question_growth.py — the Question-Growth Engine (SPEC-36/logicvid, DEV_PLAN §1.2).

Prima materia from the pushing method (SPEC-33/34) + logicvid3: questioning is a GRAPH-GROWTH machine.
Each root question starts a TREE; edges are question-growth (a question forces the next). The load-
bearing property (logicvid3): "the same primitive should be rediscovered independently from many
directions" — an independently-rediscovered primitive is ROBUST, not one fragile chain.

This kernel makes question-growth concrete and measurable:
  - GrowthTree: nodes = questions, edges = question -> next_pressure.
  - PrimitiveRobustness: how many INDEPENDENT questions converge on the same primitive (the convergence
    metric from SPEC-36: "independent rediscovery count = evidence of fundamentality, not popularity").
  - The growth loop: each (question + passages -> theorem -> next_pressure) record is a learnable
    example (predict next_pressure from question+passages) — "if we record how questions grow, we can
    learn the growth."

Grounded in: scripts/experiment-question-growth.py (the proven prototype), lib/pushing_miner.py (the
crux compass, 7/7), SPEC-36/logicvid3 (convergence-graph research OS), SPEC-34 (autonomous pushing).
"""
from __future__ import annotations


class Question:
    """A node in the growth tree: a question, its theorem, its honest boundary, the next it forces."""

    def __init__(self, qid, question, shape="ROOT", theorem="", boundary="", next_pressure="",
                 passages=None, primitive=None):
        self.id = qid
        self.question = question
        self.shape = shape          # ROOT | CRUX | MECHANISM_GAP | SUBVERSION | ...
        self.theorem = theorem
        self.boundary = boundary
        self.next_pressure = next_pressure
        self.passages = passages or []
        self.primitive = primitive  # the primitive this question converges on (e.g. "vimarśa")

    def to_dict(self):
        return {"id": self.id, "question": self.question, "shape": self.shape, "theorem": self.theorem,
                "boundary": self.boundary, "next_pressure": self.next_pressure,
                "passages": self.passages, "primitive": self.primitive}


class QuestionGrowthTree:
    """The question-growth graph: nodes = questions, edges = question-growth."""

    def __init__(self):
        self.nodes = {}   # qid -> Question
        self.children = {}  # qid -> [child qids] (from next_pressure resolution)

    def add(self, question: Question) -> Question:
        self.nodes[question.id] = question
        self.children.setdefault(question.id, [])
        return question

    def link(self, parent_id, child_id):
        """Add a question-growth edge (a question forces the next)."""
        if parent_id in self.nodes and child_id in self.nodes and child_id not in self.children[parent_id]:
            self.children[parent_id].append(child_id)

    def _resolve_edges(self):
        """Build edges from next_pressure strings (a next forces the question whose question-text it names)."""
        self.children = {q: [] for q in self.nodes}
        for qid, q in self.nodes.items():
            nxt = q.next_pressure
            if not nxt:
                continue
            token = nxt.split(":")[0].strip()
            for oid, o in self.nodes.items():
                if oid == qid:
                    continue
                if o.question.startswith(token) or token.startswith(oid) or oid == token:
                    self.link(qid, oid)
                    break

    # ---- the KEY property: independent rediscovery = robustness ----
    def primitive_robustness(self):
        """How many INDEPENDENT questions converge on each primitive (SPEC-36's fundamentality signal).

        A primitive reached from N independent roots is N-robust. Robustness = evidence of fundamentality,
        NOT popularity (a primitive is only counted once per independent question)."""
        from collections import Counter
        counts = Counter(q.primitive for q in self.nodes.values() if q.primitive)
        return {p: {"independent_questions": n,
                    "robust": n >= 2,
                    "question_ids": [qid for qid, q in self.nodes.items() if q.primitive == p]}
                for p, n in counts.items()}

    def robust_primitives(self, min_independent=2):
        """Primitives independently rediscovered from >= `min_independent` questions."""
        return {p: v for p, v in self.primitive_robustness().items() if v["independent_questions"] >= min_independent}

    # ---- the growth loop: each record is a learnable example ----
    def growth_examples(self):
        """Each (question + passages -> theorem -> next_pressure) as a supervised example."""
        return [{"input": {"question": q.question, "shape": q.shape, "passages": q.passages,
                           "theorem": q.theorem},
                 "target": q.next_pressure} for q in self.nodes.values()]

    def next_pressures(self, qid):
        """The next questions a given question forces (its children in the growth tree)."""
        return [self.nodes[c] for c in self.children.get(qid, [])]

    def summary(self):
        rob = self.primitive_robustness()
        return {"questions": len(self.nodes),
                "edges": sum(len(c) for c in self.children.values()),
                "primitives": len(rob),
                "robust_primitives": len([p for p, v in rob.items() if v["robust"]]),
                "growth_examples": len(self.growth_examples())}
