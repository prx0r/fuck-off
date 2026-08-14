#!/usr/bin/env python3
"""validate-graph-stable.py — the stable-graph projection kernel (DEV_PLAN §1.5).

Verifies: identical input yields byte-identical stable output (determinism); the LCC is deterministic;
the content hash is a staleness check (hash mismatch = stale); stable LCC isolates the largest component.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from graph_stable import StableGraph

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=== STABLE-GRAPH PROJECTION (lib/graph_stable.py) ===\n")

# ---- build a graph from a small knowledge structure (concepts + edges) ----
g = StableGraph()
g.add_node("free_will", type="concept")
g.add_node("indeterminism", type="concept")
g.add_node("determinism", type="concept")
g.add_node("quantum", type="concept")
g.add_node("causality", type="concept")
g.add_edge("free_will", "indeterminism")
g.add_edge("free_will", "determinism")
g.add_edge("indeterminism", "quantum")
g.add_edge("causality", "determinism")

# ---- 1. determinism: identical input -> byte-identical stable output ----
s1 = g.stabilize()
s2 = g.stabilize()
check("stable projection is byte-reproducible (identical input -> identical output)",
      s1 == s2, f"({len(s1['nodes'])} nodes, {len(s1['edges'])} edges)")
# the two additions below are in different order but the set is the same -> stable result must be identical
g2 = StableGraph()
g2.add_node("b"); g2.add_node("a"); g2.add_node("c")
g2.add_edge("c", "a"); g2.add_edge("a", "b")   # added in different order
g3 = StableGraph()
g3.add_node("c"); g3.add_node("a"); g3.add_node("b")
g3.add_edge("a", "b"); g3.add_edge("a", "c")
check("node/edge insertion order does NOT change the stable projection",
      g2.stabilize() == g3.stabilize())

# ---- 2. the content hash is a staleness check ----
h1 = g.graph_hash()
g.add_edge("quantum", "causality")   # a change -> the hash MUST change
h2 = g.graph_hash()
check("a graph change changes the content hash (hash mismatch = stale)",
      h1 != h2, f"({h1} != {h2})")

# ---- 3. the stable LCC is deterministic + isolates the largest component ----
lcc = g.stable_lcc()
# the graph: free_will-indeterminism-quantum-causality-determinism-free_will = all 5 connected
check("the stable LCC keeps all connected nodes", lcc.summary()["nodes"] == 5, f"({lcc.summary()['nodes']})")
check("the LCC is deterministic", lcc.stabilize() == lcc.stabilize())

# ---- 4. disconnected components are correctly isolated ----
g4 = StableGraph()
g4.add_node("x"); g4.add_node("y"); g4.add_node("z")
g4.add_edge("x", "y")   # component of 2
g4.add_node("solo")     # isolated
check("the stable LCC isolates the largest component (2, not the isolated nodes)",
      g4.stable_lcc().summary()["nodes"] == 2, f"({g4.stable_lcc().summary()['nodes']})")
check("components are counted correctly (x-y, z, solo)", g4.n_components() == 3)

s = g4.summary()
check("summary reports the graph honestly", s["nodes"] == 4 and s["components"] == 3, f"({s})")

print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
print("\nSTABLE-GRAPH PROJECTION: deterministic byte-reproducible serialization + content-addressed")
print("staleness check + stable LCC. The Co-Evolving Organism's stable projection (DEV_PLAN §1.5, SPEC-13).")
sys.exit(0 if all(c for _,c in results) else 1)
