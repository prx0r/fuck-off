"""lib/translation_variant.py — the three-version translation as scholarship (GEM 5.1).

GEM 5.1 (migration/v2/GEMS.md): "The three-version translation is the scholarship. One translation can
be wrong in ways that look right. Three translations, composed independently, cannot be wrong in the same
way — where they agree is the hard core; where they differ is the interpretation-space; the adjudication
is the commentary."

This kernel: given N independent translations of a source passage, compute:
  - the AGREEMENT CORE (where ≥2 translations agree token-wise) = the hard core
  - the INTERPRETATION SPACE (where they differ) = what the commentary must adjudicate
  - an honest agreement score (a real measure, never a vibe)
The three-version method is the scholarship itself: agreement = the load-bearing core, divergence = the
interpretation-space, adjudication = the commentary (GEM 5.1).
"""
from __future__ import annotations


def _tokens(text):
    return text.lower().split()


class TranslationVariant:
    """Compares independent translations to expose the hard core vs interpretation-space."""

    def __init__(self, passage_id):
        self.passage_id = passage_id
        self.translations = {}     # translator -> text

    def add(self, translator, text):
        self.translations[translator] = text
        return translator

    # ---- agreement: the hard core (where ≥2 translations share the token) ----
    def agreement_core(self, min_agreement=2):
        """Tokens shared by ≥ `min_agreement` translations = the hard core (GEM 5.1)."""
        from collections import Counter
        token_counts = Counter()
        per_tr = {}
        for tr, text in self.translations.items():
            toks = set(_tokens(text))
            per_tr[tr] = toks
            token_counts.update(toks)
        core = {t for t, c in token_counts.items() if c >= min_agreement}
        return {"core_tokens": sorted(core), "n_core": len(core), "per_translation": per_tr}

    # ---- divergence: the interpretation-space (what the commentary adjudicates) ----
    def interpretation_space(self):
        """Tokens NOT in the agreement core (the differing readings)."""
        core = set(self.agreement_core()["core_tokens"])
        space = set()
        for tr, text in self.translations.items():
            space |= (set(_tokens(text)) - core)
        return {"divergent_tokens": sorted(space), "n_divergent": len(space)}

    # ---- agreement score (honest: real, reproducible, not a vibe) ----
    def agreement_score(self):
        """Mean pairwise Jaccard between translations (0..1). 1 = identical, 0 = disjoint."""
        trs = list(self.translations.values())
        if len(trs) < 2:
            return 0.0
        total = 0.0
        pairs = 0
        for i in range(len(trs)):
            for j in range(i + 1, len(trs)):
                a, b = set(_tokens(trs[i])), set(_tokens(trs[j]))
                total += len(a & b) / max(1, len(a | b))
                pairs += 1
        return round(total / pairs, 3)

    # ---- the scholarship: core + space + a commentary recommendation ----
    def analyze(self):
        core = self.agreement_core()
        space = self.interpretation_space()
        score = self.agreement_score()
        return {"passage": self.passage_id,
                "n_translations": len(self.translations),
                "agreement_core": core["n_core"],
                "interpretation_space": space["n_divergent"],
                "agreement_score": score,
                "verdict": "HARD_CORE" if score >= 0.6 else "HIGH_DIVERGENCE"}
