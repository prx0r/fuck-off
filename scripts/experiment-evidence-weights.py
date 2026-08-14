#!/usr/bin/env python3
"""experiment-evidence-weights.py — Kappa-style epistemic weighting (experimental).

For each concept, compute:
  grounding      = fraction of corpus documents mentioning it (how anchored it is)
  support        = weighted co-occurrence with corroborated concepts (physics/info)
  contradiction  = how often it co-occurs with the philosophical thesis set
  diversity      = number of distinct sections it appears in

This is EXPERIMENTAL: it tests whether the data reveals meaningful epistemic structure beyond raw
term co-occurrence. NOT the final scoring — just a probe.
"""
import os, sys, json, re
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from epistemic import rank

CORPUS = "/mnt/HC_Volume_106427611/ip-graph/data/corpus.jsonl"
GRAPH = "/mnt/HC_Volume_106427611/ip-graph/data/graph/graph.json"
OUT = "/mnt/HC_Volume_106427611/ip-graph/data/graph/evidence-weights.json"

# concept lexicon (id -> phrase) — reuse the same set as the graph
CONCEPTS = {
    "free_will": "free will", "determinism": "determinism", "indeterminism": "indeterminism",
    "causality": "causality", "entropy": "entropy", "information": "information",
    "consciousness": "consciousness", "qualia": "qualia", "quantum_mechanics": "quantum",
    "wave_function": "wave function", "entanglement": "entanglement", "measurement": "measurement",
    "superposition": "superposition", "probability": "probability", "randomness": "randomness",
    "chance": "chance", "knowledge": "knowledge", "belief": "belief", "truth": "truth",
    "mind": "mind", "agency": "agency", "responsibility": "responsibility",
    "compatibilism": "compatibilism", "libertarianism": "libertarianism",
    "arrow_of_time": "arrow of time", "second_law": "second law", "computation": "computation",
    "life": "life", "evolution": "evolution", "value": "value", "morality": "morality",
}
# corroborated (grounded) vs thesis (speculative) concept sets
GROUNDED = {"entropy","information","probability","quantum_mechanics","measurement","superposition",
            "wave_function","entanglement","information_theory","computation","second_law",
            "arrow_of_time","causality","determinism","life","evolution","randomness","knowledge"}
THESIS = {"free_will","agency","responsibility","value","morality","belief","truth","chance","qualia",
          "compatibilism","libertarianism","indeterminism","consciousness","mind"}

def norm(s): return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()

# per-doc concept presence + section
doc_concepts = {}  # id -> set of concepts
sections = {}
N = 0
for l in open(CORPUS):
    r = json.loads(l); text = norm(r["text"]); N += 1
    present = {cid for cid, phrase in CONCEPTS.items() if phrase in text}
    doc_concepts[r["id"]] = present
    sections[r["id"]] = r["section"]

from collections import Counter, defaultdict
df = Counter()          # doc frequency
sec_count = defaultdict(set)
for did, cs in doc_concepts.items():
    for c in cs:
        df[c] += 1
        sec_count[c].add(sections[did])

# support / contradiction via co-occurrence
support = defaultdict(float); contradict = defaultdict(float)
for did, cs in doc_concepts.items():
    grounded_hit = bool(cs & GROUNDED)
    thesis_hit = bool(cs & THESIS)
    for c in cs:
        if c in GROUNDED: support[c] += 1.0
        if c in THESIS: contradict[c] += 0.5   # thesis concepts co-occurring = proposed, contested
        if grounded_hit and c in THESIS:
            contradict[c] += 0.3   # thesis grounded alongside physics -> tension (proposed bridge)

rows = {}
for cid in CONCEPTS:
    rows[cid] = {
        "concept": cid,
        "grounding": round(df[cid]/N, 3),
        "doc_frequency": df[cid],
        "support_weight": round(support.get(cid,0), 2),
        "contradiction_weight": round(contradict.get(cid,0), 2),
        "section_diversity": len(sec_count.get(cid, set())),
        "class": "GROUNDED" if cid in GROUNDED else ("THESIS" if cid in THESIS else "MIXED"),
    }

json.dump({"N_docs": N, "concepts": rows}, open(OUT, "w"), indent=1)

print("=== KAPPA-STYLE EVIDENCE WEIGHTS (experimental probe) ===")
print(f"documents: {N}")
print(f"\n{'concept':16s} {'class':10s} {'ground':>6s} {'df':>4s} {'support':>8s} {'contra':>7s} {'sections':>8s}")
for cid in sorted(rows, key=lambda c: -rows[c]["grounding"]):
    r = rows[cid]
    print(f"{cid:16s} {r['class']:10s} {r['grounding']:6.3f} {r['doc_frequency']:4d} "
          f"{r['support_weight']:8.1f} {r['contradiction_weight']:7.1f} {r['section_diversity']:8d}")
print(f"\nwrote {OUT}")
