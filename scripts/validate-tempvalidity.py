#!/usr/bin/env python3
"""validate-tempvalidity.py — graphiti-style temporal validity intervals in the staleness kernel.

Verifies lib/staleness.TemporalFact: facts/edges carry valid_at/invalid_at so the engine answers
"what was true at time t" and auto-expires superseded facts — interval-based fact truth complementing
the event-based blast-radius staleness (graphiti edges.py:263-281).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from staleness import TemporalFact, active_facts_at, supersede_fact, fact_as_of

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=== TEMPORAL VALIDITY INTERVALS (graphiti) in the staleness kernel ===\n")

# a fact valid from t=100, plus a superseded one valid 100-200
facts = [
    TemporalFact("f1", 100, payload={"ceiling": "MACHINE_PROPOSED"}),
    TemporalFact("f2", 100, 200, payload={"ceiling": "SCHOLARLY_CORROBORATED"}),  # superseded at 200
]

check("fact is active inside its validity interval",
      active_facts_at(facts, 150) == facts, f"({len(active_facts_at(facts,150))} active)")
check("a superseded fact is NOT active after invalid_at",
      all(f.fact_id != "f2" for f in active_facts_at(facts, 250)), "f2 expired at 200")

# auto-expire a currently-valid fact (supersede)
supersede_fact(facts, "f1", 300)
check("supersede_fact auto-expires a fact (sets invalid_at)",
      not any(f.fact_id == "f1" for f in active_facts_at(facts, 350)), "f1 expired at 300")

# answer "what was true at time t" for a fact with multiple versions
facts2 = [TemporalFact("v", 0, 100, payload={"state": "OLD"}),
          TemporalFact("v", 100, None, payload={"state": "NEW"})]
check("fact_as_of returns the version valid at time t",
      fact_as_of(facts2, "v", 50) == {"state": "OLD"} and fact_as_of(facts2, "v", 150) == {"state": "NEW"},
      "OLD@50, NEW@150")

print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
print("\nTemporal validity intervals give the engine interval-based fact truth (graphiti): facts carry")
print("valid_at/invalid_at, superseded facts auto-expire, and 'what was true at time t' is queryable —")
print("complementing the event-based blast-radius staleness with a time dimension.")
sys.exit(0 if all(c for _,c in results) else 1)
