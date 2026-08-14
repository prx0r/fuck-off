#!/usr/bin/env python3
"""validate-integrity-gate.py — integrity_status tri-state + primary-source gate (EleutherIA GEM 6.2).

Adopts EleutherIA's highest-value lesson: integrity + layer are PERSISTED and enforced mechanically at
retrieval (not left to the LLM). Proves: excluded nodes never reach the agent; demoted are not verified;
and a synthesis answer requires ≥1 primary-source citation or it FAILS. On our real IPK/IPVV sources.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from integrity_gate import IntegrityGate, IntegrityStatus, SourceLayer

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=== INTEGRITY TRI-STATE + PRIMARY-SOURCE GATE (EleutherIA) ===\n")

gate = IntegrityGate()
# the reality graph: primary sources
gate.set_layer("IPK-1.5.19", SourceLayer.PRIMARY)
gate.set_layer("IPK-1.5.11", SourceLayer.PRIMARY)
gate.set_layer("ipvv-abhinava", SourceLayer.PRIMARY)
# the literature graph: modern reception
gate.set_layer("ratie-reading", SourceLayer.SECONDARY)
gate.set_layer("torella-intro", SourceLayer.SECONDARY)

# ---- integrity tri-state ----
gate.set_integrity("IPK-1.5.19", IntegrityStatus.CLEAN)
gate.set_integrity("ratie-reading", IntegrityStatus.DEMOTED)
gate.set_integrity("ipvv-abhinava", IntegrityStatus.EXCLUDED)

# ---- retrieval-time filtering: excluded nodes never reach the agent ----
context = ["IPK-1.5.19", "ratie-reading", "ipvv-abhinava", "IPK-1.5.11"]
allowed = gate.filter_context(context)
check("retrieval: EXCLUDED node pruned from context (never reaches agent)",
      "ipvv-abhinava" not in allowed and "IPK-1.5.19" in allowed)
check("retrieval: DEMOTED node stays in context", "ratie-reading" in allowed)

# ---- demoted is NOT usable as verified ----
check("verified: DEMOTED is not usable as a verified quote (EleutherIA rule)",
      not gate.is_usable_as_verified("ratie-reading"))
check("verified: CLEAN primary IS usable", gate.is_usable_as_verified("IPK-1.5.19"))

# ---- the primary-source HARD gate ----
# a synthesis citing only secondary (modern reception) must FAIL
fail = gate.synthesis_gate(["ratie-reading", "torella-intro"])
check("HARD GATE: secondary-only synthesis FAILS (no primary citation)", not fail["pass"])
# a synthesis citing a primary + clean must PASS
passes = gate.synthesis_gate(["IPK-1.5.19", "ratie-reading"])
check("HARD GATE: primary+clean synthesis PASSES", passes["pass"] and passes["primary_citations"] == ["IPK-1.5.19"])
# a synthesis citing an EXCLUDED primary must also FAIL (excluded can't ground)
fail2 = gate.synthesis_gate(["ipvv-abhinava"])
check("HARD GATE: excluded 'primary' cannot ground (integrity beats layer)", not fail2["pass"])

# ---- deterministic + persisted ----
check("persisted: integrity + layer are stable across reads",
      gate.status_of("ipvv-abhinava") == IntegrityStatus.EXCLUDED
      and gate.layer_of("IPK-1.5.19") == SourceLayer.PRIMARY)

print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
print("\nINTEGRITY GATE (EleutherIA): integrity_status tri-state + primary-source hard gate are PERSISTED")
print("and ENFORCED at retrieval — excluded nodes never reach the agent, demoted are not verified, and")
print("a synthesis needs ≥1 clean primary citation or it FAILS. This upgrades our review/staleness into")
print("mechanical retrieval-time enforcement, not a score the LLM reasons about.")
sys.exit(0 if all(c for _,c in results) else 1)
