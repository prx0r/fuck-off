"""lib/self_healing.py — self-healing orchestration, adapted to our delivery loop (arXiv 2606.01416).

Steal (2606.01416, Self-Healing Agentic Orchestrators): when a step/tool fails, the orchestrator
DIAGNOSES and RECOVERS (retry → degrade → reroute) instead of aborting the whole run.

Our adaptation for the epistemic organism: the delivery loop (agent_delivery.py) currently aborts on
failure. This adds a typed repair cascade keyed to failure classes:
  - TRANSIENT   -> retry (with backoff) up to N times
  - STALE       -> re-plan via staleness blast-radius (the data changed under us)
  - BLOCKED     -> degrade gracefully (return partial, note the gap)
  - UNRECOVERABLE -> abort + file a review item (never silently succeed)
The recovery decisions feed next_action.py to re-plan the degraded path. Closes the agent_delivery
repair gap (the weakest kernel).
"""
from __future__ import annotations
import time


class FailureClass:
    TRANSIENT = "transient"          # retry with backoff
    STALE = "stale"                  # inputs changed; re-plan via staleness
    BLOCKED = "blocked"              # degraded gracefully; note the gap
    UNRECOVERABLE = "unrecoverable"  # abort + file review item


class HealingStep:
    """One step in the delivery loop, with its failure + recovery policy."""
    def __init__(self, step_id, action, max_retries=3):
        self.id = step_id
        self.action = action
        self.max_retries = max_retries
        self.retries = 0
        self.last_failure = None
        self.recovered = False

    def run(self, work):
        """Run the step; on failure, return the FailureClass so the orchestrator can heal."""
        try:
            result = self.action(work)
            return {"ok": True, "result": result}
        except Exception as e:
            self.retries += 1
            self.last_failure = str(e)
            return {"ok": False, "error": str(e)}


class SelfHealingOrchestrator:
    """The delivery loop with a typed repair cascade (2606.01416)."""

    def __init__(self, max_transient_retries=3, backoff_base=0.1):
        self.max_transient_retries = max_transient_retries
        self.backoff_base = backoff_base
        self.healing_log = []
        self.review_items = []       # unrecoverable failures -> review queue

    def classify(self, step, error):
        """Classify a failure into the repair policy (typed, not a catch-all)."""
        if "timeout" in error or "network" in error.lower() or "retry" in error.lower():
            return FailureClass.TRANSIENT
        if "stale" in error.lower() or "changed" in error.lower():
            return FailureClass.STALE
        if "blocked" in error.lower() or "gate" in error.lower():
            return FailureClass.BLOCKED
        return FailureClass.UNRECOVERABLE

    def heal(self, step, failure_class, work):
        """The repair cascade: retry -> degrade -> reroute -> abort(+review item)."""
        if failure_class == FailureClass.TRANSIENT:
            # loop retries until success or max (typed backoff)
            while step.retries < step.max_retries:
                time.sleep(self.backoff_base * (2 ** (step.retries - 1)))  # backoff
                r = step.run(work)   # retry
                if r["ok"]:
                    step.recovered = True
                    self.healing_log.append({"step": step.id, "heal": "retried", "ok": True})
                    return r
            return {"ok": False, "heal": "retries_exhausted", "error": step.last_failure}
        if failure_class == FailureClass.STALE:
            # re-plan: the inputs changed; the caller re-plans via next_action/staleness
            self.healing_log.append({"step": step.id, "heal": "replanned", "ok": False,
                                     "note": "staleness detected, re-plan needed"})
            return {"ok": False, "heal": "replan", "error": step.last_failure}
        if failure_class == FailureClass.BLOCKED:
            # degrade gracefully: return partial + note the gap (never silently succeed)
            self.healing_log.append({"step": step.id, "heal": "degraded", "ok": False,
                                     "note": "blocked by gate, returning partial"})
            return {"ok": False, "heal": "degraded", "partial": True, "error": step.last_failure}
        # UNRECOVERABLE: abort + file a review item (never silently succeed)
        self.review_items.append({"step": step.id, "error": step.last_failure, "status": "open"})
        self.healing_log.append({"step": step.id, "heal": "aborted+reviewed", "ok": False})
        return {"ok": False, "heal": "abort", "error": step.last_failure}

    def run_with_healing(self, step, work):
        """Run a step; classify + heal on failure; log the cascade."""
        r = step.run(work)
        if r["ok"]:
            self.healing_log.append({"step": step.id, "heal": "ok", "ok": True})
            return r
        fclass = self.classify(step, r["error"])
        return self.heal(step, fclass, work)
