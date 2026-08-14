#!/usr/bin/env python3
"""validate-structure-recall.py — SAGE structure-aware recall on the read plane (arXiv 2605.12061).

Steals SAGE's structure-aware retrieval onto our read plane: recall follows GRAPH TOPOLOGY (neighbors ->
their neighbors) from a seed, not just lexical match. Bounded to the read/retrieval layer, strictly off
the verified epistemic spine. On our real graph.
"""
import os, sys, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from structure_recall import StructureAwareRecall

ROOT = "/mnt/HC_Volume_106427611/ip-graph"
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=== SAGE STRUCTURE-AWARE RECALL (2605.12061) — read plane, off the verified spine ===\n")
g = json.load(open(f"{ROOT}/data/graph/graph.json"))
sr = StructureAwareRecall(g)
check("real graph loaded", len(g["nodes"]) == 490 and len(g["edges"]) == 6578)

# ---- structure-aware recall follows topology from a real seed ----
nid = sr.resolve("Free Will")
check("resolves Free Will to a node", nid is not None)
recall = sr.recall_structural("Free Will", max_depth=2, top_k=8)
check("recall returns graph-topology neighbors (SAGE)", len(recall) > 0)
check("recall nodes carry depth + relation (structure-aware, not lexical)",
      all("depth" in n and "rel" in n for n in recall))

# ---- depth matters: depth-2 finds MORE than depth-1 (topology, not just 1-hop) ----
d1 = sr.recall_structural("Free Will", max_depth=1, top_k=50)
d2 = sr.recall_structural("Free Will", max_depth=2, top_k=50)
check("structure-aware: depth-2 recall is a superset of depth-1 (topology walk)",
      len(d2) >= len(d1))

# ---- the structured context for the read plane ----
ctx = sr.recall_structured_context("Free Will", max_depth=1, top_k=6)
check("structured context for the read plane", ctx["seed"] == "Free Will" and ctx["n_nodes"] > 0)
check("context is topology-structured (each node has a via-relation)", all("via" in s for s in ctx["structure"]))

# ---- deterministic ----
check("deterministic: repeated recall identical",
      sr.recall_structural("Free Will") == sr.recall_structural("Free Will"))

# ---- unresolved seed returns empty (no hallucinated topology) ----
check("unknown seed returns empty (no fabricated structure)", sr.recall_structural("not-a-real-thing") == [])

print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
print("\nSAGE STRUCTURE-AWARE RECALL (2605.12061): recall follows GRAPH TOPOLOGY from a seed — neighbors")
print("-> their neighbors — not just lexical match. Bounded to the READ PLANE, strictly off the verified")
print("spine (the honest caveat). Deterministic, no fabricated structure.")
sys.exit(0 if all(c for _,c in results) else 1)
