#!/usr/bin/env python3
"""experiment-signed-corpus.py — Merkle root over the corpus + signed release (SPEC-19 #6/7).

Content-address the accepted epistemic state into a Merkle tree, producing a single root hash that
fingerprints the entire corpus. Any change to any claim/edge changes the root. This is the
'signed corpus root' + 'immutable release' — the provable, reproducible snapshot.
"""
import json, hashlib, os

ROOT = "/mnt/HC_Volume_106427611/ip-graph"
def sha(b): return hashlib.sha256(b.encode() if isinstance(b, str) else b).hexdigest()

# collect all canonical objects as canonical-JSON strings
objects = []
arg = json.load(open(f"{ROOT}/data/graph/argument.json"))
for n in arg["information_nodes"]:
    objects.append(json.dumps({"type":"claim","id":n["id"],"text":n["text"],
                               "ceiling":n["epistemic_ceiling"]}, sort_keys=True))
for f in arg["inference_nodes"]:
    objects.append(json.dumps({"type":"inference","id":f["id"],"scheme":f["scheme"],
                               "premises":f["premise_ids"],"conclusion":f["conclusion_id"]}, sort_keys=True))
for c in arg["conflict_nodes"]:
    objects.append(json.dumps({"type":"conflict","id":c["id"],"a":c["a_id"],"b":c["b_id"]}, sort_keys=True))

# include the canonical DAG
import yaml
dag = yaml.safe_load(open(f"{ROOT}/data/graph/canonical-dag.yaml"))
objects.append(json.dumps({"type":"dag","deps":{k: sorted(v.get("requires",[])) for k,v in dag["dependencies"].items()}}, sort_keys=True))

# ---- Merkle root: hash each leaf, then hash the sorted concatenation ----
def merkle_root(leaf_hashes):
    level = sorted(leaf_hashes)
    while len(level) > 1:
        level = sorted(sha(level[i] + level[i+1]) for i in range(0, len(level)-1, 2))
        if len(level) % 2 == 1 and len(level) > 1:
            level = level + [level[-1]]
    return level[0]

leaf_hashes = [sha(o) for o in objects]
root = merkle_root(leaf_hashes)

print("=== SIGNED CORPUS ROOT (Merkle + content-addressing) ===\n")
n_claims = sum(1 for o in objects if '"type": "claim"' in o)
n_inf = sum(1 for o in objects if '"type": "inference"' in o)
n_conf = sum(1 for o in objects if '"type": "conflict"' in o)
print(f"canonical objects hashed: {len(objects)}")
print(f"  claims: {n_claims}")
print(f"  inferences: {n_inf}")
print(f"  conflicts: {n_conf}")
print(f"  dag: 1")
print(f"\nMERKLE ROOT: {root}")

# mutation detection: any single change -> different root
objects2 = list(objects)
objects2[0] = objects2[0].replace('"ceiling": "SCHOLARLY_CORROBORATED"', '"ceiling": "MACHINE_PROPOSED"')
root2 = merkle_root([sha(o) for o in objects2])
print(f"\nroot after 1-claim mutation: {root2}")
print(f"root CHANGED on mutation: {root != root2}")

# save the signed release manifest
manifest = {
    "root": root, "object_count": len(objects),
    "generated": "2026-08-14",
    "algorithm": "sha256-merkle",
    "leaves": len(leaf_hashes),
}
os.makedirs(f"{ROOT}/data/graph", exist_ok=True)
json.dump(manifest, open(f"{ROOT}/data/graph/corpus-root.json", "w"), indent=1)
print(f"\nwrote data/graph/corpus-root.json")

print("\n=== INSIGHT ===")
print("A single hash fingerprints the ENTIRE accepted epistemic state. Any retraction, any sneaky")
print("ceiling-flip, any new claim changes the root. This is the signed corpus root (SPEC-19 #6/7)")
print("— the content-addressed, immutable, verifiable release. In production this root would be")
print("signed with Sigstore/Rekor (cosign) for a tamper-evident ScholarReviewCertificate.")
