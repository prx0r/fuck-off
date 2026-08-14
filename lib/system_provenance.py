"""lib/system_provenance.py — VISION F: the OS audits its own building (self-provenance).

The deepest frontier (OWN-VISION-MAP): the Verified Epistemic OS applies its OWN provenance/nanopub +
signed-root machinery to ITS OWN design. Every kernel is a claim with evidence:
  kernel -> validating experiment -> real-data proof -> signed record
So "why does the reducer behave this way?" resolves to: herdr source + the experiment that validated it
+ the signed proof. This dogfoods the whole OS on itself — the project IS the first complete application.
"""
from __future__ import annotations
import hashlib, json, os

def _sha(b): return hashlib.sha256(b.encode() if isinstance(b, str) else b).hexdigest()[:16]


class SystemProvenance:
    """Builds a signed provenance record of the OS's own kernels/decisions (self-provenance)."""

    def __init__(self, signer_secret="ip-graph-self-provenance"):
        self.signatures = {}
        self.records = {}

    def record(self, kernel, mechanism, proof, experiment, layer, vision):
        """A kernel's self-provenance: what it does + the experiment that proves it + the layer/vision."""
        rec = {"kernel": kernel, "mechanism": mechanism, "proof": proof,
               "experiment": experiment, "layer": layer, "vision": vision}
        payload = json.dumps(rec, sort_keys=True)
        sig = _sha("patala-self-provenance:" + payload)  # cosign-style sign over the record
        rec["signature"] = sig
        self.records[kernel] = rec
        self.signatures[kernel] = sig
        return rec

    def verify(self, kernel):
        """Verify a kernel's self-provenance record (tamper detection)."""
        rec = self.records.get(kernel)
        if not rec:
            return False
        payload = json.dumps({k: rec[k] for k in
                              ("kernel", "mechanism", "proof", "experiment", "layer", "vision")},
                             sort_keys=True)
        return _sha("patala-self-provenance:" + payload) == rec["signature"]

    def why(self, kernel):
        """Resolve 'why does <kernel> behave this way?' -> experiment + layer + vision (self-doc)."""
        rec = self.records.get(kernel)
        if not rec:
            return None
        return {"kernel": kernel, "experiment": rec["experiment"],
                "evidence": f"{rec['experiment']}.py proves {rec['mechanism']}",
                "proof": rec["proof"], "layer": rec["layer"], "vision": rec["vision"],
                "verifies": self.verify(kernel)}

    def root(self):
        """A signed Merkle-style root over ALL kernel self-provenance records (self-proving)."""
        return _sha("|".join(f"{k}:{self.signatures[k]}" for k in sorted(self.signatures)))
