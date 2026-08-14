#!/usr/bin/env python3
"""validate-evidence-ledger.py — typed evidence events + kind-aware confidence (GEM 6.5 + fojin).

Proves the fojin `confidence_kind` discipline + GEM 6.5 typed-events upgrade: the review reducer consumes
TYPED evidence events (not a lossy `evidence_ok: bool`), and confidence is never compared across kinds.
Two import_flag "1.0" scores are NOT treated as equal to one expert "1.0". This is the correctness win.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from evidence_ledger import EvidenceLedger, ConfidenceKind

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=== TYPED EVIDENCE EVENTS + KIND-AWARE CONFIDENCE (GEM 6.5 + fojin) ===\n")

# ---- a claim supported ONLY by LLM confidence is NOT yet supported at catalog strength ----
ledger = EvidenceLedger()
ledger.attach("IPK-1.5.19", 0.8, ConfidenceKind.LLM, "model-v1")
s = ledger.state_of("IPK-1.5.19")
check("LLM-only support does NOT reach catalog strength (kind discipline)",
      s["phase"] == "UNSUPPORTED" and s["support"] is None)

# ---- add a CATALOG confirmation -> now evidenced ----
ledger.attach("IPK-1.5.19", 1.0, ConfidenceKind.CATALOG, "torella-edition")
s = ledger.state_of("IPK-1.5.19")
check("catalog confirmation promotes to EVIDENCED", s["phase"] == "EVIDENCED")
check("support reports kind honestly (not a bare number)",
      s["support"]["kind"] == "catalog")

# ---- fojin discipline: import_flag 1.0 ≠ expert 1.0 (never compare incomparable) ----
l2 = EvidenceLedger()
l2.attach("claim-A", 1.0, ConfidenceKind.IMPORT_FLAG, "mitra-import")   # flag, not a real score
l2.attach("claim-B", 1.0, ConfidenceKind.EXPERT, "scholar-adjudication") # real human verdict
a = l2.best_supported("claim-A", ConfidenceKind.EXPERT)
b = l2.best_supported("claim-B", ConfidenceKind.EXPERT)
check("import_flag 1.0 does NOT pass an expert-strength gate (fojin discipline)", a is None)
check("expert 1.0 DOES pass the expert gate", b is not None and b["kind"] == "expert")

# ---- typed events drive the reducer (agents submit events, not state) ----
l3 = EvidenceLedger()
l3.attach("thesis", 0.9, ConfidenceKind.CATALOG, "source-1")
l3.contradict("thesis", "rival-scholar")
check("contradiction event flips state to CONTRADICTED (even with evidence)",
      l3.state_of("thesis")["phase"] == "CONTRADICTED")
l3.resolve_finding("thesis", "reviewer")
l3.adjudicate("thesis", "ACCEPTED", ConfidenceKind.EXPERT, "scholar")
check("adjudication event promotes to ADJUDICATED with verdict",
      l3.state_of("thesis")["phase"] == "ADJUDICATED"
      and l3.state_of("thesis")["verdict"] == "verdict=ACCEPTED")

# ---- citation phantom is a typed event, not a bool ----
l4 = EvidenceLedger()
l4.verify_citation("IPK-1.5.99", "some-essay", phantom=True)
l4.verify_citation("IPK-1.5.19", "good-essay", phantom=False)
phantoms = [e for e in l4.events if e.type.value == "CitationPhantom"]
check("phantom citations are typed events (auditable, not a bool)",
      len(phantoms) == 1 and phantoms[0].target == "IPK-1.5.99")

# ---- append-only + content-addressed events ----
check("ledger is append-only + events are content-addressed",
      len(l3.events) == 4 and all(e.id for e in l3.events))

print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
print("\nTYPED EVIDENCE LEDGER (GEM 6.5 + fojin confidence_kind): review now consumes typed evidence")
print("events instead of a lossy bool, and confidence is never compared across kinds. An import_flag")
print("'1.0' is honestly NOT treated as an expert '1.0'. This is the correctness win for multi-source")
print("verification — the flywheel and marketplace both depend on it.")
sys.exit(0 if all(c for _,c in results) else 1)
