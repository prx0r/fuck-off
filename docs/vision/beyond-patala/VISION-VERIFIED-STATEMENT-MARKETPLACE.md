# VISION — THE VERIFIED-STATEMENT MARKETPLACE (verification as an economic good)

*2026-08-14. Grounded in our validated capabilities: epistemic envelope (knows HOW a claim is known),
mutation-testing (measures verifier strength), signed Merkle roots (tamper-evident), nanopubs
(portable provenance), cross-review (consensus = bias-robust), KG2Code (executable queries).*

---

## THE EMERGENT SYNERGY

We proved three things independently:
1. **Every claim can carry a verifiable epistemic status** (envelope + invariant)
2. **The verifier's own strength is measurable** (mutation-testing kill-rates)
3. **Consensus across independent reviewers is bias-robust** (37.1% bias found in single-reviewer systems)

**The synergy nobody has put together:** if you can *verify* a claim AND *measure how well you verify it*,
then **verification itself becomes a transferable, ownable, productive asset** — not a cost.

---

## THE IDEA

> **A marketplace where the unit of value is a *verifiable statement with a measured verification
> confidence*** — not a document, not a token, but a claim that (a) resolves to evidence, (b) carries an
> epistemic ceiling, (c) has a measured verifier kill-rate backing it, and (d) is signed + time-stamped.

Why this is different from every "knowledge marketplace" that failed:
- Those sold **content** (copies of facts — zero marginal value, instantly replicable).
- This sells **verified status** (the *certification* that a claim survived adversarial review + mutation
  testing + consensus) — which is expensive to produce, hard to fake, and compounding (a certification's
  value grows as more downstream claims build on it).

## THE FLYWHEEL

```
more verification done → more measured verifier strength → higher trust in certifications
        ↑                                                        ↓
  more claims seek certification                     more downstream builds on certified claims
        ↑                                                        ↓
  certification value rises ←────────────────── more demand for verification
```

**Each layer of the flywheel strengthens the next:**
- Verifier strength (mutation kill-rates) is itself a metric that improves with use.
- Every certified claim becomes load-bearing for downstream claims (counterfactual engine), so the
  *installed base* of certified statements is worth more over time.
- Signed roots + temporal validity mean the *history* of certifications is an asset (VISION E: temporal
  scholarship).

## THE FUTURE MOAT (why it matters as AI advances)

As AI agents proliferate and generate infinite content, **the scarce resource is not information — it is
trustworthy, *verified* information.** Models are disposable compute (our founding thesis); verified state
is durable. A system that:
- produces **verifiable** statements,
- **measures** how well it verifies,
- and **compounds** the value of verified statements over time

...becomes the **trust substrate** that agents (and humans) must pay to use. That is a flywheel moat that
gets stronger, not weaker, as AI content floods the world.

## THE NOVEL MECHANISM: "CERTIFICATION WEIGHT"

A concrete mechanism we can build: **a claim's certification weight** that compounds:

```
CW(claim) = verifier_kill_rate × consensus_multiplicity × downstream_load × time_signed
```

- **verifier_kill_rate** — did mutation testing show our verifier would catch corruption of this?
- **consensus_multiplicity** — how many independent reviewers confirmed it (bias-robust)?
- **downstream_load** — how much depends on it (counterfactual engine)?
- **time_signed** — how long has it survived unchanged (temporal validity + signed root)?

Certification weight is **monotonic and compounding** — the longer a claim survives verified, the more
downstream builds on it, the higher its weight. This is a *network-effect moat encoded in the data
itself*.

## WHY START NOW

- The components are all **validated** (envelope, mutation-testing, cross-review, counterfactual,
  signed-root, nanopub) — we're not inventing, we're composing.
- The data will only become more valuable as it accumulates; **every claim we verify today compounds
  tomorrow**.
- It's orthogonal to patala (Sanskrit/philosophy/science) — it works on *any* domain's claims, which is
  exactly the General-Engine bet.

## WHAT TO BUILD NEXT

1. **Certification weight** calculator (`lib/certificate.py`) — the compounding metric.
2. **Verifier-strength ledger** — record mutation kill-rates per claim type (a self-improving verifier).
3. **The certification surface** — expose verified statements via KG2Code queries + nanopub export.

See `docs/vision/VISION-UNCONSIDERED-FRONTIERS.md` (VISION D verifier-as-rival, VISION F system
self-provenance) — this marketplace is where those frontiers become an economic flywheel.
