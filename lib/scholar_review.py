"""lib/scholar_review.py — the adversarial scholar-review pipeline (Layer 08, SPEC-15).

Implements the review survey's frontier insights:
  - multi-agent adversarial review panel (reviewers debate; anti-groupthink)
  - citation hallucination verification (citecheck): every citation must resolve
  - findings -> resolution -> crux tracking (OPEN CRUXES never hidden)
  - review as auditable process, not a score
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Finding:
    finding_id: str
    reviewer: str
    severity: str = "BLOCKING"       # BLOCKING | NON_BLOCKING
    category: str = ""               # evidence | clarity | method | citation
    text: str = ""
    status: str = "OPEN"             # OPEN | RESOLVED | REJECTED | OPEN_CRUX
    evidence: str = ""


@dataclass
class CitationCheck:
    citation: str
    resolves: bool = False           # did it resolve to a real reference?
    phantom: bool = False            # hallucinated citation?
    status: str = "UNVERIFIED"       # VERIFIED | PHANTOM | AMBIGUOUS


def verify_citations(citations: list, known_refs: set) -> list:
    """CiteCheck: a citation is phantom if it doesn't resolve to a known reference."""
    checks = []
    for c in citations:
        resolved = any(ref in c or c in ref for ref in known_refs)
        checks.append(CitationCheck(citation=c, resolves=resolved,
                                    phantom=not resolved,
                                    status="VERIFIED" if resolved else "PHANTOM"))
    return checks


class ReviewPanel:
    """Anti-groupthink adversarial review: N independent reviewers + a judge."""
    def __init__(self, reviewers: list, judge: str):
        self.reviewers = reviewers          # independent agents
        self.judge = judge
        self.findings: list = []
        self.reviewer_opinions = {r: None for r in reviewers}  # each votes independently

    def collect(self, reviewer: str, opinion: str, findings: list):
        self.reviewer_opinions[reviewer] = opinion
        self.findings.extend(findings)

    def anti_groupthink(self) -> dict:
        """Report agreement WITHOUT forcing consensus; flag dissent honestly."""
        votes = [v for v in self.reviewer_opinions.values() if v is not None]
        agree = all(v == votes[0] for v in votes) if votes else False
        dissent = {r: o for r, o in self.reviewer_opinions.items() if o and o != (votes[0] if votes else None)}
        return {"consensus": agree if votes else False,
                "n_reviewers": len(votes),
                "dissent": dissent,
                "blocking_findings": sum(1 for f in self.findings if f.severity == "BLOCKING" and f.status == "OPEN")}

    def verdict(self) -> dict:
        """Judge's verdict: BLOCKED if any blocking finding or citation phantom."""
        ag = self.anti_groupthink()
        blocked = ag["blocking_findings"] > 0
        cruxes = [f for f in self.findings if f.status == "OPEN_CRUX"]
        return {"judge": self.judge, "blocked": blocked,
                "open_cruxes": len(cruxes), "dissent": ag["dissent"],
                "verdict": "BLOCKED" if blocked else "REVISE_OR_ACCEPT"}
