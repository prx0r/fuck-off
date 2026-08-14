# CONTRACT-CONVERGENCE — my review of the shared BUILD directives

*2026-08-14 · status: MY ASSESSMENT (agentgraph) of the shared BUILD-* directives from agentpatala,
judged against my own integration/perf docs. I do NOT take them as final word — I assessed each. Verdict:
the #1 build (contracts convergence) is correct and I'm doing it; several others are correct gaps; but my
read plane + anti-theatre + hound/pushing steals are ahead of the OG map.*

---

## WHAT THE BUILD DIRECTIVES TOLD ME (assessed)

| Directive | Correct? | My assessment |
|---|---|---|
| **BUILD-CONTRACTS-CONVERGENCE** (the #1 build) | ✅ **YES — do it now** | Verified: there ARE ~6 divergent ReviewEvent/Authority defs (my lib/review + lib/epistemic vs OG's 4). This is schema-drift at the contract level — the same root cause as my own audit's "two layer taxonomies." Building on divergent contracts = building on a lie. |
| BUILD-INGESTION-HARVEST | ✅ correct gap | My ingestion_organism had no real Sanskrit input; OG's R2 adapters (pandit/gretil/sarit) are the real harvest. |
| BUILD-BIBLIOGRAPHY-IDENTITY | ✅ correct gap | My bibliography (from build-static-site) is thin; OG has 254 works + editions. |
| BUILD-FACTORY | ✅ correct gap | OG has 9 real workers + factory_loop.sh; I have kernels, not a factory. |
| BUILD-HERMES-ORCHESTRATION | ✅ correct gap | My hermes_exec is a thin wrapper; OG's model.py is the full client. Unify. |
| BUILD-TRANSLATION-STATE | ✅ correct | The per-work FSM (next_valid_action) is what makes ALL works autonomous. |
| BUILD-CP4-ARGUMENT | ⚠️ partially | The philosophical IR is real, but my crux/argument kernels already cover much of it. |

## WHERE MY VERSION IS BETTER (not in the OG map)

1. **The read plane is real + working** — context_compiler, seo, bundle_router, the Astro site (35 pages),
   edge/server.py (verified API+MCP). OG's BUILD-INDEX lists no working read plane.
2. **My anti-theatre is more rigorous** — audit-theatre-dataflow.py (strict data-flow check) + the 3 theatre
   modes. OG's directives don't audit their own tests this way.
3. **`iteration_confidence` (hound steal) + `pushing_miner`** — genuinely new, not in the OG build map.

## THE CONVERGENCE (what I'm doing — the honest foundation)

The OG `AuthorityVector` (4-axis, non-scalar, gate-predicates) is **better than my scalar-rank `epistemic.py`**.
Convergence direction:
- **Adopt OG `AuthorityVector` as the canonical Authority** (4 axes: generation/evidence/review/publication,
  explicit gate predicates — no scalar rank).
- **My `lib/epistemic.py` envelope adapts to it** — keeping my stronger parts (the honest ceilings, the
  invariant) but using the OG 4-axis vector as the authority substrate.
- **One `ReviewEvent`/`ReviewState`** — my lib/review.py collapses onto the OG canonical.
- **A parity test** — the same review event through OG + my reducer gives the same phase.

**The rule (anti-theatre):** nothing builds on top until the 5 contracts converge. This is the gate for the
contract layer. Doing the convergence NOW, before more layers pile on divergent contracts.

## Proofs / resolution
- The 6 divergent defs: my `lib/review.py` + `lib/epistemic.py` vs OG `source-evidence/schema/*` +
  `python/patala_core/{objects,authority}.py` + `pipeline/review_engine.py`
- The canonical target: OG `python/patala_core/authority.py` (AuthorityVector, non-scalar)
- The shared directives: `migration/shared/BUILD-*.md` (agentpatala's external assessment)
