#!/usr/bin/env python3
"""validate-misconception.py — the misconception repair-cascade kernel (DEV_PLAN §1.1).

Verifies: likelihood formula is monotonic in the signals; crossing threshold flags the source for
scholar review; propagate_fix reuses the RKA blast-radius to stale every downstream dependent; the
confusion is measured to dissolve after the fix.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from misconception import MisconceptionRepairCascade, misconception_likelihood
from staleness import build_dependency_index

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=== MISCONCEPTION REPAIR CASCADE (lib/misconception.py) ===\n")

# ---- 1. the likelihood formula is monotonic (more signal = higher likelihood) ----
low = misconception_likelihood(cluster_size=2, persistence=1, ambiguity_signal=0.1, novice_rate=0.1)
high = misconception_likelihood(cluster_size=40, persistence=12, ambiguity_signal=0.9, novice_rate=0.8)
check("likelihood is monotonic in the signals (low < high)",
      low < high, f"({low} < {high})")
check("likelihood stays in [0,1]",
      0.0 <= low <= 1.0 and 0.0 <= high <= 1.0, f"(low={low}, high={high})")

# ---- 2. a genuine misconception (large cluster, persistent, ambiguous, high novice) crosses threshold
#         and is FLAGGED for scholar review ----
cascade = MisconceptionRepairCascade(threshold=0.7)
cascade.record("C1", "free_will_requires_quantum_chance",
               cluster_size=30, persistence=9, ambiguity_signal=0.8, novice_rate=0.7)
cascade.record("C2", "minor_confusion",
               cluster_size=1, persistence=0, ambiguity_signal=0.0, novice_rate=0.05)
flagged = cascade.flag_for_review()
check("a real misconception (large/persistent/ambiguous/novice) is flagged",
      any(m.claim_id == "C1" for m in flagged), f"({len(flagged)} flagged)")
check("an isolated confusion is NOT flagged",
      all(m.claim_id != "C2" for m in flagged))

# ---- 3. propagate_fix reuses the RKA blast-radius: correcting the source stales every dependent ----
# dag: {id: {'requires': [upstream]}} — C4,C5 depend on C1; C6 depends on C4.
cascade.dag = {
    "C1": {"requires": []},
    "C4": {"requires": ["C1"]},
    "C5": {"requires": ["C1"]},
    "C6": {"requires": ["C4"]},
}
cascade.depends_on = build_dependency_index(cascade.dag)
stale = cascade.propagate_fix("C1")
check("propagate_fix stales the transitive downstream dependents (RKA blast-radius)",
      {"C4", "C5", "C6"} <= stale, f"(stale={sorted(stale)})")
check("propagate_fix does NOT mark the source itself as its own dependent",
      "C1" not in stale)

# ---- 4. measure_dissolution: after the fix + re-exposure, the confusion dissolves ----
after = cascade.measure_dissolution("C1",
                                    cluster_size=1, persistence=0,
                                    ambiguity_signal=0.05, novice_rate=0.05)
check("measure_dissolution records the confusion as dissolved once it falls below threshold",
      after is not None and after.review_state == "DISSOLVED",
      f"(before-flag->after={after.likelihood})")
check("dissolved is recorded in the cascade",
      len(cascade.dissolved) == 1 and cascade.dissolved[0]["claim_id"] == "C1")

s = cascade.summary()
check("summary reports the cascade state honestly",
      s["total"] == 2 and s["dissolved"] == 1 and s["propagated_stale"] >= 3, f"({s})")

print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
print("\nMISCONCEPTION REPAIR CASCADE: likelihood -> flag -> RKA propagate -> measure dissolution.")
print("The kernel closes the organism's closing edge (DEV_PLAN §1.1).")
sys.exit(0 if all(c for _,c in results) else 1)
