"""lib/enquiry.py — the Enquiry-Discovery Organism (DEV_PLAN §1.3, SPEC-46/logic5).

Prima materia: the presence enquiry (SPEC-46). A structured enquiry is NOT just curiosity — it is DATA
ABOUT THE TOPIC ITSELF. The presence enquiry DISCOVERED a structure: the words (prakāśa/presence/
experience/consciousness) are NOT equivalent -> a discovered taxonomy -> a theorem -> a boundary -> a
frontier.

This kernel makes enquiry-as-discovery concrete:
  - DiscoveryProgression: the structure an enquiry reveals = taxonomy -> theorem -> boundary -> frontier.
  - Each element feeds a different graph: taxonomy -> ontology; theorem -> a claim; boundary -> a
    research gap (What-If Machine); frontier -> a new question-root (Question-Growth tree).
  - The progression is ALSO a pedagogical order: the learner reconstructs the argument the enquiry grew,
    and a learner's confusion AT a step = the boundary/frontier -> feeds the organism loop.

Grounded in: scripts/experiment-enquiry-discovery.py (the proven prototype), SPEC-46 (logic5: the four
disambiguated terms), lib/question_growth.py (the question tree the frontier feeds), the LOGICVID gold
(human enquiry as discovery).
"""
from __future__ import annotations


class DiscoveryProgression:
    """The structure an enquiry reveals: taxonomy -> theorem -> boundary -> frontier.

    This is enquiry-as-discovery: a structured set of questions reveals the topic's internal structure,
    which then feeds ontology (taxonomy), claims (theorem), research-gaps (boundary), and the
    question-growth tree (frontier).
    """

    def __init__(self, enquiry_id, topic, taxonomy=None, theorem="", boundary=None, frontier="",
                 question_ids=None):
        self.enquiry_id = enquiry_id
        self.topic = topic
        self.taxonomy = taxonomy or {}     # {term: definition} — discovered distinctions
        self.theorem = theorem             # what the enquiry actually established (a candidate claim)
        self.boundary = boundary or []     # what it did NOT establish (honest limit)
        self.frontier = frontier           # the next genuine pressure point (new question-root)
        self.question_ids = question_ids or []

    def to_dict(self):
        return {"enquiry_id": self.enquiry_id, "topic": self.topic, "taxonomy": self.taxonomy,
                "theorem": self.theorem, "boundary": self.boundary, "frontier": self.frontier,
                "question_ids": self.question_ids}

    # ---- the progression as a learnable / pedagogical order ----
    def progression(self):
        """The ordered steps the enquiry grew (the pedagogical + research order)."""
        steps = [f"{t} ({d})" for t, d in self.taxonomy.items()]
        steps += [f"theorem: {self.theorem}"]
        steps += [f"boundary: {b}" for b in self.boundary]
        steps += [f"frontier: {self.frontier}"]
        return steps

    # ---- what each element feeds ----
    def feeds(self):
        """Map each discovered element to the graph it feeds (ontology / claim / gap / question-root)."""
        return {
            "taxonomy": {"feeds": "ontology", "items": list(self.taxonomy.keys())},
            "theorem": {"feeds": "claim", "item": self.theorem},
            "boundary": {"feeds": "research_gap", "items": self.boundary},
            "frontier": {"feeds": "question_root", "item": self.frontier},
        }


class EnquiryDiscovery:
    """Collects enquiries and measures what the body of enquiries DISCOVERED about a topic."""

    def __init__(self):
        self.enquiries = {}

    def add(self, progression: DiscoveryProgression) -> DiscoveryProgression:
        self.enquiries[progression.enquiry_id] = progression
        return progression

    def discovered_taxonomy(self, topic):
        """The union of all distinctions an enquiry (or set of enquiries) revealed about a topic."""
        merged = {}
        for p in self.enquiries.values():
            if p.topic == topic:
                merged.update(p.taxonomy)
        return merged

    def frontiers(self, topic):
        """The open pressure points an enquiry discovered (the next question-roots)."""
        return [p.frontier for p in self.enquiries.values()
                if p.topic == topic and p.frontier]

    def boundaries(self, topic):
        """The honest limits an enquiry did not cross (research gaps)."""
        return [b for p in self.enquiries.values() if p.topic == topic for b in p.boundary]

    def summary(self, topic=None):
        tops = [topic] if topic else {p.topic for p in self.enquiries.values()}
        out = {}
        for t in tops:
            ps = [p for p in self.enquiries.values() if p.topic == t]
            out[t] = {"enquiries": len(ps),
                      "taxonomy_terms": len(self.discovered_taxonomy(t)),
                      "theorems": len([p for p in ps if p.theorem]),
                      "boundaries": len(self.boundaries(t)),
                      "frontiers": len(self.frontiers(t))}
        return out[topic] if topic else out
