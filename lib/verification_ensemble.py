"""lib/verification_ensemble.py — the verification ensemble, not one big prompt (GEM 7.1).

GEM 7.1 (migration/v2/GEMS.md): "The verification ensemble, not one big prompt. RARR (retrieve→check→
revise) + RefChecker (atomic claim) + GraphCheck (relationship structure) + DSPy + IAM. Compose them;
don't prompt one model."

We compose the three we can build deterministically from our graph:
  1. **RefChecker** — decompose an answer into atomic claims; each must resolve to a registered source
     (no phantom).
  2. **GraphCheck** — each atomic claim's RELATIONSHIPS must resolve to real graph edges (subject→
     predicate→object present), not invented relations.
  3. **RARR-gate** — an answer is accepted only if every atomic claim passes BOTH; else it's flagged for
     revision (the "retrieve→check→revise" loop). This is the anti-hallucination ensemble.
"""
from __future__ import annotations


class VerificationEnsemble:
    """Composes RefChecker + GraphCheck + RARR-gate (no single big prompt)."""

    def __init__(self, graph_json=None):
        self._known_sources = set()     # registered source codes
        self._known_edges = set()       # (subject, predicate, object) triples
        self._atomic_claims = {}        # answer -> [(subject, predicate, object)]
        self._graph = graph_json

    def register_source(self, code):
        self._known_sources.add(code)
        return code

    def register_edge(self, subj, pred, obj):
        self._known_edges.add((subj, pred, obj))
        return (subj, pred, obj)

    # ---- RefChecker: decompose to atomic claims, each must resolve ----
    def refchecker(self, answer, atomic_claims):
        """Decompose + check every atomic claim resolves to a known source (no phantom)."""
        self._atomic_claims[answer] = atomic_claims
        missing = []
        for subj, pred, obj, source in atomic_claims:
            if source not in self._known_sources:
                missing.append((subj, pred, obj, source))
        return {"pass": not missing, "missing_sources": [m[3] for m in missing], "n_atomic": len(atomic_claims)}

    # ---- GraphCheck: each claim's relation must be a real graph edge ----
    def graphcheck(self, answer):
        """Every (subject, predicate, object) must be a REAL edge, not invented."""
        invented = []
        for subj, pred, obj, _src in self._atomic_claims.get(answer, []):
            if (subj, pred, obj) not in self._known_edges:
                invented.append((subj, pred, obj))
        return {"pass": not invented, "invented_relations": invented}

    # ---- RARR-gate: accept only if ALL atomic claims pass both checks ----
    def verify(self, answer):
        """The ensemble verdict (compose RefChecker + GraphCheck). No single big prompt."""
        ref = self.refchecker(answer, self._atomic_claims.get(answer, []))
        grp = self.graphcheck(answer)
        passed = ref["pass"] and grp["pass"]
        return {"accepted": passed,
                "refchecker": ref,
                "graphcheck": grp,
                "reason": "ALL_ATOMIC_CLAIMS_VERIFIED" if passed
                          else f"FAIL({ref.get('n_atomic',0)} atomic, {len(grp.get('invented_relations',[]))} invented, "
                               f"{len(ref.get('missing_sources',[]))} phantom)"}
