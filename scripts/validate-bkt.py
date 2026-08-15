#!/usr/bin/env python3
"""validate-bkt.py — Bayesian Knowledge Tracing (pyBKT) in the pedagogy engine.

Verifies lib/pedagogy.bkt_update: a wrong answer is modeled as a GUESS/SLIP, not a collapse to 0 mastery —
the uncertainty-bounded learner state. A wrong answer lowers P(mastery) but keeps the learner teachable;
correct answers raise it. Weakest-skill selection targets what to teach next.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from pedagogy import BKTState, bkt_update, bkt_weakest_skill, MasteryEvidence

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=== BAYESIAN KNOWLEDGE TRACING (pyBKT) in the pedagogy engine ===\n")

st = BKTState("learner-1")
skill = "TERM_SENSE"

# a correct answer should raise P(mastery) from the prior
bkt_update(st, MasteryEvidence("learner-1", "c1", skill, correct=True))
after_correct = st.p_mastered(skill)
check("a correct answer raises latent P(mastery)", after_correct > BKTState("x").p_mastered(skill),
      f"(prior=0.2 -> {after_correct})")

# a wrong answer should LOWER but NOT collapse to 0 (it may be a guess/slip, not ignorance)
bkt_update(st, MasteryEvidence("learner-1", "c1", skill, correct=False))
after_wrong = st.p_mastered(skill)
check("a wrong answer lowers P(mastery) but not to 0 (guess/slip, not ignorance)",
      0 < after_wrong < after_correct, f"({after_correct} -> {after_wrong})")

# repeated correct answers converge mastery upward
for _ in range(6):
    bkt_update(st, MasteryEvidence("learner-1", "c1", skill, correct=True))
high = st.p_mastered(skill)
check("repeated correct answers converge P(mastery) upward", high > 0.8, f"({high})")

# two skills: weakest under threshold is the next target
st2 = BKTState("learner-2")
bkt_update(st2, MasteryEvidence("learner-2", "a", "TERM_SENSE", correct=True))
for _ in range(5):
    bkt_update(st2, MasteryEvidence("learner-2", "b", "SOURCE_GROUNDING", correct=False))
w = bkt_weakest_skill(st2, threshold=0.7)
check("weakest-skill selection targets what to teach next",
      w == "SOURCE_GROUNDING", f"(weakest={w})")

print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
print("\nBayesian Knowledge Tracing gives the pedagogy engine an uncertainty-bounded learner state:")
print("wrong answers are modeled as guess/slip (mastery drops but stays teachable), correct answers")
print("converge mastery upward, and weakest-skill selection drives adaptive teaching (pyBKT insight).")
sys.exit(0 if all(c for _,c in results) else 1)
