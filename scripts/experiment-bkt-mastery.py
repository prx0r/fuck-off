#!/usr/bin/env python3
"""experiment-bkt-mastery.py — Bayesian Knowledge Tracing for the Co-Evolving Organism (VISION).

pyBKT (cloned, CAHLR/pyBKT) estimates learner mastery from problem-solving sequences using the BKT
model: P(mastered) updated by prior mastery, learn rate, guess, and slip. We apply this to our
co-evolving-organism vision — tracking a learner's mastery of the free-will concepts as they answer
questions, feeding the misconception graph.

BKT update (per response):
  P(L_t) = P(L_{t-1}) + (1 - P(L_{t-1})) * learn_rate      # prior mastery + learning
  P(correct | L) = guess*(1-P(L)) + (1-slip)*P(L)          # how likely correct given mastery
  P(L | correct) = (1-slip)*P(L) / P(correct)              # posterior after a correct answer
"""
import json

# BKT params for a concept (learn rate, guess, slip) — from pyBKT's model
CONCEPTS = {
    "quantum":     {"prior": 0.85, "learn": 0.05, "guess": 0.05, "slip": 0.05},
    "free_will":   {"prior": 0.30, "learn": 0.10, "guess": 0.10, "slip": 0.10},
    "indeterminism":{"prior": 0.40, "learn": 0.10, "guess": 0.10, "slip": 0.10},
    "compatibilism":{"prior": 0.20, "learn": 0.08, "guess": 0.15, "slip": 0.10},
}

def bkt_update(prior, learn, guess, slip, correct):
    """One BKT step: update mastery probability given a response (correct/incorrect)."""
    pL = prior + (1 - prior) * learn                    # updated prior mastery
    p_correct = guess * (1 - pL) + (1 - slip) * pL       # P(correct) given mastery
    if correct:
        pL_given = (1 - slip) * pL / max(p_correct, 1e-9)
    else:
        pL_given = slip * pL / max((1 - p_correct), 1e-9)
    return pL_given

print("=== BKT MASTERY TRACKING (Co-Evolving Organism) ===\n")

# simulate a learner answering 8 questions about 'free_will' (some right, some wrong)
concept = "free_will"
p = CONCEPTS[concept]
mastery = p["prior"]
seq = [True, False, True, True, False, True, True, True]   # responses
print(f"learner on '{concept}' (prior mastery {mastery:.2f}):")
for i, correct in enumerate(seq, 1):
    mastery = bkt_update(mastery, p["learn"], p["guess"], p["slip"], correct)
    print(f"  Q{i} {'✓' if correct else '✗'} -> mastery {mastery:.3f}")

print(f"\n  final mastery: {mastery:.3f}")
print(f"  (starts at {p['prior']:.2f}, grows with correct, dips on slips)")

# comparison: novice concept (compatibilism) with a persistent misconception
print("\n-- a novice struggling on 'compatibilism' (persistent confusion) --")
p2 = CONCEPTS["compatibilism"]
m = p2["prior"]
# the learner keeps confusing it with free_will (wrong answers) -> mastery stays low
for i in range(6):
    m = bkt_update(m, p2["learn"], p2["guess"], p2["slip"], correct=False)
print(f"  after 6 wrong answers: mastery {m:.3f}  (correctly stays low)")
print(f"  -> this learner's confusion feeds the MisconceptionGraph as a demand signal")

print("\n=== INSIGHT ===")
print("BKT gives the organism a PRINCIPLED mastery signal per learner per concept — not just")
print("correct/wrong, but a calibrated P(mastered) that updates on each response. Low mastery +")
print("persistent errors = the misconception graph's demand signal (Co-Evolving Organism vision).")
print("This is the mechanism pyBKT productionizes; we apply it to our epistemic graph's concepts.")
