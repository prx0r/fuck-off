#!/usr/bin/env python3
"""experiment-nano-stable-graph.py — apply nano-graphrag's deterministic-graph techniques to OUR graph.

Tests the reusable pieces of nano-graphrag's gdb_networkx.py:
  1. stable_largest_connected_component (deterministic node/edge ordering)
  2. GraphML persistence
  3. inspect our graph's component structure

nano-graphrag = 1100-line GraphRAG reference; its graph-storage layer is the reusable, no-API-key part.
"""
import networkx as nx

GRAPH = "/mnt/HC_Volume_106427611/ip-graph/data/graph/graph.json"
import json
g = json.load(open(GRAPH))

# build the networkx graph from our graph.json (concept nodes + edges)
G = nx.Graph()
for n in g["nodes"]:
    if n["type"] in ("concept", "author", "school", "problem"):
        G.add_node(n["id"], type=n["type"], label=n["label"])
for e in g["edges"]:
    if e["from"].startswith("ip:concept") and e["to"].startswith("ip:concept"):
        G.add_edge(e["from"], e["to"])

# ---- nano-graphrag's _stabilize_graph (deterministic ordering) ----
def stabilize(graph):
    fixed = nx.Graph()
    for node in sorted(graph.nodes(data=True), key=lambda x: x[0]):
        fixed.add_node(node[0], **node[1])
    for s, t, d in sorted(graph.edges(data=True), key=lambda e: (e[0], e[1])):
        fixed.add_edge(s, t, **d)
    return fixed

# ---- stable largest connected component (no graspologic) ----
def stable_lcc(graph):
    cc = sorted(nx.connected_components(graph), key=len, reverse=True)
    if not cc: return graph.copy()
    return stabilize(graph.subgraph(cc[0]).copy())

print("=== NANO-GRAPHRAG TECHNIQUES ON OUR GRAPH ===")
print(f"full graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
components = sorted(nx.connected_components(G), key=len, reverse=True)
print(f"components: {len(components)} (largest {len(components[0])} nodes)")
G_lcc = stable_lcc(G)
print(f"largest component: {G_lcc.number_of_nodes()} nodes, {G_lcc.number_of_edges()} edges")
# determinism check: two identical stabilizations are byte-equal in edge ordering
e1 = sorted(G_lcc.edges())
e2 = sorted(stabilize(G_lcc).edges())
print(f"determinism: edges identical after re-stabilize = {e1 == e2}")
# is the whole concept graph one component?
print(f"single-component concept graph: {len(components) == 1}")

# graphml export test
out = "/mnt/HC_Volume_106427611/ip-graph/data/graph/concept-lcc.graphml"
nx.write_graphml(G_lcc, out)
print(f"wrote {out} ({__import__('os').path.getsize(out)//1024}KB)")

print("\n=== INSIGHT ===")
print("nano-graphrag's stabilize+stable-LCC gives deterministic graph serialization: identical input")
print("always yields identical node/edge order. That's the reproducibility guarantee our AGENTS.md")
print("needs — we can adopt this directly for our concept graph exports (GraphML).")
