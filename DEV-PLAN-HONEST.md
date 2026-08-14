# DEV PLAN — the honest, sober path forward

*2026-08-14. A realistic dev plan grounded in what actually exists (verified, not aspirational). The
machine is over-built in breadth (37 kernels) and under-built in depth (only ONE claim proven end-to-end
on real IPVV). This plan is about closing the depth gap, not adding more breadth.*

---

## THE HONEST STATE (verified)

**What's real:** 37 kernels, 75/75 tests, 35 proofs on real data, 48 cloned repos, full traceability,
read plane built, IPVV graduation 18/18 (one claim).

**What's NOT real (the gap):**
1. **The corpus-wide IPVV run** — we proved ONE claim (IPK 1.5.19) end-to-end. The whole point was the
   corpus. Not done.
2. **The organism layer (L09) is mechanism-proven, not production-integrated.** `education`, `pedagogy`,
   `organism`, `organism_loop`, `agent_delivery`, `evolve` are synthetic — the real learner/consumer data
   doesn't exist yet.
3. **Gaps A-E are all DISCOVERED** — context paging, execution branching, deterministic replay,
   content-addressed run-traces, signed human attestation. None wired.
4. **The 3 v3 needs-build products** — Commentary, live Tokenization (vidyut cheda), Essay projection.
5. **GAPS.md is stale** — it claims "no projection compiler / no surfaces / no retrieval," all of which
   are now built. The docs lag the code.

---

## THE REAL PROBLEM (not "build more")

> **We have a beautifully-proven machine and almost no real data running through it.** The 75 passing
> validators prove mechanisms on curated inputs. The organism's value only materializes when real IPVV
> text, real learners, and real consumer probes flow through it at corpus scale.

So the plan is: **STOP adding kernels. WIRE the real corpus.**

---

## THE PLAN (priority-ordered, depth over breadth)

### PHASE 1 — THE MONA LISA: Tantrāloka from scratch, the canonical full-stack test — HIGHEST VALUE
Replace the single-claim IPVV proof with a **real, large, philosophically-loaded text through the whole
organism, from scratch, then validated against the established translation**.

**The target: Tantrāloka (Abhinavagupta).** Sources already on disk:
- **Sanskrit root** (translate from THIS, not the English): `gretil_tantraloka.txt` — 17,684 lines, the
  Kashmir Series 1918-38 edition via GRETIL/Takashima, clean `AbhT_1.1` kārikā refs + Jayaratha's Viveka.
- **Dyczkowski's translation** (validation reference, not the source): all 11 volumes
  `tantraloka-vol{1..11}-dyczkowski.txt`.

**The test:**
1. Ingest the root → SOURCE → L0 (vidyut) → TranslationProof → Commentary → Argument (our kernels, no
   reading Dyczkowski).
2. Translate a flagship āhnika from scratch (Āhnika 1: upāyas, reflexivity, prakāśa/vimarśa, the three
   means, recognition — connects to the IPVV/thesis).
3. Compile products → bundles → Astro → MCP (the full read plane).
4. **Validate vs Dyczkowski** (three-version method, GEM 5.1): agreement = hard core, divergence =
   interpretation-space for the commentary to adjudicate. The IPVV connection makes this the apex test.

**Why:** the IPVV graduation proved the mechanism on ONE claim; Tantrāloka proves it on a real large text,
connects to Abhinavagupta + recognition (the thesis), and has the richest existing pushing material
(`research-library/recognition/pushing-tantraloka/`). This is the canonical "does the organism actually
work" test.

### PHASE 2 — fix the docs-to-code lag (cheap, unblocks trust) — DO THIS WEEK
- **Update GAPS.md** — it claims the read plane doesn't exist; it does. Resync to `BUILT-BY-LAYER.md`.
- **Fix the 3 stale counts**: the state docs reference 55/55 and 63/63; reality is 75/75, 37 kernels.
- Rationale: a new agent reading the stale GAPS will rebuild what exists. This is pure waste.

### PHASE 3 — close the two security-critical gaps (E + A) — before any marketplace
- **Gap E: signed human attestation** — replace plain `human_authorize()` with a cryptographic
  `HumanAttestation{actor, action, target_revision, scope, timestamp, signature}`. Critical before the
  Verified-Statement-Marketplace is real. We have `system_provenance.py` (cosign-style signing) — reuse it.
- **Gap A: context paging** — lossless context virtualization over the compiled bundles.
- **Gap B/C/D: execution branching + deterministic replay + content-addressed run-traces** — these exist
  as experiment scripts; promote them to wired kernels in `agent_delivery`.

### PHASE 4 — build the 3 v3 needs-build products (the real content gaps)
- **Commentary** (passage-local) — the missing spine step between TranslationProof and Argument.
- **Live Tokenization** — wire vidyut cheda (it's installed + data on disk at `/root/vidyut-0.4.0`).
- **Essay projection** — the reactive-essay mechanism is proven; compile the projection compiler output.

### PHASE 5 — get real consumer data (the organism's fuel)
The misconception flywheel, pedagogy, and organism_loop are all built but data-starved. The plan:
- Stand up the read plane (Astro/Workers/MCP) so real learners can actually interact.
- Instrument real interactions → `MisconceptionGraph` → the repair cascade.
- This is the ONLY way L09 becomes production-real, and it requires the surfaces from Phase 1/4.

---

## WHAT TO PRIORITIZE (the honest answer)

| Priority | Why |
|---|---|
| **1. THE MONA LISA — Tantrāloka from scratch** | the canonical full-stack test on a real large text, then validated vs Dyczkowski |
| **2. Docs-to-code resync** | cheap, unblocks trust + prevents rebuild waste |
| **3. Gap E (signed attestation)** | security-critical, blocks the marketplace vision |
| **4. Gap A (context paging)** | the agent read-plane is incomplete without it |
| **5. The 3 needs-build products** | the real content gaps (Commentary/Tokenization/Essay) |
| **6. Real consumer data** | the organism's fuel; requires surfaces to be live |

---

## THE SOBER ONE-LINE VERDICT

> The machine is over-proven and under-fed. **76 validators prove a machine, not a corpus.** The honest
> next step is NOT another kernel — it's running **Tantrāloka from scratch** through the whole organism
> (ingest the Sanskrit root → L0 → TranslationProof → Commentary → Argument → products), then validating
> the result against Dyczkowski (three-version: agreement = hard core, divergence = interpretation-space).
> That's the canonical proof the organism actually works on a real text. Then resync the docs, close the
> two security gaps, and get real consumer data so the teaching layer stops being mechanism-only.

## Proofs / resolution
- What's built: `BUILT-BY-LAYER.md`, `KERNELS-INDEX.md`, `COHERENCE-AUDIT.md`
- What's not: `STATE.yaml` (gaps A-G all DISCOVERED), `GAPS.md` (stale), `TODO.md`
- **The Mona Lisa sources:** Sanskrit root `gretil_tantraloka.txt` + Dyczkowski vols 1-11 (both on disk)
- The milestone proof: `scripts/validate-graduation-ipvv.py` (18/18, ONE claim) — needs widening to corpus
