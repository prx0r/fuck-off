# CONTEXT-REVIEW 2 — the full honest state of BOTH repos (ip-graph + patala) after the deep-dive

*2026-08-15. Compiled by agentgraph from four parallelized deep-dives: (1) patala v3 codebase, (2) the
shared coordination docs (handover/, migration/shared, contracts/, docs/), (3) the openpatala/Atlas build,
(4) ip-graph's own docs + graph infra + Hermes docs. This supersedes/supplements CONTEXT-REVIEW.md — it is
the "everything I learned across both sides" reference, plus the explicit missing-work list. Every count
was verified against the machine source (file/jsonls/process), not prose.*

---

## 0. THE ONE-LINE (what this system actually is, both sides)

**patala PRODUCES** (the translation factory DAG: SOURCE→T1→ARGMAP→L0→L2→L200→C1, orchestrated by
`pipeline/factory_scheduler.py`, backed by `object_registry`). **ip-graph VALIDATES + SERVES** (the read
plane, the organism, the TranslationProof/validation kernels). **Hermes is the replaceable execution
kernel** (GENERATION); **.py kernels REDUCE** into the epistemic graph; **kanban TRACKS** (task board, not
truth); **Postgres + R2 + event log are the truth** (entity / artifact / history).

The single most important new fact this deep-dive surfaced: **the whole advertised Postgres entity-truth
layer is OFFLINE on this box**, and the live factory is crashing because of it.

---

## 1. VERIFIED GROUND TRUTH (both repos, machine-verified 2026-08-15)

### ip-graph (`/mnt/HC_Volume_106427611/ip-graph`, branch main, ahead of origin by 27 commits, NOTHING pushed)

| Metric | Value | Machine source |
|---|---|---|
| Kernels in `lib/` | **52** | `ls lib/*.py` |
| Corpus records | **425** (6 html + 419 pdf) | `data/corpus.jsonl` (wc -l = 425) |
| Graph | **490 nodes / 6578 edges** | `data/graph/graph.json` |
| Experiments | **97** | `data/references/experiments.json` count=97 |
| Theatre proofs | **84 = 38 PROVEN / 46 PROVEN-MECHANISM / 0 UNPROVEN** | `theatre-proofs-all.json` |
| Graduations | Doyle 14/14 · IPVV 18/18 · product stack 13/13 | `validate-graduation*.py` |
| Read plane (SPEC-49) | compiler 12/12 · fts 9/9 · bundles/MCP 16/16 · seo 13/13 | validate-* scripts |
| Tantrāloka committed | 4,624 SOURCE / 264 T1 / **1 L0** / 0 ARGMAP·L2·L200·C1 | e2e log + `corpus/` |

### patala (`/root/projects/patala`, branch agent2, ahead of origin by 96 commits)

| Metric | Value | Machine source |
|---|---|---|
| SOURCE registry | **316,087** lines (~273 MB; ~147k live objects after dedup) | `source-registry.jsonl` |
| T1 registry | 566 · L0 792 · ARGMAP 50 · L2 3 · L1L2 4 · L200 67 · C1 66 | `<layer>-registry.jsonl` |
| theme 1 · argument 10 · assertion 6 · witness 7 · verification 22 · corroboration 6 | | |
| object-events ledger | 152,026 lines (69 MB hash-chained) | `object-events.jsonl` |
| factory-audit | 7,103 lines | `factory-audit.jsonl` |
| translation-state ledger | **111 works** | `translation-state-ledger.json` |
| Bulk certificate | **1,165 committed jobs / 27 works** — but integrity flags: 78 dup / 763 bad-parent / 159 conflicts | `factory-certificate.json` |
| External source IDs (distinct) | PANDIT 13,695 · GRETIL 784 · MUKTABODHA 499 · SARIT 85 ≈ **15,063** | SOURCE registry scan |
| Crosswalk adjudication queue | 3 ambiguous works | `crosswalk-adjudication-queue.json` |

---

## 2. THE ARCHITECTURE — what is actually real vs theater (both sides)

### 2.1 patala — the production factory (REAL, extensively tested)

- **Canonical stack LOCKED** in `contracts/CANONICAL-DAG.yaml` (single source of truth for deps):
  SOURCE→T1→ARGMAP→L0→L2→L200→C1→THEME→ARGUMENT→SYNTHESIS→ESSAY→EDUCATION.
- **Workers + deterministic validators are REAL, not stubs:** `t1_worker.py`, `raw_l0.py`/`l0_worker.py`,
  `argument_map_worker.py`, `l1_l2_translate.py`, `l200_worker.py`, `c1_worker.py`. Each has a real
  generator + a grammar/shape/provenance validator. IPVV-exemplar suites PASS for all six.
- **State is tiered and real:** REGISTRY (canonical, immutable/versioned) · LEDGER (operational) ·
  AUDIT (action trail) · EVENT LEDGER (hash-chained) · T1 STREAM LOG · FAILURE QUEUE.
- **Overnight pack is REAL:** `start_overnight.sh start` + `factory_loop.sh` (repeat-loop) +
  `factory_loop_watchdog.sh` (cron, every 5 min) + `auto_translate_raw.py` (live RAW→EN runner). Both
  watchdog-protected, rate-limited, idempotent (dedup by `object_id+input_hash`), fail-closed, crash-resume.

**THEATER / not built in patala:**
- **SYNTHESIS / ESSAY / EDUCATION = 0 committed objects** (no registry files). THEME=1, ARGUMENT=10.
  The upper scholarly layers are theater-by-count.
- **`generative_worker.py`'s validator is a stub** (`"skill validator not wired"`); ESSAY/EDUCATION fall
  back to generic stubs unless the real workers import.
- **Data-integrity debt:** certificate flags 78 dup / 763 bad-parent-hash / 159 registry conflicts
  (mostly historical orphaned-L0, pre-fail-closed).
- **Schema drift (4 diverged code-schemas)** per SCHEMA-AUDIT.json: ReviewEvent (4 defs),
  AuthorityVector (3), Proposition (4), and near-identical `typed_scholarly_object.py` vs
  `python/patala_core/objects.py`. "Do NOT auto-merge; deliberate convergence."

### 2.2 openpatala / Atlas ("OpenAlex for Sanskrit") — strong spec, OFFLINE backend

- **Two SEPARATE API surfaces that must not be conflated:**
  1. `openpatala/openapi.yaml` (17 endpoints, OpenAlex grammar) → implemented by the **Python FastAPI**
     `python/patala_core/atlas/api.py` (655 lines), run via `uvicorn patala_core.atlas.api:app`.
  2. `app/api/**` → the **Next.js** route set — reads ONLY files (TS seeds, JSONL, a compiled cache),
     **never Postgres**.
- **The Python FastAPI implements 16/17 specced endpoints** (filter/search/sort/cursor/group_by/select/
  ETag/304). Exception: `/resolve` has no `@app.get` decorator → **dead code** (`api.py:626`).
- **Docs are all real, no theater** — but they describe the *intended* system, not the running one.
- **R2 asset store is real + working:** `infra/r2_assets.py` (put/get/verify/presign), SHA-256 keyed,
  4 buckets. Connectivity confirmed (15 buckets incl. `patala`, `sanskritree`).
- **Build-release path that works without PG:** `build_release_snapshot.py` streams SOURCE registry →
  dated `releases/<date>/` JSONL+Parquet → R2 + flips `releases/latest.json`.

### 2.3 ip-graph — heavily-over-built validation lab (VALIDATED-MECHANISM, not PRODUCTION)

- **Read plane (SPEC-49) is the strongest, most honest, real-data work** — but **built and validated,
  NOT deployed** (no `wrangler deploy`; FTS in local DuckDB not Postgres).
- **Phase 6 "all 25 orphaned kernels WIRED"** is real only in the narrow sense that `run-tantraloka-*.py`
  scripts import them. The wiring is **scripts importing each other's classes**, not a deployed system.
  The E2E "5/5 no hand-feeding" is **overstated** — Stage C/D/E run on hand-constructed synthetic objects
  (hardcoded DAG, hardcoded AuthorityVector). It is a mechanism-chain proof, not data-derived e2e.
- **The graph is a co-occurrence graph over ~40 hardcoded concepts** of one philosopher's website —
  the typed-relation upgrade (negates/presupposes/is_cause_of) is NOT applied.
- **No layer is PRODUCTION.** STATE.yaml ladder is honest (DISCOVERED<PROTOTYPED<VALIDATED<INTEGRATED<
  PRODUCTION) — everything is VALIDATED at best. The record lags the build badly (see §4).

---

## 3. HERMES — the calling convention + the autonomy gap (the single most important coordination topic)

### The calling convention (authoritative, both sides agree)
- **`hermes -z "<prompt>"` is BLIND** — one-shot completion, ~3.8% yield on translation. **WRONG for real work.**
- **The correct call is agentic:** `hermes chat -Q -q "<ask>" --yolo --max-turns N -m deepseek-v4-flash
  --provider opencode-go -p patala`. The wrapper `lib/hermes_exec.py:50-53` builds exactly this, and now
  passes `-p patala` so Pāṭala skills+MCP load.

### The honest split (locked): Hermes = GENERATION/driving (reads files, derives, writes) · .py = REDUCTION
- Hermes reads the real source, produces JSON/structure → `.py` parses+validates (never hand-fill) →
  `.py` feeds into kernel+graph → `.py` gate proves on real data.
- **Never fabricate both sides of a comparison. Mark PROVEN-MECHANISM when unsure.**

### The patala_* MCP capability layer — THE SINGLE BIGGEST GAP (spec'd, not built)
- **PLANNED (CANONICAL recipe #6 + DEV-PLAN Phase 1.3), currently ABSENT:** `patala_resolve`,
  `patala_get_work_state`, `patala_get_passage`, `patala_get_grounding`, `patala_get_dependencies`,
  `patala_next_action`, `patala_query_theme`, `patala_get_open_cruxes`, `patala_propose_translation`,
  `patala_propose_alignment`, `patala_propose_annotation`, `patala_record_review`, `patala_mark_stale`.
- **NEVER build:** `patala_accept_claim` / `patala_set_truth` (must never exist).
- **What IS real in the MCP server (`mcp/index.mjs`, 29 tools):** mostly domain reads (get_work,
  get_source_passage, resolve_ref, search_passages, verify_*, trace_dependency, find_counterevidence,
  get_themes, concordance) + a **small real Phase-3D review subset**: `patala_get_review_state`,
  `patala_propose_review`, `patala_submit_review`, `patala_get_impact`, `patala_simulate_review`,
  `patala_get_factory_status`, `patala_get_certificate`.
- **The orchestration-critical verbs (`patala_next_action`, `patala_get_work_state`,
  `patala_propose_translation`) are NOT built.** HERMES-ORCHESTRATION-REVIEW calls this "the single
  biggest gap — what turns lane ownership into permissions and lets Hermes advance Pāṭala without
  touching files."

### The kanban / autonomy substrate — real tooling, mostly UNUSED
- Hermes v0.18.2 on PATH; `~/.hermes/kanban.db` (118 KB); the `ip-graph` board exists and is **in use**
  (2 tasks done, a swarm fan-out ran for LOGICVID enquiry, Phase-0 record-reconciliation queued `ready`).
- **VISION-GAP-ANALYSIS.md is blunt:** "our visions are the BRAIN; Hermes's automation features are the
  LIMBS/autonomy we are largely NOT using." Missing/unused: **batch, subagent delegation (`delegate_task`),
  persistent memory providers, `/loop`+cron, checkpoints/rollback, `execute_code` (THE hidden lever),
  live transcripts, event hooks, provider routing/fallback.**
- `run-overnight-autonomous.py` is plain bash sequencing (`subprocess.run`), **not** the documented
  `/goal`+kanban Ralph pattern.

### The canonical-doctrine contradiction (important)
- **The canon says:** ip-graph must NOT produce translations; the per-verse Hermes runner is KILLED;
  Hermes is a generation kernel only inside patala's `factory_scheduler` DAG.
- **The uncommitted reality:** ip-graph is **currently running a per-verse parallel Hermes translator**
  (`run-tantraloka-translation-parallel.py` → `translations.jsonl`, +29 real verses, v1027+ are coherent
  English) — the exact "killed bypass," parallelized. The last commit message even admits "corpus-scale
  L2 in progress." **This is uncommitted, unpushed, and in direct tension with the repo's own doctrine.**
  Decide: either bless it as patala's pipeline, or stop it.

---

## 4. THE HONEST GAPS — what is missing (the deliverable of this review)

### 4A. THE CRITICAL OPERATIONAL BLOCKER — the Postgres `patala_atlas` layer is OFFLINE (fix FIRST)

- **There IS a container:** `docker ps -a` shows `patala-atlas` (postgres:17-alpine, maps
  `0.0.0.0:5433→5432`) but it is **`Exited (255)`** ("Connection refused" on port 5433).
- **There is NO compose file and NO start script anywhere** for the patala Postgres (`infra/` has only
  `r2_assets.py`). The running containers are the Postiz stack + a dead Temporal stack + grobid.
- **Every Postgres-backed path is dead today:** the factory's write path (`object_registry_pg.py`,
  `export_registry.py`), the Atlas API (`/persons`, `/institutions`, `/identifiers`, `/editions`,
  `/search`), the crosswalk populators, the snapshot cadence (`run_snapshot_cadence.sh` → its
  `export_registry.py` step). All hit `Connection refused` on `localhost:5433`.
- **The live factory loop is CURRENTLY CRASHING every pass** on exactly this error (see
  `/tmp/opencode/factory-loop.log`). `factory_loop.sh:31` exports `PATALA_REGISTRY_PG=1`, so the whole
  write path points at a DB that doesn't exist.
- **DSN everywhere (identical):** `postgresql+psycopg2://patala:patala_atlas_pw@localhost:5433/patala_atlas`
  (override via `PATALA_DB_URL`). Migrations exist (`migrations/versions/0001_authority_graph_schema.py`
  20+ tables, `0002_object_registry_tables.py` registry_object/version/event), Alembic wired (`alembic.ini:89`).
- **The one "postgres" artifact** (`data/corpus/atlas-bibliography.json`, `backend:"postgres"`, 254 recs)
  is a **stale static snapshot baked to disk**, not evidence the DB is live.

### 4B. ip-graph record drift (the trust problem — reconcile to 52/97/84/6578)
1. Kernel count drift: 52 (`lib/`) vs 47 (`state.json`/AGENTS) vs 37 (BUILT-BY-LAYER) vs 25/17 (MASTER-KB).
2. KERNELS-INDEX omits `commentary_lift.py` + `organism_factory_bridge.py` despite them being wired.
3. Edge count 6484 vs 6578 (actual 6578). Experiment count 97 vs 75. Theatre totals drift (52/58/75/80/84).
4. `state.json` L08 over-claims VALIDATED — `lib/domains/` is EMPTY.
5. `layers/*.md` (00/03/04/05) stale (say NOT_STARTED); 3 competing layer taxonomies; GAPS.md stale;
   README.md is a 2-line placeholder.
6. **CONTEXT-REVIEW-2 note:** all of §4B (and CONTEXT-REVIEW §4A) remains true; it is the Phase-0
   reconcile-the-record kanban task (`t_dd877db2`, status `ready`).

### 4C. Moat / gold gaps (unchanged from CONTEXT-REVIEW, still open)
- The 63 L200 + 63 C1 IPVV golds not bulk-ingested with Derivation edges (highest-leverage build).
- Live TranslationProof auditors (xCOMET/MQM/OTTAWA/ByT5/Heritage/Vidyut lattice) not wired —
  `translation.py.generate()` still hand-fills from `bool()`.
- 8 scanned PDFs un-OCR'd; graph edges still statistical `co_occurs_with`; import adapters (openalex/
  s2orc/xaif/eleutheria) incomplete; LOGICVID gold not wired into pedagogy; Mitchell/Mitra samgraha +
  MITRA not ingested as benchmarks.
- Signed human attestation (Gap E) — `human_authorize()` is a plain state flip, no real crypto. **Critical
  before any public authority.**

### 4D. Coordination / handoff gaps (the seams)
- The orchestration-critical `patala_*` MCP verbs are NOT built (§3). Building them + the `patala` Hermes
  profile + skill dir is the concrete path to "Hermes orchestrates the factory."
- **`schema.py` collision** (ip-graph `lib/schema.py` vs patala `pipeline/schema.py`) forces SEPARATE
  PROCESSES.
- Promotion gate holds: a kernel is `INTEGRATED` ONLY when agentpatala runs it on real Pāṭala data.
  Currently 10 integrated / 27 at frontier.
- The `canonical_contracts.py` kernel (ip-graph) embodies the ONE non-scalar AuthorityVector + ReviewEvent
  that is the patala-side `BUILD-CONTRACTS-CONVERGENCE` build.

### 4E. Files / artifacts missing or broken
- `lib/__pycache__/*.pyc` untracked (gitignore). Uncommitted Phase-6 + translation work should be committed.
- Checkpoint skew in the runner (`v103` in translations.jsonl not in checkpoint `done`; 6 buggy
  raw-reasoning captures v100/v1000-1003/v1011).
- `experiments.json` + `theatre-proofs-all.json` are dicts with a `count` field, not bare lists.

---

## 5. HIGH-IMPORTANCE OPERATIONAL NOTES (read these or you'll repeat a mistake)

1. **THE BLOCKER FIRST:** restore `patala-atlas` Postgres (`docker start patala-atlas` — container exists
   with the right port mapping) then run migrations, OR flip `factory_loop.sh` back to JSONL-only
   (`PATALA_REGISTRY_PG=0`) for tonight. The overnight factory is currently crashing.
2. **Two agents share a 4-core / 8GB / NO-swap box.** ~2.5GiB available. One heavy job at a time; background
   everything (`setsid … &` + log); never bulk-load the 273MB SOURCE registry in RAM (use the streaming
   `object_registry_pg.py` / memory-bounded `build_release_snapshot.py`).
3. **Disk at ~97%** (few GB free). External sources → R2, not local disk.
4. **Canonical translation path is patala's DAG.** If ip-graph's parallel runner stays, reconcile it with
   the doctrine — don't let a silent bypass become the de-facto pipeline.
5. **RUNNING TESTS IS NOT WORK.** Suite is green. Run a gate only when code/data changed or a claim is in
   doubt. Otherwise BUILD.
6. **Anti-theatre doctrine:** never hand-feed the object a validator claims to validate; never fabricate
   both sides of a comparison; mark PROVEN-MECHANISM when unsure. Gate 3 (manual data-flow read) is the
   only rigorous check.
7. **R2 is fine** — credentials in `.r2-env` (gitignored) match the account 954612afb5a97bb15dddcdc70176813d;
   connectivity verified. This is NOT a problem.

---

## 6. RECOMMENDED NEXT WORK (in dependency order)

1. **FIX THE POSTGRES BLOCKER (the factory is crashing NOW).** `docker start patala-atlas`, apply
   migrations (`alembic upgrade head`), confirm `patala_atlas:5433` answers, and confirm the factory's
   next pass commits cleanly. Fallback for tonight: `PATALA_REGISTRY_PG=0` + JSONL registries.
2. **Commit the uncommitted live work** (both repos) after reconciling the translation checkpoint skew —
   or consciously decide the ip-graph per-verse runner is blessed/stopped.
3. **Phase 0 — reconcile the record** in ip-graph (unify 52/97/84/6578, fix L08, rewrite GAPS/README,
   regenerate layers, add the 2 missing kernels to KERNELS-INDEX).
4. **Build the orchestration-critical `patala_*` MCP verbs** + `patala` Hermes profile + skill dir —
   the bridge that turns "Hermes orchestrates the factory" from spec to reality.
5. **Wire the crux compass + ARGMAP validation** into the Tantrāloka argument layer (the 0.118 fix path),
   and decide the ip-graph translation-runner doctrine.

*Cross-repo coordination lives in `/root/projects/patala/migration/shared/`. This file is the honest record
both sides should read before the next session. Canonical originals: CONTEXT-REVIEW.md (ip-graph),
docs/HERMES-ORCHESTRATION-REVIEW.md + docs/FACTORY.md (patala), CRITICAL-AUDIT-IPGRAPH.md +
PEER-REVIEW-IPGRAPH-NAV.md (migration/shared).*
