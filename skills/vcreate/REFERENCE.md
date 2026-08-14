# SKILL — VCREATE (reverse-delivery planning)

**Name:** vcreate
**Type:** agent behavior / planning skill
**Formal name in the AI literature:** goal-regression / backward chaining (Fikes & Nilsson STRIPS 1971;
Newell & Simon GPS 1963); applied to product delivery it's *reverse-delivery planning*.
**Mechanism code:** `scripts/reverse-deliver.py`
**Checkpoint DAGs:** `data/checkpoints/<vision>.json`

---

## WHAT IT IS

> **vcreate turns a vision into a deliverable plan by walking BACKWARD from the vision to current
> implementations.** Instead of asking "what can I build with what I have?" (forward/capability-driven,
> under-delivers), vcreate asks "**what must EXIST for this vision to be true?**" and regresses through
> checkpoints until it reaches what's already built.

The plan is the **reverse-topological path** from the vision (goal) down to current reality (roots).
Every checkpoint is testable — it's DONE when its prerequisites exist and its gate passes.

## THE ALGORITHM (goal-regression loop)

```
1. frontier = {vision_goal}
2. while frontier:
     pick goal g
     for each checkpoint whose effect == g:
       unmet = [p for p in prerequisites if p not in done]
       if not unmet: mark g DELIVERED, add checkpoint to plan
       else: frontier += unmet        # backward step — need these sub-goals first
3. to_build = prerequisites that are needed but no checkpoint produces + not already done
4. plan = reverse-topological (dependencies first); to_build = the real work items
```

## THE THREE OUTPUTS

1. **`reuse`** — what the vision reuses from current implementations (the joyful part; how much is done)
2. **`to_build`** — the actual work items (prerequisites needed but not built)
3. **`ungrounded`** — parts of the vision no checkpoint can deliver (vision exceeds capability map — a
   signal to either add a checkpoint or admit the vision is premature)

## WHEN TO USE IT (as an agent)

- **Starting a new vision doc** → run vcreate to produce the delivery plan before writing code.
- **Reviewing an existing vision** → run vcreate to see how much is already built (reuse) and what's left.
- **Before building anything** → vcreate tells you the dependency order (dependencies first), so you
  don't build a checkpoint whose prerequisites don't exist.
- **Detecting vision-drift** → if a vision's backward walk shows lots of `ungrounded`, the vision isn't
  grounded in your capability map yet.

## HOW TO RUN

```bash
# produce the backward plan for a vision
python3 scripts/reverse-deliver.py --vision Verified-Statement-Marketplace

# override what's "already done" (e.g. after building some checkpoints)
python3 scripts/reverse-deliver.py --vision Verified-Statement-Marketplace --done cert-a cert-b
```

## HOW TO CREATE A VISION'S CHECKPOINT DAG

`data/checkpoints/<vision>.json`:
```json
{
  "vision": "<name>",
  "goal": "<the exact effect string that one checkpoint's effect equals>",
  "already_done": ["<ids of built checkpoints>"],
  "checkpoints": [
    {"id": "<cp>", "effect": "<what it delivers>", "prereqs": ["<ids or effects it needs>"]}
  ]
}
```

**Discipline:** the `goal` must exactly match a checkpoint's `effect` (the mechanism won't chase
a mismatched string — that's a feature: it catches spec errors).

## WHY IT'S A COMPOUNDING AGENT BEHAVIOR

- **Every vision gets a delivery plan** — not a vague roadmap, a checkable backward walk.
- **The checkpoint DAGs accumulate** — each vision you analyze adds to `data/checkpoints/`, so the
  next vision analysis gets richer (more reuse discovered).
- **It composes with our flywheels** — the backward plan says *what to build*; the flywheel says *why it
  compounds once built*. Forward for value, backward for delivery.
- **It's the missing half of the vision→chunk→layer map** — that map goes forward (vision→chunks→layers);
  vcreate goes backward (vision→checkpoints→current-implementations). Together they're a complete
  bidirectional delivery mechanism.

## REFERENCES

- Fikes & Nilsson (1971) "STRIPS" — goal-regression / backward chaining.
- Newell & Simon (1963) "GPS" — means-ends analysis.
- STRIPS/PDDL planning — backward search.
- This project: `THESIS-REVERSE-DELIVERY.md` (the full thesis) + `scripts/reverse-deliver.py` (the code)
  + `data/checkpoints/` (the DAGs).
