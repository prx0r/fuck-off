# VISION — THE WHAT-IF MACHINE (counterfactual reasoning as discovery)

*2026-08-14. Grounded in our validated capabilities: counterfactual-engine (whole-graph load-bearing
analysis), crux-compiler (minimal divergence), blast-radius (staleness), canonical-DAG, the two-stage vs
compatibilism conflict. The striking validated result: THERMODYNAMICS is the most load-bearing layer
(11 downstream claims collapse if false) — a counterintuitive, *useful* discovery.*

---

## THE EMERGENT SYNERGY

The counterfactual engine produced a genuinely novel, non-obvious result: **THERMODYNAMICS, not
PHYSICS, is the most load-bearing layer** in our Doyle graph (11 downstream claims collapse if it's
false). Nobody would have guessed that by reading the philosophy.

This revealed that **"what-if" analysis generates real research signal** — it finds the linchpins, the
vulnerabilities, the load-bearing assumptions that close reading misses.

## THE IDEA

> **A machine that discovers by asking "what if" across an entire epistemic graph** — generating
> candidate research questions from the graph's own vulnerability structure, then testing them.

Instead of a human choosing what to research, the OS:
1. Computes which assumptions are **most load-bearing** (counterfactual blast-radius)
2. Computes which **cruxes separate rival positions** (crux-compiler)
3. **Proposes** the highest-value open questions (where a load-bearing premise is weakly verified)
4. Spawns targeted research at exactly those points

## THE FLYWHEEL

```
graph → load-bearing analysis → weak-but-load-bearing claims → proposed research
    ↑                                                              ↓
  improved graph ← new evidence verified ← research conducted at the crux
```

**The flywheel is *discovery*, not just retrieval:**
- Every graph produces load-bearing analysis.
- Load-bearing + weakly-verified claims = the highest-value research targets.
- Research at those targets either confirms (strengthens the foundation) or refutes (triggers a repair
  cascade via RKA).
- Either outcome improves the graph, which sharpens the next load-bearing analysis.

## THE FUTURE MOAT

This is a **compound-interest moat**: the value isn't the current facts, it's the *map of what's
load-bearing and what's fragile*. As the graph grows, the map grows more valuable because:

- **It's the R&D roadmap** — it tells you exactly where the field is vulnerable, where effort pays most.
- **It compounds** — each verified claim reshapes the load-bearing map, so the "research intelligence"
  improves with every fact added.
- **It's hard to copy** — it requires the full stack (graph + counterfactual + crux + verification +
  signed history) working together, not a scraper.

## THE NOVEL MECHANISM: "RESEARCH VALUE SCORE"

A concrete mechanism — prioritize research by expected value:

```
ResearchValue(claim) = load_bearing(claim) × (1 − verifier_strength(claim)) × crux_pressure(claim)
```

- **load_bearing** — how much collapses if it's wrong (counterfactual engine)
- **1 − verifier_strength** — how *unverified* it currently is (mutation-testing gives us this)
- **crux_pressure** — how much separates rival positions (crux-compiler)

ResearchValue is highest for claims that are **load-bearing, weakly verified, and contested** — exactly
the ones worth attacking. This turns the OS from a record into a **research strategist**.

## WHY START NOW

- The counterfactual engine already produces real findings (THERMODYNAMICS > PHYSICS).
- ResearchValue is a simple composition of validated metrics.
- It's domain-agnostic — works on any epistemic graph, so it inherits the General-Engine bet.

## WHAT TO BUILD NEXT

1. **`lib/discovery.py`** — ResearchValue score + the proposed-research-queue.
2. **A research-candidate test** — run ResearchValue on our Doyle graph, see which claims get prioritized
   (expect the two-stage's load-bearing indeterminism premise).
3. **The discovery-loop experiment** — propose a research target, simulate evidence arriving, measure how
   the graph + ResearchValue shift.

See `docs/vision/VISION-UNCONSIDERED-FRONTIERS.md` (VISION B counterfactual engine) + the
counterfactual-engine experiment — this vision makes discovery a flywheel.
