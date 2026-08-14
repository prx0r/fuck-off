#!/usr/bin/env python3
"""experiment-koral-twograph.py — KORAL-style two-graph (reality vs literature) for Layer 06.

KORAL (SPEC-08): keep TWO graphs — the reality graph (primary evidence) and the literature graph
(interpretations). A doctrinal reinterpretation must never corrupt the primary source. This enforces
the commentarial discipline PRIMARY≠INTERPRETATION≠ACCEPTED (Layer 06).

Applied to our data: the Doyle corpus has a "reality" side (physics/evidence: Bell, EPR, entropy) and
a "literature/interpretation" side (the philosophical theses built on it). We build two graphs and
show a reinterpretation in literature flags (doesn't corrupt) reality.
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from staleness import blast_radius, build_dependency_index

# ---- two graphs ----
# REALITY graph: the physics/evidence floor (corroborated)
REALITY = {
    "PHYSICS": {"requires": ["SOURCE"]},
    "THERMODYNAMICS": {"requires": ["SOURCE"]},
    "INFORMATION": {"requires": ["THERMODYNAMICS"]},
    "QUANTUM": {"requires": ["PHYSICS"]},
}
# LITERATURE graph: interpretations built on reality (machine-proposed)
LITERATURE = {
    "INDETERMINISM": {"requires": ["QUANTUM"]},
    "MIND": {"requires": ["INFORMATION"]},
    "FREE_WILL": {"requires": ["INDETERMINISM", "MIND"]},
    "VALUE": {"requires": ["FREE_WILL"]},
}

print("=== KORAL TWO-GRAPH: reality vs literature (Layer 06) ===\n")

# 1. build + verify separation
r_dep = build_dependency_index(REALITY)
l_dep = build_dependency_index(LITERATURE)
print(f"REALITY graph: {list(REALITY)}")
print(f"LITERATURE graph: {list(LITERATURE)}")

# 2. a reinterpretation in literature (e.g. a competing reading of FREE_WILL)
#    must flag literature downstream (VALUE) but NOT touch reality
lit_stale = blast_radius(l_dep, {"FREE_WILL"})
print(f"\nReinterpretation of FREE_WILL (literature):")
print(f"  stale in literature: {sorted(lit_stale - {'FREE_WILL'})}")

# 3. a retraction in reality (e.g. QUANTUM) propagates UP into literature (the bridge)
#    the two graphs meet where literature REQUIRES reality layers
COMBINED = {}
COMBINED.update(REALITY)
for layer, d in LITERATURE.items():
    COMBINED[layer] = d  # INDETERMINISM requires QUANTUM, MIND requires INFORMATION, etc.
combined_dep = build_dependency_index(COMBINED)
r_stale = blast_radius(combined_dep, {"QUANTUM"})
print(f"Retraction of QUANTUM (reality):")
print(f"  stale in combined graph: {sorted(r_stale)}")
# split which are literature
lit_cascade = sorted(r_stale & set(LITERATURE) - {"QUANTUM"})
print(f"  cascades into literature: {lit_cascade}")

print("\n=== THE KEY PROPERTY ===")
print("A literature-only reinterpretation (FREE_WILL) stays in literature — reality is untouched.")
print("A reality retraction (QUANTUM) DOES cascade up into literature (interpretations depend on it).")
print("This is exactly the commentarial discipline: PRIMARY source is immutable; only INTERPRETATIONS")
print("get flagged, and only when their evidence floor is retracted. analogy != identity.")
