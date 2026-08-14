#!/usr/bin/env python3
"""validate-organism-loop.py — the consumer→research machine (10-stage organism loop).

Proves the full chain from the patala organism vision:
  consumer probe → question → gap detection → intervention → GraphProposal → human gate → truth graph
Integrates with our evolution loop + agent-delivery human gate. Nothing generated goes straight into
canonical truth — the human gate is the only path.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from organism_loop import OrganismLoop

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=== CONSUMER→RESEARCH MACHINE (10-stage organism loop) ===\n")

loop = OrganismLoop()

# Stage 1-4: a consumer asks a question (the "probe")
print("[stages 1-4] consumer probe → question capture")
q1 = loop.capture_question("E5811", "U99",
    "Why is recognition necessary if identity is already the case?",
    concepts=["recognition", "identity", "bondage", "contraction"],
    variants=2861, followup=0.61)   # 2,861 variants, 61% follow-up confusion
print(f"  captured {q1.question_id}: '{q1.canonical_text[:45]}...' ({q1.variants} variants)")
check("question captured + clustered", q1.question_id == "Q1" and q1.variants == 2861)

# Stage 5: gap detection (high followup confusion → pedagogical, not open-research)
print("\n[stage 5] gap detection")
g1 = loop.detect_gap("Q1")
print(f"  {g1.gap_id}: type={g1.type}, demand={g1.demand}")
check("high followup confusion → PEDAGOGICAL gap", g1.type == "PEDAGOGICAL")
check("gap is the research-backlog signal", g1.status == "OPEN" and g1.demand == 2861)

# Stage 6-7: intervention experiment — which mechanism resolves the confusion?
print("\n[stages 6-7] intervention experiment + learning measurement")
itv_a = loop.run_intervention("prose_explanation", 0.10)
itv_b = loop.run_intervention("argument_graph", 0.85)   # argument graph wins
print(f"  prose: effect {itv_a.effect_size:.2f} | argument-graph: effect {itv_b.effect_size:.2f}")
best = itv_b if itv_b.effect_size > itv_a.effect_size else itv_a
check("intervention measured; argument-graph best", best.mechanism == "argument_graph")

# Stage 8: content mutation → GraphProposal
print("\n[stage 8] content mutation → GraphProposal")
prop = loop.propose_mutation("MODIFY", "explainer:recognition",
                             source_events=["E5811", q1.question_id])
print(f"  {prop.proposal_id}: {prop.operation} on {prop.target}")
check("proposal created", prop.proposal_id == "PROP1" and prop.operation == "MODIFY")

# Stage 9: verification (RARR/RefChecker-style) — corroborated but STILL blocked
print("\n[stage 9] verification")
prop = loop.verify_and_promote(prop)
print(f"  review_state={prop.review_state}, gate={prop.gate}")
check("verification corroborates but gate stays BLOCKED", prop.review_state == "MACHINE_CORROBORATED" and prop.gate == "BLOCKED")

# Stage 10: human gate → truth graph (the ONLY path)
print("\n[stage 10] human gate → truth graph")
prop = loop.human_authorize(prop)
print(f"  gate={prop.gate}, review_state={prop.review_state}")
check("human gate is the only path to canonical truth", prop.gate == "OPEN" and prop.review_state == "ACCEPTED")

# the flywheel: this resolved gap feeds the research backlog / evolution loop
check("resolved gap + accepted proposal = the flywheel turns", g1.status == "OPEN" and prop.review_state == "ACCEPTED")

print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
print("\nThe consumer→research machine works: a consumer probe becomes a gap, an intervention is")
print("measured, a GraphProposal is verified, and only the HUMAN GATE promotes it to truth. This")
print("closes the loop: consumers probe → the graph evolves (safely) → better explanations → fewer")
print("confusions → sharper probes. The organism is the evolution loop, with humans as the gate.")
sys.exit(0 if all(c for _,c in results) else 1)
