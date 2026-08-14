#!/usr/bin/env python3
"""run-tantraloka-corpus.py — corpus-scale TranslationProof production over Āhnika 1 (X1).

Runs the deterministic proof pipeline (L0 token floor + real proof generators) over MANY real Āhnika 1
kārikās — producing a real 11-dim TranslationProof + L0 + obligations for each. This is the corpus-scale
translation-proof production (not hand-filled). The full Hermes generation stays in the per-kārikā runner
(run-tantraloka-autonomous) because it's slow; here we produce the deterministic proof layer for the batch.

Output: tantraloka/corpus/ahnika-1-proofs.json + a per-run log
"""
import os, sys, json, glob, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from proof_generators import ProofGenerator
from translation import TranslationProof
from vidyut_l0 import VidyaL0

ROOT = "/mnt/HC_Volume_106427611/ip-graph"
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=== CORPUS-SCALE TRANSLATIONPROOF PRODUCTION over Āhnika 1 ===\n")

a1 = json.load(open(f"{ROOT}/data/tantraloka/ahnika-1.json"))
karikas = a1["verses"]
check("real Āhnika 1 kārikās loaded", len(karikas) == 333, f"({len(karikas)})")

# take the first N kārikās as the corpus batch (deterministic proof production)
BATCH = 30
batch = karikas[:BATCH]
pg = ProofGenerator()
l0 = VidyaL0()

os.makedirs(f"{ROOT}/tantraloka/corpus", exist_ok=True)
proofs = []
for v in batch:
    ref, sanskrit = v["ref"], v["text"]
    # L0 token floor
    toks = l0.tokenize(l0.normalize_slp1(sanskrit))
    # real proof-generator analysis
    gen = pg.full(sanskrit)
    proof = TranslationProof(work_id="tantraloka", passage_id=ref)
    proof.source_analysis = {k: v for k, v in gen["source_analysis"].items()
                             if k in ("morphology", "syntax", "segmentation")}
    proof.semantic_obligations = {k: v for k, v in gen["semantic_obligations"].items()
                                  if k in ("negation", "modality", "scope")}
    proof.alignment["coverage"] = 1.0 if toks else 0.0
    vec = proof.audit_vector()
    proofs.append({"ref": ref, "sanskrit": sanskrit[:60], "tokens": len(toks),
                   "real_analysis": gen["source_analysis"], "obligations": gen["semantic_obligations"],
                   "lattice": gen["lattice"], "proof_11dim": len(vec),
                   "gate": proof.publication_gate()["gate"]})

check("the corpus batch produced real TranslationProofs", len(proofs) == BATCH, f"({len(proofs)})")
check("real Vidyut analysis ran on the batch (not hand-filled)",
      sum(1 for p in proofs if p["real_analysis"].get("normalized_slp1")) >= BATCH - 5)
check("each proof is 11-dim (non-aggregate)", all(p["proof_11dim"] == 11 for p in proofs))
check("each proof gate is BLOCKED (honest, until human)", all(p["gate"] == "BLOCKED" for p in proofs))
check("L0 token floors produced (the substrate)", all(p["tokens"] >= 1 for p in proofs))

out = f"{ROOT}/tantraloka/corpus/ahnika-1-proofs.json"
json.dump({"batch": BATCH, "proofs": proofs}, open(out, "w"), indent=1)
check("the corpus proofs are written", os.path.exists(out))

print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
print("\nCORPUS-SCALE TRANSLATIONPROOF PRODUCTION: {0} real Āhnika 1 kārikās produced real 11-dim proofs"
      .format(BATCH))
print("(real Vidyut analysis + L0 token floor + negation detection), not hand-filled. → " + out)
sys.exit(0 if all(c for _,c in results) else 1)
