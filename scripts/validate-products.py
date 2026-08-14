#!/usr/bin/env python3
"""validate-products.py — verifiable validations for the three new product kernels.

Layer 03 TranslationProof (SPEC-16): non-aggregate audit vector + publication gate.
Layer 08 Scholar Review (SPEC-15): adversarial panel + citation phantom detection.
Layer 00 Schema Compiler (SPEC-17): single-source schema validation.

Prints PASS/FAIL. Exit 0 if all pass.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from translation import TranslationProof
from scholar_review import verify_citations, ReviewPanel, Finding
from schema import validate_object

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=== LAYER 03 — TRANSLATIONPROOF (non-aggregate audit vector) ===\n")
# good translation: all PASS, adjudicated -> OPEN
good = TranslationProof(work_id="W1", passage_id="P1")
good.alignment = {"coverage": 0.99, "target_grounding": 0.97}
good.source_analysis = {"morphology": "PASS", "syntax": "PASS"}
good.semantic_obligations = {"negation": "PASS", "modality": "PASS"}
good.terminology = {"consistency": "PASS"}
good.audits = {"entailment": "PASS", "xcomet": 0.93}
good.review = {"adjudication": "ACCEPTED"}
v = good.audit_vector()
check("good translation: SOURCE_COVERAGE >= 0.99", v["SOURCE_COVERAGE"] >= 0.99)
check("good translation: publication gate OPEN", good.publication_gate()["gate"] == "OPEN")
check("good translation: NO single aggregate score field", "quality" not in good.to_dict() and "score" not in good.to_dict())

# conflict: parallel witness conflict + no adjudication -> BLOCKED with reason
bad = TranslationProof(work_id="W1", passage_id="P2")
bad.alignment = {"coverage": 0.9, "target_grounding": 0.9}
bad.source_analysis = {"morphology": "PASS", "syntax": "PASS"}
bad.semantic_obligations = {"negation": "PASS", "modality": "PASS"}
bad.audits = {"entailment": "WARN", "xcomet": 0.8}
bad.parallels = [{"status": "conflict"}]
gate = bad.publication_gate()
check("conflicting translation: gate BLOCKED", gate["gate"] == "BLOCKED", f"reason={gate['reason']}")
check("conflicting translation: reason is dimension-specific", gate["reason"] in ("PARALLEL_WITNESS_FAIL", "SEMANTIC_ENTAILMENT_WARN", "PARALLEL_WITNESS_CONFLICT"))

print("\n=== LAYER 08 — SCHOLAR REVIEW (adversarial panel + citation verify) ===\n")
# citation phantom detection
known = {"Bell 1966", "EPR 1935", "Landauer 1961"}
checks = verify_citations(["Bell 1966", "Einstein 2025 (fabricated)", "Landauer 1961"], known)
check("real citations VERIFIED", checks[0].status == "VERIFIED" and checks[2].status == "VERIFIED")
check("fabricated citation flagged PHANTOM", checks[1].status == "PHANTOM")

# adversarial panel with dissent (anti-groupthink)
panel = ReviewPanel(reviewers=["A1", "A2", "A3"], judge="J")
panel.collect("A1", "ACCEPT", [])
panel.collect("A2", "REJECT", [Finding("f1", "A2", "BLOCKING", "evidence")])
panel.collect("A3", "REJECT", [Finding("f2", "A3", "BLOCKING", "method")])
ag = panel.anti_groupthink()
check("panel detects dissent (no forced consensus)", not ag["consensus"] and len(ag["dissent"]) > 0)
verdict = panel.verdict()
check("panel verdict BLOCKED on blocking findings", verdict["blocked"] and verdict["verdict"] == "BLOCKED")

print("\n=== LAYER 00 — SCHEMA COMPILER (single-source) ===\n")
good_claim = {"claim_id": "C1", "claim_text": "x", "epistemic_ceiling": "MACHINE_PROPOSED", "source_refs": ["S1"]}
bad_claim = {"claim_id": "C2", "claim_text": "x", "epistemic_ceiling": "NOT_A_CEILING", "source_refs": []}
check("valid claim passes schema", validate_object("claim", good_claim) == [])
errs = validate_object("claim", bad_claim)
check("invalid ceiling rejected", any("epistemic_ceiling" in e for e in errs))

print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
sys.exit(0 if all(c for _,c in results) else 1)
