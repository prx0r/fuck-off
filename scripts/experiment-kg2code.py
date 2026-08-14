#!/usr/bin/env python3
"""experiment-kg2code.py — KG2Code-style executable graph queries for agents.

Paper: KG2Code (arXiv 2607.22652). Formulate KGQA as code generation: the KG becomes executable code
with verifiable traces. Instead of 40 MCP tools, give the agent a tiny graph-query language:
  resolve / neighbors / path / filter / evidence
The program executes DETERMINISTICALLY (agent plans, engine preserves truth).
"""
import json

g = json.load(open("/mnt/HC_Volume_106427611/ip-graph/data/graph/graph.json"))
nodes = {n["id"]: n for n in g["nodes"]}
label = {n["id"]: n["label"] for n in g["nodes"]}
edges = g["edges"]

# adjacency: concept -> [(neighbor, rel, evidence)]
adj = {}
for e in edges:
    f, t = e["from"], e["to"]
    if f in label and t in label:
        adj.setdefault(f, []).append((t, e["relationship"]))
        adj.setdefault(t, []).append((f, e["relationship"]))

# ---- the executable query language (KG2Code-style) ----
def resolve(name):
    """resolve('Free Will') -> concept node id (deterministic)."""
    for nid, n in nodes.items():
        if n["type"] == "concept" and n["label"].lower() == name.lower(): return nid
    return None

def neighbors(nid, rel=None):
    """neighbors(nid, rel=...) -> [(node_id, relationship)]"""
    return [n for n in adj.get(nid, []) if rel is None or n[1] == rel]

def path(start_id, end_id, via=None, max_hops=4):
    """path(from, to, via=[rels]) -> list of node-sequences (BFS, deterministic)."""
    from collections import deque
    q = deque([[start_id]])
    out = []
    while q:
        p = q.popleft()
        if len(p) > max_hops: continue
        last = p[-1]
        if last == end_id and len(p) > 1:
            out.append(p)
            if len(out) >= 5: break
            continue
        for (nb, rel) in adj.get(last, []):
            if nb not in p and (via is None or rel in via):
                q.append(p + [nb])
    return out

def evidence(nid):
    """evidence(nid) -> epistemic ceiling + review_state."""
    return {"ceiling": nodes[nid]["properties"].get("epistemic_ceiling"),
            "review_state": nodes[nid]["properties"].get("review_state")}

def run(program, expected_nodes):
    """Execute a composed query; assert it resolves to expected nodes (verifiable trace)."""
    result = program()
    if isinstance(result, list) and result and isinstance(result[0], list):
        trace = " | ".join(" -> ".join(label.get(n, n.split(':')[-1]) for n in p) for p in result[:2])
        ok = any(label.get(n) in expected_nodes for p in result for n in p)
    else:
        trace = [label.get(n, n) for n in result] if isinstance(result, list) else result
        ok = isinstance(result, list) and any(label.get(n) in expected_nodes for n in result)
    return trace, ok

print("=== KG2CODE: executable graph queries (deterministic, verifiable) ===\n")

# Query 1: resolve + neighbors with relation filter
print("Q: what concepts is Free Will connected to?")
fw = resolve("Free Will")
print(f"  resolve('Free Will') -> {fw.split(':')[-1]}")
for n, rel in neighbors(fw)[:6]:
    print(f"    {label[n]:18s} ({rel})")

# Query 2: composed path query with relation filter
print("\nQ: path from Quantum Mechanics to Free Will via presupposition-like edges")
qm = resolve("Quantum Mechanics")
for p in path(qm, fw, max_hops=3)[:3]:
    print("  " + " -> ".join(label[n].split(":")[-1] for n in p))

# Query 3: verifiable trace (KG2Code's key property)
print("\nQ: does a 2-hop path Quantum->FreeWill exist? (verifiable)")
trace, ok = run(lambda: path(qm, fw, max_hops=2), ["Free Will"])
print(f"  executed; resolved={'YES' if ok else 'NO'}, trace={trace}")

# Query 4: evidence alongside
print("\nQ: evidence for Free Will")
print(f"  {evidence(fw)}")

print("\n=== INSIGHT ===")
print("KG2Code gives agents a tiny deterministic graph language (resolve/neighbors/path/evidence)")
print("instead of 40 MCP tools. The agent writes the PLAN; the engine executes TRUTH-PRESERVING code")
print("with verifiable traces — this is our Bet 2 and the agent-query frontier. Adopt into Layer 06.")
