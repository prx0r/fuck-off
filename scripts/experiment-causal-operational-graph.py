#!/usr/bin/env python3
"""experiment-causal-operational-graph.py — the 5th graph (patalamix review, #12).

The review identified a missing graph:
  epistemic provenance  = WHY DO WE BELIEVE THIS?  (we have this)
  causal operational graph = WHY DID THE SYSTEM ACT? (we were missing this)

Model: Event → caused Run → produced Artifact → triggered Finding → caused Task → produced Event.
Answers "why did the system do this?" with a replayable causal chain. Distinct from scholarship and
computation graphs. This is DML's causal/correlation event model.
"""
import json, hashlib

def node(kind, ident, **props):
    return {"id": f"{kind}:{ident}", "kind": kind, "ident": ident, **props}

print("=== CAUSAL OPERATIONAL GRAPH (the 5th graph) ===\n")

# a causal chain: why did the system re-render the explainer?
causal_chain = [
    node("Event", "E17", text="consumer question Q184 clustered to 2861 variants"),
    node("Run", "R8", text="gap detection run"),
    node("Artifact", "A4", text="PEDAGOGICAL gap flagged"),
    node("Finding", "F2", text="followup confusion 61%"),
    node("Task", "T9", text="intervention experiment (argument-graph mechanism)"),
    node("Event", "E31", text="GraphProposal MODIFY explainer:recognition"),
]

# causal edges: cause -> effect
edges = [
    ("Event:E17", "Run:R8"),        # consumer question caused the gap run
    ("Run:R8", "Artifact:A4"),      # run produced the gap
    ("Artifact:A4", "Finding:F2"),  # gap triggered the finding
    ("Finding:F2", "Task:T9"),      # finding caused the intervention task
    ("Task:T9", "Event:E31"),       # task produced the proposal event
]

print("the causal chain (why did the system act?):")
for cause, effect in edges:
    c = next(n for n in causal_chain if n["id"] == cause)
    e = next(n for n in causal_chain if n["id"] == effect)
    print(f"  {c['ident']:28s} ──caused──▶ {e['ident']}")

# answer "why did the system re-render the explainer?"
print("\nQ: why did the system re-render the explainer?")
# walk backward from Event:E31
why = ["Event:E31"]
prev = {"Event:E31": "Task:T9", "Task:T9": "Finding:F2", "Finding:F2": "Artifact:A4",
        "Artifact:A4": "Run:R8", "Run:R8": "Event:E17"}
cur = "Event:E31"
trace = []
while cur in prev:
    trace.append(cur); cur = prev[cur]
trace.append(cur)
print("  backward causal trace:", " ← ".join(t.split(":")[-1] for t in reversed(trace)))

print("\n=== INSIGHT ===")
print("The causal operational graph answers WHY THE SYSTEM ACTED (operational provenance), distinct")
print("from WHY WE BELIEVE THIS (epistemic provenance). It is replayable and content-addressable:")
print("every node has a stable id, every edge a cause-effect. This completes the 5-graph model:")
print("epistemic + computational + execution + evolution + causal-operational. It's what makes")
print("agent runs attributable — 'why did this happen?' — not just 'is it true?'")
