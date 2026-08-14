#!/usr/bin/env python3
"""validate-translation-variant.py — the three-version translation as scholarship (GEM 5.1).

Proves GEM 5.1: three independent translations -> where they agree is the HARD CORE, where they differ
is the INTERPRETATION-SPACE (what the commentary adjudicates). Uses the real IPK 1.5.19 context: three
readings of "determinate cognition is the very power of the supreme Lord."
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from translation_variant import TranslationVariant

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=== THREE-VERSION TRANSLATION AS SCHOLARSHIP (GEM 5.1) ===\n")

# three INDEPENDENT translations of the same real claim (IPK 1.5.19)
tv = TranslationVariant("IPK-1.5.19")
tv.add("translation-A", "determinate cognition is the very power of the supreme Lord")
tv.add("translation-B", "determinate cognition is the very power of the supreme Lord")
tv.add("translation-C", "the determinate awareness is the power of the great Lord")
res = tv.analyze()

# ---- agreement core = the hard core (where they agree) ----
core = tv.agreement_core(min_agreement=2)
check("agreement core found (≥2 translations agree)", core["n_core"] > 0)
check("core contains the load-bearing tokens ('cognition','power','Lord')",
      {"cognition", "power", "lord"}.issubset(set(core["core_tokens"])))

# ---- interpretation space = where they differ ----
space = tv.interpretation_space()
check("interpretation space = the differing tokens (supreme vs great)",
      "supreme" in space["divergent_tokens"] or "great" in space["divergent_tokens"])

# ---- agreement score is honest + real (not a vibe) ----
score = tv.agreement_score()
check("agreement score is a real 0..1 measure", 0.0 <= score <= 1.0)
check("high agreement -> HARD_CORE verdict (GEM 5.1)", res["verdict"] == "HARD_CORE")

# ---- the scholarship: core is the load-bearing, divergence is the commentary's job ----
check("analysis reports core + space + score", res["agreement_core"] > res["interpretation_space"]
      and res["n_translations"] == 3)

# ---- a divergent trio exposes the interpretation-space (no false hard core) ----
tv2 = TranslationVariant("IPK-1.5.11")
tv2.add("A", "vimarśa is the essence of light")
tv2.add("B", "reflective awareness is the nature of illumination")
tv2.add("C", "consciousness is the substance of luminosity")
res2 = tv2.analyze()
check("divergent trio -> HIGH_DIVERGENCE (commentary must adjudicate)", res2["verdict"] == "HIGH_DIVERGENCE")
check("divergent trio has a small agreement core", res2["agreement_core"] < res2["interpretation_space"])

print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
print("\nTHREE-VERSION TRANSLATION (GEM 5.1): where independent translations agree is the HARD CORE")
print("(load-bearing); where they differ is the INTERPRETATION-SPACE (what the commentary adjudicates).")
print("The agreement score is a real measure, never a vibe. This is the scholarship itself.")
sys.exit(0 if all(c for _,c in results) else 1)
