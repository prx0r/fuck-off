#!/usr/bin/env python3
"""experiment-signed-statement.py — signing certified statements (Self-Proving + Marketplace visions).

cosign (cloned) does artifact signing + transparency (Sigstore/Rekor). We apply the sign→verify flow to
our certified statements: a claim's Merkle root + certification weight gets signed, and any tampering is
detected on verify. This is the trust mechanism the Verified-Statement-Marketplace + Self-Proving-System
visions need.
"""
import json, hashlib, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from certificate import Certification

def sha(b): return hashlib.sha256(b.encode() if isinstance(b, str) else b).hexdigest()

# ---- a simple keypair (emulates cosign's signing; production would use Sigstore keyless) ----
# using Python's hmac-free approach: sign = hash(private_key + payload), verify = recompute
class SimpleSigner:
    def __init__(self, secret):
        self.secret = secret.encode()
    def sign(self, payload):
        return sha(self.secret + payload.encode())
    def verify(self, payload, signature):
        return sha(self.secret + payload.encode()) == signature

signer = SimpleSigner("patala-signing-secret")   # in prod: Sigstore ephemeral key + Rekor transparency

# ---- a certified statement ----
cert = Certification("I1", verifier_kill_rate=1.0, consensus_multiplicity=3,
                     downstream_load=5, time_signed_years=1.0)
statement = {
    "claim": "Quantum events are genuinely indeterministic",
    "certification_weight": cert.weight(),
    "merkle_root": sha("I1:indeterminism"),   # content-address of the claim
    "timestamp": "2026-08-14",
}
payload = json.dumps(statement, sort_keys=True)
sig = signer.sign(payload)

print("=== SIGNED CERTIFIED STATEMENT (Self-Proving + Marketplace) ===\n")
print(f"statement payload:")
for k, v in statement.items():
    print(f"  {k}: {v}")
print(f"certification weight: {cert.weight():.2f}  (from lib/certificate.py)")

print(f"\nsignature: {sig[:20]}...")

# ---- verify (tamper detection) ----
print("\n-- verification --")
ok = signer.verify(payload, sig)
print(f"  verify(untampered): {ok}  {'PASS' if ok else 'FAIL'}")

# tamper: change the claim or the weight
tampered = dict(statement); tampered["certification_weight"] = 999.0
tampered_payload = json.dumps(tampered, sort_keys=True)
ok2 = signer.verify(tampered_payload, sig)
print(f"  verify(tampered weight): {ok2}  {'PASS (caught)' if not ok2 else 'FAIL'}")

print("\n=== INSIGHT ===")
print("A certified statement carries: content-address (Merkle root) + certification weight + a")
print("signature. Any tampering (weight, claim, timestamp) breaks verification. Combined with cosign's")
print("Sigstore/Rekor transparency log in production, this is the trust substrate the marketplace")
print("sells — a signed, verified, tamper-evident statement with a measured certification weight.")
print("The Self-Proving System vision extends this to design decisions (every decision signed).")
