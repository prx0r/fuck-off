#!/usr/bin/env python3
"""validate-alignment-flywheel.py — the mine→stage→review→promote flywheel (fojin cross-source moat).

Proves fojin's alignment flywheel on our real IPK/IPVV corpus: blind candidate matching is staged, human-
reviewed, and only PROMOTED pairs become evidence — a bad auto-match is never served as cross-source
ground truth unreviewed. Plus anchor-expansion (alignment locality) grows verified pairs cheaply.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from alignment_flywheel import AlignmentFlywheel

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=== MINE→STAGE→REVIEW→PROMOTE FLYWHEEL (fojin cross-source moat) ===\n")

# ---- MINE: a blind match below threshold is NOT even staged ----
fw = AlignmentFlywheel(min_similarity=0.65)
fw.mine("IPK-1.5.19 (Sanskrit)", "a spurious modern paraphrase", 0.40, "embed_llm")
check("MINE: low-similarity blind match is not staged (threshold)", len(fw.candidates) == 0)

# ---- MINE: a real candidate IS staged as pending (high-recall, but unreviewed) ----
fw.mine("IPK-1.5.19 (vimarśa = essence of light)", "Ratié Ch4 (experience-not-construction)", 0.82)
fw.mine("IPK-1.5.11 (pratyavamarsa)", "Ratié Ch7 (camatkāra)", 0.78)
check("MINE: real candidates staged as pending", len(fw.pending()) == 2)
check("MINE: staged candidates are LLM-kind (NOT yet evidence)", fw.candidates[0].kind.value == "llm")

# ---- a candidate is NOT served until promoted ----
check("REVIEW: pending candidates are NOT served as evidence", fw.served_parallels() == [])

# ---- REVIEW: one accepted, one rejected (human-in-the-loop) ----
fw.review(0, accept=True)
fw.review(1, accept=False)
check("REVIEW: accepted promotes to flywheel-verified", fw.candidates[0].kind.value == "flywheel-verified")
check("REVIEW: rejected does not become evidence", fw.candidates[1].status == "rejected")

# ---- only promoted pairs are served ----
served = fw.served_parallels()
check("PROMOTE: only accepted pairs served as evidence", len(served) == 1 and served[0]["kind"] == "flywheel-verified")

# ---- ANCHOR-EXPANSION: from the verified pair, propose neighbours (alignment locality) ----
before = len(fw.candidates)
fw.mine_from_anchors(("IPK-1.5.19", "Ratie-Ch4"), neighbour_offsets=(-1, 1))
check("ANCHOR-EXPANSION: verified pair grows outward (±1 neighbours)", len(fw.candidates) == before + 2)
check("ANCHOR-EXPANSION: new candidates are auto-proposed, still pending review",
      all(c.status == "pending" for c in fw.candidates[2:]))

# ---- the flywheel never serves a bad auto-match as ground truth ----
check("HUMAN-IN-LOOP: no candidate can reach evidence without review", fw.served_parallels() == served)

print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
print("\nALIGNMENT FLYWHEEL (fojin moat): blind matching is staged, human-reviewed, and only PROMOTED")
print("pairs become cross-source evidence. Anchor-expansion grows verified pairs cheaply via alignment")
print("locality. A bad auto-match is NEVER served as ground truth unreviewed — the cross-source moat.")
sys.exit(0 if all(c for _,c in results) else 1)
