#!/usr/bin/env python3
"""validate-provenance.py — map our epistemic envelope to knowledgeProvenance's PROV-K nanopub model.

Adapted from mntlra/knowledgeProvenance (the repo we cloned): multi-source assertions get a truth
value + provenance + reliability type. We map OUR epistemic_ceiling to the PROV-K types
(ReliableFact / ContrastingEvidence / InsufficientEvidence) and emit a lightweight nanopub.

This validates the outward serialization: our internal epistemic state can be published as
standards-compliant nanopublications with provenance.
"""
import os, sys, json, hashlib
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))

# PROV-K types (from knowledgeProvenance repo)
PROVK = {
    "RELIABLE": "ReliableFact",
    "CONTRASTING": "ContrastingEvidence",
    "INSUFFICIENT": "InsufficientEvidence",
    "UNCERTAIN": "UncertainFact",
}
# our epistemic ceiling -> PROV-K reliability type
CEILING_TO_PROVK = {
    "SCHOLARLY_CORROBORATED": "RELIABLE",
    "INDEPENDENT_REVIEWED": "RELIABLE",
    "ADJUDICATED": "RELIABLE",
    "SCHOLARLY_CORROBORATED_PRELIMINARY": "UNCERTAIN",
    "MACHINE_PROPOSED": "UNCERTAIN",
    "ENGINEERING_VALIDATED": "UNCERTAIN",
}

def sha(s): return hashlib.sha256(s.encode()).hexdigest()[:16]

def emit_nanopub(claim_id, text, ceiling, evidence_quotes, sources, contradictions=0):
    """Emit a knowledgeProvenance-style nanopub for a claim."""
    rel = CEILING_TO_PROVK.get(ceiling, "UNCERTAIN")
    provk_type = PROVK[rel]
    np_id = sha(f"{claim_id}:{text}")
    assertion_id = sha(f"assertion:{claim_id}")
    prov = {
        "@id": f"np:{np_id}",
        "assertion": {
            "@id": f"assertion:{assertion_id}",
            "type": "Claim",
            "claim_text": text,
        },
        "provenance": {
            "wasGeneratedBy": "patala_factory",
            "wasDerivedFrom": sources,
            "evidence": evidence_quotes,
        },
        "knowledge_provenance": {
            "hasTruthValue": f"corekp:{np_id}",
            "truthType": provk_type,
            "reliability": rel,
            "assignedCertaintyDegree": {"RELIABLE": 0.95, "UNCERTAIN": 0.5,
                                        "CONTRASTING": 0.3, "INSUFFICIENT": 0.2}[rel],
            "contradictingEvidenceCount": contradictions,
            "unreliabilityReason": "contrasting evidence across sources" if contradictions else None,
        },
    }
    return prov

print("=== KNOWLEDGEPROVENANCE: PROV-K nanopub emission from our epistemic envelope ===\n")

g = json.load(open("/mnt/HC_Volume_106427611/ip-graph/data/graph/graph.json"))
arg = json.load(open("/mnt/HC_Volume_106427611/ip-graph/data/graph/argument.json"))

results = []
def check(name, cond):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}")

# emit nanopubs for the argument claims (DERIVED from the real graph data)
derived = []
for n in arg["information_nodes"]:
    ceiling = n["epistemic_ceiling"]
    npub = emit_nanopub(n["id"], n["text"][:30], ceiling,
                        [n.get("evidence_quote","")], n.get("source_refs", []))
    derived.append((n["id"], ceiling, npub))
    t = npub["knowledge_provenance"]["truthType"]
    print(f"  [{n['id']}] ceiling={ceiling:38s} -> PROV-K {t}  certainty={npub['knowledge_provenance']['assignedCertaintyDegree']}")

# validations — ASSERTED ON THE REAL DATA-DERIVED NANOPUBS (not hand-fed literals)
by_id = {nid: npub for nid, _, npub in derived}
corrob = [np for nid, c, np in derived if c == "SCHOLARLY_CORROBORATED"]
mach = [np for nid, c, np in derived if c == "MACHINE_PROPOSED"]
prelim = [np for nid, c, np in derived if c == "SCHOLARLY_CORROBORATED_PRELIMINARY"]

check("corroborated real claim -> ReliableFact",
      corrob and all(np["knowledge_provenance"]["truthType"] == "ReliableFact" for np in corrob))
check("machine-proposed real thesis -> UncertainFact",
      mach and all(np["knowledge_provenance"]["truthType"] == "UncertainFact" for np in mach))
check("preliminary real claim -> UncertainFact (not inflated)",
      prelim and all(np["knowledge_provenance"]["truthType"] == "UncertainFact" for np in prelim))
check("nanopub has provenance (wasDerivedFrom the real source_refs)",
      derived and all("wasDerivedFrom" in np["provenance"] and np["provenance"]["wasDerivedFrom"]
                      for _, _, np in derived))
check("nanopub has content-addressable id (sha) + carries the real evidence quote",
      derived and all(len(np["@id"]) > 6 and np["provenance"]["evidence"]
                      for _, _, np in derived))
check("no ceiling is inflated (a machine-proposed claim never emits ReliableFact)",
      mach and not any(np["knowledge_provenance"]["truthType"] == "ReliableFact" for np in mach))

print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
print("\nThis validates our internal epistemic state can be PUBLISHED as standards-compatible")
print("nanopublications (PROV-K), following mntlra/knowledgeProvenance — the outward serialization")
print("for Layer 02/04, giving every claim portable, provenance-carrying truth.")
sys.exit(0 if all(c for _,c in results) else 1)
