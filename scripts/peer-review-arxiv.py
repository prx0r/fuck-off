#!/usr/bin/env python3
"""peer-review-arxiv.py — cross-reference the SPEC-08 architectures against our implementation.

For each architecture in the graph-reasoning survey, classify:
  status: IMPLEMENTED | PARTIAL | GAP | VALIDATES
  what_we_have: the piece of our engine it maps to
  steal: the specific idea worth adopting
  why: why it's promising for OUR project
Writes a machine-readable review to data/graph/arxiv-review.json + prints a summary.
"""
import json, os

ARCH = [
  {"id":"G-reasoner/GFM-RAG","status":"GAP","what_we_have":"None (no learned graph encoder)",
   "steal":"export_gfm_graph() + benchmark 34M G-reasoner on our 490-node graph",
   "why":"Learned graph foundation model could give our small graph a strong retrieval prior."},
  {"id":"Reasoning-on-Graphs","status":"GAP","what_we_have":"argument.json (chain structure)",
   "steal":"graph-valid plan generation before answering",
   "why":"Maps to our argument engine: plan over the two-stage chain, then answer."},
  {"id":"ToG-2","status":"GAP","what_we_have":"None",
   "steal":"alternating text<->graph search for trace()/investigate()",
   "why":"Agent retrieval over our corpus should interleave reading and graph-walking."},
  {"id":"FastToG","status":"GAP","what_we_have":"graph.json communities",
   "steal":"graph communities as search units",
   "why":"Cheap way to bound retrieval over our 490 nodes."},
  {"id":"HyperGraphRAG","status":"BET","what_we_have":"AIF Argument (multi-premise) in argument.json",
   "steal":"keep Argument object non-flat; project to property/hypergraph/xAIF/RDF",
   "why":"Our Argument object already has premises+conclusion+defeaters = naturally hypergraphic."},
  {"id":"PathRAG","status":"GAP","what_we_have":"None",
   "steal":"retrieve reasoning paths, not node piles; bounded token context",
   "why":"Directly informs context(token_budget=N) for agent bundles."},
  {"id":"SubgraphRAG","status":"VALIDATES","what_we_have":"co_occurs subgraph",
   "steal":"retrieve smallest useful graph",
   "why":"Confirms our 'one agent question = one bounded request' doctrine."},
  {"id":"HippoRAG","status":"GAP","what_we_have":"None",
   "steal":"Personalized PageRank over the KG for retrieval",
   "why":"Gives our small graph associative (not just exact) retrieval."},
  {"id":"LightRAG","status":"VALIDATES","what_we_have":"corpus + graph",
   "steal":"dual-level (low/high) retrieval",
   "why":"Confirms compiling the corpus once, not at query time."},
  {"id":"KAG/OpenSPG","status":"GAP","what_we_have":"canonical-dag.yaml (logical form)",
   "steal":"ontology + logic + retrieval with logical-form QA",
   "why":"Our DAG is a logical form; KAG shows how to make it queryable."},
  {"id":"Graphiti","status":"GAP","what_we_have":"review_state in envelope",
   "steal":"separate epistemic graph from temporal event history",
   "why":"Our review events (SPEC-02) must not be jammed into semantic claims."},
  {"id":"AriGraph","status":"GAP","what_we_have":"None",
   "steal":"semantic memory + episodic memory + world model",
   "why":"Separating claims (semantic) from agent runs (episodic) is the right split."},
  {"id":"KG2Code","status":"BET","what_we_have":"None",
   "steal":"let agents write executable graph queries: path(from,via,to).filter()",
   "why":"The agent-query frontier: deterministic execution, agent does planning."},
  {"id":"LLM-Wiki","status":"VALIDATES","what_we_have":"projection compiler (SPEC-00)",
   "steal":"graph-as-compiled-wiki output",
   "why":"Confirms our compiler model: knowledge compiled once into addressable artifacts."},
  {"id":"KORAL","status":"GAP","what_we_have":"None",
   "steal":"two graphs: reality vs literature",
   "why":"Separating primary evidence from interpretation = patala's commentarial layer."},
  {"id":"TechGraphRAG","status":"GAP","what_we_have":"epistemic_ceiling",
   "steal":"evidence sufficiency as a first-class gate",
   "why":"Our ceilings should gate retrieval, not just annotate."},
  {"id":"nano-graphrag","status":"REFERENCE","what_we_have":"build-graph.py",
   "steal":"~1100-line reference GraphRAG",
   "why":"Cheap reference for our compiler."},
]

# Our implemented pieces
implemented = {
  "epistemic_envelope": True, "canonical_dag": True, "argument_graph": True,
  "evidence_weights": True, "co_occurs_graph": True, "review_state": True,
}
summary = {"reviewed": len(ARCH), "by_status": {}}
for a in ARCH:
    summary["by_status"][a["status"]] = summary["by_status"].get(a["status"], 0) + 1

json.dump({"architectures": ARCH, "implemented": implemented, "summary": summary},
          open("/mnt/HC_Volume_106427611/ip-graph/data/graph/arxiv-review.json", "w"), indent=1)

print("=== PEER REVIEW: 17 arxiv graph-reasoning architectures vs our engine ===")
print(f"status counts: {summary['by_status']}\n")
print(f"{'arch':22s} {'status':11s} why-promising")
print("-"*90)
for a in ARCH:
    print(f"{a['id']:22s} {a['status']:11s} {a['why'][:55]}")
print(f"\nwrote data/graph/arxiv-review.json")
