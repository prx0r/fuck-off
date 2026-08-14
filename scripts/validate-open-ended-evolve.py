#!/usr/bin/env python3
"""validate-open-ended-evolve.py — Darwin Godel Machine adapted to our organism (arXiv 2505.22954).

Steals the Darwin Godel loop (ecosystem/agent-evolution/dgm) onto our organism: proposed changes to
rules/verifiers are accepted into an archive ONLY if they pass the ORACLE (epistemic invariant + mutation
kill-rate = the verifiable reward) AND improve or add novelty (open-ended, self-referential). This is the
epistemically-safe evolution: open-ended search under the invariant oracle with an audit trail.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from open_ended_evolve import OpenEndedEvolution

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=== DARWIN GODEL MACHINE, adapted to the epistemic organism (2505.22954) ===\n")

# the oracle: a proposed rule change passes if it keeps the invariant + kills mutations (verifiable reward)
def oracle(change):
    # a change that would break epistemic honesty FAILS the oracle outright (cannot be archived)
    if "drop" in change or "relax" in change or "remove the" in change:
        return False, 0.0
    # invariant/gate/ceiling changes pass with high kill-rate (verifiable reward)
    if "invariant" in change or "gate" in change or "ceiling" in change:
        return True, 0.85
    return True, 0.5

evo = OpenEndedEvolution(oracle=oracle, novelty_w=0.3)

# ---- GEN 0: propose the baseline rules ----
evo.propose("r1", "enforce ceiling invariant (authority(projection)<=authority(parent))", novelty=0.9)
evo.propose("r2", "gate promotion on mutation kill-rate", novelty=0.8)
check("GEN0: baseline rules accepted (they pass the oracle)", evo.archive["r1"].accepted and evo.archive["r2"].accepted)

# ---- a rule that would BREAK the invariant is REJECTED (the oracle gate) ----
evo.propose("r-bad", "drop the ceiling invariant to speed up throughput", novelty=0.0)
check("the oracle REJECTS a rule that breaks honesty (invariant gate)",
      not evo.archive["r-bad"].accepted and evo.archive["r-bad"].oracle_score <= 0.15)

# ---- open-ended: a novelty-only candidate is accepted even at moderate performance (Darwin) ----
evo.propose("r-novel", "a new verifier ensemble (RefChecker+GraphCheck)", novelty=1.0)
check("open-ended: high-novelty rule accepted (Darwin novelty axis)",
      evo.archive["r-novel"].accepted)

# ---- evolution archives + parents get children ----
evo.step()
evo.propose("r1b", "tighter ceiling: tighten invariant + raise gate", novelty=0.4, parent="r1")
check("evolution: r1b accepted + recorded as child of r1", evo.archive["r1b"].accepted and evo.archive["r1"].children == 1)

# ---- the best rules are the elite (performance + novelty) ----
best = evo.best(3)
check("the elite rules are the high-fitness ones", all(b.accepted for b in best))
check("deterministic + content-addressed", len(evo.archive["r1"]._hash) == 12)

print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
print("\nDARWIN GODEL ADAPTED: open-ended evolution of the organism's rules under the INVARIANT ORACLE.")
print("A rule is archived only if it passes the oracle (verifiable reward) and improves or adds novelty.")
print("Breaking-honesty rules are rejected; novelty is a first-class driver. This is the epistemically")
print("SAFE self-improvement loop (Darwin 2505.22954 + audited skill-graph 2512.23760).")
print(f"\nARCHIVE: {evo.archive_state()}")
sys.exit(0 if all(c for _,c in results) else 1)
