# migration/ — reconciling patala's v2 spec with our proven lab

*2026-08-14 · This is the OTHER side of the handover. The patala agent (`/root/projects/patala/migration/v2/`)
spec'd the target: 16 products, a `LAYERS.yaml` contract, a ground-up plan, and named the machinery
that SHOULD exist. We have been RAPIDLY PROTOTYPING those exact mechanisms in this lab (`ip-graph` /
`fuck-off`). This folder reconciles the two: **patala spec'd what we need → we prove what we can build,
with verifiable proofs, and expand beyond their plan.**

**The handover contract:** the agent we hand off to will take our proven kernels + specs and BUILD +
TEST properly what we've prototyped. Our job here is to hand them the **what + how + proof** for every
product patala listed — and the **extra products** they didn't anticipate.*

---

## What's in here

| Path | What it is |
|------|-----------|
| `v2/README.md` | the mirror of patala's v2 reading hierarchy, grounded in OUR implementations |
| `v2/LAYERS.yaml` | our codified layer contract — each layer mapped to a PROVEN kernel + experiment |
| `v2/PRODUCTS.md` | the 16 patala products, EACH with our proven mechanism + proof + expansion |
| `v2/RECONCILIATION.md` | their spec ↔ our implementations (what's built, what needs building) |
| `v2/EXPANSIONS.md` | the products/mechanisms BEYOND their plan (what our lab discovered) |
| `v2/PUSHING-ORGANISM-ESSAYS.md` | the human side: logicvid gold + organism + essays-as-machine |
| `v2/ESSAY-INGEST.md` | the deep essay-ingest architecture (9 stages, each → proven kernel) |
| `v2/INGESTION-ARCHITECTURE.md` | source-text vs essay-about-source vs standalone essay (KORAL two-graph) |
| `v2/GRADUATION.md` | **the full organism test is real** — one claim through the whole stack (14/14) |
| `v2/strategy/` | the strategic view from our side |

## The one-line summary

> Patala v2 spec'd a coherent system (one kernel, one graph, clear names, 16 products).
> We built 17 kernels + 53 experiments that PROVE the mechanisms for most of those products —
> and discovered 6 more product-level capabilities they didn't list. This folder makes every patala
> product traceable to a proven lab mechanism, so the next agent can build them properly.

## Reading order (for the handoff agent)

1. `RECONCILIATION.md` — which patala v2 products we've already proven, and which need building.
2. `PRODUCTS.md` — the 16 products, each with our proven kernel + experiment + verifiable proof.
3. `EXPANSIONS.md` — the 6+ products beyond their plan (organism, marketplace, what-if, question-growth,
   enquiry-discovery, self-proving).
4. `LAYERS.yaml` — our layer contract (proven kernels per layer).
5. `../AGENTS.md` + `../TRACEABILITY-MAP.md` — the axioms + how everything resolves.
