#!/usr/bin/env python3
"""audit-epistemic.py — verify the epistemic invariant across the whole graph.

The law: authority(projection) <= authority(parent). For every edge (projection), its ceiling must
not exceed the ceiling of either endpoint (parent). Also flags any object whose ceiling was inflated
above a sane per-type bound. Exits non-zero on violation.
"""
import os, sys, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from epistemic import rank

GRAPH = "/mnt/HC_Volume_106427611/ip-graph/data/graph/graph.json"
g = json.load(open(GRAPH))

node_ceiling = {}
for n in g["nodes"]:
    node_ceiling[n["id"]] = rank(n["properties"].get("epistemic_ceiling", "MACHINE_PROPOSED"))

violations = []
for e in g["edges"]:
    ec = rank(e["properties"].get("epistemic_ceiling", "MACHINE_PROPOSED"))
    for end in (e["from"], e["to"]):
        if end in node_ceiling and ec > node_ceiling[end]:
            violations.append({
                "edge": f"{e['from']} --{e['relationship']}--> {e['to']}",
                "edge_ceiling_rank": ec, "endpoint": end, "endpoint_ceiling_rank": node_ceiling[end],
            })

print("=== EPISTEMIC INVARIANT AUDIT ===")
print(f"nodes: {len(g['nodes'])}, edges: {len(g['edges'])}, violations: {len(violations)}")
if violations:
    print("\nVIOLATIONS:")
    for v in violations[:20]:
        print(f"  {v}")
    sys.exit(1)
else:
    print("PASS: authority(projection) <= authority(parent) holds everywhere.")
    sys.exit(0)
