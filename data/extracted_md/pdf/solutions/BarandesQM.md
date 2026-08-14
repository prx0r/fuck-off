# New Prospects for a Causally Local Formulation of Quantum Theory

**source:** pdf · **section:** solutions
**file:** BarandesQM
---


                                                                                              Jacob A. Barandes1, 2, ∗
                                                                    1
                                                                        Jefferson Physical Laboratory, Harvard University, Cambridge, MA 02138
                                                                         2
                                                                           Department of Philosophy, Harvard University, Cambridge, MA 02138
                                                                                               (Dated: February 28, 2024)
                                                            It is difficult to extract reliable criteria for causal locality from the limited ingredients found
                                                         in textbook quantum theory. In the end, Bell humbly warned that his eponymous theorem was
                                                         based on criteria that “should be viewed with the utmost suspicion.” Remarkably, by stepping
                                                         outside the wave-function paradigm, one can reformulate quantum theory in terms of old-fashioned
                                                         configuration spaces together with ‘unistochastic’ laws. These unistochastic laws take the form of
                                                         directed conditional probabilities, which turn out to provide a hospitable foundation for encoding
                                                         microphysical causal relationships. This unistochastic reformulation provides quantum theory with
arXiv:2402.16935v1 [quant-ph] 26 Feb 2024

                                                         a simpler and more transparent axiomatic foundation, plausibly resolves the measurement problem,
                                                         and deflates various exotic claims about superposition, interference, and entanglement. Making
                                                         use of this reformulation, this paper introduces a new principle of causal locality that is intended
                                                         to improve on Bell’s criteria, and shows directly that systems that remain at spacelike separation
                                                         cannot exert causal influences on each other, according to that new principle. These results therefore
                                                         lead to a general hidden-variables interpretation of quantum theory that is arguably compatible with
                                                         causal locality.

                                                                                                                    ensures that appropriately defined quantum sys-
                                                                                                                    tems—such as local quantum fields—cannot be
                                                                                                                    used to send superluminal signals, so these quan-
                                                             I.   INTRODUCTION                                      tum systems are signal-local.
                                                                                                                  • The cluster decomposition principle [5, 6] is the
                                               In physics, ‘locality’ can refer to any of several distin-           condition that correlation functions for a physical
                                            guishable concepts. What follows is a non-exhaustive list               system consisting of widely separated constituent
                                            of historically important examples.                                     subsystems should factorize into a product of cor-
                                               • In physical theories like Newtonian mechanics that                 relation functions for each of those individual sub-
                                                 involve forces, one can ask whether those forces are               systems. This condition ensures that the statisti-
                                                 limited by the speed of light, or instead consist                  cal behavior of nearby physical systems does not
                                                 of faster-than-light action at a distance. A well-                 depend on the inaccessible details of other systems
                                                 known case of action at a distance is the Newtonian                that are very far away, assuming the absence of any
                                                 gravitational force Fg = Gm1 m2 /|r1 −r2 |2 between                initial correlations between the nearby and faraway
                                                 two spherically symmetric bodies with respective                   systems.
                                                 masses m1 and m2 , and with respective centers of                • For a local quantum field theory, one typically im-
                                                 mass located at positions r1 and r2 , where G is                   poses microcausality conditions [6], which require
                                                 Newton’s constant. The status of this form of non-                 that bosonic field operators should commute at
                                                 locality is somewhat murkier in textbook formu-                    spacelike separation, and that fermionic field oper-
                                                 lations of quantum theory, in which forces do not                  ators should anticommute at spacelike separation.
                                                 appear to play a fundamental role.                                 Among other consequences, these microcausality
                                                                                                                    conditions ensure that local observables at spacelike
                                               • A physical theory is signal-local [1, 2] if it does not            separation are capable of being statistically uncor-
                                                 permit the transmission of controllable signals or                 related.
                                                 messages faster than light. In principle, there are
                                                 no constraints in Newtonian mechanics that would                 • At the level of mereology, a spatially extended
                                                 preclude sending superluminal signals—say, by ex-                  physical entity that is fully reducible to spatially
                                                 ploiting the action-at-a-distance features of Newto-               local parts is said to be separable, and is otherwise
                                                 nian gravitational forces. Newtonian mechanics is                  said to be nonseparable or holistic [7, 8].
                                                 therefore presumably signal-nonlocal. By contrast,
                                                                                                                 This paper will be concerned with a different type of
                                                 the aptly named no-communication theorem [3, 4]
                                                                                                              locality, called causal locality, which will be taken to con-
                                                                                                              sist of the following statement:
                                                                                                                                                                   
                                                                                                                     Causal influences should not be able to
                                            ∗ jacob barandes@harvard.edu                                                                                                (1)
                                                                                                                     propagate faster than light.
2

   Going back at least to the work of Albert Einstein,               should allow a system to be steered or piloted
Boris Podolsky, and Nathan Rosen in 1935 [9], and con-               into one or the other type of state at the ex-
tinuing through the work of John Bell in the 1960s and               perimenter’s mercy in spite of his having no
beyond [10–16], there has been an ongoing debate over                access to it. [19]
whether quantum theory is causally local in this sense.           The EPR paper took for granted that causal nonlocal-
A major challenge for all such arguments is that causal        ity should be impossible, and argued that the only avail-
locality expressly depends on the notion of a ‘causal in-      able alternative was to assert that the faraway system
fluence,’ which is a notoriously difficult concept to define   should already know what measurement result it would
rigorously. One of the main goals of this paper will be        reveal according to any hypothetical choice of measure-
to address this difficulty directly, as a stepping stone to-   ment basis. Because this information was not encoded
ward arguing that a specific new formulation of quantum        in the system’s overall wave function, the authors of
theory [17, 18] is, in fact, causally local.                   the EPR paper concluded that quantum theory was in-
   After a high-level overview of the Einstein-Podolsky-       complete. Indeed, the EPR paper was titled “Can [the]
Rosen (EPR) argument and Bell’s subsequent work in             Quantum-Mechanical Description of Physical Reality Be
Section II, Section III will continue with a detailed anal-    Considered Complete?”
ysis of Bell’s results and their assumed criteria for causal      If one were to regard the EPR paper’s reasoning as
locality. Section IV will then review a new unistochas-        sound, then one would seemingly be confronted with
tic formulation of quantum theory, based on ‘unistochas-       the following logical fork: either accept causal nonlo-
tic’ microphysical laws [17, 18]. Section V will intro-        cality in quantum theory, or instead assert both the in-
duce salient topics related to causality from the theory       completeness of quantum theory and the existence of a
of Bayesian networks, and then, inspired in part by those      causally local way for measurement results to be “pre-
ideas, Section VI will recast the unistochastic formulation    determined,” in the language of John Bell’s 1964 paper
in causal terms. Section VII will show that this overall       “On the Einstein-Podolsky-Rosen Paradox” [10]. Writ-
approach makes possible an improved criterion for causal       ing about the EPR argument in a 1981 paper, Bell de-
locality. Section VIII will then argue that the unistochas-    scribed this logical fork in the following way:
tic formulation is causally local according that improved
criterion. Section IX will conclude with a summary and a                 For after observing only one particle[,] the
discussion of relevant implications for the interpretation           result of subsequently observing the other
of quantum theory.                                                   (possibly at a very remote place) is imme-
                                                                     diately predictable. Could it be that the first
                                                                     observation somehow fixes what was unfixed,
II.   EINSTEIN, PODOLSKY, ROSEN, AND BELL                            or makes real what was unreal, not only for
                                                                     the near particle[,] but also for the remote
                                                                     one? For EPR[,] that would be an unthink-
   The EPR argument [9] was based on a rudimentary
                                                                     able ‘spooky action at a distance.’ To avoid
version of quantum steering, a term introduced by Erwin
                                                                     such action at a distance[,] they have to at-
Schrödinger shortly thereafter [19, 20].
                                                                     tribute, to the space-time [sic] regions in ques-
   In quantum steering, two observers, Alice and Bob,
                                                                     tion, real properties in advance of observa-
split a pair of quantum systems described by an entan-
                                                                     tion, correlated properties, which predeter-
gled wave function, and then move a large distance apart.
                                                                     mine the outcomes of these particular obser-
If Bob decides to carry out a local measurement on his
                                                                     vations. Since these real properties, fixed in
system, then his choice of measurement basis will appear
                                                                     advance of observation, are not contained in
to ‘steer’ Alice’s system to collapse to a corresponding
                                                                     [the] quantum formalism, that formalism for
basis. However, Bob will not be able to control which
                                                                     EPR is incomplete.” [Emphasis in the origi-
specific wave function Alice’s system selects in that ba-
                                                                     nal.] [13]
sis, nor will Alice be aware that anything strange has
happened until she later confers with Bob. (Note that             In his 1964 paper [10], Bell argued that this logical fork
this paper will use the terms ‘wave function’ and ‘state       was, in the end, a mirage, and that quantum theory un-
vector’ interchangeably.)                                      avoidably entailed causal nonlocality. To set up his argu-
   Nonetheless, the overall behavior of the entangled pair     ment, Bell considered general reformulations of quantum
of systems looks suspiciously like a form of causal nonlo-     theory involving ‘hidden variables’ that uniquely pre-
cality—a concrete manifestation of what Einstein in 1947       determined measurement outcomes. Bell’s goal was to
called “spooky action at a distance” (“spukhafte Fern-         show that any such measurement-deterministic hidden-
wirkung”) [21]. Following the EPR paper’s publication,         variables theory would have to involve causally nonlocal
Schrödinger described the situation in the following way:     effects.
                                                                  As Bell noted in his 1964 paper, one such
         It is rather discomforting that the theory            measurement-deterministic hidden-variables theory was
                                                                                                                          3

already known, at least for the case of nonrelativis-          this way required introducing a controversial new crite-
tic systems of finitely many particles. Called the de          rion for causal locality, a principle that Bell called “local
Broglie-form pilot-wave formulation of quantum theory,         causality.” Bell was able to show that all formulations of
or Bohmian mechanics [22–24], this theory featured             quantum theory satisfying his principle of local causality
faster-than-light action at a distance, which Bell called      should obey a generalization of his inequality originally
“a grossly nonlocal structure.”                                derived in 1969 by John Clauser, Michael Horne, Ab-
   The result of Bell’s 1964 paper was the first version       ner Shimony, and Richard Holt [11]. This generalized
of what is now called Bell’s theorem, which implied that       inequality is likewise violated by quantum theory.
if a measurement-deterministic hidden-variables theory
were based on causally local dynamics, according to Bell’s        In keeping with the terminology of [30], this paper will
criteria, then the theory should satisfy an inequality that    distinguish ‘local causality’ from the more basic condi-
is violated in quantum theory. The 2022 Nobel Prize in         tion of ‘causal locality’ defined in (1). In short, ‘causal
Physics [25] was awarded to Alain Aspect, John Clauser         locality’ means that any causal influences that happen
and Anton Zeilinger for their experiments verifying that       to occur in a given scenario should not propagate faster
quantum systems indeed violate Bell’s inequality, fully in     than light, whereas ‘local causality’ positively asserts the
accord with the predictions of quantum theory.                 existence of local causal relationships in specific situa-
   Importantly, Bell’s 1964 paper assumed the soundness        tions.
of the EPR argument, which, in turn, implicitly relied
on several contestable principles. These included appeal-
                                                                  There are several incorrect ways to read the stronger
ing to an explicit form of wave-function collapse, as well
                                                               1975 version of Bell’s theorem. One is that the theo-
as treating measurement interventions as primitive ax-
                                                               rem rules out hidden variables altogether. Another false
iomatic ingredients of quantum theory.
                                                               reading is that one can avoid violating Bell’s principle of
   At an even deeper level, the EPR argument depended
                                                               local causality merely by avoiding the introduction of hid-
on an interventionist conception of causation, in which
                                                               den variables—but this reading confuses the weaker 1964
causation is supposed to be explicated in terms of ab-
                                                               version of Bell’s theorem with the stronger 1975 version,
stract agents carrying out formal interventions on one
                                                               which applies even to theories that do not include hid-
set of variables that then imply changes in another set
                                                               den variables at all, like textbook quantum theory itself.
of variables. (For a review of interventionist accounts
                                                               The correct reading of Bell’s theorem is to stay close to
of causation, see [26].) It is not obvious how to express
                                                               what Bell himself wrote and conclude that his principle
the EPR argument more fundamentally in terms of the
                                                               of local causality is violated by all empirically adequate
constituent atoms that make up measuring devices and
                                                               formulations of quantum theory, including the textbook
embodied observers, all undergoing some global physical
                                                               version of the theory, again putting aside various poten-
process. Nor is it clear that the EPR argument would
                                                               tial loopholes.
be applicable to any formulation of quantum theory that
foregoes not only primitive measurement interventions,
but also lacks unique measurement outcomes, such as               It is far from clear, however, that the principle of lo-
Hugh Everett’s ‘many worlds’ interpretation [27–29].           cal causality that Bell used to prove the stronger ver-
   Given these substantive reasons for doubting the EPR        sion of his theorem was the correct way to formulate the
argument, Bell’s 1964 results could not be taken to im-        more basic condition of causal locality in the first place.
ply that quantum theory necessarily involved causal non-       Bell himself warned against taking his principle of local
locality. His 1964 results instead reduced to the more         causality too seriously. Indeed, in a 1990 lecture [15], he
modest consequence of only ruling out measurement-             cautioned that his principle “should be viewed with the
deterministic hidden-variables theories obeying causally       utmost suspicion.”
local dynamics.
   Putting aside several other potential loopholes (see [30]      Bell had good reasons for being skeptical of his own
for a review), Bell’s 1964 paper therefore left open           theorem’s premises, due to his history with an older the-
three possibilities: measurement-deterministic hidden-         orem proved by John von Neumann decades before. That
variables theories with nonlocal dynamics, hidden-             earlier theorem had been widely viewed as completely rul-
variables theories with stochastic measurement out-            ing out the possibility of hidden variables [34–36]. Al-
comes, and formulations of quantum theory that es-             ready in 1935, Grete Hermann had determined that von
chewed hidden variables altogether.                            Neumann’s theorem depended on an assumption about
   In 1975 [12], Bell updated his theorem to encompass         expectation values that was too narrow [37, 38]. Bell
the second and third of these classes of possibilities,        essentially discovered the same flaw in von Neumann’s
where the third class includes ‘textbook’ quantum the-         proof decades later [39]. (For an excellent historical dis-
ory itself. (For pedagogical reviews of textbook quantum       cussion of von Neumann’s theorem, its shortcomings, and
theory, see [31–33].) Crucially, extending his theorem in      its critics, see [40].)
4

       III.   BELL’S PRINCIPLE OF LOCAL                       Today these assumptions are known as Parameter Inde-
                    CAUSALITY                                 pendence [41].
                                                                 Crucially, Bell’s proof also relied on a special implica-
   To lay the groundwork for the discussion ahead, it will    tion of Outcome Determinism and Parameter Indepen-
be important to begin with a brief presentation of the        dence. Letting ρ(λ) denote an assumed probability dis-
1964 and 1975 versions of Bell’s theorem, with a focus on     tribution for the hidden variables, Outcome Determinism
their key implicit assumptions. It is precisely these im-     (2) and Parameter Independence (3) suggested that the
plicit assumptions that will be challenged in this paper,     expectation value of the product of the measurement out-
for the eventual purpose of developing a better criterion     comes A and B over many runs of the experiment should
for causal locality.                                          be given by
   In his 1990 lecture, Bell noted the limitations of text-                          Z
book quantum theory, which lacked any notion of “local                   P (a, b) = dλ ρ(λ)A(a, λ)B(b, λ).             (4)
beables”—meaning actual properties possessed by local-
ized physical systems—as opposed to the theory’s more         (As an aside, notice that the very existence of the prob-
austere and instrumentalist notions of observables, mea-      ability distribution ρ(λ) for the hidden variables was yet
surement settings, and measurement outcomes:                  one more implicit assumption in Bell’s proof.)
                                                                 Invoking the formula (4) for the expectation value
         Even then, we are frustrated by the vague-
                                                              P (a, b), the end-result of the 1964 paper was the well-
     ness of contemporary quantum mechanics.
                                                              known Bell inequality:
     You will hunt in vain in the text-books [sic]
     for the local beables of the theory. What you                        1 + P (b, c) ≥ |P (a, b) − P (a, c)|.        (5)
     may find there are the so-called ‘local observ-
     ables’. It is then implicit that the apparatus           Here c is an alternative choice of measurement setting.
     of ‘observation’, or, better, of experimenta-            Quantum theory predicts violations of this inequality,
     tion, and the experimental results, are real             and, again, the 2022 Nobel Prize in Physics [25] was
     and localized. We will have to do as best we             awarded for the experimental confirmation of those vi-
     can with these rather ill-defined local beables,         olations.
     while hoping always for a more serious re-                 Given Bell’s criticism [39] of von Neumann’s hidden-
     formulation of quantum mechanics where the               variables theorem over its assumptions about expectation
     local beables are explicit and mathematical              values, as described earlier in this paper, it is ironic that
     rather than implicit and vague. [Emphasis in             Bell’s own theorem likewise hinged on a statement about
     the original.] [15]                                      how expectation values were supposed to work. Without
                                                              Outcome Determinism and Parameter Independence, the
  In setting up the 1964 version of his theorem [10],         formula (4) is not the correct way to calculate the neces-
Bell resorted to a pair of bivalent measurement outcomes      sary expectation value.
A = ±1 and B = ±1 at far separation in space, together          To see why, consider a theory with stochastic mea-
with their respective local measurement settings a and        surement outcomes, as in Bell’s 1975 paper, with some
b, with the special feature that if a = b, then A = −B.       set of variables λ representing beables, whether hidden
Bell then imagined a measurement-deterministic hidden-        variables or not. (As noted by Bell in [13], one could even
variables theory containing a set of hidden variables λ,      try to regard wave functions themselves as ‘spatially non-
and supposed that these hidden variables λ, together          separable beables.’) For this more general case, in the
with the measurement settings a and b, fully predeter-        formula (4) for the expectation value, one then needs to
mined the values of the measurement outcomes A and            replace the product
B:
                                                                                      A(a, λ)B(b, λ)                   (6)
    A = A(a, b, λ) = ±1,      B = B(a, b, λ) = ±1.      (2)
Following the terminology of [30], this assumption will       with the statistical average
be called Outcome Determinism.
                                                                                X
                                                                                    ρ(A, B|a, b, λ)AB,                 (7)
   In that 1964 paper, Bell’s causal-locality assumptions                       A,B
included the condition that the measurement outcome
A should not depend on the faraway measurement set-           where ρ(A, B|a, b, λ) is some joint probability distribu-
ting b, and, similarly, that the measurement outcome B        tion conditioned on the measurement settings a and b,
should not depend on the faraway measurement setting          as well as conditioned on the variables λ representing the
a. Bell concluded that A should be a function A(a, λ) of      theory’s beables. It follows that (4) should be replaced
a and λ alone, and that B should be a function B(b, λ)        with
of b and λ alone:
                                                                                Z         X
                                                                     P (a, b) = dλ ρ(λ)       ρ(A, B|a, b, λ)AB.     (8)
      A(a, b, λ) = A(a, λ),    B(a, b, λ) = B(b, λ).    (3)                                 A,B
                                                                                                                                    5

In place of Outcome Determinism (2) and Parameter In-           which closely resembles the 1964 version (4) of the same
dependence (3), one then needs new assumptions in order         expectation value. This formula thereby makes it possi-
to derive something like the Bell inequality (5).               ble to derive a more general form of the Bell inequality,
   From the standard rules for working with conditional         as first obtained in 1969 by Clauser, Horne, Shimony,
probabilities, one can always write down the decomposi-         and Holt [11]. This inequality is violated by all theo-
tion                                                            ries that are empirically equivalent to textbook quantum
                                                                theory—including the textbook theory itself—so all such
      ρ(A, B|a, b, λ) = ρ(A|a, b, λ, B)ρ(B|a, b, λ).     (9)
                                                                theories must also violate Bell’s principle of local causal-
For a given measurement-stochastic theory, Bell’s new           ity.
principle of local causality was the condition that the the-       Bell’s principle of local causality—in either of its equiv-
ory should contain variables λ representing a sufficiently      alent forms (10) or (11)—implicitly depends on an as-
rich collection of beables localized in the overlap of the      sumption that goes beyond questions of locality. That
past light cones of the measurement outcomes A and B            implicit assumption is called Reichenbach’s principle of
that λ screens off B and b from A, and also screens off         common causes. (For a review, see Section 19 of Hans
a from B, in the sense that                                     Reichenbach’s book [42], and also [43].)
                                                                   Reichenbach’s principle of common causes states that
 ρ(A|a, b, λ, B) = ρ(A|a, λ),   ρ(B|a, b, λ) = ρ(B|b, λ).       if two variables A and B are correlated, in the sense that
                                                      (10)      their joint probability P (A, B) fails to factorize as the
   Looking back at the decomposition (9), it is clear that      product of their standalone probabilities P (A) and P (B),
this new assumption (10) is equivalent to requiring that
conditioning on the variables λ representing beables lo-                            P (A, B) ̸= P (A)P (B),                     (15)
calized in the overlap of the past light cones of A and B
leads to the following factorization condition:                 and if A and B do not causally influence each other,
          ρ(A, B|a, b, λ) = ρ(A|a, λ)ρ(B|b, λ).         (11)    then there should exist some other variable C such that
                                                                conditioning on C leads to the following factorization:
Indeed, in his 1981 paper [13], Bell took this latter for-
mula to be his basic principle of local causality, and at-                      P (A, B|C) = P (A|C)P (B|C).                    (16)
tempted to justify it on its own merits.
   The factorization version (11) of Bell’s principle of lo-    That is, Reichenbach’s principle positively asserts the ex-
cal causality is, in turn, also equivalent to the conjunction   istence of a ‘common-cause’ variable C for A and B. In
of two other assumptions.                                       this way, the variable C is said to ‘explain’ or ‘account
   The first assumption is the following weaker factoriza-      for’ the correlation between A and B.1
tion condition:                                                    Bell’s principle of local causality—again in either of its
                                                                equivalent forms (10) or (11)—clearly invokes Reichen-
                                                                bach’s principle, with the role of the asserted common-
      ρ(A, B|a, b, λ) = ρ(A|a, b, λ)ρ(B|a, b, λ).       (12)    cause variable C played by the variables λ representing
This property is now called Outcome Independence [41].          beables localized in the overlap of the past light cones of
   The other assumption is a generalization of Parameter        the measurement results A and B.
Independence (3) to mean that the conditional proba-               Reichenbach’s principle of common causes may seem
bilities for the measurement outcome A do not depend            sensible and intuitive in the context of everyday experi-
on the measurement setting b, and that the conditional          ence, but those are far from definitive reasons to take it
probabilities for the measurement outcome B do not de-          to be a fundamental requirement for causal locality. In
pend on the measurement setting a:                              particular, embedded in both Reichenbach’s principle of
                                                                common causes and Bell’s principle of local causality is
  ρ(A|a, b, λ) = ρ(A|a, λ),    ρ(B|a, b, λ) = ρ(B|b, λ).        the assumption that the asserted common causes in ques-
                                                         (13)   tion must specifically take the form of variables that can
   Assuming Outcome Independence (12) together with             be conditioned on and then summed or integrated over.
the updated version of Parameter Independence (13), one            Just as a formulation of quantum theory that violates
obtains Bell’s factorization (11), where again λ denotes        von Neumann’s assumptions about expectation values
variables representing a sufficiently rich collection of be-    can evade von Neumann’s theorem and thereby admit
ables localized in the overlap of the past light cones of the   hidden variables, a formulation of quantum theory that
measurement results A and B. The expectation value (8)
then becomes
           Z                           !                    !
                        X                   X
                                                                1 Note that this presentation of the principle is slightly generalized
P (a, b) = dλ ρ(λ)          ρ(A|a, λ)A         ρ(B|b, λ)B ,
                        A                   B                     from Reichenbach’s original formulation, which assumed that A
                                                        (14)      and B were positively correlated, so that P (A, B) > P (A)P (B).
6

fails to adhere to the strictures of Reichenbach’s prin-         these theorems depend on an interventionist conception
ciple of common causes could violate Bell’s principle of         of causation, as defined earlier in this paper. It is there-
local causality without necessarily entailing nonlocal cau-      fore not clear whether the theorems would make sense if
sation—as was pointed out, for example, by William Un-           one were instead to work at the level of the constituent
ruh:                                                             atoms of the relevant measuring devices and physically
                                                                 embodied observers, all as parts of some sort of global
          It is true that this common cause cannot               probabilistic process.
      be stated in exactly the form which for ex-
                                                                    Indeed, when thinking in terms of a global probabilistic
      ample Reichenbach set up to describe com-
                                                                 process, without abstract agents and primitive interven-
      mon causes for a classical statistical system.
                                                                 tions, it is far from obvious how to identify causal in-
      But that is not surprising. Quantum mechan-
                                                                 fluences or even nonlocal interactions, especially without
      ics is not classical mechanics. The structure
                                                                 concrete notions like Newtonian forces that are capable of
      of the correlations in a quantum system dif-
                                                                 establishing definitive physical linkages between systems.
      fer from those in a classical system, as Bell
                                                                 (For an introduction to some of the challenges that arise
      so succinctly showed. But those correlations
                                                                 when attempting to make sense of causation in physics,
      do not arise mysteriously somehow in the de-
                                                                 see [45].)
      velopment of a widely spaced system. Those
                                                                    Other theorems, such as [46], depend on strong as-
      correlations do not require some mysterious
                                                                 sumptions about the existence of theoretical joint proba-
      non-local [sic] action to be explained. They
                                                                 bility distributions involving the measurement results of
      are simply there, as are correlations in a clas-
                                                                 subsystems at intermediate times during an overall uni-
      sical system, due to the evolution from a com-
                                                                 tary process. The new formulation of quantum theory to
      mon (quantum) cause in the past. [44]
                                                                 be reviewed shortly provides principled reasons why such
  Returning once again to Bell’s 1990 lecture [15], Bell         theoretical joint probability distributions should not be
actually formulated two versions of his principle of local       assumed to exist—the formulation simply does not sup-
causality.                                                       ply them in its microphysical laws, due in part to indi-
  Bell identified the first version as the following state-      visibility, a concept that will turn out to play a central
ment:                                                            role.

     The direct causes (and effects) of events 
                                               
                                                                 IV.   THE UNISTOCHASTIC FORMULATION OF
     are near by [sic], and even the indirect
                                               
                                                         (17)                QUANTUM THEORY
     causes (and effects) are no further away 
     than permitted by the velocity of light.
                                                                    As described in [17, 18], one can reformulate quan-
This first version is very close in spirit to the condition of   tum theory in terms of a sufficiently general theory of
causal locality introduced at the beginning of this paper        stochastic processes, working entirely outside the tradi-
in (1), and is merely a locality condition on whatever           tional ‘wave-function paradigm.’ Note that this approach
causal influences happen to occur.                               is not continuous with older attempts to formulate quan-
   However, Bell then stated that “The above principle of        tum theory in stochastic terms [47–52], all of which as-
local causality is not yet sufficiently sharp and clean for      sumed a fundamental Markov condition, nor is it con-
mathematics,” followed by “Now it is precisely in clean-         nected with stochastic-collapse approaches to quantum
ing up intuitive ideas for mathematics that one is likely        theory [53], which treat wave functions or density matri-
to throw out the baby with the bathwater. So the next            ces as basic ingredients of physical reality.
step should be viewed with the utmost suspicion.” It was            The necessary axioms for this stochastic formulation
at this point that Bell turned to the second version of his      are much simpler and more transparent than for tra-
principle of local causality, which positively asserted the      ditional textbook treatments of quantum theory, with-
existence of common causes and became the mathemat-              out any need for metaphysically opaque postulates about
ical statement (10).                                             wave functions in abstract Hilbert spaces over the com-
   This paper is hardly the first written argument to claim      plex numbers.2
that Bell’s principle of local causality is not the correct
way to capture causal locality in a formulation of quan-
tum theory. Beyond implicitly depending on Reichen-
                                                                 2 Technically speaking, the Hilbert spaces of quantum theory are
bach’s principle of common causes, one should also note
that some readings of Bell’s theorem, like several related         defined not over the complex numbers alone, but over the pseudo-
                                                                   quaternions [54], which are a Clifford algebra generated by 1,
theorems [11, 14], assume a notion of causation based on           the imaginary unit i, and the complex-conjugation operator
treating measurement settings and measurement results              K. This operator K is needed for implementing time-reversal
as primitive interventions by abstract agents. That is,            transformations, and satisfies K 2 = 1 together with the anti-
                                                                                                                                            7

   At the level of kinematics, one assumes a system with                    and one can write the collection of transition probabilities
a set of configurations, forming an old-fashioned configu-                  as an N × N transition matrix,
ration space C. The specific choice of configuration space                                                              
depends on the particular kind of system one is modeling,                                       Γ11 (t) Γ12 (t)
just like in classical physics, so C could consist of arrange-                         Γ(t) ≡ Γ (t) . . .               .        (23)
                                                                                                                        
                                                                                                       21
ments of particle positions, or of local field intensities, or                                                           ΓN N (t)
of digital bits, or of some other physical ingredients alto-
gether.                                                                     One can then naturally express the basic linear relation-
   Sticking for simplicity to the discrete case, perhaps af-                ship (21) as an elementary matrix product:
ter a suitable degree of coarse-graining, the configura-
                                                                                                   p(t) = Γ(t)p(0).                       (24)
tion space then consists of a collection of configurations
i = 1, . . . , N . (One can generalize the analysis ahead                     The N × N transition matrix Γ(t) consists of non-
to the continuous case by introducing a measure on the                      negative entries, and its columns each sum to 1:
configuration space and by replacing summations with                                                                           
integrations.)                                                                         Γij (t) ≥ 0 [for i, j = 1, . . . , N ], 
                                                                                                                               
                                                                                                                               
   At the level of dynamics, the microphysical laws consist                           N
                                                                                      X                                          (25)
of conditional or transition probabilities of the form                                    Γij (t) = 1 [for j = 1, . . . N ].  
                                                                                                                               
                                                                                      i=1
         Γij (t) ≡ p(i, t|j, 0)        [for i, j = 1, . . . N ],     (18)
                                                                            Mathematically speaking, these properties identify Γ(t)
each of which supplies the probability for the system to                    as a (column) stochastic matrix.
be in its ith configuration at a continuously variable time                    An important concept here is the historically recent no-
t, given that the system is in its jth configuration at                     tion of divisibility [55, 56], which is loosely related to the
a suitable initial time 0. (No assumption is made here                      well-known Markov property. For a divisible transition
that t > 0 or t < 0.) Introducing standalone probability                    matrix Γ(t) with a variable time t, and given an interme-
distributions at the initial time 0 and at arbitrary times                  diate time t′ between 0 and t, there always exists a valid
t,                                                                          stochastic matrix Γ(t ← t′ ) such that one can ‘divide’ the
  pj (0) ≡ p(j, 0),       pi (t) ≡ p(i, t)
                                     [for i, j = 1, . . . N ],              dynamics from 0 to t into subintervals from 0 to t′ , and
                                                           (19)             then from t′ to t, as ordinary matrix multiplication:
the conditional or transition probabilities (18) that make                                    Γ(t) = Γ(t ← t′ ) Γ(t′ ) .                  (26)
up the basic microphysical laws give a simple linear re-                                      |{z} | {z } | {z }
                                                                                              0 to t         t′ to t   0 to t′
lationship between the standalone probabilities p(j, 0) at
the initial time 0 and the standalone probabilities p(i, t)                    By contrast, for the kind of stochastic process that
at the final time t, in accordance with the standard rules                  is equivalent to a quantum system, the transition ma-
for conditional probabilities and marginalization:                          trix will generically be indivisible, meaning that no valid
               N                                                            such stochastic matrix Γ(t ← t′ ) satisfying the divisibility
               X
   p(i, t) =         p(i, t|j, 0)p(j, 0)    [for i = 1, . . . N ].   (20)   property (26) will exist. A stochastic process based on a
               j=1                                                          potentially indivisible transition matrix will be called a
                                                                            generalized stochastic system or process.
Following the somewhat more succinct notation intro-                           An N × N matrix Γ is called a unistochastic matrix
duced above, this linear relationship becomes                               if there exists a (generally non-unique) N × N unitary
                 N
                 X                                                          matrix U such that the individual entries of Γ are each
      pi (t) =         Γij (t)pj (0)    [for i = 1, . . . N ].       (21)   the modulus-squares of the corresponding entries of U :
                 j=1                                                                                   2
                                                                                        Γij = |Uij |        [for i, j = 1, . . . , N ].   (27)
  Working in terms of matrices, one can write the stan-
dalone probability distributions here as N × 1 column                       In [57], Alfred Horn originally called such matrices
vectors,                                                                    “ortho-stochastic,” but that term is now reserved for
                                                                        the special case in which U can be taken to be a real-
                   p1 (0)             p1 (t)
                                                                            orthogonal matrix. The term “unistochastic” appears to
         p(0) ≡  ... , p(t) ≡  ... ,           (22)
                                          
                                                                            have first been introduced by Robert Thompson in [58].
                         pN (0)                    pN (t)                     Crucially, notice that the equalities appearing in (27)
                                                                            hold entry-by-entry. That is, Γ is not given by a sim-
                                                                            ple matrix product like U † U , which would just give the
  commutation relation Ki = −iK. Altogether, the elementary                 identity matrix 1, due to the unitarity of U . In partic-
  pseudo-quaternions 1, i, K, and iK satisfy the basic relations            ular, the overall relationship between Γ and U does not
  −i2 = K 2 = (iK)2 = (i)(K)(iK) = 1.                                       commute with matrix multiplication.
8

  A generalized stochastic system with a unistochastic                      matrix ρ(0) whose other entries are all 0s,
transition matrix Γ(t) will be called a unistochastic sys-                                                                                 
tem or process. As proved in [18], one can always as-                                                                p1 (0) 0
sume that a generalized stochastic system is, in fact, a                     ρ(0) ≡ diag(p1 (0), . . . , pN (0)) ≡  0
                                                                                                                           ..    ,
                                                                                                                                  
                                                                                                                               .
unistochastic system, by slightly enlarging or dilating the                                                                 pN (0)
configuration space if necessary, and invoking the Stine-                                                                          (34)
spring dilation theorem [59]. It therefore suffices to focus                the quantum system’s density matrix at all other times
one’s attention on unistochastic systems.                                   is defined by the usual similarity transformation given by
  Reconstructing quantum theory from the set of unis-                       the time-evolution operator U (t):
tochastic systems is then an extended mathematical ex-
ercise.                                                                                         ρ(t) ≡ U (t)ρ(0)U † (t).                    (35)
  Given the N × N unistochastic transition matrix Γ(t)
for a given unistochastic system, one starts by taking                      Observe that the resulting time-dependent density ma-
the quantum system’s unitary time-evolution operator to                     trix ρ(t) is not generally diagonal for times t ̸= 0.
be a (generally not-uniquely) associated N × N time-                           Notice also that the famous linearity of the time evo-
dependent unitary matrix U (t):                                             lution of quantum theory, as exhibited by relationship
                                                                            between ρ(t) and ρ(0), is not a mystery, but ultimately
                                 2
           Γij (t) = |Uij (t)|         [for i, j = 1, . . . , N ].   (28)   descends from the linearity of the basic relationship (21),
                                                                            which again follows directly from the standard rules for
  Unlike the underlying unistochastic transition matrix                     conditional probabilities and marginalization.
Γ(t), this unitary time-evolution operator U (t) satisfies a                   Assuming sufficient smoothness in t, so that Stone’s
divisibility condition in the form of the usual composition                 theorem applies [60], one can define the system’s self-
law                                                                         adjoint Hamiltonian H(t) as the infinitesimal generator
                                                                            of time translations,

                    U (t) = U (t ← t′ ) U (t′ ),                     (29)                              ∂U (t) †
                                                                                          H(t) ≡ iℏ          U (t) = H † (t),               (36)
                                                                                                        ∂t
                    |{z} | {z } | {z }
                    0 to t           t′ to t   0 to t′

where the relative time-evolution operator U (t ← t′ ) is                   in which case the system’s density matrix ρ(t) satisfies
defined by                                                                  the von Neumann equation,

                                                                                                    ∂ρ(t)
                    U (t ← t′ ) ≡ U (t)U † (t′ )                     (30)                      iℏ         = [H(t), ρ(t)],                   (37)
                                                                                                     ∂t
and is guaranteed to be unitary. The fact that modulus-                     where the brackets denote the usual matrix commutator
squaring the entries of a matrix, as in (28), does not com-                 (not a Poisson bracket):
mute with matrix multiplication accounts for the failure
of Γ(t) likewise to be divisible.                                                               [X, Y ] ≡ XY − Y X.                         (38)
   Indeed, if one attempts to define a unistochastic tran-
sition matrix Γ(t ← t′ ) from t′ to t based on the relative                 If the system’s density matrix ρ(t) is rank-one, then it
time-evolution operator (30),                                               can be factorized in terms of a complex-valued N × 1
                                                                            state vector or wave function Ψ(t),
                                                         2
                 Γij (t ← t′ ) ≡ |Uij (t ← t′ )| ,                   (31)                                                      
                                                                                                                         Ψ1 (t)
then one ends up with a discrepancy between the actual-                       ρ(t) = Ψ(t)Ψ† (t) [if rank-one], Ψ(t) ≡  ... ,
                                                                                                                               
indivisible dynamical evolution Γ(t) from 0 to t and the                                                                           ΨN (t)
nearest-divisible dynamical evolution Γ(t ← t′ )Γ(t′ ):                                                                         (39)
                                                                            in which case the state vector Ψ(t) evolves according to
                     Γ(t) ̸= Γ(t ← t′ )Γ(t′ ).                       (32)   the Schrödinger equation,
From the standpoint of regarding the quantum system                                                  ∂Ψ(t)
as a unistochastic system, the well-known interference                                          iℏ         = H(t)Ψ(t).                      (40)
                                                                                                      ∂t
effects of quantum theory merely reflect this discrepancy:
                                                                            It is notable that these familiar quantum-theoretic equa-
    Γ(t) − Γ(t ← t′ )Γ(t′ ) ̸= 0         [interference effects].     (33)   tions emerge from an underlying stochastic process,
                                                                            which ultimately consists of a system moving along some
   Writing the initial standalone probability distribution                  trajectory in a prosaic configuration space according to
pj (0) as the diagonal entries of an N × N initial density                  (indivisible) stochastic transition probabilities.
                                                                                                                                    9

   Observe that the state vector or wave function Ψ(t)                       Just as one can represent a stochastic process in the
appears here as just a convenient piece of secondary, de-                 Hilbert-space formalism familiar from quantum theory,
rived mathematics, rather than as anything like a pri-                    one can take any quantum system in its Hilbert-space
mary or fundamental physical object. In the context of                    formalism and turn the relationship (28) around to de-
this overall stochastic picture, the wave function is not a               fine a corresponding stochastic process. This stochastic-
piece of ontological furniture, but instead encodes epis-                 quantum correspondence is a many-to-one relationship in
temic information—the system’s probabilities—as well as                   both directions—a single stochastic process will gener-
nomological information—the system’s unistochastic mi-                    ally have many different-looking Hilbert-space represen-
crophysical dynamics.                                                     tations, and a given quantum system in its Hilbert-space
   Given a random variable A(t) on the system’s con-                      formalism may represent many different-looking stochas-
figuration space, meaning a spectrum of magnitudes                        tic processes. The relationship between a stochastic
a1 (t), . . . , aN (t) that depend on the system’s configura-             process and its corresponding Hilbert-space representa-
tion i = 1, . . . , N and that generically also depend ex-                tion is therefore analogous to the relationship between a
plicitly on the time t, the statistical expectation value of              classical-deterministic system described by second-order
A(t) is defined as                                                        differential equations of motion and its corresponding
                                                                          Hamiltonian phase-space representation, a relationship
                               N
                               X                                          that is likewise many-to-one in both directions.
                  ⟨A(t)⟩ ≡           ai (t)pi (t).                 (41)
                                                                             At a practical level, one can therefore regard the
                               i=1
                                                                          Hilbert-space formalism as a form of ‘analytical mechan-
In terms of the system’s density matrix ρ(t), as defined in               ics’ for highly general stochastic processes, just as the
(35), and introducing a diagonal matrix A(t) according                    Hamiltonian phase-space formalism provides an analyti-
to                                                                        cal mechanics for a second-order classical-deterministic
                                                                        system. Like any form of analytical mechanics, the
                                          a1 (t) 0
                                                                          Hilbert-space formalism provides a powerful set of math-
  A(t) ≡ diag(a1 (t), . . . , aN (t)) ≡  0 . . .     ,
                                                     
                                                                          ematical tools for specifying microphysical laws in a sys-
                                                          aN (t)          tematic manner, for studying dynamical symmetries, for
                                                    (42)                  proving theorems, and for calculating predictions.
one can rewrite the expectation value (41) in the equiv-                     The fact that one can reformulate a given quantum
alent form                                                                system as a unistochastic system deflates much of the
                                                                          exotic talk about quantum theory. As spelled out in [17],
                   ⟨A(t)⟩ = tr(A(t)ρ(t)),                          (43)   from the standpoint of this unistochastic formulation of
which looks just like the standard formula from quantum                   quantum theory, the measurement problem arguably dis-
theory.                                                                   appears, because measuring devices are now to be mod-
  Consider the special case in which A = Pi is a rank-                    eled as ordinary (if complicated) subsystems of an overall
one projector consisting of a matrix with a 1 in its ith                  stochastic process, and one can show that they end up
diagonal entry and 0s in all its other entries:                           in measurement-outcome configurations probabilistically
                                                                          in accord with the usual predictions of the Born rule.
              Pi ≡ diag(0, . . . , 0, 1, 0, . . . , 0).            (44)   Moreover, superposition is no longer a literal smearing of
                                       ↑
                                   ith entry                              configurations, interference is just a breakdown (33) in di-
                                                                          visible dynamics, and decoherence is merely the leakage
It follows that if ρ(t) is similarly rank-one, in the sense               of statistical correlations out into the larger environment.
of being factorizable according to (39) in terms of a state                  In particular, as explained in [17], decoherence auto-
vector Ψ(t), then the expectation value (43) reduces to                   matically generates division events, which are new times
the simplest version of the Born rule:                                    t′ at which the microphysical transition matrix Γ(t) does
                                           2                              divide, in the sense of (26). A division event t′ is there-
                       pi (t) = |Ψi (t)| .                         (45)
                                                                          fore a time that can serve in place of the initial time 0
   Random variables on the unistochastic system’s con-                    in the unistochastic system’s microphysical conditional
figuration space have the status of beables, in Bell’s ter-               probabilities.
minology. By modeling the measurement process in de-                         If t′ is a division event, then the unistochastic system
tail—treating measurement devices as mundane stochas-                     contains genuine microphysical conditional probabilities
tic systems in their own right—one can show that non-                     of the form
diagonal self-adjoint operators represent observables that                                Γii′ (t ← t′ ) ≡ p(i, t|i′ , t′ ),     (46)
are emergent phenomena at the level of measurements,
and so are called emergeables in [17]. A unistochastic                    which are conditioned on the system’s configuration i′ at
system’s beables and emergeables together comprise the                    the division event t′ , where Γ(t ← t′ ) is a valid stochas-
system’s full noncommutative algebra of observables.                      tic matrix satisfying the divisibility condition (26). One
10

                                 B                                  It follows that if the random variables B, C, and D
                                                                  were to develop contingent joint probabilities p(b, c, d) in
                        A            C                            some concrete, real-life instantiation of the Bayesian net-
                                                                  work, then the random variable A would automatically
                                                                  inherit a contingent standalone probability distribution
                                 D
                                                                  p(a) of its own according to the standard multilinear rule
                                                                                       X
Figure 1. A simple Bayesian network with four random vari-                      p(a) =      p(a|b, c, d)p(b, c, d).       (48)
ables A, B, C, and D denoted by nodes, with directed edges
                                                                                          b,c,d
pointing to A from B, C, and D.
                                                                  Said in another way, the basic conditional probabilities
                                                                  p(a|b, c, d), together with the contingent joint probabil-
expects that for a macroscopic system in strong contact           ities p(b, c, d) for B, C, and D, dictate the contingent
with a noisy environment that eavesdrops on the sys-              standalone probabilities p(a) for A, and they do so in a
tem’s configuration over a characteristic time scale δt,          multilinear way.
the system’s microphysical laws will become effectively              Importantly, the basic conditional probability distribu-
Markovian for time steps of duration δt.                          tion p(a|b, c, d) supplied by the Bayesian network in the
                                                                  present example is directed, in the sense that the value a
                                                                  of the random variable A appears to the left of the ‘given’
V.    BAYESIAN NETWORKS AND CAUSATION
                                                                  symbol |, whereas the respective values b, c, and d of the
                                                                  random variables B, C, and D appear to the right. To
   As explained earlier, the traditional textbook formu-          understand the significance of this directedness, it will be
lation of quantum theory does not provide a hospitable            worthwhile to construct a different conditional probabil-
domain for a non-interventionist account of causation,            ity for comparison.
making it very difficult to devise clear statements about            To that end, notice that if one were to combine the
causal influences in general or causal locality in particu-       Bayesian network’s basic conditional probability distri-
lar. By replacing the Hilbert-space axioms with a true            bution p(a|b, c, d) with the contingent joint probability
set of microphysical laws consisting of conditional proba-        distribution p(b, c, d), then one could formally define a
bilities Γij (t) ≡ p(i, t|j, 0), as introduced in (18), the new   joint probability distribution p(a, b, c, d) for all four of
unistochastic formulation of quantum theory reviewed in           the random variables A, B, C, and D by invoking the
this paper opens up an important connection with the              standard rule for conditional probabilities:
literature on Bayesian networks [61], which provide a
much more amenable foundation for a non-interventionist                        p(a, b, c, d) ≡ p(a|b, c, d)p(b, c, d).            (49)
causal account.
   In simple terms, a Bayesian network is a model that            Defining a joint probability distribution p(a, c, d) for A,
consists of a set of random variables connected by a col-         C, and D alone by marginalizing the joint probability
lection of conditional probabilities. Displayed graphi-           distribution p(a, b, c, d) over B,
cally, a Bayesian network will typically denote the ran-                                        X
                                                                                 p(a, c, d) ≡      p(a, b, c, d),        (50)
dom variables by nodes, and will denote the conditional
                                                                                                     b
probabilities by directed line segments or edges connect-
ing some of those nodes together.                                 and assuming that this joint probability p(a, c, d) ̸= 0
   For example, if a node representing a random variable          were nonzero, one could then formally condition on A,
A is at the pointed end of directed edges from nodes rep-         C, and D to obtain the conditional probability
resenting random variables B, C, and D, as in Figure 1,
then the Bayesian network must supply a basic condi-                                    p(a, b, c, d)
                                                                       p(b|a, c, d) ≡                    [if p(a, c, d) ̸= 0].    (51)
tional probability distribution p(a|b, c, d) among its laws,                             p(a, c, d)
where lowercase letters denote the possible values of the
                                                                  Writing out this conditional probability in more detail,
corresponding random variables:
                                                                  one would obtain the formula
     p(a|b, c, d) ≡ p(A = a|B = b, C = c, D = d).         (47)                                    p(a|b, c, d)p(b, c, d)
                                                                            p(b|a, c, d) = P              ′          ′
                                                                                                                              ,   (52)
                                                                                                  b′ p(a|b , c, d)p(b , c, d)
This conditional probability is the probability that the
random variable A has the value a, given that the random          which makes clear that p(b|a, c, d) would depend on the
variables B, C, and D have the respective values b, c, and        contingent joint probability distribution p(b, c, d)—and
d. In other words, the values of B, C, and D determine            in a nonlinear manner. Hence, although p(b|a, c, d)
the conditional probability distribution for the values of        might exist, it would be a derived conditional probabil-
A.                                                                ity distribution that depended on the contingencies of
                                                                                                                                     11

the given concrete instantiation of the Bayesian network,                can read the microphysical laws of the unistochastic sys-
and would therefore have a different physical status from                tem as providing a microphysical notion of causal influ-
the basic, nomological conditional probability distribu-                 ences.
tion p(a|b, c, d) supplied by the Bayesian network’s laws.                 To make things more concrete, suppose that the unis-
   There exists a reading of a Bayesian network as a                     tochastic system consists of two subsystems Q and R, in
model of causal relationships, with causal influences man-               the sense that i = (qt , rt ) and j = (q0 , r0 ), where low-
ifesting as the Bayesian network’s directed conditional                  ercase letters denote specific configurations of the corre-
probabilities. That is, if the Bayesian network supplies                 sponding subsystems. One can then write the directed
a directed conditional probability distribution p(a|b, c, d)             conditional probabilities (18) for the overall system as
in its basic laws, then one should read the Bayesian net-
work as implying that the random variables B, C, and                                        p((qt , rt ), t|(q0 , r0 ), 0).         (53)
D causally influence the random variable A.
   Although the causal influences encoded in Bayesian                    To say that the subsystem Q is free of causal influences
networks can be given an interventionist cast, a non-                    from the subsystem R over the time interval from 0 to
interventionist interpretation is available as well, with                t would then be the statement that after marginalizing
stochastic fluctuations in B, C, and D dictating stochas-                over the configuration rt of R, the resulting conditional
tic fluctuations in A through the directed conditional                   probability distribution no longer depends on r0 :
probability distribution p(a|b, c, d).3
                                                                                      p(qt , t|(q0 , r0 ), 0) = p(qt , t|q0 , 0).   (54)
   Notice how the directedness of the conditional proba-
bility distributions supplied by a Bayesian network cap-
tures the inherently asymmetric nature of cause-and-
                                                                         VII.    AN IMPROVED PRINCIPLE OF CAUSAL
effect relationships.
                                                                                          LOCALITY
   Interestingly, this connection between the directedness
of a Bayesian network’s basic conditional probabilities
                                                                            One can now formulate an improved principle of causal
and the asymmetry of cause-and-effect also sheds light
                                                                         locality:
on why causal language is so fraught in the context of
theories that are based on microphysical laws that are                         A theory with microphysical directed 
                                                                                                                           
deterministic and reversible. In a deterministically re-                       conditional probabilities is causally local 
                                                                                                                           
                                                                                                                           
versible theory, if a value a of a variable A implies a cor-
                                                                                                                           
                                                                               if any pair of localized systems Q and R 
                                                                                                                           
                                                                                                                           
responding value b of another variable B, then p(b|a) = 1,
                                                                                                                           
                                                                               that remain at spacelike separation for 
                                                                                                                           
                                                                                                                           
and, in addition, any contingent standalone probability
                                                                                                                           
                                                                               the duration of a given physical process
                                                                                                                           
p(a) assigned to a will necessarily equal the contingent                                                                     (55)
                                                                               do not exert causal influences on each 
standalone probability p(b) assigned to b. It follows im-
                                                                                                                           
                                                                               other during that process, in the sense 
                                                                                                                           
                                                                                                                           
mediately from Bayes’ theorem that p(a|b) = p(b|a) = 1,
                                                                                                                           
                                                                               that the directed conditional probabili- 
                                                                                                                           
                                                                                                                           
so these conditional probabilities are not directed, and
                                                                                                                           
                                                                               ties for Q are independent of R, and vice 
                                                                                                                           
                                                                                                                           
the asymmetry of cause-and-effect relationships is lost.
                                                                                                                           
                                                                               versa.
                                                                         Having stated this new principle of causal locality, one
     VI.    A MICROPHYSICAL ACCOUNT OF                                   can show that quantum theory, formulated as a theory
                   CAUSATION                                             of unistochastic processes, indeed satisfies it.
                                                                            For that purpose, consider a unistochastic system con-
  As reviewed in this paper, one can reformulate a quan-                 sisting of a pair of localized subsystems Q and R that re-
tum system in terms of an underlying unistochastic sys-                  main at spacelike separation during a given physical pro-
tem. The microphysical laws of that unistochastic sys-                   cess. The overall system’s unistochastic transition matrix
tem consist of directed conditional probabilities (18),                  ΓQR (t) has a corresponding unitary time-evolution oper-
Γij (t) ≡ p(i, t|j, 0), which are very much like the directed            ator UQR (t) in the sense of (28). Invoking the spacelike
conditional probabilities that define the basic laws of a                separation of Q and R together with the usual assump-
Bayesian network. Taking this resemblance seriously, one                 tions employed in textbook quantum theory, the over-
                                                                         all time-evolution operator UQR (t) tensor-factorizes into
                                                                         respective unitary time-evolution operators UQ (t) for Q
                                                                         and UR (t) for R individually:
3 Note that this conception of causation as corresponding to di-

  rected conditional probability distributions is fundamentally dis-
                                                                                          UQR (t) = UQ (t) ⊗ UR (t).                (56)
  tinct from probability-raising theories of causation. In particular,
  no assumption is made here that the directed conditional prob-           In contrast with matrix multiplication, tensor prod-
  abilities specifically raise any standalone probabilities.             ucts do commute with modulus-squaring the entries of
12

a matrix, so the overall system’s unistochastic transition                                             (Q, A)                                  (R, B)
matrix ΓQR (t) likewise tensor-factorizes:                                                                t
                                                                                        time
                       ΓQR (t) = ΓQ (t) ⊗ ΓR (t).                         (57)
                                                                                                               A     Q                R        B
Here ΓQ (t) is the unistochastic transition matrix for the
                                                                                            space
subsystem Q corresponding to UQ (t) in the sense of the
                                                                                                          t′
modulus-squaring relationship (28), and ΓR (t) is simi-
larly the unistochastic transition matrix for the subsys-                                                 0
tem R corresponding to UR (t).                                                                                            (Q, R)
   It follows immediately from the tensor-factorization
(57), together with the definition (18) of the entries of                        Figure 2. A spacetime diagram depicting an idealized version
                                                                                 of the EPR thought experiment, with the two subsystems
a transition matrix as conditional probabilities, that the
                                                                                 Q and R separating in space after they interact at the time
overall system’s directed conditional probabilities factor-                      t′ , and then respectively joining up with the two observer-
ize as                                                                           subsystems A (‘Alice’) and B (‘Bob’). The two observer-
                                                                                 subsystems A and B are assumed to remain spacelike sepa-
     p((qt , rt ), t|(q0 , r0 ), 0) = p(qt , t|q0 , 0)p(rt , t|r0 , 0).   (58)   rated throughout the experiment.

Hence, marginalizing over rt leaves a conditional prob-                                    VIII. REVISITING THE
ability for Q that does not depend on r0 , precisely as                            EINSTEIN-PODOLSKY-ROSEN ARGUMENT
in (54), and a similar statement holds with Q and R
switched. One can therefore conclude that the principle
                                                                                    The stage is now set for revisiting the EPR argument.
of causal locality stated above in (55) is satisfied within
                                                                                 Referring to Figure 2, suppose that an observer A (‘Al-
this unistochastic formulation of quantum theory.
                                                                                 ice’) has local access to the first subsystem Q, and that
   By contrast, suppose that the two subsystems Q and R                          an observer B (‘Bob’) has local access to the second sub-
are not kept at spacelike separation during the physical                         system R, with no assumption that A and B are in local
process in question, but locally interact at some inter-                         contact with each other. Treating A and B as ordinary
mediate time t′ between 0 and t. Then, again following                           (if complicated) subsystems of the overall stochastic pro-
standard textbook arguments, the overall system’s uni-                           cess, one now has a transition matrix of the form
tary time-evolution operator UQR (t) will fail to tensor-
factorize at t′ :                                                                                               ΓQRAB (t),                               (61)
                                                                                 with individual entries consisting of directed conditional
                      UQR (t′ ) ̸= UQ (t′ ) ⊗ UR (t′ ).                   (59)   probabilities of the form

Because the corresponding transition matrix ΓQR (t) en-                                       p((qt , rt , at , bt ), t|(q0 , r0 , a0 , b0 ), 0).        (62)
codes cumulative statistical effects starting at the ini-
                                                                                 (Note that A and B here do not denote random variables
tial time 0, the transition matrix will continue to fail to
                                                                                 or observables, but refer to subsystems.)
tensor-factorize for all times t ≥ t′ (at least until the next
                                                                                    The calculations ahead, which will be closely related to
division event):
                                                                                 the no-communication theorem [3, 4], will show that the
                                                                                 observer-subsystem B does not exert a causal influence
               ΓQR (t) ̸= ΓQ (t) ⊗ ΓR (t)          [for t ≥ t′ ].         (60)   on the observer-subsystem A. By symmetry, it will also
                                                                                 follow that A does not exert a causal influence on B.
   The breakdown (60) in tensor-factorization for t ≥ t′                            One begins by expressing the directed conditional
is precisely entanglement, as manifested at the level of                         probabilities (62) in the usual Hilbert-space formalism
the underlying indivisible stochastic process. The factor-                       as the following trace:
ization (58) therefore also breaks down, and so one can
conclude that the two subsystems Q and R exert causal                                                tr(Pqt ,rt ,at ,bt ρQRAB (t)).                      (63)
influences on each other, stemming from their local in-                          Here Pqt ,rt ,at ,bt is a rank-one projector onto the state
teraction at the time t′ .                                                       vector |qt , rt , at , bt ⟩,
   Notice that this local interaction, despite being the
‘common cause’ of the correlations between Q and R, is                                     Pqt ,rt ,at ,bt ≡ |qt , rt , at , bt ⟩⟨qt , rt , at , bt |,   (64)
not the sort of ‘variable’ that can be plugged into the                          and ρQRAB (t) is the overall system’s density matrix at
unistochastic theory’s microphysical conditional proba-                          the time t,
bilities. Reichenbach’s principle of common causes (16)
                                                                                                                    †
therefore does not hold.                                                             ρQRAB (t) ≡ UQRAB (t)ρQRAB (0)UQRAB (t),                            (65)
                                                                                                                                              13

with ρQRAB (0) the initial density matrix at the time 0,                       where

           ρQRAB (0) ≡ |q0 , r0 , a0 , b0 ⟩⟨q0 , r0 , a0 , b0 |,        (66)    p(at , t|(q0 , r0 , a0 ), 0)
                                                                                                              
and with UQRAB (t) the unitary time-evolution operator                           ≡ ⟨at |trQR UQA (t ← t′ ) ⊗ 1R
for the overall system.
  Suppose that the two subsystems Q and R locally in-                                                                                
                                                                                                                       †
teract only at a time t′ > 0. Then one can rewrite the                                     |ΨQR , a0 ⟩⟨ΨQR , a0 |     UQA (t ← t′ ) ⊗ 1R |at ⟩.
formula (65) for the overall system’s density matrix at                                                                                     (72)
the later time t ≥ t′ as
                                            †                                  One sees explicitly that there is no causal influence on the
 ρQRAB (t) ≡ UQRAB (t ← t′ )ρQRAB (t′ )UQRAB     (t ← t′ ).                    observer-subsystem A from the observer-subsystem B, in
                                                        (67)                   the sense of causal influences used in this paper. The only
Here UQRAB (t ← t′ ) is the relative time-evolution oper-                      causal influences on the observer-subsystem A are from
ator for the time interval from t′ to t, defined as in (30),                   the two subsystems Q and R, which both intersect the
and ρQRAB (t′ ) is the overall system’s density matrix at                      past light cone of A.
the interaction time t′ ,

      ρQRAB (t′ ) ≡ UQRAB (t′ )ρQRAB (0)UQRAB (t′ ).
                                                                                                     IX.    CONCLUSION
                          = |ΨQR , a0 , b0 ⟩⟨ΨQR , a0 , b0 |,           (68)

with ΨQR denoting the (now-entangled) wave function of                            The past century has seen the appearance of many in-
the subsystem pair (Q, R).                                                     terpretations of quantum theory, nearly all of which treat
   By assumption, the relative time-evolution operator                         the wave function and the Schrödinger equation as the
UQRAB (t ← t′ ) from t′ to t encodes local interactions                        central entities of the theory, and differ on whether to
between the two subsystems Q and A, as well as local                           regard the wave function as a physical object. As a pur-
interactions between the two subsystems R and B, but                           portedly physical object, the wave function would pre-
no local interactions between the subsystem pair (Q, A)                        sumably be understood to be some sort of field on a con-
and the subsystem pair (R, B). Hence, the relative time-                       figuration space of very high dimension, as Schrödinger
evolution operator tensor-factorizes as                                        originally imagined in his early work on what he called
                                                                               ‘undulatory mechanics’ [62], or as existing in an abstract
   UQRAB (t ← t′ ) = UQA (t ← t′ ) ⊗ URB (t ← t′ ).                     (69)   Hilbert space of some very high dimension, as might be
                                                                               more in keeping with Everett’s ‘many worlds’ interpre-
  It follows from a straightforward calculation that the
                                                                               tation [27–29]. Other approaches either augment the
reduced density matrix for the subsystem pair (Q, A) at
                                                                               wave function with additional (‘hidden’) variables, like
the later time t ≥ t′ is given by
                                                                               the pilot-wave approach of de Broglie and Bohm [22–24],
 ρQA (t) ≡ trRB (ρQRAB (t))                                                    or insist that the wave function is merely an instrumen-
                                                                            talist tool for encoding epistemic information about mea-
  = trRB UQA (t ← t′ ) ⊗ URB (t ← t′ )                                         surement settings and results, as in some versions of the
                                                                               Copenhagen interpretation [63].
                                                
                                                                                  None of these approaches provide a particularly hos-
                 
                   †               †
      ρQRAB (t′ ) UQA (t ← t′ ) ⊗ URB (t ← t′ )
                                                                               pitable domain for talking about causation. They either
                                                                               rely inextricably on an interventionist conception of cau-
                           
  = trR UQA (t ← t′ ) ⊗ 1R                                                     sation, or they simply lack the kinds of microphysical
                                                                          ingredients that merit being given causal meanings.
                                   †       ′
          |ΨQR , a0 ⟩⟨ΨQR , a0 | UQA (t ← t ) ⊗ 1R , (70)                         As explained above, the unistochastic formulation of
                                                                               quantum theory reviewed in this paper lies outside the
where 1R is the identity operator on the Hilbert space of                      wave-function paradigm, and is based on treating ev-
the subsystem R. Notice that all the dependence on b0                          ery quantum system as a unistochastic process in dis-
has disappeared. Thus, upon marginalizing over qt , rt ,                       guise [17, 18], an approach that deflates a lot of the
and bt , one finds                                                             exotic talk about quantum phenomena. The laws of
                                                                               this unistochastic process take the form not of differen-
       p(at , t|(q0 , r0 , a0 , b0 ), 0)                                       tial equations, but of directed conditional probabilities,
            X                                                                  which have a long history of admitting an interpretation
        =          p((qt , rt , at , bt ), t|(q0 , r0 , a0 , b0 ), 0)
                                                                               as encoding causal relationships. From this perspective,
             qt ,rt ,bt
                                                                               quantum theory could be understood as a theory of mi-
          = p(at , t|(q0 , r0 , a0 ), 0),                               (71)   crophysical causation par excellence.
14

   By invoking this microphysical notion of causation, one           Variable Theories”. Physical Review Letters, 23(15):880–
can formulate a more straightforward criterion (55) for              884, October 1969. doi:10.1103/PhysRevLett.23.880.
causal locality than Bell’s principle of local causality—in     [12] J. S. Bell. “The Theory of Local Beables”. CERN,
either of its equivalent forms (10) or (11). As this pa-             1975.     URL: https://cds.cern.ch/record/980036/
                                                                     files/197508125.pdf.
per has shown, quantum theory, regarded as a theory of          [13] J. S. Bell. “Bertlmann’s Socks and the Nature of Re-
unistochastic processes, satisfies this improved criterion,          ality”. Journal de Physique Colloque, 42(C2):C2–41,
and is therefore arguably a causally local theory. Re-               March 1981. doi:10.1051/jphyscol:1981202.
markably, one therefore arrives at what appears to be a         [14] D. M. Greenberger, M. A. Horne, and A. Zeilinger.
causally local hidden-variables formulation of quantum               “Going Beyond Bell’s Theorem”.            In Bell’s Theo-
theory, despite many decades of skepticism that such a               rem, Quantum Theory and Conceptions of the Uni-
theory could exist.                                                  verse, Fundamental Theories of Physics, pages 69–
                                                                     72. Springer, 1989. arXiv:0712.0921, doi:10.1007/
                                                                     978-94-017-0849-4_10.
                                                                [15] J. S. Bell. “La Nouvelle Cuisine”. In A. Sarlemijn and
               ACKNOWLEDGMENTS                                       P. Kroes, editors, Between Science and Technology, pages
                                                                     97–115. Elsevier, 1990.
                                                                [16] N. D. Mermin. “Quantum Mysteries Revisited”. Amer-
  The author would especially like to thank Isaac Friend,
                                                                     ican Journal of Physics, 58(8):731–734, 1990. URL:
Wayne Myrvold, Travis Norsen, John Norton, and Ward                  http://dx.doi.org/10.1119/1.16503.
Struyve for helpful discussions.                                [17] J. A. Barandes. “The Stochastic-Quantum Correspon-
                                                                     dence”, 2023.      URL: https://arxiv.org/abs/2302.
                                                                     10778, arXiv:2302.10778.
                                                                [18] J. A. Barandes.        “The Stochastic-Quantum Theo-
                                                                     rem”, 2023. URL: https://arxiv.org/abs/2309.03085,
 [1] B. Skyrms. “Counterfactual Definiteness and Local Cau-          arXiv:2309.03085.
     sation”. Philosophy of Science, 49(1):43–50, March 1982.   [19] E. Schrödinger.      “Discussion of Probability Rela-
     URL: https://doi.org/10.1086/289033;https://www.                tions between Separated Systems”.             Mathematical
     jstor.org/stable/186879, doi:10.1086/289033.                    Proceedings of the Cambridge Philosophical Society,
 [2] B. Skyrms. “EPR: Lessons for Metaphysics”. Midwest              31(04):555–563, October 1935. URL: http://journals.
     Studies in Philosophy, 9(1):245–255, September 1984.            cambridge.org/article_S0305004100013554, doi:10.
     doi:10.1111/j.1475-4975.1984.tb00062.x.                         1017/S0305004100013554.
 [3] G. C. Ghirardi, A. Rimini, and T. Weber. “A General        [20] E. Schrödinger. “Probability Relations Between Sepa-
     Argument Against Superluminal Transmission Through              rated Systems”. Mathematical Proceedings of the Cam-
     the Quantum Mechanical Measurement Process”. Lettere            bridge Philosophical Society, 32(3):446–452, 1936. doi:
     al Nuovo Cimento, 27(10):293–298, 1980. doi:10.1007/            10.1017/S0305004100019137.
     BF02817189.                                                [21] A. Einstein. “Letter to Max Born”, March 1947.
 [4] T. F. Jordan. “Quantum Correlations do not Transmit        [22] L. de Broglie. An Introduction to the Study of Wave
     Signals”. Physics Letters A, 94(6):264, 1983. doi:10.           Mechanics. E. P. Dutton and Company, Inc., 1930.
     1016/0375-9601(83)90713-2.                                 [23] D. J. Bohm. “A Suggested Interpretation of the Quan-
 [5] E. H. Wichmann and J. H. Crichton. “Cluster De-                 tum Theory in Terms of ‘Hidden’ Variables. I”. Physi-
     composition Properties of the S Matrix”. Physical Re-           cal Review, 85(2):166–179, January 1952. doi:10.1103/
     view, 132(6):2788–2799, December 1963. doi:10.1103/             PhysRev.85.166.
     PhysRev.132.2788.                                          [24] D. J. Bohm. “A Suggested Interpretation of the Quan-
 [6] S. Weinberg. The Quantum Theory of Fields, Volume 1.            tum Theory in Terms of ‘Hidden’ Variables. II”. Physi-
     Cambridge University Press, 1996.                               cal Review, 85(2):180–193, January 1952. doi:10.1103/
 [7] D. Howard.      “Einstein on Locality and Separabil-            PhysRev.85.180.
     ity”. Studies in History and Philosophy of Science Part    [25] A. Aspect, J. F. Clauser, and A. Zeilinger. “The No-
     A, 16(3):171–201, 1985. doi:10.1016/0039-3681(85)               bel Prize in Physics 2022”. Nobel Prize Official Website,
     90001-9.                                                        2022. Awarded for experiments with entangled photons,
 [8] D. Howard. “Holism, Separability, and the Metaphysical          establishing the violation of Bell inequalities and pioneer-
     Implications of the Bell Experiments”. In J. T. Cushing         ing quantum information science. URL: https://www.
     and E. McMullin, editors, Philosophical Consequences of         nobelprize.org/prizes/physics/2022/summary.
     Quantum Theory: Reflections on Bell’s Theorem, pages       [26] J. Woodward. “Causation and Manipulability”. In
     224–253. University of Notre Dame Press Notre Dame,             E. N. Zalta and U. Nodelman, editors, The Stan-
     1989.                                                           ford Encyclopedia of Philosophy. Metaphysics Re-
 [9] A. Einstein, B. Podolsky, and N. Rosen. “Can Quantum-           search Lab, Stanford University, Summer 2023 edition,
     Mechanical Description of Physical Reality Be Consid-           2023. URL: https://plato.stanford.edu/archives/
     ered Complete?”. Physical Review, 47(10):777–780, May           sum2023/entries/causation-mani.
     1935. doi:10.1103/PhysRev.47.777.                          [27] H. Everett III. “ ‘Relative State’ Formulation of Quan-
[10] J. S. Bell. “On the Einstein-Podolsky-Rosen Paradox”.           tum Mechanics”. Reviews of Modern Physics, 29(3):454–
     Physics, 1(3):195–200, 1964.                                    462, July 1957. doi:10.1103/RevModPhys.29.454.
[11] J. F. Clauser, M. A. Horne, A. E. Shimony, and R. A.       [28] H. Everett III. “The Theory of the Universal Wave Func-
     Holt. “Proposed Experiment to Test Local Hidden-                tion”. In The Many-Worlds Interpretation of Quantum
                                                                                                                            15

     Mechanics, Volume 1, page 3, 1973.                                of Philosophy. Metaphysics Research Lab, Stan-
[29] B. S. DeWitt.       “Quantum mechanics and reality”.              ford University, Winter 2023 edition, 2023.        URL:
     Physics Today, 23(9):30–35, September 1970. URL:                  https://plato.stanford.edu/archives/win2023/
     http://scitation.aip.org/content/aip/magazine/                    entries/causation-physics.
     physicstoday/article/23/9/10.1063/1.3022331,                 [46] K.-W. Bong, A. Utreras-Alarcón, F. Ghafari, Y.-C.
     doi:10.1063/1.3022331.                                            Liang, N. Tischler, E. G. Cavalcanti, G. J. Pryde, and
[30] W. Myrvold, M. Genovese, and A. Shimony. “Bell’s                  H. M. Wiseman. “A Strong No-Go Theorem on the
     Theorem”. In E. N. Zalta and U. Nodelman, editors,                Wigner’s Friend Paradox”. Nature Physics, August 2020.
     The Stanford Encyclopedia of Philosophy. Metaphysics              arXiv:1907.05607, doi:10.1038/s41567-020-0990-x.
     Research Lab, Stanford University, Spring 2024 edition,      [47] F. A. Bopp. “Quantenmechanische Statistik und Ko-
     2024. URL: https://plato.stanford.edu/archives/                   rrelationsrechnung”. Zeitschrift für Naturforschung A,
     spr2024/entries/bell-theorem.                                     2(4):202–216, 1947. doi:10.1515/zna-1947-0402.
[31] J. J. Sakurai. Modern Quantum Mechanics. Addison             [48] F. A. Bopp.        “Ein für die Quantenmechanik be-
     Wesley, revised edition, 1993.                                    merkenswerter       Satz    der  Korrelationsrechnung”.
[32] R. Shankar. Principles of Quantum Mechanics. Plenum               Zeitschrift für Naturforschung A, 7(1):82–87, 1952.
     Press, 2nd edition, 1994.                                         doi:10.1515/zna-1952-0117.
[33] D. J. Griffiths and D. F. Schroeter. Introduction to Quan-   [49] F. A. Bopp. “Statistische Untersuchung des Grund-
     tum Mechanics. Cambridge University Press, 3rd edition,           prozesses der Quantentheorie der Elementarteilchen”.
     2018.                                                             Zeitschrift für Naturforschung A, 8(1):6–13, 1953. doi:
[34] J. von Neumann.         “Wahrscheinlichkeitstheoretischer         10.1515/zna-1953-0103.
     Aufbau der Quantenmechanik”.             Nachrichten von     [50] I. Fényes.        “Eine wahrscheinlichkeitstheoretische
     der Gesellschaft der Wissenschaften zu Göttingen,                Begründung und Interpretation der Quantenmechanik”.
     Mathematisch-Physikalische Klasse, 1927:245–272, 1927.            Zeitschrift für Physik, 132(1):81–106, February 1952.
     URL: https://eudml.org/doc/59230.                                 doi:10.1007/BF01338578.
[35] J. von Neumann. Mathematische Grundlagen der Quan-           [51] E. Nelson. “Dynamical Theories of Brownian Motion”.
     tenmechanik. Berlin: Springer, 1932.                              1967.
[36] J. von Neumann. Mathematical Foundations of Quantum          [52] E. Nelson. “Quantum Fluctuations”. 1985.
     Mechanics: New Edition. Princeton University Press,          [53] G. C. Ghirardi, A. Rimini, and T. Weber. “Unified
     2018. With the English translation by Robert T. Beyer,            Dynamics for Microscopic and Macroscopic Systems”.
     and edited by Nicholas A. Wheeler.                                Physical Review D, 34(2):470–491, 1986. doi:10.1103/
[37] G. Hermann. “Der Zirkel in Neumann’s Beweis (Section              PhysRevD.34.470.
     7 of Die Naturphilosophischen Grundlagen de Quanten-         [54] E. C. G. Stueckelberg. “Quantum Theory in Real
     mechanik)”. Die Naturphilosophischen Grundlagen de                Hilbert Space”. Helvetica Physica Acta, 33(4):727–
     Quantenmechanik, 1935.                                            752, 1960. URL: https://www.e-periodica.ch/digbib/
[38] M. Seevinck. “Challenging the Gospel: Grete Hermann               view?pid=hpa-001:1960:33::715#735.
     on von Neumann’s No-Hidden-Variables Proof”. In Grete        [55] M. M. Wolf and J. I. Cirac. “Dividing Quantum
     Hermann: Between Physics and Philosophy, Volume 42,               Channels”. Communications in Mathematical Physics,
     pages 107–117. Springer, October 2017. doi:10.1007/               279:147–168, 2008. arXiv:math-ph/0611057, doi:10.
     978-94-024-0970-3_7.                                              1007/s00220-008-0411-y.
[39] J. S. Bell. “On the Problem of Hidden Variables in Quan-     [56] S. Milz and K. Modi. “Quantum Stochastic Processes and
     tum Mechanics”. Reviews of Modern Physics, 38(3):447–             Quantum Non-Markovian Phenomena”. PRX Quantum,
     452, July 1966. doi:10.1103/RevModPhys.38.447.                    2:030201, May 2021. URL: https://dx.doi.org/10.
[40] G. Bacciagaluppi. “The Statistical Interpretation: Born,          1103/PRXQuantum.2.030201, arXiv:2012.01894v2, doi:
     Heisenberg and von Neumann, 1926-27”. October 2021.               10.1103/PRXQuantum.2.030201.
     URL: http://philsci-archive.pitt.edu/19650.                  [57] A. Horn. “Doubly Stochastic Matrices and the Diagonal
[41] A. Shimony. “Events and Processes in the Quantum                  of a Rotation Matrix”. American Journal of Mathemat-
     World”. In R. Penrose and C. Isham, editors, Quan-                ics, 76(3):620–630, 1954. doi:10.2307/2372705.
     tum Concepts in Space and Time, pages 182–203. Oxford        [58] R. C. Thompson. “Lecture notes from a Johns Hopkins
     University Press, Oxford, 1986. Reprinted in Shimony              University lecture series”. Unpublished lecture notes,
     (1993), 140–162.                                                  1989.
[42] H. Reichenbach. The Direction of Time, Volume 65. Univ       [59] W. F. Stinespring. “Positive functions on C*-algebras”.
     of California Press, 1956.                                        Proceedings of the American Mathematical Society,
[43] C. Hitchcock and M. Rédei. “Reichenbach’s Com-                   6(2):211–216, April 1955. doi:10.2307/2032342.
     mon Cause Principle”. In E. N. Zalta, editor, The            [60] M. H. Stone.        “Linear Transformations in Hilbert
     Stanford Encyclopedia of Philosophy. Metaphysics Re-              Space”. Proceedings of the National Academy of Sciences,
     search Lab, Stanford University, Summer 2021 edition,             16(2):172–175, 1930. doi:10.1073/pnas.16.2.172.
     2021. URL: https://plato.stanford.edu/archives/              [61] J. Pearl. Causality: Models, Reasoning and Inference.
     sum2021/entries/physics-Rpcc.                                     Cambridge University Press, 2009.
[44] W. G. Unruh. “Is Quantum Mechanics Non-Local?”. In           [62] E. Schrödinger. “An Undulatory Theory of the Me-
     T. Placek and J. Butterfield, editors, Non-Locality and           chanics of Atoms and Molecules”.           Physical Re-
     Modality, pages 125–136. Springer, 2002. doi:10.1007/             view, 28(6):1049–1070, December 1926. doi:10.1103/
     978-94-010-0385-8_8.                                              PhysRev.28.1049.
[45] M. Frisch. “Causation in Physics”. In E. N. Zalta            [63] W. Heisenberg. Physics and Philosophy: The Revolution
     and U. Nodelman, editors, The Stanford Encyclopedia               in Modern Science. Harper & Brothers Publishers, 1958.

