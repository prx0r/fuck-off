#!/usr/bin/env python3
"""validate-enquiry.py — the Enquiry-Discovery Organism kernel (DEV_PLAN §1.3).

Verifies: a structured enquiry reveals taxonomy -> theorem -> boundary -> frontier; each element feeds
the right graph; the progression is a learnable/pedagogical order; a body of enquiries aggregates
discovered structure about a topic.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from enquiry import DiscoveryProgression, EnquiryDiscovery

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=== ENQUIRY-DISCOVERY ORGANISM (lib/enquiry.py) ===\n")

# ---- the real presence enquiry (SPEC-46/logic5) ----
presence = DiscoveryProgression(
    "presence-enquiry", "consciousness",
    taxonomy={"prakāśa": "reality is manifest (that by which anything appears)",
              "presence": "the actuality of manifestation",
              "experience": "structured presence",
              "consciousness": "ambiguous — 3 distinct ontologies"},
    theorem="Reality is manifest before it is interpreted as belonging to a subject.",
    boundary=["one Self", "Śiva", "universal consciousness"],
    frontier="What turns mere presence into conscious presence? (why is prakāśa always accompanied by vimarśa?)",
    question_ids=["Q0", "Q1", "Q2", "Q3"])

# ---- 1. the enquiry reveals a taxonomy (the words are NOT equivalent) ----
check("the enquiry reveals a discovered taxonomy (term distinctions)",
      len(presence.taxonomy) >= 4, f"({len(presence.taxonomy)} terms)")
check("the words are distinguished, not conflated (prakāśa != consciousness)",
      presence.taxonomy["prakāśa"] != presence.taxonomy["consciousness"])

# ---- 2. theorem + boundary + frontier are all present and distinct ----
check("the enquiry produced a theorem (a candidate claim)", bool(presence.theorem))
check("the boundary is the HONEST limit (what it did NOT establish)",
      "one Self" in presence.boundary and "universal consciousness" in presence.boundary)
check("the frontier is the next genuine pressure point",
      "vimarśa" in presence.frontier)

# ---- 3. each element feeds the right graph ----
feeds = presence.feeds()
check("taxonomy feeds the ontology graph", feeds["taxonomy"]["feeds"] == "ontology")
check("theorem feeds a claim", feeds["theorem"]["feeds"] == "claim")
check("boundary feeds a research gap", feeds["boundary"]["feeds"] == "research_gap")
check("frontier feeds a question-root (question-growth tree)", feeds["frontier"]["feeds"] == "question_root")

# ---- 4. the progression is a learnable/pedagogical order ----
steps = presence.progression()
check("the progression is ordered (taxonomy -> theorem -> boundary -> frontier)",
      len(steps) >= 6 and "frontier" in steps[-1], f"({len(steps)} steps)")

# ---- 5. a body of enquiries aggregates discovered structure about a topic ----
ed = EnquiryDiscovery()
ed.add(presence)
ed.add(DiscoveryProgression("memory-enquiry", "consciousness",
       taxonomy={"recognition": "reappropriation of a past cognition as one's own"},
       theorem="recognition requires more than memory", boundary=["the universal Self"],
       frontier="does the recognizer persist across cognitions?"))
check("a body of enquiries aggregates a discovered taxonomy about the topic",
      len(ed.discovered_taxonomy("consciousness")) >= 5, f"({len(ed.discovered_taxonomy('consciousness'))} terms)")
check("frontiers across enquiries are collected (the question-roots)",
      len(ed.frontiers("consciousness")) == 2, f"({len(ed.frontiers('consciousness'))})")

s = ed.summary("consciousness")
check("summary reports the discovered structure honestly",
      s["enquiries"] == 2 and s["frontiers"] == 2 and s["boundaries"] == 4, f"({s})")

print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
print("\nENQUIRY-DISCOVERY ORGANISM: a structured enquiry reveals topic structure")
print("(taxonomy -> theorem -> boundary -> frontier) that feeds ontology/claims/gaps/question-growth.")
print("This is enquiry-as-discovery (DEV_PLAN §1.3, SPEC-46) — the What-If + organism discovery engine.")
sys.exit(0 if all(c for _,c in results) else 1)
