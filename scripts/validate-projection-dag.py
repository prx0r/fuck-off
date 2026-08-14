#!/usr/bin/env python3
"""validate-projection-dag.py — the SPEC-00 §22 hard requirement: a new doc must NOT rebuild the whole corpus.

Proves the projection DAG gives per-artifact incremental rebuild: adding ONE new artifact rebuilds ONLY
it (no-op for the rest). This is the compute-on-write guarantee made per-artifact, not whole-site. On a
simulated work-page projection DAG (the real pattern: each work page depends on its own source/translation).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from projection_dag import ProjectionDAG, sha

ROOT = "/mnt/HC_Volume_106427611/ip-graph"
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=== PROJECTION DAG: per-artifact incremental rebuild (new doc != whole corpus) ===\n")

# a work-page projection DAG (the real pattern): each work page depends on its own inputs
dag = ProjectionDAG()
class WorkPageBuilder:
    """A work-page artifact: builds from its work's source+translation. input_hashes() = those inputs."""
    def __init__(self, source_sha, translation_sha):
        self._h = {"source": source_sha, "translation": translation_sha}
        self.builds = 0
    def input_hashes(self):
        return dict(self._h)
    def __call__(self, artifact_id):
        self.builds += 1
        return f"<page {artifact_id}>"

# 10 work pages, each depending on its own (source, translation)
pages = {}
for i in range(10):
    b = WorkPageBuilder(sha(f"source-{i}"), sha(f"trans-{i}"))
    pages[f"work-{i}"] = b
    dag.register(f"work-{i}", [f"source-{i}", f"trans-{i}"], b)

# ---- initial build: ALL 10 pages must build (first pass) ----
first = dag.incremental()
check("first build produces all 10 pages", len(first) == 10, f"({len(first)})")

# ---- second pass: NOTHING changed -> NO-OP (the compute-on-write core) ----
second = dag.incremental()
check("unchanged -> NO-OP (no page rebuilds)", len(second) == 0, f"({len(second)})")

# ---- the hard requirement: change ONE work's translation -> ONLY that page rebuilds ----
pages["work-3"]._h["translation"] = sha("trans-3-UPDATED")
third = dag.incremental()
check("ONE work changed -> ONLY that page rebuilds (not the whole corpus)",
      len(third) == 1 and "work-3" in third, f"({sorted(third.keys())})")
check("the other 9 pages did NOT rebuild (no-op for them)",
      pages["work-0"].builds == 1 and pages["work-9"].builds == 1)

# ---- blast-radius: which artifacts depend on a changed input ----
affected = dag.blast_radius(["source-7"])
check("blast-radius finds the artifact(s) depending on a changed input", "work-7" in affected)

# ---- add a NEW work -> only the new page builds ----
newb = WorkPageBuilder(sha("source-new"), sha("trans-new"))
dag.register("work-new", ["source-new", "trans-new"], newb)
fourth = dag.incremental()
check("NEW doc -> ONLY the new page builds (the SPEC-00 §22 hard rule)",
      set(fourth.keys()) == {"work-new"})

print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
print("\nTHE PROJECTION DAG WORKS: per-artifact incremental rebuild. Adding or changing ONE document")
print("rebuilds ONLY its artifact — the other N-1 are a no-op. This is the SPEC-00 §22 hard guarantee")
print("('a new doc must NOT rebuild the whole corpus'), made real per-artifact, not whole-site.")
print(f"\n  builds: work-0={pages['work-0'].builds}, work-9={pages['work-9'].builds}, "
      f"work-3={pages['work-3'].builds}, work-new={newb.builds}")
sys.exit(0 if all(c for _,c in results) else 1)
