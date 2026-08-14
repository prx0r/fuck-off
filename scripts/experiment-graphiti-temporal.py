#!/usr/bin/env python3
"""experiment-graphiti-temporal.py — Graphiti's temporal validity pattern applied to our claims (Layer 09).

Graphiti (cloned) models edges with valid_at / invalid_at + episode timelines, and uses Episodic nodes
as provenance. We apply this temporal-validity pattern to our epistemic claims: each claim is valid
from when it was accepted until invalidated; querying "what was accepted at time T" returns the correct
temporal slice. This is the organism/user-knowledge temporal layer (Layer 09).
"""
import json

arg = json.load(open("/mnt/HC_Volume_106427611/ip-graph/data/graph/argument.json"))

# claims with temporal validity (simulated: when accepted, when invalidated)
# Graphiti model: edge has valid_at, invalid_at, episodes
claims_temporal = []
for n in arg["information_nodes"]:
    # higher ceiling = accepted earlier (corroborated physics was known first)
    accept_order = {"SCHOLARLY_CORROBORATED": 1, "SCHOLARLY_CORROBORATED_PRELIMINARY": 2, "MACHINE_PROPOSED": 3}
    claims_temporal.append({
        "id": n["id"], "text": n["text"],
        "ceiling": n["epistemic_ceiling"],
        "valid_at": accept_order.get(n["epistemic_ceiling"], 3),
        "invalid_at": None,   # still valid
    })

def accepted_at(time):
    """Graphiti query: what claims were valid (not invalidated) at time T?"""
    return [c for c in claims_temporal if c["valid_at"] <= time and (c["invalid_at"] is None or c["invalid_at"] > time)]

def invalidate(claim_id, at_time):
    """Graphiti: invalidate a claim at a time (episode ends)."""
    for c in claims_temporal:
        if c["id"] == claim_id:
            c["invalid_at"] = at_time

print("=== GRAPHITI TEMPORAL VALIDITY (Layer 09) ===\n")
print("claims with validity (valid_at = acceptance epoch, higher = later/less sure):")
for c in claims_temporal:
    print(f"  [{c['id']}] valid_at={c['valid_at']} ceiling={c['ceiling'][:30]:30s} {c['text'][:35]}")

print("\n-- temporal slice: what was accepted at time 1 (only corroborated) --")
for c in accepted_at(1):
    print(f"  {c['id']}: {c['text'][:40]}")

print("\n-- invalidate the QM-indeterminism claim (I1) at time 2 --")
invalidate("I1", 2)

print("-- temporal slice at time 3 (I1 now invalidated) --")
ids = [c["id"] for c in accepted_at(3)]
print(f"  accepted: {ids}  (I1 removed)")

print("\n=== INSIGHT ===")
print("Graphiti's valid_at/invalid_at + episodes gives TEMPORAL truth: what was accepted at any past")
print("time is replayable. This is the Layer 09 organism/user-knowledge temporal layer — user beliefs,")
print("question clusters, and concept mastery all carry validity periods, so 'what did we know and")
print("when' is always answerable (combined with our Merkle-root signed history from SPEC-19).")
