# THE REVERSE-DELIVERY THESIS — building backward from a vision to current reality

*2026-08-14. A standalone process/methodology. The idea: take a vision, fully detail the technical
dependency graph + checkpoints needed for a working implementation, then **work backward** from that
vision to current implementations. This is the inverse of most projects (which build forward from what
they have). It turns a vision into an executable, checkable delivery plan.*

---

## 1. WHAT THIS IS (and the names it has in the literature)

This is not a new idea — it's a **composition of several established AI/SE concepts**, and naming them
is what gives the mechanism credibility:

| Concept | Field | What it is |
|---------|-------|-----------|
| **Backward chaining / backward search** | classic AI planning (STRIPS, planners) | start from the GOAL, repeatedly reduce it to sub-goals whose preconditions you already satisfy |
| **Goal-regression** | AI planning (Fikes & Nilsson 1971, STRIPS) | the formal mechanism: regress the goal through operators to find a state reachable from the start |
| **Reverse planning / reverse engineering a plan** | planning + software re-engineering | derive the plan from the target rather than from the current state |
| **Means-ends analysis** | Newell & Simon (GPS, 1963) | notice a gap between current and goal state, find an operator to reduce it, recurse |
| **Impact analysis / backward dependency walk** | software engineering | trace a change's consequences back through a dependency graph |
| **Reverse-engineering the spec** | software architecture | derive the required components from the desired behavior |

**The precise term for "start at the goal and walk backward through dependencies until you hit what
you already have" is GOAL-REGRESSION / BACKWARD CHAINING.** When the "goal" is a product vision and the
"dependencies" are technical checkpoints, it's a **reverse-delivery / backward-delivery plan**.

## 2. WHY IT'S POWERFUL (and why most projects don't do it)

Most projects build **forward**: they inventory what they have, then ask "what can we make?" This is
*capability-driven* — it under-delivers the vision (you build what's easy, not what matters).

**Reverse delivery** builds **backward from the vision**:
```
                    VISION (the goal)
                        │  "what must EXIST for this vision to be true?"
                        ▼
                 TECHNICAL DEPENDENCIES
                        │  (each is a checkpoint)
                        ▼
                 SUB-DEPENDENCIES
                        │
                        ▼
                 ... backward ...
                        │
                        ▼
                 CURRENT IMPLEMENTATIONS  (the root, what we already have)
```

The plan is the **path from current-reality to the vision**, discovered by walking the dependency graph
in reverse. Every checkpoint is **testable** — you know it's done when its precondition is met. This is
the difference between a *roadmap* (forward, vague) and a *delivery plan* (backward, checkable).

## 3. THE FORMAL MECHANISM (the goal-regression loop)

```
Given:  a VISION (goal state G)
        a set of CHECKPOINTS (operators, each = "to achieve X you need {prereqs}")
        CURRENT STATE (what's built, the axioms / root)

1.  Start: frontier = {G}
2.  While frontier non-empty:
      pick a goal g from frontier
      for each checkpoint c whose effect is g:
        if all prereqs of c are satisfied in CURRENT STATE:
            mark c DONE, g DELIVERED
        else:
            add c's unmet prereqs to frontier   ← the sub-goals (backward step)
3.  The plan = the ordered set of checkpoints, dependencies-first.
4.  A checkpoint is TESTABLE: it flips DONE when its prereqs exist AND it passes its gate.
```

This is literally **backward chaining over a checkpoint DAG**. The vision is the root; current
implementations are the leaves; the plan is the reverse topological walk.

## 4. THE CONNECTION TO WHAT WE'VE BUILT

This is the **VISION-CHUNK-LAYER-MAP** made fully mechanical. What we have:

```
VISION-CHUNK-LAYER-MAP.md   = the vision → 10 chunks → 10 layers (forward)
VISION-CHUNKS.json          = machine-resolvable form
STATE.yaml                  = per-layer status (current reality)
FRONTIER-MAP.md             = layer → build → validation (the checkpoints)
EXPERIMENT-MATRIX           = which experiments validate which layer
```

**What's missing is the BACKWARD walk.** Today we say "layer 00 → 01 → ... → 12" (forward). Reverse
delivery would ask: "for the Verified-Statement-Marketplace vision, what must EXIST? A certification
weight (have it, lib/certificate.py). What must certify it? A verifier ledger. What must feed that? ..."
— walking BACKWARD from the marketplace to what we already built.

## 5. THE STANDALONE PROCESS (the thesis in executable form)

### Step 1 — State the vision as a testable goal
> "The Verified-Statement-Marketplace works when any agent can get a signed, verified statement with a
> measured certification weight." → that's the goal G.

### Step 2 — Decompose the vision into checkpoints (each = "to achieve X you need {Y, Z}")
Each checkpoint is an **operator** with:
- **effect**: what it delivers
- **prerequisites**: what must already exist
- **gate**: how you know it's done (a test)

### Step 3 — Walk backward from the vision
Starting at G, repeatedly regress through checkpoints until you hit prerequisites that are **already
satisfied** by current implementations. Those roots are your start.

### Step 4 — The plan is the reverse-topological order
Dependencies first. Each checkpoint flips DONE when its gate passes. This gives you:
- **what to build** (the un-satisfied checkpoints between roots and vision)
- **in what order** (reverse topo)
- **how to know it's done** (the gate)

### Step 5 — Re-run on every vision
The mechanism is vision-agnostic. Feed it ANY vision doc; it produces the backward delivery plan.

## 6. THE CODE (the mechanism is machine-checkable)

`scripts/reverse-deliver.py` (to build): given a VISION's checkpoint DAG + a set of "already-done"
prerequisites, output the backward plan. This is the executable form of the thesis.

```python
def reverse_plan(goal, checkpoints, done):
    """Backward chaining over the checkpoint DAG."""
    plan = []
    frontier = {goal}
    while frontier:
        g = frontier.pop()
        for cp in checkpoints:
            if cp["effect"] == g:
                unmet = [p for p in cp["prereqs"] if p not in done]
                if not unmet:
                    done.add(g); plan.append(cp["id"])   # g is deliverable now
                else:
                    frontier.update(unmet)               # backward step: need sub-goals
    return plan  # reverse-topological (dependencies already ordered)
```

## 7. WHY THIS IS A SICK CONCEPT (the honest case)

1. **It kills vision-drift.** A vision stays connected to reality: every dream must resolve backward to
   something buildable or it's flagged as ungrounded.
2. **It makes visions checkable.** Not "we'll build the marketplace" but "the marketplace needs
   certificate.py (DONE), verifier-ledger (TODO), certification-surface (TODO)".
3. **It reuses what's built.** Walking backward, you discover how much of the vision you ALREADY have —
   which is the joyful part (like finding the marketplace is 60% built).
4. **It composes with our flywheels.** Each vision's backward plan shows what to build; the flywheel
   shows why it compounds once built. Forward for value, backward for delivery.

## 8. REFERENCES (the names to cite)

- **Fikes, R. & Nilsson, N. (1971).** "STRIPS: A New Approach to the Application of Theorem Proving to
  Problem Solving." — goal-regression, backward chaining from a goal state.
- **Newell, A. & Simon, H. (1963).** "GPS: A Program that Simulates Human Thought." — means-ends
  analysis, reducing the gap between current and goal state.
- **STRIPS/PDDL planning literature** — backward search, the foundation of automated planning.
- **Software impact analysis** — backward dependency walk (our blast-radius / staleness in reverse).
- This project: `VISION-CHUNK-LAYER-MAP.md` (forward) + `scripts/reverse-deliver.py` (the backward
  mechanism) + `STATE.yaml` (current reality) + `FRONTIER-MAP.md` (checkpoints).

---

## THE ONE-LINE CARRY-FORWARD

> **A vision is a goal state. Backward-chain through checkpoints (each = "to make X you need Y,Z")
> until you reach what's already built — the plan is the reverse-topological path, every checkpoint
> testable. That's how you deliver a vision instead of drifting toward it.**
