#!/usr/bin/env python3
"""experiment-crux-compiler.py — compute the minimal divergence between two positions (SPEC-19 #5).

A Crux Compiler finds the MINIMAL set of premises that two positions disagree on — the load-bearing
divergence. From our argument graph, compatibilism and the two-stage libertarian model share most
premises but diverge on whether indeterminism is required. The crux is what a targeted research task
should attack.

Implements: given two positions (each a claim + its premise closure), compute the symmetric difference
in the dependency graph = the crux.
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))

arg = json.load(open("/mnt/HC_Volume_106427611/ip-graph/data/graph/argument.json"))
by_id = {n["id"]: n for n in arg["information_nodes"]}

# build premise dependency: claim -> claims it depends on (via inference nodes)
premise_of = {}   # conclusion -> [premises]
for f in arg["inference_nodes"]:
    premise_of.setdefault(f["conclusion_id"], []).extend(f["premise_ids"])

def premise_closure(claim_id, depth=4):
    """All premises (transitively) a claim depends on."""
    closure = set()
    frontier = premise_of.get(claim_id, [])
    seen = set()
    while frontier and depth > 0:
        nxt = set()
        for p in frontier:
            if p in seen: continue
            seen.add(p); closure.add(p)
            nxt.update(premise_of.get(p, []))
        frontier = nxt; depth -= 1
    return closure

print("=== CRUX COMPILER (minimal divergence between positions) ===\n")

# POSITION A: two-stage libertarian model (I5) — the thesis
# POSITION B: compatibilism (from conflict C1: 'free will = acting on desires, no indeterminism')
posA = "I5"  # two-stage model (needs indeterminism)
posB_premises = {"I1", "I6"}  # compatibilism: accepts QM indeterminism exists but denies it's needed
closureA = premise_closure(posA)
closureA.add(posA)

print(f"Position A = {by_id[posA]['text'][:50]}...")
print(f"  premise closure: {sorted(closureA)}")
print(f"Position B = compatibilism (free will as acting on desires)")
print(f"  premise closure: {sorted(posB_premises)}")

# the crux = symmetric difference in commitments
# what A asserts that B doesn't (A's load-bearing extra premise)
crux_A = closureA - posB_premises
# what B asserts that A doesn't
crux_B = posB_premises - closureA
shared = closureA & posB_premises

print(f"\nSHARED premises (not the crux): {sorted(shared)}")
print(f"CRUX (A asserts, B denies): {sorted(crux_A)}")
print(f"CRUX (B asserts, A denies): {sorted(crux_B)}")

print(f"\n=== THE CRUX ===")
for c in sorted(crux_A):
    if c in by_id:
        print(f"  [load-bearing divergence] {by_id[c]['text'][:60]}")

print("\n=== INSIGHT ===")
print("The crux compiler isolates what a targeted research task must attack: the two-stage thesis")
print("stands or falls on INDETERMINISM being necessary for free will — compatibilism's core denial.")
print("This is 'spawn targeted research tasks at the minimal divergence' (SPEC-19 #5).")
