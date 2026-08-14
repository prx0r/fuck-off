#!/usr/bin/env python3
"""validate-design-provenance.py — the design-decision provenance kernel (DEV_PLAN §1.4).

Verifies: every design decision -> a signed nanopub (rationale + alternatives + validator); the signature
is tamper-evident (changing any field breaks verification); a design decision resolves via why() (the
self-doc); a Merkle root covers the whole decision ledger.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from design_provenance import DesignDecision, DesignProvenance

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=== DESIGN-DECISION PROVENANCE (lib/design_provenance.py) ===\n")

dp = DesignProvenance()

# ---- a REAL design decision from this session (the canonical translation orchestration choice) ----
dp.record(DesignDecision(
    "transl-orchestration", "translation orchestration",
    "patala factory_scheduler DAG (argument-guided T1->ARGMAP->L0->L2->L200->C1), Hermes=generation kernel only",
    "the canonical DAG is the deterministic Python controller; Hermes is the execution kernel not the "
    "orchestrator; ip-graph's per-verse runner bypassed ARGMAP and scored 0.118 vs Dyczkowski",
    alternatives=[
        {"choice": "per-verse Hermes runner", "rejected_reason": "bypasses the DAG, no ARGMAP, 0.118 vs gold, KILLED"},
        {"choice": "Hermes kanban drives the factory", "rejected_reason": "Hermes = scheduler not constitution; eligibility must be deterministic Python"},
        {"choice": "ip-graph factory_pool shadow orchestrator", "rejected_reason": "duplicates patala's scheduler = shadow task system"},
    ],
    validator="validate-tantraloka-corpus", layer="L03"))

# ---- a second real decision (the PG registry flip) ----
dp.record(DesignDecision(
    "registry-backend", "registry storage",
    "Postgres-backed registry behind PATALA_REGISTRY_PG=1 (default JSONL), JSONL demoted to export",
    "the 172MB SOURCE JSONL rewrite OOM'd the 8GB box; Postgres is the designed entity-truth layer",
    alternatives=[{"choice": "keep JSONL canonical", "rejected_reason": "full-file rewrite OOMs on 147k objects"}],
    validator="validate_registry_pg", layer="L03"))

# ---- 1. a design decision -> a signed nanopub ----
check("a design decision produces a signed nanopub",
      len(dp.decisions) == 2 and all("signature" in d for d in dp.decisions.values()))

# ---- 2. the signature is tamper-evident (the Self-Proving property) ----
check("a recorded design decision verifies (untampered)",
      dp.verify("transl-orchestration") and dp.verify("registry-backend"))
# tamper: flip the decision
tampered = dict(dp.decisions["transl-orchestration"]); tampered["decision"] = "per-verse Hermes runner"
check("changing any field breaks verification (tamper-evident)",
      not DesignDecision("transl-orchestration", tampered["topic"], tampered["decision"],
                         tampered["rationale"], tampered["alternatives"],
                         tampered["validator"], tampered["layer"]).verify(tampered))

# ---- 3. why() resolves the rationale + rejected alternatives (self-doc) ----
why = dp.why("transl-orchestration")
check("why() resolves 'why did you decide this?' to the rationale",
      why is not None and "deterministic Python controller" in why["rationale"])
check("why() surfaces the rejected alternatives",
      len(why["alternatives"]) == 3 and any("0.118" in a["rejected_reason"] for a in why["alternatives"]))
check("why() confirms the decision verifies", why["verifies"] is True)

# ---- 4. a Merkle root covers the whole decision ledger (self-proving) ----
root = dp.root()
check("a Merkle-style root covers all design decisions", len(root) > 0 and len(dp.decisions) == 2)

s = dp.summary()
check("summary reports the decision ledger honestly",
      s["decisions"] == 2 and s["verified"] == 2 and s["with_validator"] == 2, f"({s})")

print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
print("\nDESIGN-DECISION PROVENANCE: every design decision -> a signed nanopub (rationale + alternatives")
print("+ validator), tamper-evident, why()-resolvable, Merkle-rooted. The Self-Proving System (DEV_PLAN §1.4).")
sys.exit(0 if all(c for _,c in results) else 1)
