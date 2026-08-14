"""lib/pedagogy.py — the live adaptive pedagogy engine (the education motherlode).

From the education vision (SPEC-29 + educationmain): Pāṭala places the learner INSIDE the evidential
structure, then records what they can reconstruct/discriminate/manipulate/transfer/ground.

The architecture (absurdly coherent — one graph becomes scholarship/benchmark/education/tutoring/media):
  learner answer = a tiny EPISTEMIC EVENT (MasteryEvidence)
  → LearnerState is DERIVED via a reducer (like ReviewEvent[] → DerivedState)
  → three graphs (epistemic + pedagogical + learner) → NEXT INTERACTION
  → every interaction has what_it_tests + answer provenance (proof-carrying multiple choice)
  → scholarly correction regenerates questions safely (dependency propagation)

Live adaptive pedagogy: ask "what cannot this learner currently do?" not "what lesson is next?"
Content and skill are separate axes (a learner can know Abhinavagupta but be bad at argument reconstruction).
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

# ---- the evidence hierarchy (levels of demonstrated understanding) ----
EVIDENCE_LEVELS = ["E0_RECALL", "E1_RECOGNIZE", "E2_DISCRIMINATED", "E3_RECONSTRUCTED",
                   "E4_TRANSFERRED", "E5_GROUNDED"]

# ---- the interaction operators (finite powerful set) ----
OPERATORS = ["LOCATE_SOURCE", "IDENTIFY_PROPOSITION", "WRONG_SPEAKER", "TERM_DISCRIMINATION",
             "MISSING_PREMISE", "ARGUMENT_ASSEMBLY", "RIVAL_READING", "SUPPORT_VS_ATTACK",
             "RETRACT_PREMISE", "PREDICT_DOWNSTREAM", "IDENTIFY_CRUX", "UNSEEN_TRANSFER",
             "SOURCE_GROUND", "DEFEND"]

# ---- skills (the pedagogical axis, separate from content) ----
SKILLS = ["TERM_SENSE", "SPEAKER_ATTRIBUTION", "PROPOSITION_EXTRACTION", "WARRANT_RECONSTRUCTION",
          "CRUX_IDENTIFICATION", "SOURCE_GROUNDING", "SENSE_DISCRIMINATION"]


@dataclass
class MasteryEvidence:
    """A learner answer = a tiny epistemic event (never mutates LearnerState directly)."""
    learner: str
    learning_claim: str
    skill: str                     # what skill axis it tests
    response: str = ""
    correct: bool = False
    evidence_level: str = "E1_RECOGNIZE"
    timestamp: str = ""


@dataclass
class InteractionFixture:
    """A gold interaction: what it tests + answer provenance (proof-carrying)."""
    id: str
    text: str
    what_it_tests: dict = field(default_factory=dict)   # target_object, discrimination, reasoning_skill, known_misconceptions
    options: list = field(default_factory=list)         # each: text, correct, derives_from


@dataclass
class LearnerState:
    """DERIVED from MasteryEvidence[] via a reducer (never mutated directly)."""
    learner: str
    skill_state: dict = field(default_factory=dict)     # skill -> evidence_level
    concept_state: dict = field(default_factory=dict)   # concept -> evidence_level
    misconception_state: list = field(default_factory=list)
    learning_history: list = field(default_factory=list)

    def strongest_skill(self):
        if not self.skill_state: return None
        return max(self.skill_state, key=lambda s: EVIDENCE_LEVELS.index(self.skill_state[s]))
    def weakest_skill(self):
        if not self.skill_state: return None
        return min(self.skill_state, key=lambda s: EVIDENCE_LEVELS.index(self.skill_state[s]))


def mastery_reducer(state: LearnerState, ev: MasteryEvidence):
    """The reducer: MasteryEvidence[] → LearnerState (reuses the ReviewEvent[] → DerivedState pattern).
    A correct answer raises the skill level; a wrong one holds it and records a misconception."""
    cur = state.skill_state.get(ev.skill, "E0_RECALL")
    cur_i = EVIDENCE_LEVELS.index(cur)
    if ev.correct:
        # level up (but evidence is earned one level at a time)
        nxt = EVIDENCE_LEVELS[min(cur_i + 1, len(EVIDENCE_LEVELS) - 1)]
        state.skill_state[ev.skill] = nxt
        state.learning_history.append(("up", ev.skill, nxt, ev.learning_claim))
    else:
        state.skill_state[ev.skill] = cur
        state.misconception_state.append(ev.learning_claim)
        state.learning_history.append(("wrong", ev.skill, cur, ev.learning_claim))
    return state


def next_interaction(learner: LearnerState, fixtures: list, content_focus=None) -> dict:
    """The adaptive engine: choose the NEXT interaction from what the learner CANNOT do.
    Skill and content are separate axes. Target the weakest skill; prefer unseen content."""
    weakest = learner.weakest_skill()
    # pick a fixture that tests the weakest skill (and content_focus if given)
    for f in fixtures:
        skill = f.what_it_tests.get("reasoning_skill", "")
        if skill == weakest and (content_focus is None or content_focus in f.text):
            return {"fixture": f.id, "target_skill": weakest, "why": f"weakest skill: {weakest}"}
    # fallback: any fixture on the weakest skill
    for f in fixtures:
        if f.what_it_tests.get("reasoning_skill") == weakest:
            return {"fixture": f.id, "target_skill": weakest, "why": f"weakest skill: {weakest}"}
    return {"fixture": None, "target_skill": weakest, "why": f"no fixture for {weakest} yet"}
