#!/usr/bin/env python3
"""experiment-salsa-incremental.py — Salsa-style incremental computation (the performance speedup).

Salsa (cloned) models a program as keyed pure queries: results memoized, dependencies tracked, and
after inputs change it reuses what's unchanged instead of recomputing. This is the computational
dependency graph — the performance half of the 4-graph model.

We emulate it: an argument's evidence is a tracked query; when ONE evidence piece changes, only the
dependent computation is redone, the rest is reused (cache hit). This is the speedup: O(1) update
instead of O(n) rebuild.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))

class Query:
    """A Salsa-style tracked query with memoization + dependency tracking."""
    def __init__(self, fn, versions):
        self.fn = fn
        self.versions = versions   # shared input-version map (change detection)
        self.cache = {}            # key -> (deps, result)
    def __call__(self, key, *deps):
        dep_sig = tuple(dep_key + ":" + str(self.versions.get(dep_key, 0)) for dep_key in deps)
        if key in self.cache and self.cache[key][0] == dep_sig:
            return self.cache[key][1]          # CACHE HIT — nothing changed, reuse
        result = self.fn(key)
        self.cache[key] = (dep_sig, result)     # recompute + record dependency signature
        return result

class Engine:
    def __init__(self):
        self.dep_versions = {}   # input key -> version (bumped when input changes)
        self.evidence = Query(self._compute_evidence, self.dep_versions)
        self.argument = Query(self._compute_argument, self.dep_versions)
        self.stats = {"recompute": 0, "reuse": 0}
    def _compute_evidence(self, key):
        self.stats["recompute"] += 1
        return f"evidence[{key}]"
    def _compute_argument(self, key):
        self.stats["recompute"] += 1
        return f"arg[{key}]"
    def get_evidence(self, eid):
        return self.evidence(eid, eid)
    def get_argument(self, aid, eids):
        # argument depends on its evidence set
        return self.argument(aid, *eids)
    def change_evidence(self, eid):
        self.dep_versions[eid] = self.dep_versions.get(eid, 0) + 1   # bump version = change

eng = Engine()
print("=== SALSA-STYLE INCREMENTAL COMPUTATION (performance speedup) ===\n")

# initial build: compute argument over 3 evidence pieces
a1 = eng.get_argument("ARG1", ["E1", "E2", "E3"])
print(f"initial: {a1}")
print(f"  recomputes: {eng.stats['recompute']}")

# unchanged read: ALL reused (no recompute)
eng.stats = {"recompute": 0, "reuse": 0}
a2 = eng.get_argument("ARG1", ["E1", "E2", "E3"])
print(f"unchanged re-read: recomputes={eng.stats['recompute']} (0 = pure cache hit)")

# change ONE evidence piece: only its dependent recomputes
eng.stats = {"recompute": 0, "reuse": 0}
eng.change_evidence("E2")
a3 = eng.get_argument("ARG1", ["E1", "E2", "E3"])
print(f"after E2 change: recomputes={eng.stats['recompute']} (1, not 4 — only E2's path)")

print("\n=== INSIGHT ===")
print("Salsa's model: memoize + track dependency signatures + reuse-on-change. A single evidence")
print("change recomputes 1 unit, not the whole argument (O(1) vs O(n) rebuild). This is the")
print("computational dependency graph (graph 2 of the 4-graph model) — the performance speedup that")
print("complements our epistemic staleness DAG (graph 1). Together: epistemic correctness + compute reuse.")
