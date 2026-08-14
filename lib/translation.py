"""lib/translation.py — the Pāṭala TranslationProof object (SPEC-16).

A first-class, non-aggregate audit vector for a translation. No single "quality = 94%" score — instead
a vector of per-dimension checks + a publication gate that BLOCKS on any failing dimension.

Dimensions (from SPEC-16 §26-28):
  SOURCE_COVERAGE · TARGET_GROUNDING · MORPHOLOGY · SYNTAX · NEGATION · MODALITY · TERM_CONSISTENCY ·
  SEMANTIC_ENTAILMENT · XCOMET · PARALLEL_WITNESS · HUMAN_REVIEW
Each: PASS | WARN | CONFLICT | FAIL | PENDING (or a 0-1 score).
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class TranslationProof:
    work_id: str
    passage_id: str
    source_identity: dict = field(default_factory=dict)   # {witness, edition, source_hash}
    source_analysis: dict = field(default_factory=dict)   # {segmentation, morphology, syntax}
    alignment: dict = field(default_factory=dict)         # {sentence, word_spans, unaligned_src, unaligned_tgt}
    semantic_obligations: dict = field(default_factory=dict)  # {negation, modality, scope, ...}
    terminology: dict = field(default_factory=dict)       # {lexical_senses, previous_occurrences}
    audits: dict = field(default_factory=dict)            # {xcomet: 0.94, ottoava: PASS, entailment: WARN}
    parallels: list = field(default_factory=list)         # [commentary, tibetan, chinese, ...]
    unresolved_issues: list = field(default_factory=list)
    review: dict = field(default_factory=dict)            # {agent_reviewers, scholar_reviewers, adjudication}

    # ---- the audit vector (NO single aggregate) ----
    def audit_vector(self) -> dict:
        v = {
            "SOURCE_COVERAGE": self.alignment.get("coverage", 0.0),
            "TARGET_GROUNDING": self.alignment.get("target_grounding", 0.0),
            "MORPHOLOGY": self.source_analysis.get("morphology", "PENDING"),
            "SYNTAX": self.source_analysis.get("syntax", "PENDING"),
            "NEGATION": self.semantic_obligations.get("negation", "PENDING"),
            "MODALITY": self.semantic_obligations.get("modality", "PENDING"),
            "TERM_CONSISTENCY": self.terminology.get("consistency", "PENDING"),
            "SEMANTIC_ENTAILMENT": self.audits.get("entailment", "PENDING"),
            "XCOMET": self.audits.get("xcomet", "PENDING"),
            "PARALLEL_WITNESS": "PASS" if not self.parallels else "CONFLICT" if any(
                p.get("status") == "conflict" for p in self.parallels) else "PASS",
            "HUMAN_REVIEW": self.review.get("scholar_reviewers", "PENDING"),
        }
        return v

    # ---- the publication gate (blocks on any failing dimension) ----
    def publication_gate(self) -> dict:
        """BLOCKED unless all hard dimensions PASS and no WARN-blocking issues."""
        BLOCKING_WARN = {"SEMANTIC_ENTAILMENT", "PARALLEL_WITNESS", "TERM_CONSISTENCY"}
        v = self.audit_vector()
        reasons = []
        for dim, status in v.items():
            if status == "FAIL" or (status == "CONFLICT"):
                reasons.append(f"{dim}_FAIL")
            elif dim in BLOCKING_WARN and status == "WARN":
                reasons.append(f"{dim}_WARN")
        if self.review.get("adjudication") != "ACCEPTED":
            reasons.append("HUMAN_ADJUDICATION_PENDING")
        return {"gate": "BLOCKED" if reasons else "OPEN",
                "reason": reasons[0] if reasons else "ALL_DIMENSIONS_PASS"}

    def to_dict(self) -> dict:
        return {
            "work_id": self.work_id, "passage_id": self.passage_id,
            "source_identity": self.source_identity,
            "audit_vector": self.audit_vector(),
            "publication_gate": self.publication_gate(),
            "unresolved_issues": self.unresolved_issues,
        }
