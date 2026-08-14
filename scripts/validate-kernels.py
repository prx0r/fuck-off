#!/usr/bin/env python3
"""validate-kernels.py — validate the kernels that lacked proper test coverage.

Promotes the RUN experiments' logic into the authoritative test suite, covering:
  lib/certificate.py   — Certification Weight (marketplace)
  lib/discovery.py     — Research Value Score (what-if machine)
  lib/translation.py   — TranslationProof (translation product)
  lib/query.py         — KG2Code executable queries
  lib/retrieval.py     — PathRAG + HippoRAG
  lib/scholar_review.py — adversarial panel + citecheck

This makes the test suite authoritative: every kernel now has a validating gate.
"""
import os, sys, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from certificate import Certification, project_weight
from discovery import ResearchTarget, prioritize
from translation import TranslationProof
from query import KnowledgeQuery
from retrieval import GraphRetriever
from scholar_review import verify_citations, ReviewPanel, Finding

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=== KERNEL VALIDATION SUITE ===\n")

# ---- lib/certificate.py ----
print("[certificate] Certification Weight")
c = Certification("I1", verifier_kill_rate=1.0, consensus_multiplicity=3, downstream_load=5, time_signed_years=1.0)
check("CW = 36 for (1.0, 3, 5, 1)", abs(c.weight() - 36.0) < 1e-6, f"got {c.weight()}")
check("CW compounds over time", project_weight(c, 10) > 500)

# ---- lib/discovery.py ----
print("\n[discovery] Research Value Score")
t1 = ResearchTarget("I2", load_bearing=4, verifier_strength=0.9, crux_pressure=0.8)
t2 = ResearchTarget("I1", load_bearing=5, verifier_strength=1.0, crux_pressure=0.2)
ranked = prioritize([t1, t2])
check("unverified+contested target ranks higher", ranked[0].claim_id == "I2")
check("RV is 0 when fully verified", abs(ResearchTarget("X", load_bearing=5, verifier_strength=1.0, crux_pressure=0.5).research_value()) < 1e-9)

# ---- lib/translation.py ----
print("\n[translation] TranslationProof non-aggregate vector")
good = TranslationProof("W1", "P1")
good.alignment = {"coverage": 0.99, "target_grounding": 0.97}
good.source_analysis = {"morphology": "PASS", "syntax": "PASS"}
good.semantic_obligations = {"negation": "PASS", "modality": "PASS"}
good.terminology = {"consistency": "PASS"}
good.audits = {"entailment": "PASS", "xcomet": 0.93}
good.review = {"adjudication": "ACCEPTED"}
check("good translation gate OPEN", good.publication_gate()["gate"] == "OPEN")
check("no single aggregate score", "quality" not in good.to_dict() and "score" not in good.to_dict())

# ---- lib/query.py ----
print("\n[query] KG2Code executable queries")
g = json.load(open("/mnt/HC_Volume_106427611/ip-graph/data/graph/graph.json"))
Q = KnowledgeQuery(g)
fw = Q.resolve("Free Will", ntype="concept")
qm = Q.resolve("Quantum Mechanics", ntype="concept")
check("resolve('Free Will') finds concept", fw is not None and fw.endswith("free_will"))
trace, ok = Q.execute(lambda: Q.path(qm, fw, max_hops=3), expected_label="Free Will")
check("path(quantum, free_will) resolves", ok)

# ---- lib/retrieval.py ----
print("\n[retrieval] PathRAG + HippoRAG")
concept_edges = [(e["from"], e["to"], float(e.get("properties",{}).get("weight",1)))
                 for e in g["edges"] if e["from"].startswith("ip:concept") and e["to"].startswith("ip:concept")]
R = GraphRetriever(concept_edges)
paths = R.pathrag_paths("ip:concept:quantum_mechanics", "ip:concept:free_will", max_hops=3)
check("PathRAG finds paths", len(paths) > 0)
ppr = R.hipporag(["ip:concept:entropy"], top_k=5)
check("HippoRAG returns ranked nodes", len(ppr) > 0)

# ---- lib/scholar_review.py ----
print("\n[scholar_review] adversarial panel + citecheck")
checks = verify_citations(["Bell 1966", "Einstein 2025 (fake)"], {"Bell 1966", "EPR 1935"})
check("real citation VERIFIED", checks[0].status == "VERIFIED")
check("fake citation flagged PHANTOM", checks[1].status == "PHANTOM")
panel = ReviewPanel(reviewers=["A1", "A2"], judge="J")
panel.collect("A1", "REJECT", [Finding("f1", "A1", severity="BLOCKING", category="evidence")])
panel.collect("A2", "REJECT", [Finding("f2", "A2", severity="BLOCKING", category="evidence")])
check("panel verdict BLOCKED", panel.verdict()["blocked"])

print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
sys.exit(0 if all(c for _,c in results) else 1)
