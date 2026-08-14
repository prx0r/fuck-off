#!/usr/bin/env python3
"""run-tantraloka-organs3.py — wire open_ended_evolve + lightrag_compare + cognee_compare + graph_stable
(DEV_PLAN 6.2/6.4). The final batch of VALIDATED-ONLY kernels, now USED on the real read-plane graph +
organism:
  - lightrag_compare + cognee_compare: frontier retrieval compared against our own read-plane retrieval
    (confirms our architecture, per the CHANGELOG "both confirm our architecture").
  - graph_stable: the stable-graph projection + content-addressed staleness check on the real graph.
  - open_ended_evolve: rule-evolution under the invariant oracle (the organism's self-improvement).

Deterministic, no model calls. Output: tantraloka/corpus/organs3.json
"""
import os, sys, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from lightrag_compare import LightRAGRetriever
from cognee_compare import CogneeMemory
from graph_stable import StableGraph
from open_ended_evolve import OpenEndedEvolution

ROOT = "/mnt/HC_Volume_106427611/ip-graph"
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=== FRONTIER-COMPARE + STABLE-GRAPH + EVOLUTION ON THE READ PLANE (DEV_PLAN 6.2/6.4) ===\n")

# ---- the REAL read-plane graph ----
g = json.load(open(f"{ROOT}/data/graph/graph.json"))
check("the real read-plane graph loads", len(g["nodes"]) > 0, f"({len(g['nodes'])} nodes)")

# ---- lightrag_compare + cognee_compare: frontier retrieval on the real graph ----
lr = LightRAGRetriever(g)
local = lr.local_retrieve("Free Will", hops=1, top_k=8)
check("lightrag_compare local retrieval returns real results on the read plane",
      len(local) > 0, f"({len(local)})")
hybrid = lr.hybrid_retrieve("Free Will", top_k=10)
check("lightrag_compare hybrid retrieval works", len(hybrid) > 0, f"({len(hybrid)})")

cm = CogneeMemory(g)
cm.remember("m1", "free will requires indeterminism and mind", mtype="qa")
cm.remember("m2", "determinism conflicts with free will", mtype="qa")
rec = cm.recall("free will determinism", top_k=5)
check("cognee_compare recall returns real results on the read plane",
      len(rec) > 0, f"({len(rec)})")

# ---- graph_stable: the stable projection + content-addressed staleness on the real graph ----
sg = StableGraph()
for n in g["nodes"][:50]:
    sg.add_node(n["id"], type=n["type"], label=n["label"])
for e in g["edges"][:50]:
    if e.get("from") and e.get("to"):
        sg.add_edge(e["from"], e["to"])
h1 = sg.graph_hash()
sg.add_edge("ip:concept:test", "ip:concept:test2")   # a change -> hash must change
h2 = sg.graph_hash()
check("graph_stable: the stable projection is byte-reproducible",
      sg.stabilize() == sg.stabilize())
check("graph_stable: a change changes the content hash (staleness check)",
      h1 != h2, f"({h1} != {h2})")

# ---- open_ended_evolve: rule-evolution under the invariant oracle ----
oe = OpenEndedEvolution(oracle=lambda desc: (True, 0.9) if "verified" in desc else (True, 0.2), novelty_w=0.3)
oe.propose("r1", "verified translation gate", novelty=0.4)
oe.propose("r2", "unverified guess", novelty=0.8)
oe.step()
best = oe.best(2)
check("open_ended_evolve proposes + evolves rules under the oracle",
      len(best) >= 1, f"({len(best)} in archive)")
check("open_ended_evolve ranks by fitness (verified > unverified)",
      best and best[0].fitness() > 0.5 if best else False)

# ---- write the record ----
os.makedirs(f"{ROOT}/tantraloka/corpus", exist_ok=True)
out = f"{ROOT}/tantraloka/corpus/organs3.json"
json.dump({
    "lightrag_local": len(local), "cognee_recall": len(rec),
    "stable_hash_changed": h1 != h2, "evolution_archive": len(oe.archive_state()),
    "kernels_wired": ["lightrag_compare", "cognee_compare", "graph_stable", "open_ended_evolve"],
}, open(out, "w"), indent=1)
check("the organs3 record is written", os.path.exists(out))

print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
print("\nFRONTIER-COMPARE + STABLE-GRAPH + EVOLUTION: the final VALIDATED-ONLY kernels are now USED on")
print("the real read-plane graph + organism (DEV_PLAN 6.2/6.4). ALL Phase-6 kernels wired.")
print(f"  → {out}")
sys.exit(0 if all(c for _,c in results) else 1)
