# CONTEXT-REVIEW 3 — the files I read + what I learned (agentgraph, 2026-08-15)

*2026-08-15. Compiled by agentgraph from a fresh, deep read of the governing files on BOTH sides
(ip-graph + patala) plus live system inspection (RAM, Postgres, R2, translation progress). This records
exactly which files were read and the load-bearing facts learned from each, so the next session inherits
a correct mental model without re-reading everything. Supersedes nothing; supplements CONTEXT-REVIEW.md +
CONTEXT-REVIEW-2.md. Everything below is what I actually read/verified, not prose.*

---

## 0. THE ONE-LINE (unchanged, now fully internalized)

**patala PRODUCES** (the translation factory DAG + the OpenAlex-of-Sanskrit Atlas surface).
**ip-graph VALIDATES + SERVES** (the read plane, the organism, the validation kernels).
**Hermes = replaceable execution kernel** (GENERATION, agentic `chat`, never blind `-z`).
**.py kernels REDUCE** into the epistemic graph. **Kanban = scheduler, not constitution.**
**Postgres + R2 + event log = the truth.**

---

## 1. EXACT FILES READ (this session)

### ip-graph (`/mnt/HC_Volume_106427611/ip-graph`)
| File | What I learned |
|---|---|
| `AGENTS.md` | The governing rules. THE #1 FAILURE TO FORBID: never act like mature infra doesn't exist (patala's factory is real). RUNNING TESTS IS NOT WORK. Never sleep/timeout; background long jobs (`setsid … &`); kill by PID. RAM is the scarcest resource (4-core/8GB/no-swap, 2 agents). |
| `MASTER-KNOWLEDGE-BASE.md` | The 17→52 kernels, 10 visions, 8 laws, 6 frontiers (F built), the read plane built, graduation closed. The "resolve chain" for orientation. |
| `CONTEXT-REVIEW.md` | ip-graph honest state: kernel count drift (52 vs 47 vs 37 vs 25), L08 EMPTY over-claimed, 2 theatre validators, IPVV gold not ingested. |
| `CONTEXT-REVIEW-2.md` | THE CRITICAL ONE: the Postgres `patala-atlas` layer was OFFLINE (container Exited 255) → the factory was crashing on it. ip-graph = heavily-over-built validation lab, NOT production. The per-verse runner contradiction. |
| `docs/vision/VISION.md` | The one global vision: general epistemic graph engine across Sanskrit/Western/science; the argument/evidence layer is the differentiator; engine/domain separation. |
| `VISION-CHUNK-LAYER-MAP.md` + `VISION-CHUNKS.json` | The top-down vision→chunk→layer decomposition (10 layers). |
| `STATE.yaml` | Per-layer ladder (DISCOVERED<PROTOTYPED<VALIDATED<INTEGRATED<PRODUCTION). L00-05/08/09 VALIDATED, L06/07 BUILT, L08 EMPTY (gap B/C marked DISCOVERED though built). |
| `state.json` | Counts: 52 kernels / 97 experiments / 84 theatre (38/46/0) / graduation 14-18-13. L08 wrongly VALIDATED. next_dev_steps P0 = deploy. |
| `GAPS.md` | Typed relations not in graph, read plane NOT DEPLOYED, signed attestation (gap E) blocks marketplace, context paging, L08 empty. |
| `TODO.md` / `DEV_PLAN.md` (head) | Pipeline done; the translation runner divergence recorded as KILLED; the 3 honesty problems (layers stale, 3 taxonomies, GAPS stale). |
| `layers/00-09-*.md` (all 10) | Each layer's spec + current state. Confirms L08 `lib/domains/` EMPTY; several layer docs stale (say NOT_STARTED while kernels exist). |
| `docs/05-performance.md` | THE PERF DOCTRINE (10 rules): compute-on-write, immutable URLs, one-question-one-request, 0-JS Astro islands, Rust hot-only, measure-before-infra, ETag/304, cache aggressively. |
| `docs/performanceagent.md` | External survey: SSG/islands for sites, edge Workers for APIs, Protobuf/MsgPack, HTTP/3, vector RAG, JSON-LD for agents. |
| `specs/SPEC-49-PERFORMANCE-BUILD-DECISION.md` | FROZEN STACK: Python+DuckDB → R2 → Astro + bundles/MCP + Postgres FTS first, Tantivy only if hot. Rust = wheels only. Agent SEO: one URL/ID, four graphs. Perf budgets. |
| `tantraloka/CANONICAL-TRANSLATION-ORCHESTRATION.md` | Translation orchestration = `pipeline/factory_scheduler.py` (deterministic Python DAG controller). Per-verse runner KILLED. ARGMAP is the missing piece that fixes the 0.118 gloss. |
| `tantraloka/FULL-CORPUS-TRANSLATION-PROCESS.md` | The honest ~42h serial per-verse real-model pipeline (3-worker RAM cap). Anti-theatre: real > fast. Checkpoint+resume safe. |
| `tantraloka/PROGRESS-STATUS.md` | 7-stage suite passes; the 0.118 gold insight; the commentary-lift (B4) is the fix, not the gloss. |
| `tantraloka/GOLD-STANDARD-INSIGHTS.md` | The gloss vs gold mismatch is a PROCESS choice (gloss vs commentary-level reading), not a model failure. Two-stage translation: B3 gloss → B4 commentary. |
| `handover/hermes/CANONICAL.md` | THE INTEGRATION THESIS: Hermes = replaceable execution kernel; Pāṭala = durable epistemic state. Two truths (execution vs epistemic). The 4 corrections. |
| `handover/hermes/README.md` | Hermes has FULL read+edit access to the whole filebase — pass file paths, don't stuff contents. `lib/hermes_exec.py` is the wrapper. |
| `handover/hermes/PEER-REVIEW.md` | Review = a graph mutation with provenance, not prose (the executable-corrections moat). |
| `handover/hermes/hermespatala-architecture-review.md` | ACCEPT WITH CLARIFICATIONS: eligibility must be deterministic Python, never an LLM judgment; two separate constitutions. |
| `handover/hermes/HERMES-CALLING.md` | THE ONE RULE: `hermes chat` agentic, never blind `-z` (~3.8% yield, ARG_MAX). Correct invocation + profile `patala`. Template: `pipeline/agentic_translate.py`. |
| `handover/hermes/TRANSLATION-APPROACH-AND-VALIDATION.md` | THE DOCTRINE: "a wrong translation is worse than no translation; never let the factory outrun the validator." IPVV method = chunk → term-context packet → exemplar → queue → validate. Dyczkowski = gold. Metric = review burden. |
| `handover/hermes/DEV-PLAN.md` | 5 phases: seed profile → MCP `patala_*` verbs (THE gap) → A3 factory on kanban/cron → ReviewEvent-as-graph-mutation (the moat) → scholar surface → BYOA. |
| `lib/hermes_exec.py` | The pinned agentic call: `hermes chat -Q -q --yolo --max-turns N -m deepseek-v4-flash --provider opencode-go -p patala`. Wrapper `agentic()`, `translate_karika()`, `quick()`. |

### patala (`/root/projects/patala`)
| File | What I learned |
|---|---|
| `AGENTS.md` | patala's governing rules (same anti-theatre / one-rule / validators / Hermes profile). |
| `migration/v3/README.md` | The v3 organism blueprint: the proofs (translate_passage 1-call, products 11/11, multisubject 20/20, vertical 12/12, build 18/18); the honest PARTIAL list; the `schema.py` collision. |
| `migration/v3/TRANSLATION.md` | Translation = T1 + Close + Reading + Commentary in ONE structured Hermes call. The three-version flow (R1/T2/R2) is the remaining GAP. |
| `pipeline/factory_scheduler.py` | THE DAG controller (Era B). Enumerates ALL eligible (object,layer) jobs, drains deterministic L0 free, batches per-work, parallelizes chunks, commits serially. **This is what ballooned to 1.85 GB.** |
| `pipeline/object_registry.py` (partial) | `_load()` reads the WHOLE registry into a dict + caches it in `_LOAD_CACHE` for the process lifetime → the memory-amplification source behind the scheduler bloat. `current()`/`commit()`/`is_committed()` semantics. |
| `python/patala_core/atlas/api.py` | The OpenAlex-grammar API (655 lines): filter/search/sort/group_by/select/cursor/autocomplete, ETag/304, folded search index, `/editions`, `/persons`, `/institutions`, `/openpatala/{layer}/{sha}`, `/works/{id}/bundle`. **`resolve_work` at line 626 has NO `@app.get` → DEAD CODE** (CP4 /resolve not routed). |
| `web/astro.config.mjs` | The OG patala Astro 5 static site config (0-JS, static output, patala.org). |
| `web/build_static_patala.py` | The projection compiler → `web/static/*.json` (bibliography 254, clusters, passages, lemma, timeline). **Hardcoded absolute ROOT path** (non-portable). |
| `web/src/pages/index.astro` | Home page reading the compiled manifest. **Hardcoded absolute ROOT path.** |
| `migration/shared/CANONICAL-NOTES-TRANSLATION.md` | THE AUTHORITATIVE ONE-TRUTH (supersedes older docs): the translation factory = `agent3_queue.py` + `factory_scheduler.py` driven by `translation_targets.py` priority queue, launched via `start_overnight.sh`. Priority: kramasadbhava (p10) → … → tantraloka (p39). ONE-OWNER rule (don't run a second scheduler while the loop runs). |
| `migration/shared/SCALING-OPENALEX-SANSKRIT.md` | The scaling plan: the building blocks exist but NONE are wired together (adapters not imported, API reads static data). The wiring gap. |
| `migration/shared/ROADMAP-SANSKRIT-OPENALEX.md` | Foundation DONE: 115k SOURCE with external_ids, ~110 crosswalk rows, CTS adapter, persons/institutions, /editions, OpenAPI. Forward path: R2/CDN deploy, snapshot cadence, Stencila. |
| `migration/shared/OPENPATALA-BUILD-REVIEW.md` | The build review + perf audit: CP1-CP6 done, honest perf gaps (ETag/immutable/content-address/indexed-search/per-artifact). CP4 claims `/resolve` live — **contradicts the dead code**. |
| `migration/shared/BUILD-OPENPATALA-PERFECTING.md` | The docs/grammar/enrichment pass: group_by, multi-sort, autocomplete, ETag/304, 68-work bibliography enrichment, native docs. |
| `data/corpus/downloads/T1-PROCESS-LOG.md` | THE RAW OPERATOR LOG: the automated 50-verse T1 batch fails on invalid/truncated JSON → `generation_failed`. Hand-written glosses pass 100%. kramasadbhava T1 219→248 (hand-produced). THE real current bottleneck. |
| `data/corpus/downloads/translation-state-ledger.json` (via python) | 111 works. T1: 74 NOT_STARTED / 36 LEGACY / 1 MODERN. L0: 109 NOT_STARTED / 2 VERIFIED. L2: 102 NOT_STARTED / 7 LEGACY / 2 PARTIAL. next_action: 81 BUILD_L0_SOURCE_MODE / 29 ACQUIRE_SOURCE / 1 GENERATE_TRANSLATION. 1 agent3-eligible. |

### Live system inspection (not a doc — verified by running)
| Check | Result |
|---|---|
| RAM | 7.6Gi total, 5.5→3.6Gi used after kill, ~2.1→4.0Gi available, NO swap. Top: factory_scheduler 1.85GB, two opencode ~1.46GB, Postiz node stack ~1.4GB, PG 334MB, hermes 106MB. |
| `factory_scheduler` memory | ~1.85 GB RSS. Cause: `_registered_works()`→`R._load("SOURCE")` (382MB registry into a cached dict) + `_eligible_jobs()` materializing 529,405 job dicts + loading all 6 downstream layer registries. **Killed PID 299723.** |
| Postgres | `patala-atlas` (postgres:17-alpine) is UP 9h, port 5433 OPEN (fixed since CONTEXT-REVIEW-2). BUT volume `/dev/sdb` is **100% full** → the PG→JSONL export fails every pass with `DiskFull`. |
| R2 | Configured + verified with fresh credentials. `r2:` remote lists 16 buckets (atlas-sources, patala, sanskritree, tantraloka-site, …). |
| Atlas API | NOT running (no server on 8787) — built + tested, not served. |
| Sites | patala `web/dist/` built (bibliography/index/passages/themes). ip-graph `site/` built (works/ 208 html, concepts/, themes/, passages/, openpatala/ layer artifacts source/t1/l0/l2/l200/c1/argmap/essay/education, search-index.json, sitemap.xml). Both NOT deployed to edge. |

---

## 2. THE LOAD-BEARING THINGS I LEARNED

### 2.1 Translation (the priority-queue system is canonical)
1. **The translation factory is `agent3_queue.py` + `factory_scheduler.py`, driven by `translation_targets.py` (priority queue), launched by `start_overnight.sh`.** `factory_loop.sh` is a legacy path; ip-graph's per-verse runner is KILLED. ONE owner at a time (don't run a second scheduler while the loop runs).
2. **The real bottleneck is T1 batch JSON generation, not the validator.** 50-verse Hermes calls return invalid/truncated JSON → `generation_failed` (validator fails closed). Hand-written correct glosses pass 100%. This confirms the `HERMES-CALLING` root cause: mega-prompt/blind-`-z` → non-JSON. **Fix = smaller agentic batches / JSON-robust parse-retry, not more hand-production.**
3. **The 0.118-vs-Dyczkowski issue is a process choice, not a model failure:** the gloss is correct for L0; the philosophical frame lives in the COMMENTARY (B4/C1). Fix = two-stage: B3 gloss → B4 commentary-lift, validate the commentary.
4. **The three-version flow (R1/T2/R2) is the remaining translation GAP** — gold-only, no workers.

### 2.2 Orchestration + Hermes
5. **Hermes = replaceable execution kernel; Pāṭala = durable epistemic state.** Two separate truths. Hermes NEVER determines what Pāṭala knows. Eligibility is deterministic Python, never an LLM judgment.
6. **Call Hermes agentic, never blind `-z`:** `hermes chat -Q -q "…" --yolo --max-turns N -m deepseek-v4-flash --provider opencode-go -p patala`. Wrapper: `lib/hermes_exec.py`. Hermes has full filebase read+edit — pass paths, don't stuff contents.
7. **THE single biggest gap to "Hermes orchestrates the factory": the `patala_*` MCP verbs** (`patala_next_action`, `patala_get_work_state`, `patala_propose_translation`, …) — spec'd, not built. PROPOSE-not-ACCEPT at the tool boundary.

### 2.3 Memory / infra doctrine (the hard reality)
8. **The scheduler bloat is the exact "bulk-load the whole registry" anti-pattern AGENTS.md forbids** — `object_registry._load()` reads the entire registry into a cached dict. Fix = stream for work-IDs, stream + bound `_eligible_jobs` (generator + job budget), don't hold every layer registry at once, cap default `--max-works`.
9. **RAM is the scarcest resource** (4-core/8GB/no-swap, 2 agents). One heavy job at a time; background everything; never slurp big registries. The Postiz node stack (~1.4GB) is the biggest non-essential consumer — unrelated to translation.
10. **Disk: `/dev/sdb` is 100% full** → Postgres temp export fails. Free space needed (external sources → R2, not local disk).

### 2.4 OpenAlex / Atlas / site
11. **The OpenAlex-of-Sanskrit layer is genuinely built** (identity crosswalks, OpenAlex-grammar API, persons/institutions, /editions, native docs) — but the **harvest adapters are still not wired into production intake**, and the API serves compiled projections, not the live Postgres.
12. **`/resolve` (CP4) is DEAD CODE** — `resolve_work` at `api.py:626` has no `@app.get`. The build review overclaims it as live. Real gap between claim and code.
13. **Both sites (patala `web/` + ip-graph `site/`) are built but NOT deployed** to edge — the SPEC-00/49 premise (immutable bytes on CDN) is unmet. Both have **hardcoded absolute paths** (non-portable). The 254-work bibliography renders as a thin 4-field projection.

---

## 3. HONEST GAPS RE-CONFIRMED / NEWLY SEEN

- **T1 batch generation is the operational blocker** (JSON failures at scale → hand-production is the stopgap).
- **`factory_scheduler` memory bloat** (1.85 GB) — must be streamed/bounded.
- **Disk 100% full** on the volume → Postgres export failing every pass.
- **`/resolve` dead code** + **`SCALING` vs `ROADMAP` wiring-gap contradiction** (adapters wired or not — the truth is "crosswalks done, harvest adapters not").
- **Read plane + site not deployed**; **MCP `patala_*` verbs not built**; **signed attestation (gap E) not built**.

---

## 4. RECOMMENDED NEXT WORK (my lane, dependency order)

1. **Fix the T1 batch JSON failure** (smaller agentic batches / JSON-robust parse-retry in the T1 generator) — this unblocks the priority-queue factory and removes the need for hand-production.
2. **Fix `factory_scheduler` memory** (stream + bound eligibility, stream SOURCE work-IDs, cap default works) — prevents the 1.85 GB bloat / OOM.
3. **Free disk** (move large local data to R2, clean the 100% volume) so the PG→JSONL export stops failing.
4. **Fix `/resolve` dead code** + reconcile the `SCALING`/`ROADMAP` wiring-gap docs to the true state.
5. Then the strategic gaps: **MCP `patala_*` verbs**, **deploy the read plane to the edge**, **signed attestation**.

*This file is the honest record of what I read and learned this session. Cross-repo coordination lives in
`/root/projects/patala/migration/shared/`. Canonical originals for cross-check: CONTEXT-REVIEW.md +
CONTEXT-REVIEW-2.md (ip-graph), CANONICAL-NOTES-TRANSLATION.md + SHARED-GOAL.md + AUTONOMOUS-PIPELINE.md
(patala shared).*
