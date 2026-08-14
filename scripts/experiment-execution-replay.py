#!/usr/bin/env python3
"""experiment-execution-replay.py — execution branching + deterministic replay (gaps B+C).

From agentstateprotocol (Git for AI thoughts) + deterministic-memory-layer (DML):
  checkpoint / rollback / branch / merge  (agentstateprotocol)
  event-driven replay + causal caused-by   (DML)

We add these to our agent-delivery layer: an agent run can checkpoint state, branch to an alternative
strategy on failure, rollback to a known-good state, and the whole run is deterministically replayable
from its event log (with caused-by links = the causal operational graph).
"""
import os, sys, json, hashlib
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))

# ---- DML-style event store with caused-by (causal operational graph) ----
class EventStore:
    def __init__(self):
        self.events = []            # append-only log
        self.state = {}             # derived state
    def append(self, etype, data, caused_by=None):
        ev = {"id": f"ev{len(self.events)}", "type": etype, "data": data,
              "caused_by": caused_by, "hash": hashlib.sha256(json.dumps(data).encode()).hexdigest()[:10]}
        self.events.append(ev)
        self._apply(ev)
        return ev
    def _apply(self, ev):
        if ev["type"] == "SET": self.state[ev["data"]["key"]] = ev["data"]["value"]
        elif ev["type"] == "DEL": self.state.pop(ev["data"]["key"], None)
    # DETERMINISTIC REPLAY (gap C)
    def replay(self, to_event=None, exclude=()):
        """Replay the log (optionally up to an event, excluding some) → reconstructed state."""
        st = {}
        for ev in self.events:
            if to_event and ev["id"] == to_event: break
            if ev["id"] in exclude: continue
            if ev["type"] == "SET": st[ev["data"]["key"]] = ev["data"]["value"]
            elif ev["type"] == "DEL": st.pop(ev["data"]["key"], None)
        return st
    # CAUSAL TRACE (the 5th graph)
    def causal_trace(self, event_id):
        trace = []
        cur = event_id
        by_id = {e["id"]: e for e in self.events}
        seen = set()
        while cur and cur not in seen:
            seen.add(cur); ev = by_id[cur]; trace.append(cur)
            cur = ev.get("caused_by")
        return trace[::-1]

# ---- agentstateprotocol: checkpoint/rollback/branch/merge ----
class BranchingRun:
    def __init__(self):
        self.store = EventStore()
        self.checkpoints = {}       # name -> event count (snapshot point)
    def checkpoint(self, name):
        self.checkpoints[name] = len(self.store.events)
    def rollback_to(self, name):
        """Rollback = reset event log to the checkpoint, replay nothing beyond it (branch point)."""
        cut = self.checkpoints[name]
        self.store.events = self.store.events[:cut]
        self.store.state = self.store.replay()
    def branch(self, name, new_events):
        """Branch: save current as checkpoint, append alternative strategy events (caused-by the checkpoint)."""
        self.checkpoint(name)
        parent = self.store.events[-1]["id"] if self.store.events else None
        for etype, data in new_events:
            self.store.append(etype, data, caused_by=parent)

print("=== EXECUTION BRANCHING + DETERMINISTIC REPLAY (gaps B+C) ===\n")

# ---- main run: agent translates, checkpoints along the way ----
run = BranchingRun()
run.store.append("SET", {"key": "translation_candidate", "value": "v1-prose"})
run.checkpoint("after-candidate")
run.store.append("SET", {"key": "morphology_check", "value": "PASS"}, caused_by="ev0")
run.store.append("SET", {"key": "semantic_check", "value": "WARN-negation"}, caused_by="ev1")
print("[main run] events:", [e["id"] for e in run.store.events])
print("           state:", run.store.state)

# ---- branch: try an alternative strategy instead of the WARN path ----
print("\n[branch] agent branches to alternative translation strategy")
run.branch("branch-at-semantic", [
    ("SET", {"key": "translation_candidate", "value": "v2-conservative"}),
    ("SET", {"key": "semantic_check", "value": "PASS"}, ),
])
print("  branched events:", [e["id"] for e in run.store.events])
print("  branched state:", run.store.state)

# ---- deterministic replay: reconstruct state at any point ----
print("\n[replay] deterministic state reconstruction")
replayed = run.store.replay()
print("  full replay state:", replayed)
minus = run.store.replay(exclude=("ev1",))   # replay without the WARN event
print("  replay(excluding semantic):", minus)

# ---- rollback: back to the known-good candidate checkpoint ----
print("\n[rollback] recover to known-good 'after-candidate'")
run.rollback_to("after-candidate")
print("  state after rollback:", run.store.state)

# ---- causal trace (the 5th graph) ----
print("\n[causal trace] why did the branch happen?")
if run.store.events:
    last = run.store.events[-1]["id"]
    print(f"  trace from {last}:", run.store.causal_trace(last))

print("\n=== INSIGHT ===")
print("agentstateprotocol gives Git-style checkpoint/rollback/branch/merge for agent runs; DML gives")
print("deterministic event replay + causal caused-by. Together: an agent can fail mid-run, branch to an")
print("alternative strategy, rollback to a known-good state, and the whole history is deterministically")
print("replayable + causally attributable. This closes patalamix review gaps B + C and completes the")
print("causal operational graph (the 5th graph) with real execution semantics.")
