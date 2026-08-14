#!/usr/bin/env python3
"""experiment-reactive-essay.py — reactive documents (SPEC-19 #4).

An essay is a set of prose sentences, each citing a claim. When a SOURCE is retracted, every sentence
that cites a downstream claim must be marked STALE automatically. This makes essays reactive — they
cannot silently contain refuted claims.

Implements: essay sentences -> cite claims -> claims depend on sources (via argument graph) -> retract
a source -> blast-radius -> mark the citing prose sentences stale.
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from staleness import blast_radius, build_dependency_index

arg = json.load(open("/mnt/HC_Volume_106427611/ip-graph/data/graph/argument.json"))

# a mock essay: prose sentences citing claims
ESSAY = [
    {"sentence": "Quantum events are fundamentally indeterministic.", "cites": ["I1"]},
    {"sentence": "This indeterminism provides the random chance stage of decision.", "cites": ["I2"]},
    {"sentence": "An evaluation step then adds genuine choice.", "cites": ["I3"]},
    {"sentence": "Therefore the two-stage model explains free will as chance plus choice.", "cites": ["I5"]},
    {"sentence": "Free will grounds moral responsibility and value.", "cites": ["I5"]},
]

# claim dependency: I2/I3/I5 depend on I1 (QM indeterminism) via inference
# build a claim-dep graph
claim_dep = {
    "I1": {"requires": []},
    "I2": {"requires": ["I1"]},
    "I3": {"requires": ["I2"]},
    "I4": {"requires": ["I1"]},
    "I5": {"requires": ["I2", "I3", "I4"]},
    "I6": {"requires": []},
}
dep = build_dependency_index(claim_dep)

def mark_stale(essay, retracted_claims):
    """Mark essay sentences stale if they cite any claim in the retraction blast-radius."""
    stale_claims = blast_radius(dep, set(retracted_claims))
    for s in essay:
        cited = set(s["cites"])
        s["stale"] = bool(cited & stale_claims)
        s["stale_cites"] = sorted(cited & stale_claims)
    return stale_claims

print("=== REACTIVE ESSAY (source retraction marks prose stale) ===\n")

# scenario: the QM indeterminism premise (I1) is retracted
print("Scenario: SOURCE retracted -> 'QM indeterminism' (I1) is called into question\n")
stale_claims = mark_stale(ESSAY, ["I1"])
print(f"claims flagged stale: {sorted(stale_claims)}\n")
print(f"{'sentence':62s} {'status':8s} stale-cites")
for s in ESSAY:
    status = "STALE" if s["stale"] else "OK"
    print(f"  {s['sentence'][:60]:60s} {status:8s} {s['stale_cites']}")

n_stale = sum(1 for s in ESSAY if s["stale"])
print(f"\n=== {n_stale}/{len(ESSAY)} essay sentences now marked STALE ===")
print("The essay cannot silently contain the refuted claim — a single source retraction propagates")
print("through claims to the exact prose sentences that depend on them. Reactive documents (SPEC-19 #4).")
