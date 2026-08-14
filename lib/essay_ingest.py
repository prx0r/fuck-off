"""lib/essay_ingest.py — the essay-ingest pipeline (essays as derivation input).

The deep design: a scholarly essay is ingested through OUR EXISTING epistemic pipeline, NOT a
separate "essay reader." Each stage uses a proven kernel:

  STAGE 0  Source          raw essay text (Ratié txt/pdf)  ->  corpus/raw
  STAGE 1  Structurize     schema-compile the essay anatomy  ->  lib/schema.py (validated)
                           book -> chapters -> sections -> IPK kārikās -> argument-move
  STAGE 2  Mine claims     extract thesis/premise/conclusion claims with source cites
                           -> lib/epistemic.py envelope (SOURCE-SAYS vs SCHOLAR-RECONSTRUCTS vs
                              PATALA-INFERS kept distinct)
  STAGE 3  Evidence        attach verbatim quotes + source refs  -> grounded, signed
  STAGE 4  Argument graph  build AIF (info/inference/conflict)   -> lib/review.py + scholar_review.py
  STAGE 5  Crux detection  find scholar disagreements (master tensions)
                           -> experiment-crux-compiler.py logic
  STAGE 6  Review          adversarial panel + citecheck on mined claims -> lib/scholar_review.py
  STAGE 7  Organism        mined claims feed the graph; readers probe -> lib/organism.py
  STAGE 8  Pedagogy        mined structure becomes LearningClaims  -> lib/pedagogy.py
  STAGE 9  Reactive        essay is a projection; source change marks prose stale -> staleness.py

The essay becomes derivation INPUT, not dead prose. Each stage is verifiable by a proof.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
import json, hashlib

# ---- Stage 1: the essay anatomy (schema-compiled structure) ----
@dataclass
class EssaySection:
    id: str
    chapter: str
    ipk_refs: list = field(default_factory=list)   # the kārikās it treats
    argument_move: str = ""                          # thesis-move / rival / support
    text: str = ""

@dataclass
class EssayAnatomy:
    essay_id: str
    title: str
    author: str
    chapters: dict = field(default_factory=dict)     # chapter -> [EssaySection]
    def validate(self, compiled_schema):
        from schema import validate
        return validate({"id": self.essay_id, "title": self.title, "author": self.author},
                        compiled_schema)

# ---- Stage 2: mined claims (with source + honest ceiling) ----
@dataclass
class MinedClaim:
    claim_id: str
    text: str
    source_ref: str            # e.g. "Ratié Ch1, IPK 1.2.3-6"
    epistemic_ceiling: str     # from lib/epistemic
    role: str                  # thesis | premise | conclusion | rival
    verbatim: str              # the quote (Stage 3 evidence)
    section_id: str

# ---- Stage 4: AIF argument (from lib/review + scholar_review patterns) ----
@dataclass
class ArgumentMove:
    premise: str
    conclusion: str
    scheme: str                # ENTAILMENT | PRESUPPOSITION | ANALOGY | REDUCTIO
    note: str = ""

class EssayIngestor:
    """The essay-ingest pipeline: raw essay -> canonical objects, via our kernels."""
    def __init__(self, essay_id):
        self.essay_id = essay_id
        self.anatomy = None
        self.claims = []
        self.moves = []
        self.cruxes = []
        self.sections = []

    # Stage 1
    def structure(self, title, author, sections):
        """Schema-compile the essay anatomy."""
        from schema import compile_schema
        self.anatomy = EssayAnatomy(self.essay_id, title, author)
        for s in sections:
            self.sections.append(EssaySection(**s))
            self.anatomy.chapters.setdefault(s["chapter"], []).append(s)
        return self.anatomy

    # Stage 2+3: mine a claim with evidence (verbatim quote)
    def mine_claim(self, text, source_ref, ceiling, role, verbatim, section_id):
        c = MinedClaim(f"{self.essay_id}-C{len(self.claims)+1}", text, source_ref,
                       ceiling, role, verbatim, section_id)
        self.claims.append(c)
        return c

    # Stage 4: build the argument graph (AIF)
    def add_move(self, premise, conclusion, scheme, note=""):
        self.moves.append(ArgumentMove(premise, conclusion, scheme, note))

    # Stage 5: detect a crux (scholar disagreement, from crux-compiler logic)
    def detect_crux(self, claim_a, claim_b, status, evidence):
        self.cruxes.append({"a": claim_a, "b": claim_b, "status": status, "evidence": evidence})
        return self.cruxes[-1]

    # Stage 6: review the mined claims (adversarial + citecheck, from scholar_review)
    def review_claims(self):
        from scholar_review import verify_citations
        # every claim's source_ref must resolve to a real essay chapter/kārikā
        known = set()
        for s in self.sections:
            known.add(s.chapter)
            known.update(s.ipk_refs)
        checks = [verify_citations([c.source_ref], known)[0] for c in self.claims]
        return {"claims_reviewed": len(self.claims),
                "phantoms": sum(1 for x in checks if x.status == "PHANTOM")}

    # Stage 8: mine the structure into LearningClaims (pedagogy)
    def to_learning_claims(self):
        from education import LearningClaim
        return [LearningClaim(learning_claim_id=c.claim_id,
                              content=f"Learner can reconstruct: {c.text[:50]}",
                              derived_from=[c.source_ref],
                              claim_type=c.role) for c in self.claims]

    def report(self):
        return {"essay": self.essay_id, "sections": len(self.sections),
                "claims": len(self.claims), "moves": len(self.moves),
                "cruxes": len(self.cruxes),
                "hash": hashlib.sha256(json.dumps({
                    "sections": len(self.sections), "claims": len(self.claims),
                    "moves": len(self.moves)}).encode()).hexdigest()[:10]}
