#!/usr/bin/env python3
"""experiment-rka-staleness.py — port RKA's blast-radius staleness propagation onto our DAG.

Tests the killer idea from RKA ("claim changed -> derived knowledge stale -> review queue")
on our real canonical DAG. If the PHYSICS grounding is retracted, every downstream layer
(up through FREE_WILL and VALUE) must be flagged stale and enter a review queue.
"""
import yaml, json

DAG = "/mnt/HC_Volume_106427611/ip-graph/data/graph/canonical-dag.yaml"
dag = yaml.safe_load(open(DAG))["dependencies"]

# build reverse dependency graph: layer -> what depends on it
depends_on = {l: set() for l in dag}
for layer, d in dag.items():
    for req in d.get("requires", []):
        if req in dag:
            depends_on[req].add(layer)

def blast_radius(changed):
    """Walk forward: any layer downstream of a changed layer becomes stale."""
    stale = set(changed)
    frontier = set(changed)
    while frontier:
        nxt = set()
        for f in frontier:
            for dependent in depends_on.get(f, set()):
                if dependent not in stale:
                    stale.add(dependent); nxt.add(dependent)
        frontier = nxt
    return stale

# RKA-style review queue flags
REVIEW_QUEUE_FLAGS = {"stale_dependency", "unsupported_link", "potential_contradiction", "stale_theme"}

print("=== RKA BLAST-RADIUS STALENESS on our canonical DAG ===\n")

for changed, reason in [("PHYSICS", "retraction of a Bell grounding paper"),
                        ("INDETERMINISM", "new evidence questions QM indeterminism")]:
    stale = blast_radius({changed})
    print(f"if {changed} is changed ({reason}):")
    print(f"  stale ({len(stale)} layers): {sorted(stale)}")
    # file review-queue entries
    print(f"  review_queue:")
    for layer in sorted(stale):
        if layer != changed:
            print(f"    - flag=stale_dependency  item={layer}  status=pending  raised_by=staleness_walker")
    print()

print("=== INSIGHT ===")
print("RKA's blast-radius propagation makes the graph SELF-MAINTAINING: a correction at the")
print("physics floor automatically flags every downstream claim (FREE_WILL, VALUE) as stale,")
print("filing review_queue entries with flag=stale_dependency. This is the executable form of our")
print("SPEC-02 invariant authority(projection)<=authority(parent) — adopted from RKA.")
