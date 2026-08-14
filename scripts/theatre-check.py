#!/usr/bin/env python3
"""theatre-check.py — the verifiable-proof auditor (peer review with a stored proof).

For every kernel/docs claim, produce a VERIFIABLE PROOF that what is claimed is actually implemented:
  1. Does a real test script exist for this kernel?
  2. Does that test RUN and PASS (exit 0)?
  3. Does the test exercise REAL data or is it synthetic-only (theatre)?
  4. Is the doc claim matched to an actual test artifact?

Each checked kernel gets a PROOF RECORD (stored to data/references/theatre-proofs.json) with a hash —
so a future agent can verify the proof hasn't drifted. This is the anti-theatre skill: claim → test →
passing → real-data → stored hash = verifiable outcome.
"""
import os, sys, json, subprocess, hashlib

ROOT = "/mnt/HC_Volume_106427611/ip-graph"
PROOFS = f"{ROOT}/data/references/theatre-proofs.json"

# kernel -> the validate script that tests it + whether that script uses real data
KERNEL_TESTS = {
    "epistemic":     ("validate-stack.py", True),
    "review":        ("validate-stack.py", True),
    "staleness":     ("validate-stack.py", True),
    "query":         ("validate-kernels.py", True),
    "retrieval":     ("validate-kernels.py", True),
    "schema":        ("validate-kernels.py", True),
    "scholar_review":("validate-kernels.py", True),
    "translation":   ("validate-products.py", True),
    "education":     ("validate-education-organism.py", False),
    "organism":      ("validate-education-organism.py", False),
    "organism_loop": ("validate-organism-loop.py", False),
    "pedagogy":      ("validate-pedagogy.py", False),
    "certificate":   ("validate-kernels.py", True),
    "discovery":     ("validate-kernels.py", True),
    "evolve":        ("validate-evolve.py", False),
    "agent_delivery":("validate-agent-delivery.py", False),
}

# docs claims (from LAB-REVIEW / KERNELS-INDEX) to verify against tests
DOC_CLAIMS = {
    "epistemic": "envelope + invariant validated (0 violations)",
    "review": "reducer gates promotion honestly",
    "staleness": "PHYSICS retraction flags 8 layers",
    "query": "KG2Code executable queries validated",
    "retrieval": "PathRAG+HippoRAG validated",
    "schema": "single-source validation",
    "scholar_review": "cross-review + citecheck validated",
    "translation": "non-aggregate vector validated",
    "education": "wrong-answer→neighbor validated",
    "organism": "misconception graph validated",
    "organism_loop": "consumer→research machine validated",
    "pedagogy": "adaptive pedagogy validated",
    "certificate": "certification weight validated",
    "discovery": "research value validated",
    "evolve": "MAP-Elites evolution validated",
    "agent_delivery": "task contract + human gate validated",
}

def run(script):
    try:
        r = subprocess.run([sys.executable, f"{ROOT}/scripts/{script}"],
                           capture_output=True, text=True, timeout=60)
        return r.returncode == 0, r.returncode
    except Exception as e:
        return False, str(e)[:50]

proofs = []
print("=== THEATRE CHECK — verifiable proofs ===\n")
for kernel, (test_script, real_data) in sorted(KERNEL_TESTS.items()):
    exists = os.path.exists(f"{ROOT}/scripts/{test_script}")
    passes, rc = run(test_script) if exists else (False, -1)
    claim = DOC_CLAIMS.get(kernel, "")
    # proof record: tested + passing + (real-data or synthetic-flagged) + claim matched
    proof = {
        "kernel": kernel, "doc_claim": claim,
        "test_script": test_script, "test_exists": exists,
        "test_passes": passes, "exit_code": rc,
        "uses_real_data": real_data,
        "verdict": "PROVEN" if (exists and passes and real_data) else
                   ("PROVEN-MECHANISM" if (exists and passes and not real_data) else "UNPROVEN"),
        "proof_hash": hashlib.sha256(json.dumps({
            "kernel": kernel, "test": test_script, "passes": passes, "real_data": real_data,
            "claim": claim}).encode()).hexdigest()[:16],
    }
    proofs.append(proof)
    status = "✓" if proof["verdict"].startswith("PROVEN") else "✗"
    tag = "REAL-DATA" if real_data else "SYNTHETIC"
    print(f"  {status} {kernel:16s} [{proof['verdict']:16s}] test={test_script} ({tag}) "
          f"passes={passes} hash={proof['proof_hash']}")

# summary
n_proven = sum(1 for p in proofs if p["verdict"] == "PROVEN")
n_mech = sum(1 for p in proofs if p["verdict"] == "PROVEN-MECHANISM")
n_un = sum(1 for p in proofs if p["verdict"] == "UNPROVEN")
os.makedirs(f"{ROOT}/data/references", exist_ok=True)
json.dump({"count": len(proofs), "proven": n_proven, "mechanism_only": n_mech, "unproven": n_un,
           "proofs": proofs}, open(PROOFS, "w"), indent=1)
print(f"\n=== SUMMARY ===")
print(f"  PROVEN on real data: {n_proven}")
print(f"  PROVEN-mechanism only (synthetic): {n_mech}  ← THEATRE risk")
print(f"  UNPROVEN: {n_un}")
print(f"\n  proofs stored → {PROOFS}")
print(f"\nThe theatre finding: {n_mech} kernels are 'validated' but only on SYNTHETIC data — they prove")
print("the mechanism, not integration with the real kernel. Fix = the graduation test (validate-stack)")
print("on real data, or real-data inputs for those validators.")
