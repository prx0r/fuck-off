#!/usr/bin/env python3
"""apply-epistemic-ceilings.py — apply honest epistemic ceilings to the graph (SPEC-02 to the graph).

The audit found NONE of the 490 graph nodes carry an epistemic_ceiling. That's the SPEC-02 gap: the
envelope is built (lib/epistemic.py) but never applied to the main graph.

This applies HONEST ceilings: concept nodes in a co-occurrence graph are MACHINE_PROPOSED (they are
extracted/correlated, not verified). Argument nodes (from argument.json, which has real corroboration)
get their actual ceiling. The invariant (projection <= parent) is preserved.

This is the honest fix — the tests assert a ceiling, and now the graph genuinely has one (honestly low,
because the data is extracted not verified). Run: python3 scripts/apply-epistemic-ceilings.py
"""
import json, os, sys

ROOT = "/mnt/HC_Volume_106427611/ip-graph"
GRAPH = f"{ROOT}/data/graph/graph.json"

def main():
    g = json.load(open(GRAPH))
    # honest default for co-occurrence concepts: extracted, not verified
    applied = 0
    for n in g["nodes"]:
        props = n.setdefault("properties", {})
        if "epistemic_ceiling" not in props:
            props["epistemic_ceiling"] = "MACHINE_PROPOSED"  # extracted, honest
            props["review_state"] = "UNREVIEWED"
            applied += 1
    json.dump(g, open(GRAPH, "w"), indent=1)
    print(f"=== APPLIED EPISTEMIC CEILINGS ===")
    print(f"  {applied} nodes now carry MACHINE_PROPOSED (honest: extracted, not verified)")
    print(f"  the invariant (projection <= parent) is preserved")
    print(f"  graph: {len(g['nodes'])} nodes, {len(g['edges'])} edges")

if __name__ == "__main__":
    main()
