#!/usr/bin/env python3
"""validate-self-healing.py — self-healing orchestration (arXiv 2606.01416) for our delivery loop.

Proves the typed repair cascade: a failing step is DIAGNOSED and RECOVERED (retry / re-plan / degrade /
abort+review) instead of aborting the whole run. Closes the agent_delivery repair gap — the weakest
kernel (PROTOTYPED). On our IPK verification tasks.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from self_healing import SelfHealingOrchestrator, HealingStep, FailureClass

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=== SELF-HEALING ORCHESTRATION (2606.01416) — repair cascade for the delivery loop ===\n")

orch = SelfHealingOrchestrator(max_transient_retries=3, backoff_base=0.001)

# ---- TRANSIENT failure -> retry succeeds ----
calls = {"n": 0}
def flaky_step(work):
    calls["n"] += 1
    if calls["n"] < 3:
        raise RuntimeError("network timeout, retry")
    return "verified"
s = HealingStep("verify-IPK", flaky_step)
r = orch.run_with_healing(s, "IPK-1.5.19")
check("TRANSIENT: retried then succeeded", r["ok"] and r["result"] == "verified")
check("TRANSIENT: the cascade is logged (typed, auditable)", any(h["heal"] == "retried" for h in orch.healing_log))

# ---- STALE failure -> re-plan (staleness under us) ----
def stale_step(work):
    raise RuntimeError("inputs changed (source updated)")
s2 = HealingStep("translate", stale_step)
r2 = orch.run_with_healing(s2, "IPK-1.5.11")
check("STALE: re-plans (does not retry blindly)", not r2["ok"] and r2["heal"] == "replan")
check("STALE: recovery decision feeds the re-plan path", any(h["heal"] == "replanned" for h in orch.healing_log))

# ---- BLOCKED -> degrade gracefully (never silently succeed) ----
def blocked_step(work):
    raise RuntimeError("blocked by gate")
s3 = HealingStep("publish", blocked_step)
r3 = orch.run_with_healing(s3, "essay")
check("BLOCKED: degrades gracefully with partial note", not r3["ok"] and r3["heal"] == "degraded" and r3["partial"])

# ---- UNRECOVERABLE -> abort + file review item (never silently succeed) ----
def dead_step(work):
    raise RuntimeError("model API permanently unavailable")
s4 = HealingStep("synthesize", dead_step)
r4 = orch.run_with_healing(s4, "synthesis")
check("UNRECOVERABLE: aborts", not r4["ok"] and r4["heal"] == "abort")
check("UNRECOVERABLE: files a review item for humans", len(orch.review_items) == 1 and orch.review_items[0]["status"] == "open")

# ---- classification is typed (each failure class has a distinct recovery) ----
check("classification: typed failure classes (not a catch-all)",
      orch.classify(HealingStep("x", lambda w: 0), "network timeout") == FailureClass.TRANSIENT
      and orch.classify(HealingStep("x", lambda w: 0), "stale") == FailureClass.STALE)

print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
print("\nSELF-HEALING ORCHESTRATOR (2606.01416): a failing step is DIAGNOSED (transient/stale/blocked/")
print("unrecoverable) and RECOVERED — retry / re-plan / degrade / abort+review — never silently aborts")
print("and never silently succeeds. This closes the agent_delivery repair gap.")
sys.exit(0 if all(c for _,c in results) else 1)
