#!/usr/bin/env python3
"""Upgrade the graph with the epistemic envelope (SPEC-02).

Every node/edge gains epistemic_ceiling + 4-axis authority + review_state. Concept and author nodes
get type-appropriate ceilings (works = corroborated, thesis concepts = machine-proposed).
Writes data/graph/graph.json + a machine-readable epistemic audit.
"""
import os, sys, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from epistemic import EpistemicEnvelope, default_ceiling, rank, EPISTEMIC_RANK

GRAPH = "/mnt/HC_Volume_106427611/ip-graph/data/graph/graph.json"
OUT = GRAPH
AUDIT = "/mnt/HC_Volume_106427611/ip-graph/data/graph/epistemic-audit.json"

g = json.load(open(GRAPH))

# ceilings that must never be exceeded (from our domain knowledge)
CONCEPT_CEILING = {
    # physics/information = corroborated science
    "entropy": "SCHOLARLY_CORROBORATED", "information": "SCHOLARLY_CORROBORATED",
    "probability": "SCHOLARLY_CORROBORATED", "quantum_mechanics": "SCHOLARLY_CORROBORATED",
    "measurement": "SCHOLARLY_CORROBORATED", "superposition": "SCHOLARLY_CORROBORATED",
    "wave_function": "SCHOLARLY_CORROBORATED", "entanglement": "SCHOLARLY_CORROBORATED",
    "information_theory": "SCHOLARLY_CORROBORATED", "computation": "SCHOLARLY_CORROBORATED",
    "second_law": "SCHOLARLY_CORROBORATED", "arrow_of_time": "SCHOLARLY_CORROBORATED",
    "thermodynamics": "SCHOLARLY_CORROBORATED",
    # mind = partially corroborated (empirical but contested)
    "consciousness": "SCHOLARLY_CORROBORATED_PRELIMINARY", "mind": "SCHOLARLY_CORROBORATED_PRELIMINARY",
    "qualia": "MACHINE_PROPOSED",
    # free-will / value = philosophical thesis = MACHINE_PROPOSED (the honest ceiling)
    "free_will": "MACHINE_PROPOSED", "determinism": "SCHOLARLY_CORROBORATED",
    "indeterminism": "SCHOLARLY_CORROBORATED_PRELIMINARY", "agency": "MACHINE_PROPOSED",
    "responsibility": "MACHINE_PROPOSED", "causality": "SCHOLARLY_CORROBORATED",
    "life": "SCHOLARLY_CORROBORATED", "evolution": "SCHOLARLY_CORROBORATED",
    "chance": "MACHINE_PROPOSED", "randomness": "SCHOLARLY_CORROBORATED",
    "knowledge": "SCHOLARLY_CORROBORATED", "belief": "MACHINE_PROPOSED", "truth": "MACHINE_PROPOSED",
    "value": "MACHINE_PROPOSED", "morality": "MACHINE_PROPOSED",
}
SCHOOL_CEILING = {"compatibilism": "MACHINE_PROPOSED", "libertarianism": "MACHINE_PROPOSED",
                  "incompatibilism": "MACHINE_PROPOSED"}
PROBLEM_CEILING = {"measurement_problem": "SCHOLARLY_CORROBORATED_PRELIMINARY",
                   "mind_body_problem": "MACHINE_PROPOSED", "free_will_problem": "MACHINE_PROPOSED",
                   "hard_problem": "MACHINE_PROPOSED"}

def cid(node_id):
    return node_id.split(":")[-1]

# apply envelopes to nodes
violations = []
for n in g["nodes"]:
    t = n["type"]; ident = cid(n["id"])
    if t == "concept":
        ceiling = CONCEPT_CEILING.get(ident, "MACHINE_PROPOSED")
    elif t == "school":
        ceiling = SCHOOL_CEILING.get(ident, "MACHINE_PROPOSED")
    elif t == "problem":
        ceiling = PROBLEM_CEILING.get(ident, "MACHINE_PROPOSED")
    elif t == "work":
        ceiling = "SCHOLARLY_CORROBORATED"   # published papers
    elif t == "author":
        ceiling = "SCHOLARLY_CORROBORATED"
    else:
        ceiling = "MACHINE_PROPOSED"
    n["properties"]["epistemic_ceiling"] = ceiling
    n["properties"]["known_as"] = "EVIDENCE_GROUNDED" if ceiling >= "SCHOLARLY_CORROBORATED" else "EXTRACTED"
    n["properties"]["review_state"] = "GENERATED"
    n["properties"]["authority"] = {"generation": "MACHINE_PROPOSED", "evidence": ceiling,
                                    "review": "NOT_REVIEWED", "publication": "PRIVATE"}

# apply envelopes to edges (ceiling = min of endpoints; never exceeds a corroborated work)
for e in g["edges"]:
    def nceil(nid):
        for n in g["nodes"]:
            if n["id"] == nid:
                return rank(n["properties"].get("epistemic_ceiling", "MACHINE_PROPOSED"))
        return 0
    fr = nceil(e["from"]); to = nceil(e["to"])
    ceiling = min(fr, to)
    level = [k for k, v in EPISTEMIC_RANK.items() if v == ceiling][0]
    e["properties"]["epistemic_ceiling"] = level
    e["properties"]["evidence_quote"] = ""
    e["properties"]["review_state"] = "GENERATED"

json.dump(g, open(OUT, "w"), indent=1)

# audit
concepts = {n["id"]: n["properties"]["epistemic_ceiling"] for n in g["nodes"] if n["type"] == "concept"}
thesis = {k: v for k, v in concepts.items() if k in CONCEPT_CEILING and CONCEPT_CEILING[k] == "MACHINE_PROPOSED"}
audit = {
    "nodes_with_envelope": len(g["nodes"]),
    "edges_with_envelope": len(g["edges"]),
    "concepts_by_ceiling": {},
    "thesis_concepts_honestly_machine_proposed": sorted(thesis.keys()),
}
for n in g["nodes"]:
    if n["type"] == "concept":
        c = n["properties"]["epistemic_ceiling"]
        audit["concepts_by_ceiling"][c] = audit["concepts_by_ceiling"].get(c, 0) + 1
json.dump(audit, open(AUDIT, "w"), indent=1)

print("=== EPISTEMIC ENVELOPE APPLIED ===")
print(f"nodes: {len(g['nodes'])}, edges: {len(g['edges'])}")
print("concepts by ceiling:", audit["concepts_by_ceiling"])
print(f"\nthesis concepts honestly machine-proposed ({len(thesis)}):")
print("  " + ", ".join(sorted(thesis)))
print(f"\naudit -> {AUDIT}")
