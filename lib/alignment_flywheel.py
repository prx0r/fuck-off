"""lib/alignment_flywheel.py — the mine→stage→review→promote flywheel (fojin cross-source moat).

fojin (GEM 1.1 / EXTERNAL-REPOS) pattern: mine → stage → human-review → promote. The insight is NOT the
blind kNN (mostly spurious) — it's ALIGNMENT LOCALITY: verified cross-source matches grow outward cheaply
and precisely, and an automatic match is NEVER served as ground truth without a human in the loop.

This is directly our "cross-source verification" moat (fojin's `alignment_pairs` + `confidence_kind`).
For us: parallel passages (Sanskrit source ↔ translation ↔ commentary) are "aligned" candidates that
must be human-reviewed before they count as cross-source corroboration. Applied to our IPK/IPVV corpus:
a candidate parallel (e.g. Ratié's reading of IPK 1.5.19) goes through the 4 stages, and only promoted
pairs become evidence — never auto-served.
"""
from __future__ import annotations
from evidence_ledger import ConfidenceKind


class AlignmentCandidate:
    """A staged cross-source parallel (never auto-promoted)."""
    def __init__(self, source_a, source_b, similarity, method, evidence=""):
        self.a = source_a
        self.b = source_b
        self.similarity = similarity
        self.method = method            # embed_llm / expert / flywheel-verified
        self.evidence = evidence
        self.status = "pending"          # pending | accepted | rejected
        self.kind = ConfidenceKind.LLM   # until promoted: LLM


class AlignmentFlywheel:
    """mine → stage → review → promote. A bad auto-match is NEVER served as ground truth unreviewed."""

    def __init__(self, min_similarity=0.65):
        self.candidates = []
        self.promoted = []
        self.rejected = []
        self.min_similarity = min_similarity   # fojin: raised to 0.75 after prod hand-check

    # ---- MINE: propose candidates (high-recall, blind) ----
    def mine(self, source_a, source_b, similarity, method="embed_llm", evidence=""):
        if similarity >= self.min_similarity:
            self.candidates.append(AlignmentCandidate(source_a, source_b, similarity, method, evidence))
        return len(self.candidates)

    # ---- ANCHOR-EXPANSION: from a verified pair, propose neighbours (alignment locality) ----
    def mine_from_anchors(self, anchor_pair, neighbour_offsets=(-1, 1)):
        """fojin's anchor-expansion: verified pairs grow outward cheaply + precisely."""
        a_base, b_base = anchor_pair
        proposed = []
        for off in neighbour_offsets:
            proposed.append((f"{a_base}[{off:+d}]", f"{b_base}[{off:+d}]", "flywheel-anchor"))
        for a, b, m in proposed:
            self.mine(a, b, 0.8, method=m, evidence=f"anchored on {a_base}~{b_base}")
        return len(proposed)

    # ---- REVIEW: human-in-the-loop (no bulk apply) ----
    def review(self, index, accept):
        cand = self.candidates[index]
        if accept:
            cand.status = "accepted"
            cand.kind = ConfidenceKind.FLYWHEEL_VERIFIED   # human-in-the-loop promotion
            self.promoted.append(cand)
        else:
            cand.status = "rejected"
            self.rejected.append(cand)
        return cand

    # ---- PROMOTED pairs are the only ones served as evidence ----
    def served_parallels(self):
        """Only promoted pairs are served (a bad auto-match is never ground truth)."""
        return [{"a": c.a, "b": c.b, "method": c.method, "kind": c.kind.value}
                for c in self.promoted]

    def pending(self):
        return [c for c in self.candidates if c.status == "pending"]
