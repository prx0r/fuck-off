# CANONICAL — TRANSLATION ORCHESTRATION: THE ULTIMATE TRUTH, WHY, AND HOW TO RUN IT

*2026-08-14. The definitive, canonical record of how translation orchestration is SUPPOSED to work in
the integrated Pāṭala + ip-graph system, what actually went wrong (a divergence/shortcut), the full
justification grounded in every relevant file, and the exact commands to run it successfully. Read this
BEFORE touching translation. It supersedes the improvised "per-verse Hermes translation runner" and
resolves the circling.*

---

## 0. TL;DR — THE ONE-LINE

> **Run the existing deterministic Python DAG controller (`pipeline/factory_scheduler.py`) on the
> Tantrāloka work. It produces the argument-guided translation in canonical dependency order
> (T1 → ARGMAP → L0 → L2 → L200 → C1), batches model calls, uses Hermes only as the generation kernel,
> and commits versioned, validated objects to the registry. Do NOT call Hermes once per verse via a
> bespoke runner.**

---

## 1. THE ULTIMATE TRUTH (established by 3 parallel audits + the canonical docs)

### 1.1 Hermes is the EXECUTION KERNEL, not the orchestrator

`handover/hermes/CANONICAL.md` is the canonical and final statement:

> "Hermes schedules and executes epistemically permitted transformations; it **never determines what
> Pāṭala knows**." (line 7-8)
> "**Kanban = scheduler, not constitution.**" (line 54)
> "There are TWO DAGs" ... Hermes execution DAG ≠ Pāṭala epistemic DAG. "These are not interchangeable."
> (`handover/hermes/hermespatala-architecture-review.md`)

### 1.2 Eligibility/orchestration is DETERMINISTIC PYTHON, never an LLM judgment

Even the plan's own review (`hermespatala-architecture-review.md`) is explicit:

> "Hermes shouldn't even decide what's eligible ... Eligibility should be ordinary code
> (`eligible_for_l200(x)`), **not an LLM judgment**." (lines 142-144)

The refined architecture is:
```
HERMES CRON (no-agent) → patala-controller tick → read registries →
deterministically compute eligibility → claim bounded jobs →
invoke Hermes ONLY where cognition is required
```

**`pipeline/factory_scheduler.py` IS that deterministic controller.** It was built correctly and already
works (verified: `--queue` enumerates 160,425 eligible model jobs across 196 works, including Tantrāloka
at p39).

### 1.3 ip-graph never superseded patala's factory

Every ip-graph spec says the opposite:
- `devplans/MASTER-INTEGRATION-DEVPLAN.md:5-7` — "patala has the mature TRANSLATION FACTORY ... **never
  rebuild, always integrate.**"
- `MASTER-INTEGRATION-DEVPLAN.md:23` — "**patala PRODUCES translations/proofs/commentaries; ip-graph
  VALIDATES + SERVES them.**"
- `devplans/TRANSLATION-PRODUCTION.md:82-84` — "patala PRODUCES (the factory workers + Hermes). I
  VALIDATE (TranslationProof + commentary_lift + three-version + scholar_review)."

### 1.4 The SOURCE→L2 direct runner is an UNPLANNED DIVERGENCE (the bug)

`scripts/run-tantraloka-translation.py` + `scripts/run-tantraloka-translation-parallel.py` read the
SOURCE objects then call `agentic()`/`translate_karika()` directly to produce L2, bypassing
T1→L0→ARGMAP→L2. This:
- Violates the canonical DAG (`contracts/CANONICAL-DAG.yaml`: L2 requires L0 AND ARGMAP).
- Violates the "patala PRODUCES, ip-graph VALIDATES+SERVES" seam.
- Was a stopgap improvised because the factory lagged on Tantrāloka (MASTER gap #1: "Machine L200/C1 at
  corpus scale ... hand-authored, not machine").
- No ip-graph spec authorizes it. It contradicts ip-graph's own "reuse don't rebuild" doctrine.

It is also WHY the output was poor: skipping ARGMAP means no argument guide, so the gloss scored 0.118
vs Dyczkowski (`tantraloka/GOLD-STANDARD-INSIGHTS.md`) — a structural miss, not a model failure.

### 1.5 The real divergence to kill: parallel orchestrators

ip-graph built its own `lib/next_action.py`, `lib/factory_pool.py`, `lib/ingestion_organism.py` — a
parallel orchestration layer that duplicates patala's `factory_scheduler.py`/`corpus_state`. This is the
"shadow task system" `specs/SPEC-09-AGENT-ORCHESTRATION-SURVEY.md` warns against. The named conflict is
the `schema.py` collision (separate-process rule); the unlabeled one is this orchestrator overlap. The
long-term fix is to route ip-graph's organisms THROUGH patala's scheduler, not alongside it.

---

## 2. FULL JUSTIFICATION (every relevant file)

### 2.1 The canonical DAG (the contract)
- `contracts/CANONICAL-DAG.yaml` — the single source of truth for layer dependencies:
  `SOURCE → T1 → ARGMAP → L0 → L2 → L200 → C1 → THEME → ARGUMENT → SYNTHESIS → ESSAY → EDUCATION`.
  - ARGMAP requires `[SOURCE, L0]` (lateral guide).
  - **L2 requires `[L0, ARGMAP]`** — "readable prose guided by the argument map, over the token floor."
  - This is the ARGUMENT-GUIDED translation the IPVV build used.

### 2.2 The orchestration machinery (already built, correct)
- `pipeline/factory_scheduler.py` — the DAG-based backlog scheduler ("the corpus OS"). Enumerates ALL
  eligible (object, layer) jobs, drains deterministic L0 free, ranks model jobs, batches per-work,
  parallelizes chunks, commits serially. Multi-parent eligibility (L2 needs L0 AND ARGMAP).
  - Env: `PATALA_CONTEXT` (default 1000000), `PATALA_INPUT_FRAC` (0.5), `PATALA_FACTORY_BATCH_MAX`
    (1000), `PATALA_FACTORY_CHUNK` (50), `FACTORY_PARALLEL` (4).
  - Args: `--max-model-calls` (default 6), `--throttle`, `--works`, `--per-layer`, `--layers`,
    `--retry`, `--queue`.
- `pipeline/factory_batch.py` — orchestrates T1→ARGMAP→L0→L2→L200→C1 over committed SOURCE, fails
  closed on missing dependencies, reuses the real workers. CLI: `--work`, `--count`, `--layers`,
  `--retry`.
- `pipeline/object_registry.py` — the versioned canonical state; `registry = truth`. Atomic writes,
  single-writer lock, append-only hash-chained ObjectEvent ledger.
- `pipeline/corpus_state.py` — Agent 2's translation-state ledger + `next_valid_action` control plane.
- The workers: `pipeline/{t1_worker,l0_worker,argument_map_worker,l1_l2_worker,l200_worker,c1_worker}.py`.
  - `argument_map_worker.py` — produces the 4-section ARGMAP (what_is_at_issue / argument_steps /
    open_items / decision_for_l2). **This is the argument guide that unlocks L2.**
  - `l200_worker.py` + `translations/_stack/ipvv/l200/README-L200-SPEC.md` — the frozen 8-section
    derivational audit (the moat).
  - `c1_worker.py` + `translations/_stack/ipvv/c1/C1-SPEC.md` — the frozen passage commentary.

### 2.3 The Hermes integration (why Hermes is only the generation kernel)
- `handover/hermes/CANONICAL.md` — Hermes = execution kernel; kanban = scheduler not constitution.
- `docs/global/HERMES-CALLING.md` — call Hermes as an AGENT (`hermes chat`), never blind `-z` for file
  work.
- `pipeline/model.py` — `model.py` shells out to Hermes purely for the model call; all Pāṭala logic
  stays in Python. `chat_agentic()` = the correct agentic invocation.
- `pipeline/batch_translate.py` — the batch unit: ONE call, MANY verses + the term-context packet, with
  deterministic F4 verification (sha256 echo + membership + no-dupe). **This is the speed the factory
  uses** — not per-verse calls.

### 2.4 ip-graph's role (validator + server, NOT a second producer)
- `devplans/MASTER-INTEGRATION-DEVPLAN.md` — the integration seam.
- `devplans/TRANSLATION-PRODUCTION.md` — the translation moat (validate patala's output).
- `specs/SPEC-16-PATALA-TRANSLATE.md` — the proof-carrying translation spec; the verifier is the moat.
- ip-graph kernels that VALIDATE (reuse, not rebuild): `lib/{translation,translation_variant,
  commentary_lift,proof_generators,scholar_review,integrity_gate,evidence_ledger}.py`.

### 2.5 The audit findings that prove this is the right path
- `ip-graph` self-audit (SPEC-16 review): "Translation: REAL; Proof object + gate: real machinery;
  **Audit dimensions: ~2/11 real** (rest hand-filled)." — the moat is mechanism-only until the verifier
  computes real evidence.
- IPVV already ran the real argument-guided path: **49 real ARGMAP objects** in the registry
  (verified via `object_registry`). kramasadbhava is the most complete vertical (L0 96 → ARGMAP 1 →
  L200 3).

---

## 3. WHY THIS (vs the alternatives) — the decision logic

| Approach | Verdict | Reason |
|---|---|---|
| **Per-verse Hermes runner (the shortcut)** | ✗ KILLED | Bypasses the DAG, no ARGMAP → poor (0.118), no registry commit, no validation, ~42h |
| **Hermes kanban drives the factory** | ✗ Rejected by design | Hermes = scheduler, not constitution; eligibility must be deterministic Python |
| **ip-graph's own factory_pool/next_action** | ✗ Divergence | Duplicates patala's scheduler = shadow task system |
| **`factory_scheduler.py` on Tantrāloka** | ✓ THE ANSWER | Deterministic DAG controller, argument-guided (ARGMAP), batched, versioned, validated, reuses real workers |

**Why it's the answer:** it is the single source of truth (the canonical DAG), already built and
verified, does argument-guided translation (the missing piece that fixes the 0.118), batches for speed,
uses Hermes only as the generation kernel (per CANONICAL.md), and commits real versioned objects. It is
exactly what IPVV actually used.

---

## 4. HOW TO RUN IT SUCCESSFULLY (the exact commands)

### 4.1 Prerequisites (verify before running)
```bash
cd /root/projects/patala
# 1. Hermes gateway must be up (the generation kernel)
ps -eo pid,cmd | grep "hermes.*gateway" | grep -v grep
# 2. The Tantrāloka SOURCE must be committed + verse-recoverable (verified: yes)
python3 -c "import sys; sys.path.insert(0,'pipeline'); import factory_scheduler as F; \
print('tantraloka', 'tantraloka' in F._registered_works(), '| verse ok', bool(F._verse_for('tantraloka:v100')))"
# 3. No factory loop / overnight already running (avoid collision — RAM + model budget)
ps -eo pid,cmd | grep -E "factory_loop|factory_scheduler|start_overnight" | grep -v grep
```

### 4.2 The dry-run / queue preview (READ-ONLY — shows what the scheduler WILL do)
```bash
python3 pipeline/factory_scheduler.py --works tantraloka --queue
```
Expected: `tantraloka` listed, `-> T1` (then ARGMAP, then L0 after T1 commits, then L2 after both, etc.).

### 4.3 ONE DAG pass, scoped to Tantrāloka, RAM-safe (the recommended first real run)
```bash
cd /root/projects/patala
setsid nohup env FACTORY_PARALLEL=3 \
  python3 pipeline/factory_scheduler.py \
  --works tantraloka \
  --max-model-calls 6 \
  --throttle 1 \
  > /tmp/opencode/tantraloka-factory-dag.log 2>&1 &
echo "PID: $!"
```
- `FACTORY_PARALLEL=3` — the RAM-safe concurrency on the 4-core / 8 GB / 2-agent box (AGENTS.md §3.4a).
  Never unbounded.
- `--max-model-calls 6` — one pass spends 6 model calls (the batch worker fills each with many verses).
- `--throttle 1` — gentle pacing, shared with the second agent.
- It will produce T1 first, then (next passes) ARGMAP → L0 → L2 → L200 → C1 in dependency order.

### 4.4 To advance ALL layers to completion (repeat passes, or run factory_batch on a work)
The scheduler advances a bounded number per pass. To drive a work through the whole spine:
```bash
# After T1+ARGMAP+L0 commit for the target, run the batch CLI over the full layer set:
python3 pipeline/factory_batch.py --work tantraloka --count 4 --layers T1,ARGMAP,L0,L2,L200,C1
```

### 4.5 The overnight autonomous loop (the "translate while I sleep" — canonical end-state)
```bash
bash pipeline/start_overnight.sh start       # installs cron watchdogs + runs the factory loop
bash pipeline/start_overnight.sh status      # show what's running
bash pipeline/start_overnight.sh stop        # stop the factory loop (leave live runner)
# See pipeline/OVERNIGHT.md for the full runbook + morning checklist.
```
*Note: `AUTOTRANSLATE-NORTHSTAR.md` records that Hermes (the agent runtime) was hanging/unreliable on
this box; the deterministic substrate + scheduler do NOT need the Hermes kanban layer. If the overnight
loop stalls, the deterministic `factory_scheduler` path is the fallback that still works.*

### 4.6 Monitoring (do NOT block on it — background + check back, per AGENTS.md §3.1)
```bash
tail -f /tmp/opencode/tantraloka-factory-dag.log
python3 pipeline/object_registry.py   # watch T1/ARGMAP/L0/L2/L200/C1 counts grow
```

### 4.7 Success criteria (what "done" means, anti-theatre)
- `object_registry` shows committed (non-superseded) Tantrāloka objects at T1, ARGMAP, L0, L2, L200, C1.
- The ARGMAP `decision_for_l2` objects exist (the argument guide — the piece the shortcut skipped).
- The L2 was produced GUIDED BY the ARGMAP (DAG eligibility enforces this).
- Each committed object passed its validator (fail-closed; nothing partial commits).
- ip-graph then VALIDATES the output with `lib/translation.py` (TranslationProof) + `translation_variant`
  (three-version vs Dyczkowski) — per the seam, ip-graph does NOT re-produce.
- The gold comparison improves vs the 0.118 shortcut result, because the ARGMAP now supplies the
  philosophical frame (GOLD-STANDARD-INSIGHTS fix).

---

## 5. THE CARRY-FORWARD (what was decided, permanently)

1. **TRANSLATION ORCHESTRATION = `factory_scheduler.py` (deterministic Python DAG controller).**
   Not a per-verse Hermes runner; not Hermes-kanban-as-constitution; not ip-graph's parallel organisms.
2. **ARGUMENT-GUIDED** — L2 is produced only after L0 + ARGMAP commit (canonical DAG). This is how IPVV
   was built (49 ARGMAP objects) and is the fix for the 0.118 gloss.
3. **HERMES = generation kernel only** (per CANONICAL.md). Batch calls (`batch_translate.py`), never
   per-verse.
4. **ip-graph = VALIDATOR + SERVER** (TranslationProof, three-version, read plane). It does NOT produce
   translations.
5. **Kill the divergences**: retire the per-verse runner; route ip-graph's organisms through patala's
   scheduler, keep the two `schema.py` in separate processes.

---

## Proofs / resolution (everything above resolves)
- The canonical DAG: `contracts/CANONICAL-DAG.yaml`
- The controller: `pipeline/factory_scheduler.py`, `pipeline/factory_batch.py`
- The registry: `pipeline/object_registry.py`, `pipeline/corpus_state.py`
- The workers: `pipeline/{t1,l0,argument_map,l1_l2,l200,c1}_worker.py`
- The Hermes thesis: `handover/hermes/CANONICAL.md`, `hermespatala-architecture-review.md`,
  `docs/global/HERMES-CALLING.md`, `pipeline/model.py`
- The integration seam: `devplans/MASTER-INTEGRATION-DEVPLAN.md`, `devplans/TRANSLATION-PRODUCTION.md`
- The proof spec: `specs/SPEC-16-PATALA-TRANSLATE.md`
- The gold insight: `tantraloka/GOLD-STANDARD-INSIGHTS.md`
- The runner (superseded): `scripts/run-tantraloka-translation.py`,
  `scripts/run-tantraloka-translation-parallel.py` (KILLED — do not resurrect)
- The overnight loop: `pipeline/start_overnight.sh`, `pipeline/OVERNIGHT.md`, `pipeline/factory_loop.sh`
