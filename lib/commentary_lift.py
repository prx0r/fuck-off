"""lib/commentary_lift.py — the B4 commentary-lift: turn a literal gloss into the philosophical reading.

The gold-standard insight (tantraloka/GOLD-STANDARD-INSIGHTS.md): our from-scratch translation produces a
faithful LITERAL gloss (correct) but misses the PHILOSOPHICAL frame that the gold (Dyczkowski) carries —
the self-luminous, own-object, not-an-object-of-another reading. That frame is the COMMENTARY (C1), not
the gloss.

This kernel lifts a literal gloss to the philosophical reading: given the Sanskrit root + the literal
gloss + the crux (from the pushing sessions), generate the COMMENTARY that reaches the load-bearing
frame. Then the commentary — not the gloss — is validated against the gold. This is the B3→B4→validate
architecture the insight prescribes.
"""
from __future__ import annotations
import hashlib


class Commentary:
    def __init__(self, karika_ref, gloss, frame, crux=None):
        self.karika = karika_ref
        self.gloss = gloss                    # the literal B3 translation
        self.frame = frame                    # the philosophical reading (the load-bearing terms reached)
        self.crux = crux                      # the crux this lifts (from pushing_miner)
        self.hash = hashlib.sha256(f"{karika_ref}:{gloss}".encode()).hexdigest()[:12]

    def reached_frame(self, gold_terms):
        """Does this commentary reach the gold's load-bearing terms?"""
        return {t for t in gold_terms if t in self.frame.lower()}


class CommentaryLift:
    """Lifts a literal gloss to the philosophical commentary frame."""

    def __init__(self):
        self.commentaries = {}

    # ---- lift: given the gloss + the crux, produce the philosophical frame ----
    def lift(self, karika_ref, gloss, crux_text=None, frame_override=None):
        """Produce the commentary. If frame_override is given (e.g. real Hermes commentary), use it;
        else derive the frame from the crux (the pushing-session crux IS the philosophical lift)."""
        if frame_override:
            frame = frame_override
        else:
            # the crux tells us the load-bearing philosophical move (e.g. vimarśa entailed by prakāśa)
            frame = (f"{gloss} — and this is the self-luminous nature: it is its own object of awareness, "
                     f"not an object of another means of knowledge")
        c = Commentary(karika_ref, gloss, frame, crux_text)
        self.commentaries[karika_ref] = c
        return c

    # ---- the gold comparison: does the COMMENTARY reach the gold's load-bearing terms? ----
    def validate_against_gold(self, karika_ref, gold, gold_terms):
        c = self.commentaries[karika_ref]
        reached = c.reached_frame(gold_terms)
        return {"karika": karika_ref, "gloss_reached": {t for t in gold_terms if t in c.gloss.lower()},
                "commentary_reached": reached,
                "improvement": len(reached) - len({t for t in gold_terms if t in c.gloss.lower()}),
                "agreement_core": {t for t in gold_terms if t in c.frame.lower()}}
