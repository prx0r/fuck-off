"""lib/projection_dag.py — the projection DAG (SPEC-00 §4/§22): per-artifact incremental rebuild.

The hard requirement (SPEC-00 §23/§49 §6): **a new document must NOT rebuild the whole corpus.**

This kernel implements the projection DAG — ONE graph that is simultaneously:
  - the correctness graph (which projections derive from which inputs)
  - the staleness propagator (an input change flags its dependents)
  - the incremental-rebuild scheduler (only changed artifacts recompile)

Each artifact (a work page, a bundle, a search-index entry) depends on specific inputs (a source, a
translation, a proof). When an input changes, ONLY its dependent artifacts recompile — the rest are
untouched (no-op). This is the compute-on-write guarantee made per-artifact, not whole-site.

The RKA/salsa pattern: hash each (input, artifact) edge; an artifact rebuilds iff its input hash changed.
"""
from __future__ import annotations
import hashlib


def sha(x): return hashlib.sha256(x.encode() if isinstance(x, str) else x).hexdigest()[:16]


class ProjectionDAG:
    """Per-artifact incremental rebuild: input → artifacts, unchanged = no-op."""

    def __init__(self):
        self.deps = {}        # artifact_id -> [input_keys]  (which inputs feed it)
        self.artifact_builders = {}   # artifact_id -> callable(artifact_id) -> bytes/str
        self.hashes = {}      # artifact_id -> {input_key: hash}  (last-seen)

    def register(self, artifact_id, input_keys, builder):
        """Register an artifact: it depends on input_keys, and builder(artifact_id) builds it."""
        self.deps[artifact_id] = list(input_keys)
        self.artifact_builders[artifact_id] = builder
        return artifact_id

    def _input_hashes(self, artifact_id):
        """Current hashes of the artifact's inputs (from the actual input sources)."""
        # the builder is expected to expose how to hash its inputs; here we call a helper
        b = self.artifact_builders[artifact_id]
        get_hashes = getattr(b, "input_hashes", None)
        if get_hashes:
            return get_hashes()
        return {k: sha(f"{k}") for k in self.deps[artifact_id]}  # fallback (default: stable)

    def changed_artifacts(self, input_changes=None):
        """Which artifacts must rebuild (their input hash changed). """
        changed = []
        for artifact_id in self.deps:
            cur = self._input_hashes(artifact_id)
            prev = self.hashes.get(artifact_id, {})
            if cur != prev or artifact_id not in self.hashes:
                changed.append(artifact_id)
        return changed

    def rebuild(self, artifact_id):
        """Rebuild ONE artifact; return its bytes + the new hash state."""
        b = self.artifact_builders[artifact_id]
        result = b(artifact_id)
        # record the current input hashes as the new baseline
        self.hashes[artifact_id] = self._input_hashes(artifact_id)
        return result

    def incremental(self):
        """Rebuild ONLY the changed artifacts. Returns {artifact_id: result} for the rebuilt ones.
        This is the SPEC-00 §22 guarantee: unchanged artifacts are a NO-OP."""
        rebuilt = {}
        for artifact_id in self.changed_artifacts():
            rebuilt[artifact_id] = self.rebuild(artifact_id)
        return rebuilt

    # ---- the inverse: given a set of changed inputs, which artifacts are affected? ----
    def blast_radius(self, changed_inputs):
        """The artifacts that depend on a changed input (staleness propagation)."""
        affected = set()
        for artifact_id, inputs in self.deps.items():
            if set(inputs) & set(changed_inputs):
                affected.add(artifact_id)
        return sorted(affected)
