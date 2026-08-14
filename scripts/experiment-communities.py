#!/usr/bin/env python3
"""experiment-communities.py — apply graph community detection to our concept graph (Layer 02 themes).

nano-graphrag (and GraphRAG) detect communities to build thematic clusters. We apply Louvain/community
detection to our concept graph to surface emergent themes WITHOUT an LLM — a deterministic thematic map.
This is the "theme" discovery that patala's Layer 02 needs, and it's what nano-graphrag does structurally.
"""
import json, os, sys
import networkx as nx

g = json.load(open("/mnt/HC_Volume_106427611/ip-graph/data/graph/graph.json"))
G = nx.Graph()
labels = {}
for n in g["nodes"]:
    if n["type"] == "concept":
        G.add_node(n["id"], label=n["label"]); labels[n["id"]] = n["label"]
for e in g["edges"]:
    if e["from"].startswith("ip:concept") and e["to"].startswith("ip:concept"):
        G.add_edge(e["from"], e["to"], weight=float(e.get("properties", {}).get("weight", 1)))

print("=== COMMUNITY DETECTION on our concept graph (emergent themes) ===\n")
print(f"concept graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

# try python-louvain
try:
    import community
    partition = community.best_partition(G, weight="weight", random_state=42)
    method = "python-louvain (best_partition)"
except ImportError:
    # fallback: greedy modularity
    from networkx.algorithms.community import greedy_modularity_communities
    comms = list(greedy_modularity_communities(G, weight="weight"))
    partition = {}
    for ci, members in enumerate(comms):
        for m in members: partition[m] = ci
    method = "networkx greedy-modularity"

# group by community
from collections import defaultdict
comm_members = defaultdict(list)
for node, c in partition.items():
    comm_members[c].append(labels.get(node, node))

print(f"method: {method}")
print(f"communities found: {len(comm_members)}\n")
for c in sorted(comm_members, key=lambda x: -len(comm_members[x])):
    members = comm_members[c]
    if len(members) >= 2:
        print(f"  community {c} ({len(members)} concepts): {', '.join(sorted(members))}")

print("\n=== INSIGHT ===")
print("These are the EMERGENT themes from co-occurrence alone (no LLM): they should roughly match")
print("our hand-assigned 11 themes (quantum, information, mind, free-will, value...). Comparing the")
print("communities to the curated ontology reveals where the corpus structure agrees or disagrees.")
