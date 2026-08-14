"""lib/factory_pool.py — the parallel factory worker pool (BUILD-PARALLEL-FACTORY, toward full Tantrāloka).

The gap (from the shared peer-review + BUILD-PARALLEL-FACTORY): the factory is autonomous + DAG-respecting
but SINGLE-THREADED. This is the parallel pool: many layer-workers (T1/L0/L2/L200/C1...) run concurrently,
each respecting the DAG (only processes jobs whose upstream is committed), each driven by next_action
(which work+layer next, by formula), each committing independently.

The DAG chain (LAYERS): SOURCE → T1 → L0 → L2 → L200 → C1 → ARGUMENT → CRUX → ESSAY → EDUCATION.
Each worker only runs a layer whose prerequisite layer is committed. next_action picks WHAT (highest
load-bearing, most-uncertain, cost-weighted). This is "Hermes for GENERATION, .py for REDUCTION" scaled
to many layers at once.
"""
from __future__ import annotations
import hashlib
from concurrent.futures import ThreadPoolExecutor
from next_action import Task, NextActionScheduler


# the DAG: layer -> its prerequisite layer (a layer runs only when upstream committed)
LAYER_DAG = {
    "SOURCE": None, "T1": "SOURCE", "L0": "T1", "L2": "L0", "L200": "L2",
    "C1": "L200", "ARGUMENT": "C1", "CRUX": "ARGUMENT", "ESSAY": "CRUX", "EDUCATION": "ESSAY",
}


class FactoryPool:
    """Parallel layer-workers over a DAG, driven by next_action."""

    def __init__(self, next_action_scheduler=None):
        from next_action import NextActionScheduler
        self.scheduler = next_action_scheduler or NextActionScheduler()
        self.committed = {}     # work_id -> {layer: status}  (the per-work ledger)
        self.events = []        # append-only log
        self.workers = {}       # layer -> the worker callable (set via register)

    # ---- the worker registry: register a layer's producer (Hermes generation or .py reduction) ----
    def register(self, layer, producer):
        """producer(work_id) -> {ok, artifact}. Hermes for GENERATION, .py for REDUCTION."""
        self.workers[layer] = producer
        return layer

    # ---- DAG eligibility: a layer can run only when its prerequisite is committed ----
    def eligible(self, work_id, layer):
        prereq = LAYER_DAG.get(layer)
        if prereq is None:
            return True   # SOURCE has no prereq
        return self.committed.get(work_id, {}).get(prereq) == "committed"

    # ---- next_action picks WHICH work+layer next (the weighted formula) ----
    def schedule(self, works, layers):
        # reset the scheduler each pass so committed work doesn't re-rank
        self.scheduler = NextActionScheduler()
        for wid in works:
            for layer in layers:
                if self.committed.get(wid, {}).get(layer) == "committed":
                    continue   # already done — skip (don't re-schedule committed work)
                if not self.eligible(wid, layer):
                    continue   # not yet eligible (DAG gate)
                # priority: load-bearing + uncertain + cheap = do next
                self.scheduler.add(Task(f"{wid}:{layer}", layer,
                                        downstream=8 if layer in ("T1", "L200") else 4,
                                        uncertainty=0.6 if layer in ("T1", "C1") else 0.4,
                                        cost=2.0 if layer in ("T1", "C1", "ESSAY") else 0.5))
        return self.scheduler.rank()

    # ---- run the pool: one parallel pass over the eligible high-priority jobs ----
    def run_pass(self, works, layers, max_workers=4):
        ranked = self.schedule(works, layers)
        # take the top N eligible jobs, run them in parallel
        jobs = [t.id for _, t in ranked[:max_workers] if ":" in t.id]
        results = {}
        def _do(job):
            wid, layer = job.rsplit(":", 1)
            if layer not in self.workers:
                return {"job": job, "ok": False, "reason": "no worker registered"}
            if not self.eligible(wid, layer):
                return {"job": job, "ok": False, "reason": "not eligible (DAG gate)"}
            r = self.workers[layer](wid)
            if r.get("ok"):
                self.committed.setdefault(wid, {})[layer] = "committed"
                self.events.append({"job": job, "event": "committed"})
            return {"job": job, **r}
        with ThreadPoolExecutor(max_workers=max_workers) as ex:
            for job in jobs:
                results[job] = ex.submit(_do, job)
        return {job: f.result() for job, f in results.items()}

    # ---- the parallel factory loop (one constant pass) ----
    def run_constantly(self, works, layers, iterations=2, max_workers=4):
        all_results = {}
        for _ in range(iterations):
            pass_results = self.run_pass(works, layers, max_workers)
            all_results.update(pass_results)
        return all_results

    def report(self):
        return {"committed": {w: {l: s for l, s in ls.items() if s == "committed"}
                              for w, ls in self.committed.items()},
                "n_committed": sum(1 for ls in self.committed.values() for s in ls.values() if s == "committed"),
                "n_events": len(self.events)}
