"""lib/organism_factory_bridge.py — the organism→factory loop (my next_action + patala's FSM).

The integration seam (from READ-PLANE-ORGANISM + the devplans): 
  - MY next_action decides WHICH work to work on (the priority formula: load-bearing + uncertain + demand).
  - PATALA's corpus_state.next_valid_action decides the LEGAL transition for that work (its state machine).
The bridge connects them: next_action ranks works by priority, then asks patala's FSM what the top work
can legally do next. The result feeds the factory workers (which produce + commit).

This is "decide WHAT by formula (mine) + decide the legal move (theirs)" — one autonomous loop.
"""
from __future__ import annotations
import os, sys


class OrganismFactoryBridge:
    """Connects my deterministic scheduler to patala's per-work state machine."""

    def __init__(self, next_action_scheduler=None, patala_import_hint=None):
        from next_action import NextActionScheduler
        self.scheduler = next_action_scheduler or NextActionScheduler()
        # patala's corpus_state (imported in a SEPARATE process — the schema.py boundary)
        self._patala = None
        self._import_hint = patala_import_hint or "/root/projects/patala/pipeline"

    def _load_patala(self):
        """Lazy-import patala's corpus_state (separate process boundary)."""
        if self._patala is None:
            sys.path.insert(0, self._import_hint)
            import corpus_state
            self._patala = corpus_state
        return self._patala

    # ---- MY scheduler: rank works by the priority formula ----
    def add_work(self, work_id, downstream=1, uncertainty=0.5, question_demand=0, cost=1.0):
        from next_action import Task
        self.scheduler.add(Task(work_id, "work", downstream=downstream, uncertainty=uncertainty,
                                question_demand=question_demand, cost=cost))
        return work_id

    def rank_works(self):
        return self.scheduler.rank()

    # ---- THEIR FSM: the legal next action for a work ----
    def next_action_for(self, work_state):
        """pat ala's next_valid_action — the legal transition for this work's state."""
        cs = self._load_patala()
        return cs.next_valid_action(work_state)

    # ---- THE LOOP: top-priority work -> its legal next action ----
    def plan_next(self):
        """The organism's plan: the highest-priority work + its legal next action."""
        ranked = self.rank_works()
        if not ranked:
            return None
        top_id = ranked[0][1].id
        # discover the real work state (via patala) and get its legal action
        try:
            cs = self._load_patala()
            works = {w.work_id: w for w in cs.discover_works()}
            ws = works.get(top_id)
            action = cs.next_valid_action(ws) if ws else {"action": "UNKNOWN_WORK", "reason": top_id}
        except Exception as e:
            action = {"action": "FSM_ERROR", "reason": str(e)[:60]}
        return {"work": top_id, "priority": round(ranked[0][0], 3),
                "legal_next": action.get("action"), "eligible": action.get("eligible_for_agent3"),
                "reason": action.get("reason")}

    def _rank(self, priority):
        return round(priority, 3)
