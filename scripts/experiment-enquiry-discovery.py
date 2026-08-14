#!/usr/bin/env python3
"""experiment-enquiry-discovery.py — the enquiry-as-discovery mechanism.

Prima materia: the logic5 presence enquiry (SPEC-46). The key insight the user made: the questioning
isn't just curiosity — it's DATA ABOUT THE TOPIC ITSELF. The presence enquiry DISCOVERED a structure:

  The words are NOT equivalent → a discovered taxonomy
  prakāśa → presence → experience → consciousness (3 different ontologies)
  Theorem: "Reality is manifest before it is interpreted as belonging to a subject."
  Boundary: "has NOT proved one Self / Śiva / universal consciousness"
  Frontier: "What turns mere presence into conscious presence?" (why prakāśa always has vimarśa)

This is enquiry-as-discovery: a structured set of questions reveals the topic's internal structure
(taxonomy + theorem + boundary + frontier), which then FEEDS our research/organism/pedagogy graphs.
"""
import json, hashlib

print("=== ENQUIRY-AS-DISCOVERY: the presence enquiry reveals topic structure ===\n")

# ---- the enquiry discovered a TAXONOMY (words are not equivalent) ----
taxonomy = {
    "prakāśa":     "reality is manifest (that by virtue of which anything appears)",
    "presence":    "the actuality of manifestation",
    "experience":  "structured presence",
    "consciousness": "ambiguous — 3 distinct ontologies: presence / self-present presence / subject",
}
print("[discovered taxonomy] the enquiry showed the words are NOT equivalent:")
for term, defn in taxonomy.items():
    print(f"  {term:14s} = {defn}")

# ---- the THEOREM (what the enquiry established) ----
theorem = "Reality is manifest before it is interpreted as belonging to a subject."
print(f"\n[theorem] {theorem}")

# ---- the BOUNDARY (what it did NOT establish — the honest limit) ----
boundary = ["one Self", "Śiva", "universal consciousness"]
print(f"\n[boundary] has NOT proved: {boundary}")
print("  → everything beyond the theorem requires additional argument")

# ---- the FRONTIER (the next genuine pressure point it discovered) ----
frontier = "What turns mere presence into conscious presence? (why is prakāśa always accompanied by vimarśa?)"
print(f"\n[frontier] {frontier}")
print("  → this is where Abhinavagupta, Buddhist epistemologists, phenomenology, and")
print("    consciousness science DIVERGE — a discovered research crux")

# ---- THE MECHANISM: enquiry → discovered structure (enquiry-as-discovery) ----
print("\n=== THE MECHANISM: enquiry-as-discovery ===\n")
print("A structured enquiry (question-growth) does NOT just satisfy curiosity — it REVEALS:")
print("  1. a taxonomy      (terms that were assumed equivalent are not)")
print("  2. a theorem        (what the enquiry actually established)")
print("  3. a boundary       (what it did NOT establish — honest limit)")
print("  4. a frontier       (the next genuine pressure point, where fields diverge)")
print("\nEach of these is DATA ABOUT THE TOPIC, not just about the questioner:")
print("  • the taxonomy → feeds the ONTOLOGY (new concept distinctions)")
print("  • the theorem   → a candidate claim (epistemic envelope)")
print("  • the boundary  → a research gap (What-If Machine: high-value target)")
print("  • the frontier  → a new question-root (Question-Growth tree)")

# ---- connect to the pedagogy graph (the learner reconstructs this structure) ----
print("\n=== CONNECTION TO THE PEDAGOGY GRAPH ===")
print("The discovered structure is EXACTLY a pedagogical progression — the learner should")
print("reconstruct the argument the enquiry grew:")
progression = ["prakāśa (manifest)", "presence", "experience (structured presence)",
               "consciousness (3 ontologies)", "theorem", "boundary", "frontier"]
for i, step in enumerate(progression, 1):
    print(f"  step {i}: {step}")
print("\n→ the learner's 'next interaction' = the next step in this discovered structure,")
print("  and a learner's confusion AT a step = the boundary/frontier → feeds the organism loop.")

print("\n=== INSIGHT ===")
print("The enquiry is a discovery instrument: its output is topic structure (taxonomy + theorem +")
print("boundary + frontier), not just questions. This structure IS the substrate for ontology,")
print("research-gap detection, and the pedagogy graph simultaneously. The presence enquiry is one")
print("gold example of this — and our question-growth + curiosity-pattern machinery can reproduce it.")
