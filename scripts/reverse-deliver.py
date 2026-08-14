#!/usr/bin/env python3
"""reverse-deliver.py — THE backward-delivery mechanism (Reverse-Delivery thesis).

Given a VISION's checkpoint DAG (each checkpoint: effect -> [prereqs]) + the set of "already-done"
prerequisites (current implementations), output the backward plan: the reverse-topological path from
the vision down to what's already built.

This is GOAL-REGRESSION / BACKWARD CHAINING applied to product delivery. It answers:
  "what must EXIST for this vision to be true, walking backward until I hit what I already have?"

Usage:
  python3 reverse-deliver.py --vision <name> [--json]
The vision checkpoint DAGs live in data/checkpoints/<vision>.json (see example below).
"""
import json, os, sys, argparse

CHECKPOINTS_DIR = "/mnt/HC_Volume_106427611/ip-graph/data/checkpoints"

# ---- the mechanism: backward chaining over the checkpoint DAG ----
def reverse_plan(goal, checkpoints, done):
    """Backward chaining: start at goal, regress through checkpoints to already-done prerequisites.
    Returns (plan_order, delivered, to_build, open_subgoals).
    `to_build` = checkpoints that ARE the vision's work items (have an effect, aren't already done,
    and aren't delivered by another checkpoint). `open_subgoals` = needed but no checkpoint delivers.
    """
    by_effect = {cp["effect"]: cp for cp in checkpoints}
    plan = []
    delivered = set(done)
    frontier = [goal]
    seen = set()
    open_subgoals = {}
    to_build = set()

    while frontier:
        g = frontier.pop(0)
        if g in delivered or g in seen:
            continue
        seen.add(g)
        cp = by_effect.get(g)
        if cp is None:
            open_subgoals[g] = "no checkpoint delivers this — UNGROUNDED (vision exceeds capability map)"
            continue
        unmet = [p for p in cp["prereqs"] if p not in delivered]
        if not unmet:
            delivered.add(g)
            plan.append(cp["id"])
        else:
            frontier.extend(unmet)

    # the vision's actual WORK ITEMS:
    # (a) prerequisites that are needed but produced by NO checkpoint and not already done = MUST BUILD
    # (b) checkpoints whose effect is needed but the checkpoint isn't done
    produced = {cp["effect"] for cp in checkpoints}   # everything some checkpoint delivers
    all_prereqs = {p for cp in checkpoints for p in cp["prereqs"]}
    to_build = set()
    for p in all_prereqs:
        if p not in produced and p not in delivered:
            to_build.add(p)     # a leaf work item: needed, not done, no checkpoint makes it
    for cp in checkpoints:
        if cp["id"] not in delivered and cp["id"] not in plan and cp["effect"] in all_prereqs:
            to_build.add(cp["id"])
    return plan, delivered, to_build, open_subgoals


def run_vision(name, done_override=None):
    vf = os.path.join(CHECKPOINTS_DIR, f"{name}.json")
    if not os.path.exists(vf):
        print(f"no checkpoint file for vision '{name}' at {vf}"); return
    data = json.load(open(vf))
    goal = data["goal"]
    checkpoints = data["checkpoints"]
    done = set(done_override) if done_override else set(data.get("already_done", []))

    print(f"=== REVERSE-DELIVERY PLAN for: {goal} ===\n")
    print(f"[already done] {len(done)} prerequisites satisfied: {sorted(done)}")
    print(f"[checkpoints]  {len(checkpoints)} in the DAG\n")

    plan, delivered, to_build, open_subgoals = reverse_plan(goal, checkpoints, done)

    print("-- what must be BUILT (backward from vision, dependencies first) --")
    print(f"  NEW to build ({len(to_build)}): {sorted(to_build)}")
    for i, cp in enumerate(plan, 1):
        print(f"  {i:2d}. {cp}")
    newly = [cp for cp in plan if cp not in done]
    print(f"\n  total delivered: {len(delivered)}  |  NEW checkpoints in plan: {len(newly)}")

    if open_subgoals:
        print(f"\n-- UNGROUNDED (vision exceeds current capability map) --")
        for g, msg in open_subgoals.items():
            print(f"  ✗ {g}: {msg}")

    print(f"\n-- reuse: {len(delivered & done)} checkpoints were ALREADY built (the joyful part) --")
    print(f"  already-built the vision reuses: {sorted(delivered & done)}")
    return plan


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--vision", required=True)
    ap.add_argument("--done", nargs="*", default=None)
    args = ap.parse_args()
    run_vision(args.vision, args.done)
