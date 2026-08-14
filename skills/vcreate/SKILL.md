---
name: vcreate
version: 1.0.0
author: ip-graph
description: >
  Backward-delivery planning. Walks BACKWARD from a vision through its checkpoint DAG to current
  implementations, producing a reverse-topological delivery plan: reuse (already built), to_build
  (the work items), and ungrounded (vision exceeds the capability map). This is goal-regression /
  backward chaining (STRIPS, Fikes & Nilsson 1971; GPS, Newell & Simon 1963) applied to product
  delivery. Trigger when starting a new vision, reviewing an existing vision, or before building
  anything — to discover what's already built, what to build, and in what dependency order.
---

# VCREATE — backward-delivery planning

## What it is
Instead of "what can I build with what I have?" (forward/capability-driven, under-delivers), vcreate
asks **"what must EXIST for this vision to be true?"** and regresses through checkpoints until it
reaches what's already built.

## The algorithm (goal-regression loop)
```
1. frontier = {vision_goal}
2. while frontier:
     pick goal g
     for checkpoint whose effect == g:
       unmet = [p for p in prereqs if p not in done]
       if not unmet: mark g DELIVERED, add to plan
       else: frontier += unmet        # backward step
3. to_build = needed prereqs that no checkpoint produces and aren't done
4. plan = reverse-topological (dependencies first)
```

## The three outputs
1. **reuse** — what the vision reuses from current implementations (the joyful part)
2. **to_build** — the actual work items, dependency-first
3. **ungrounded** — vision parts no checkpoint can deliver (drift detector)

## Usage
```bash
python3 scripts/reverse-deliver.py --vision Verified-Statement-Marketplace
python3 scripts/reverse-deliver.py --vision Education-Organism
# override what's already done:
python3 scripts/reverse-deliver.py --vision Foo --done cert-a cert-b
```

## Creating a vision's checkpoint DAG
`data/checkpoints/<vision>.json`:
```json
{
  "vision": "<name>",
  "goal": "<must EXACTLY equal one checkpoint's effect string>",
  "already_done": ["<built checkpoint ids>"],
  "checkpoints": [{"id": "<cp>", "effect": "<what it delivers>", "prereqs": ["<needs>"]}]
}
```
Discipline: the `goal` must exactly match a checkpoint's `effect` — a mismatch is a spec error the
mechanism catches (feature, not bug).

## Trigger phrases
"plan this vision backward", "what's left to build for X", "how much of vision X is done",
"reverse-deliver X", "vcreate X", "walk back from the vision".

## Files
- Mechanism: `scripts/reverse-deliver.py`
- Checkpoint DAGs: `data/checkpoints/*.json`
- Thesis: `docs/vision/beyond-patala/THESIS-REVERSE-DELIVERY.md`
- Full process doc: `docs/process/SKILL-VCREATE.md`
