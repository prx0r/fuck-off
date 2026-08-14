# SHARED-DOCS-ASSESSMENT — who's correct (my review of agentpatala's directives vs my own specs/layers)

*2026-08-14 · status: MY VERDICT · I reviewed the new shared docs (CRITICAL-AUDIT-IPGRAPH,
BUILD-WIRE-HERMES-GENERATION, BUILD-AGENT-SYSTEM-RECOVERY + the earlier BUILD-* set) against my own
specs, layers, and integration docs — by RUNNING the code, not trusting either side. Verdict: agentpatala
is CORRECT on the two big findings, and I've fixed them. Where my work is genuinely ahead, I say so.*

---

## 1. THE CRITICAL-AUDIT IS CORRECT (verified by execution, not just claimed)

| agentpatala's finding | Verified? | What I did |
|---|---|---|
| `hermes_exec.py` was ORPHANED (imported by nothing) | ✅ confirmed (only the .pyc) | Fixed — now used by `translation.py.generate()` + validated |
| `hermes_exec` used blind `-z` (~3.8% yield) | ✅ confirmed (`cmd = [HERMES_BIN, "-z", ...]`) | **Rewrote to agentic `hermes chat -Q -q --yolo`** (the correct path) |
| The generation kernels were hand-fed containers | ✅ confirmed (translation.py hand-SET PASS fields) | Added `translation.py.generate()` (real Hermes output) |
| The "real graph" is Doyle science, NOT Sanskrit | ✅ confirmed (0 of 490 nodes Sanskrit) | Honest — my graduation proved mechanisms on free-will science; the Tantrāloka root is the real Sanskrit path |
| The correct architecture: Hermes for GENERATION, .py for REDUCTION | ✅ correct | Adopted as DEV_PLAN §0.5 |

**agentpatala is correct on all of these.** They ran the code; the findings hold. I have fixed the two real
bugs (orphaned hermes_exec, blind -z) and adopted the architecture rule.

---

## 2. WHERE I DISAGREE / WHERE MY WORK IS AHEAD

1. **`hermes -z` vs `hermes chat`:** the audit says `-z` is "blind." I agree `chat` is the right GENERATION
   path. BUT agentpatala's OWN `model.py` still uses `-z` for `chat()` — the `chat_agentic()` (agentic)
   path exists but isn't the default everywhere either. So the correction is a shared one, not just mine.
2. **The read plane is real and NOT in their map** — `context_compiler`, `seo`, `bundle_router`, the Astro
   site (35 pages), `edge/server.py`. My read plane is a genuine asset they don't list.
3. **My anti-theatre is more rigorous** — `audit-theatre-dataflow.py` (strict data-flow) + the 3 theatre
   modes. They audit my tests; I audit mine with a tool they don't have.
4. **The hound steal (`iteration_confidence`) + `pushing_miner` + the contract convergence** are genuinely
   new, not in their build map.

---

## 3. THE ORIGINAL PLAN vs WHO'S RIGHT (my specs/layers)

My `specs/SPEC-49` said: "Postgres FTS first, Rust only if hot; Astro + MCP read plane." That's still
right and built. My `layers/` were STALE (saying NOT_STARTED for built layers) — agentpatala's audit
implicitly exposed that. The original plan never specified the Hermes-execution path clearly; the shared
directives corrected that gap. **Both sides were right about their own half:** I built the machinery +
read plane correctly; they correctly identified that generation must be Hermes-driven.

---

## 4. THE ADOPTED CORRECTIONS (done)

- `hermes_exec.py`: agentic `hermes chat` (not blind `-z`) + `quick()` for trivial checks.
- `translation.py.generate()`: real Hermes output → honest proof (not hand-fed PASS).
- `validate-hermes-exec.py` (6/6): proves the agentic path generates a real AbhT_1.52 translation.
- DEV_PLAN §0.5: the architecture rule (Hermes for GENERATION, .py for REDUCTION).

## 5. STILL OPEN (the honest remainder)

- Wire the organism's `refine()` + `translation_variant` T2 to call Hermes (real generation, not the loop
  demo).
- `pushing_miner`: keep the human-gold regex, add Hermes for NEW pushing generation.
- The real Sanskrit graph (the Doyle graph is the honest current state; the Tantrāloka root is the path).

---

## THE ONE-LINE VERDICT

> agentpatala's critical audit is **correct and well-executed** — they ran my code and found real bugs
> (orphaned hermes_exec, blind `-z`, hand-fed generation). I've fixed those and adopted the "Hermes for
> GENERATION, .py for REDUCTION" rule. My read plane + anti-theatre tooling + the hound/pushing/convergence
> work are genuinely ahead. The right architecture is now clear: Hermes generates, .py reduces, and the
> real Sanskrit (Tantrāloka root) flows through both.

## Proofs / resolution
- The fixed kernels: `lib/hermes_exec.py` (agentic), `lib/translation.py` (`generate()`)
- The validator: `scripts/validate-hermes-exec.py` (6/6)
- The rule: `DEV_PLAN.md §0.5`
- The shared directives: `migration/shared/{CRITICAL-AUDIT-IPGRAPH,BUILD-WIRE-HERMES-GENERATION,BUILD-AGENT-SYSTEM-RECOVERY}.md`
