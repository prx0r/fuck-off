# THE INTERPRETATION OF QUANTUM MECHANICS:

**source:** pdf · **section:** solutions
**file:** Tegmark
---

                                                                 MANY WORLDS OR MANY WORDS?

                                                                                              Max Tegmark
                                                                     Institute for Advanced Study, Princeton, NJ 08540; max@ias.edu
                                                                                           (September 15, 1997)
                                                     As cutting-edge experiments display ever more extreme forms of non-classical behavior, the pre-
                                                    vailing view on the interpretation of quantum mechanics appears to be gradually changing. A
                                                    (highly unscientific) poll taken at the 1997 UMBC quantum mechanics workshop gave the once all-
                                                    dominant Copenhagen interpretation less than half of the votes. The Many Worlds interpretation
                                                    (MWI) scored second, comfortably ahead of the Consistent Histories and Bohm interpretations.
                                                    It is argued that since all the above-mentioned approaches to nonrelativistic quantum mechanics
                                                    give identical cookbook prescriptions for how to calculate things in practice, practical-minded ex-
arXiv:quant-ph/9709032v1 15 Sep 1997

                                                    perimentalists, who have traditionally adopted the “shut-up-and-calculate interpretation”, typically
                                                    show little interest in whether cozy classical concepts are in fact real in some untestable metaphys-
                                                    ical sense or merely the way we subjectively perceive a mathematically simpler world where the
                                                    Schrödinger equation describes everything — and that they are therefore becoming less bothered
                                                    by a profusion of worlds than by a profusion of words.
                                                    Common objections to the MWI are discussed. It is argued that when environment-induced deco-
                                                    herence is taken into account, the experimental predictions of the MWI are identical to those of the
                                                    Copenhagen interpretation except for an experiment involving a Byzantine form of “quantum sui-
                                                    cide”. This makes the choice between them purely a matter of taste, roughly equivalent to whether
                                                    one believes mathematical language or human language to be more fundamental.

                                                        I. INTRODUCTION                                 II. THE MWI: WHAT IT IS AND WHAT IT ISN’T

                                         At the quantum mechanics workshop to which these                  Much of the old criticism of the MWI was based on
                                       proceedings are dedicated, held in August 1997 at                confusion as to what it meant. Here we grant Everett the
                                       UMBC, the participants were polled as to their preferred         final say in how the MWI is defined, since he did after
                                       interpretation of quantum mechanics. The results are             all invent it [1], and take it to consist of the following
                                       shown in Table 1.                                                postulate alone:
                                               Interpretation              Votes                            • EVERETT POSTULATE:
                                               Copenhagen                     13                              All isolated systems evolve according to the
                                               Many Worlds                     8                                                    d
                                                                                                              Schrödinger equation dt |ψi = − h̄i H|ψi.
                                               Bohm                            4
                                               Consistent Histories            4                        Although this postulate sounds rather innocent, it has
                                               Modified dynamics (GRW/DRM)     1                        far-reaching implications:
                                               None of the above/undecided    18
                                                                                                            1. Corollary 1: the entire Universe evolves according
                                       Although the poll was highly informal and unscientific                  to the Schrödinger equation, since it is by definition
                                       (several people voted more than once, many abstained,                   an isolated system.
                                       etc), it nonetheless indicated a rather striking shift in
                                       opinion compared to the old days when the Copenhagen                 2. Corollary 2: there can be no definite outcome
                                       interpretation reigned supreme. Perhaps most striking of                of quantum measurements (wavefunction collapse),
                                       all is that the Many Worlds interpretation (MWI), pro-                  since this would violate the Everett postulate.
                                       posed by Everett in 1957 [1–3] but virtually unnoticed for       Because of corollary 1, “universally valid quantum me-
                                       about a decade [4,5], has survived 25 years of fierce crit-      chanics” is often used as a synonym for the MWI. What
                                       icism and occasional ridicule to become the number one           is to be considered “classical” is therefore not specified
                                       challenger to the leading orthodoxy, ahead of the Bohm           axiomatically (put in by hand) in the MWI — rather,
                                       [6], Consistent Histories [7] and GRW [8] interpretations.       it can be derived from the Hamiltonian dynamics as de-
                                       Why has this happened? The purpose of the present pa-            scribed in Section III B, by computing decoherence rates.
                                       per is to briefly summarize the appeal of the MWI in                How does corollary 2 follow? Consider a measurement
                                       the light of recent experimental and theoretical progress,       of a spin 1/2 system (a silver atom, say) where the states
                                       and why much of the traditional criticism of it is being         “up” and “down” along the z axis are denoted |↑i and |↓i.
                                       brushed aside.                                                   Assuming that the observer will get happy if she measures
                                                                                                        spin up, we let |-̈ i, |⌣
                                                                                                                                ¨ i and |⌢
                                                                                                                                         ¨ i denote the states of the

                                       To appear in “Fundamental Problems in Quantum Theory”, eds. M. H. Rubin & Y. H. Shih.
observer before the measurement, after perceiving spin              outcome |↓i. Suppose she measures the z-spin of n in-
up and after perceiving spin down, respectively. If the             dependent atoms that all√have spin up in the x-direction
measurement is to be described by a unitary Schrödinger            initially, i.e., α = β = 1/ 2. The final state correspond-
time evolution operator U = e−iHτ /h̄ applied to the total          ing to equation (2) will then contain 2n terms of equal
system, then U must clearly satisfy                                 weight, a typical term corresponding to a seemingly ran-
                                                                    dom sequence of ups and downs, of the form
 U |↑i ⊗ |-̈ i = |↑i ⊗ |⌣
                        ¨i   and U |↓i ⊗ |-̈ i = |↓i ⊗ |⌢
                                                        ¨ i.
                                                          (1)        2−n/2 | ↓↓↑↓↑↑↑↓↓↑ · · ·i ⊗ |⌢
                                                                                                  ¨⌢¨⌣
                                                                                                     ¨⌢¨⌣
                                                                                                        ¨⌣¨⌣
                                                                                                           ¨⌢¨⌢
                                                                                                              ¨⌣¨ · · ·i.
                                                                                                                             (3)
Therefore if the atom is originally in a superposition
α|↑i + β|↓i, then the Everett postulate implies that the            Thus the perceived inside view of what happened accord-
state resulting after the observer has interacted with the          ing to an observer described by a typical element of the
atom is                                                             final superposition is a seemingly random sequence of ups
  U (α|↑i + β|↓i) ⊗ |-̈ i = α|↑i ⊗ |⌣                               and downs, behaving as if generated though a random
                                    ¨ i + β|↓i ⊗ |⌢
                                                  ¨ i.    (2)
                                                                    process with probabilities p = α2 = β 2 = 0.5 for each
In other words, the outcome is not |↑i ⊗ |⌣¨ i or |↓i ⊗ |⌢
                                                         ¨i         outcome. This can be made more formal if we replace
with some probabilities, merely these two states in super-          “⌢¨ ” by “0”, replace “⌣  ¨ ” by “1”, and place a decimal
position. Very few physicists have actually read Everett’s          point in front of it all. Then the above observer state
book (printed in [2]), which has lead to a common mis-              |⌢¨⌢¨⌣ ¨⌢¨⌣¨⌣¨⌣ ¨⌢¨⌢ ¨⌣ ¨ · · ·i = |.0010111001...i, and we
conception that it contains a second postulate along the            see that in the limit n → ∞, each observer state cor-
following lines:                                                    responds to a real number on the unit interval (writ-
                                                                    ten in binary). According to Borel’s theorem on nor-
   • What Everett does NOT postulate:                               mal numbers [10,11], almost all (all except for a set of
     At certain magic instances, the the world undergoes            Borel measure zero) real numbers between zero and one
     some sort of metaphysical “split” into two branches            have a fraction 0.5 of their decimals being “1”, so in the
     that subsequently never interact.                              same sense, almost all terms in our wavefunction describe
                                                                    observers that have perceived the conventional quantum
This is not only a misrepresentation of the MWI, but
                                                                    probability rules to hold. It is in this sense that the MWI
also inconsistent with the Everett postulate, since the
                                                                    predicts apparent randomness from the inside viewpoint
subsequent time evolution could in principle make the
                                                                    while maintaining strict causality from the outside view-
two terms in equation (2) interfere. According to the
                                                                    point.∗ For a clear and pedagogical generalization to the
MWI, there is, was and always will be only one wavefunc-
                                                                    general case with unequal probabilities, see [1,2].
tion, and only decoherence calculations, not postulates,
can tell us when it is a good approximation to treat two
terms as non-interacting.
                                                                    B. “It doesn’t explain why we don’t perceive weird
                                                                                      superpositions”
    III. COMMON CRITICISM OF THE MWI
                                                                       That’s right! The Everett postulate doesn’t! Since the
A. “It doesn’t explain why we perceive randomness”
                                                                    state corresponding to a superposition of a pencil lying
                                                                    in two macroscopically different positions on a table-top
                                                                    is a perfectly permissible quantum state in the MWI,
   Everett’s brilliant insight was that the MWI does                why do we never perceive such states? Indeed, if we
explain why we perceive randomness even though the                  were to balance a pencil exactly on its tip, it would by
Schrödinger equation itself is competely causal. To avoid          symmetry fall down in a superposition of all directions
linguistic confusion, it is crucial that we distinguish be-         (a calculation shows that this takes about 30 seconds),
tween [9]
   • the outside view of the world (the way a mathemat-
     ical thinks of it, i.e., as an evolving wavefunction),
                                                                     ∗
     and                                                               It is interesting to note that Borel’s 1909 theorem made a
                                                                    strong impression on many mathematicians of the time, some
   • the inside view, the way it is perceived from the              of whom had viewed the entire probability concept with a
     subjective frog perspective of an observer in it.              certain suspicion, since they were now confronted with a the-
                                                                    orem in the heart of classical mathematics which could be
|⌣¨ i and |⌢
           ¨ i have by definition perceived two opposite            reinterpreted in terms of probabilities [11]. Borel would un-
measurement outcomes from their inside views, but share             doubtedly have been interested to know that his work showed
the same memory of being in the state |-̈ i moments ear-            the emergence of a probability-like concept “out of the blue”
lier. Thus |⌢
            ¨ i describes an observer who remembers per-            not only in in mathematics, but in physics as well.
forming a spin measurement and observing the definite

                                                                2
thereby creating such a macrosuperposition state. The               be termed the Platonic paradigm, all of physics is ulti-
inability to answer this question was originally a serious          mately a mathematics problem, since an infinitely intel-
weakness of the MWI, which can equivalently be phrased              ligent mathematician given the equations of the Universe
as follows: why is the position representation so special?          could in principle compute the inside view, i.e., com-
Why do we perceive macroscopic objects in approximate               pute what self-aware observers the Universe would con-
eigenstates of the position operator r and the momen-               tain, what they would perceive, and what language they
tum operator p but never in approximate eigenstates of              would invent to describe their perceptions to one another.
other Hermitian operators such as r + p? The answer                 Thus in the Platonic paradigm, the axioms of an ultimate
to this important question was provided by the realiza-             “Theory of Everything” would be purely mathematical
tion that environment-induced decoherence rapidly de-               axioms, since axioms or postulates in English regarding
stroys macrosuperpositions as far as the inside view is             interpretation would be derivable and thus redundant.
concerned, but this was explicitly pointed out only in              In paradigm 2, on the other hand, there can never be a
the 70’s [12] and 80’s [13], more than a decade after Ev-           “Theory of Everything”, since one is ultimately just ex-
erett’s original work. This elegant mechanism is now                plaining certain verbal statements by other verbal state-
well-understood and rather uncontroversial [14], and the            ments — this is known as the infinite regress problem
interested reader is referred to [15] and a recent book             (e.g., [20]).
on decoherence [16] for details. Essentially, the position             The reader who prefers the Platonic paradigm should
basis gets singled out by the dynamics because the field            find the MWI natural, whereas the reader leaning to-
equations of physics are local in this basis, not in any            wards paradigm 2 probably prefers the Copenhagen in-
other basis.                                                        terpretation. A person objecting that the MWI is
   Historically, the collapse postulate was introduced to           “too weird” is essentially saying that the inside and
suppress the off-diagonal density matrix elements ele-              outside views are extremely different, the latter being
ments corresponding to strange macrosuperpositions (cf.             “weird”, and therefore prefers paradigm 2. In the Pla-
[17]). However, many physicists have shared Gottfried’s             tonic paradigm, there is of course no reason whatsoever
view that “the reduction [collapse] postulate is an ugly            to expect the inside view to resemble the outside view, so
scar on what would be beautiful theory if it could be               one expects the correct theory to seem weird. One rea-
removed” [18], since it is not accompanied by any equa-             son why theorists are becoming increasingly positive to
tion specifying when collapse occurs (when the Everett              the MWI is probably that past theoretical breakthroughs
postulate is violated). The subsequent discovery of de-             have shown that the outside view really is very different
coherence provided precisely such an explicit mechanism             from the inside view. For instance, a prevalent mod-
for suppression of off-diagonal elements, which is essen-           ern view of quantum field theory is (e.g., [21,22]) that
tially indistinguishable from the effect of a postulated            the standard model is merely an effective theory, a low-
Copenhagen wavefunction collapse from an observational              energy limit of a yet to be discovered theory that is even
(inside) point of view (e.g. [19]). Since this eliminates ar-       more removed from our cozy classical concepts (perhaps
guably the main motivation for the collapse postulate, it           involving superstrings in 26 dimensions, say). General
may be a principal reason for the increasing popularity             Relativity has already introduced quite a gap between
of the MWI.                                                         the outside view (fields obeying covariant partial differ-
                                                                    ential equations on a 4-dimensional manifold) and the
                                                                    inside view (where we always perceive spacetime as lo-
               C. “It’s too weird for me”                           cally Minowski, and our perceptions depend not only on
                                                                    where we are but also on how fast we are moving).
  The reader must choose between two tenable but dia-                  One reason why experimentalists are becoming increas-
metrically opposite paradigms regarding physical reality            ingly positive to the MWI is probably that they have re-
and the status of mathematics:                                      cently produced so many “weird” (but perfectly repeat-
                                                                    able) experimental results (Bell inequality violations with
   • PARADIGM 1: The outside view (the mathe-                       kilometer baselines [23], molecule interferometry [24],
     matical structure) is physically real, and the inside          vorticity quantization in a macroscopically large amount
     view and all the human language we use to describe             of liquid Helium [25], etc.), and therefore simply accept
     it is merely a useful approximation for describing             that the world is a weirder place than we thought it was
     our subjective perceptions.                                    and get on with their calculations.
   • PARADIGM 2: The subjectively perceived in-
     side view is physically real, and the outside view
                                                                                 D. “Many words” objections
     and all its mathematical language is merely a use-
     ful approximation.
                                                                      The questions addressed in Sections III A and III B
What is more basic — the inside view or the outside                 are in the author’s opinion quite profound, and were an-
view? What is more basic — human language or math-                  swered thanks to the ingenuity of Everett and the dis-
ematical language? Note that in case 1, which might

                                                                3
coverers of decoherence, respectively. However, there are          [30], it is not only suggested that MWI adherents “repre-
also a number of questions/objections that in the au-              sent a relatively small minority” and “tend to be working
thor’s opinion belong in the category “many words”, be-            in other areas of physics” (both in apparent contradiction
ing issues of semantics rather than physics. When dis-             to the above-mentioned poll), but also that they “tend to
cussing the MWI, it is of course within the context of the         have non-standard views on the nature of scientific the-
Platonic paradigm described above, paradigm 1, where               ories”. In our terminology, this “objection” presumable
equations are ultimately more fundamental than words.              reflects the obvious fact that MWI adherents subscribe
Since human language is merely something that certain              to paradigm 1 rather than 2. Moreover, Galileo once held
observers have invented to describe their subjective per-          “non-standard” views on the epicycle theory of planetary
ceptions, many words describe concepts that by neces-              motion.
sity are just useful approximations (cf. [26]). We know               A large number of other objections have been raised
that the classical concept of gas pressure is merely an            against the MWI, tacitly based on some variant of
approximation that breaks down if we consider atomic               paradigm 2. The opinion of this author is that if
scales, and in the Platonic paradigm, we should not be             paradigm 1 is adopted, then there are no outstanding
surprised if we find that other traditional concepts (e.g.,        problems with the MWI when decoherence is taken into
that of physical probability, and indeed the entire notion         account (as discussed in e.g. [16,19,32]).
of a classical world) also turn out to be merely convenient
approximations.
   As an example of a “many words” objection, let us                             IV. IS THE MWI TESTABLE?
consider the rather subtle claim that the MWI does not
justify the use of the word “probability” [27]. When our                     A. The “shut-up-and-calculate” recipe
observer is described by the state |-̈ i before measuring
her atom, there is no aspect of the measurement out-                  When comparing the contenders in Table 1, it is im-
come of which she has epistemological uncertainty (lack            portant to distinguish between their experimental pre-
of knowledge): she simply knows that with 100% cer-                dictions and their philosophical interpretation. When
tainty, she will end up in a superposition of |⌣     ¨ i and       confronted with experimental questions, adherents of the
|⌢¨ i. After the measurement, there is still no epistemo-          first four will all agree on the following cookbook pre-
logical uncertainty, since both |⌣   ¨ i and |⌢
                                              ¨ i know what        scription for how to compute the right answer, which we
they have measured. For those who feel that the word               will term the “shut-up-and-calculate”† recipe:
probability should only be used when there is true lack
of knowledge, probabilities can readily be introduced by                   Use the Schrödinger equation in all your cal-
performing the experiment while the observer is sleep-                     culations. To compute the probability for
ing, and placing her bed in one of two identical rooms                     what you personally will perceive in the end,
depending on the outcome [28]. On awakening, the ob-                       simply convert to probabilities in the tradi-
server described by either of the two states in the super-                 tional way at the instant when you become
position can thus say that she is in the first room with                   mentally aware of the outcome. In practice,
50% probability in the sense that she has lack of knowl-                   you can convert to probabilities much earlier,
edge as to where she is. If there were 2n identical rooms                  as soon as the superposition becomes “macro-
and n measurements dictated the room number in bi-                         scopic”, and you can determine when this oc-
nary, then the observers in the final superposition could                  curs by a standard decoherence calculation.
compute probabilities for observing specific numbers of
zeroes and ones in their room number. Moreover, these              The fifth contender (a dynamical reduction mechanism
could have been computed in advance of the experiment,             such as that proposed by Ghirardi, Rimini & Weber) is
used as gambling odds, etc., before the orthodox linguist          the only one in the table to prescribe a different calcu-
would allow us to call them probabilities, which is why            lational recipe, since it modifies the Heisenberg equation
they are a useful concept regardless of what we call them.         of motion ρ̇ = −i[H, ρ]/h̄ by adding an extra term [8].
   Let us also consider a paper entitled “Against Many-
Worlds Interpretations” by Kent [29,30]. Although most
of its claims were subsequently shown to result from mis-                              B. Quantum suicide
conceptions [31] (as to the definition of the MWI, as to
the mathematical distinction between “measure” [of a                 The fact that the four most popular contenters in Ta-
subset] and “norm” [of a vector], etc.), it also contained         ble 1 have given identical predictions for all experiments
a number of objections in the “many words” category.               performed so far probably explains why practical-minded
In Section II.A, the author states that “one needs to de-
fine [...] the preferred basis [...] by an axiom.” Accord-
ing to what preconceived notion is this necessary, since
decoherence can determine the preferred basis dynami-               †
                                                                        The author is indebted to Anupam Garg for this phrase.
cally? In the foreword to a 1997 version of this paper

                                                               4
physicists show so little interest in interpretational ques-              Many physicists would undoubtedly rejoice if an om-
tions. Is there then any experiment that could distin-                 niscient genie appeared at their death bed, and as a re-
guish between say the MWI and the Copenhagen in-                       ward for life-long curiosity granted them the answer to
terpretation using currently available technology? (Cf.                a physics question of their choice. But would they be
[33,34].) The author can only think of one: a form of                  as happy if the genie forbade them from telling anybody
quantum suicide in a spirit similar to so-called quantum               else? Perhaps the greatest irony of quantum mechanics
roulette. It requires quite a dedicated experimentalist,               is that if the MWI is correct, then the situation is quite
since it is amounts to an iterated and faster version of               analogous if once you feel ready to die, you repeatedly
Schrödinger’s cat experiment [35] — with you as the cat.              attempt quantum suicide: you will experimentally con-
   The apparatus is a “quantum gun” which each time its                vince yourself that the MWI is correct, but you can never
trigger is pulled measures
                    √          the z-spin of a particle in the         convince anyone else!
state (|↑i + |↓i)/ 2. It is connected to a machine gun
that fires a single bullet if the result is “down” and merely             The author wishes to thank David Albert, Orly Al-
makes an audible click if the result is “up”. The details of           ter, Geoffrey Chew, Angélica de Oliveira-Costa, Michael
the trigger mechanism are irrelevant (an experiment with               Gallis, Bill Poirier, Svend Erik Rugh, Marlan Scully,
photons and a half-silvered mirror would probably be                   Robert Spekkens, Lev Vaidman, John Wheeler and Wo-
cheaper to implement) as long as the timescale between                 jciech Zurek (some of whom disagree passionately with
the quantum bit generation and the actual firing is much               the opinions expressed in the present paper!) for thought-
shorter than that characteristic of human perception, say              provoking and entertaining discussions. This work was
10−2 seconds. The experimenter first places a sand bag in              supported by Hubble Fellowship #HF-01084.01-96A,
front of the gun and tells her assistant to pull the trigger           awarded by the Space Telescope Science Institute, which
ten times. All contenders in Table 1 agree that the “shut-             is operated by AURA, Inc. under NASA contract NAS5-
up-and-calculate” prescription applies here, and predict               26555.
that she will hear a seemingly random sequence of shots
and duds such as “bang-click-bang-bang-bang-click-click-
bang-click-click.” She now instructs her assistant to pull
the trigger ten more times and places her head in front
of the gun barrel. This time the shut-up-and-calculate
recipe is inapplicable, since probabilities have no mean-
ing for an observer in the dead state | ××                              [1] Everett, H. 1957, Rev. Mod. Phys, 29, 454
                                              ⌢ i, and the con-
tenders will differ in their predictions. In interpretations            [2] Everett, N. 1973, in The Many-Worlds Interpretation of
where there is an explicit non-unitary collapse, she will                   Quantum Mechanics, ed. DeWitt, B. S. & Graham, N.
                                                                            (Princeton: Princeton Univ. Press)
be either dead or alive after the first trigger event, so she
                                                                        [3] Wheeler, J. A. 1957, Rev. Mod. Phys., 29, 463
should expect to perceive perhaps a click or two (if she
                                                                        [4] Cooper, L. M. & van Vechten, D. 1969, Am. J. Phys, 37,
is moderately lucky), then “game over”, nothing at all.
                                                                            1212
In the MWI, on the other hand, the state after the first                [5] DeWitt, B. S. 1971, Phys. Today, 23 (9), 30
trigger event is                                                        [6] Bohm, D. & Hiley, B. J. 1993, The Undivided Universe:
                                                                        an Ontological Interpretation of Quantum Theory (Lon-
    1                           1                         ××
U √ |↑i + |↓i ⊗ |-̈ i = √ |↑i ⊗ |⌣           ¨ i + |↓i ⊗ | ⌢ i .            don: Routledge)
     2                           2                                      [7] Omnes, R. 1992, The Interpretation of Quantum Mechan-
                                                            (4)             ics (Princeton: Princeton Univ. Press)
                                                                        [8] Ghirardi, G. C., Rimini, A. & Weber, T. 1986, Phys. Rev.
Since there is exactly one observer having perceptions                      D, 34, 470
both before and after the trigger event, and since it oc-               [9] Tegmark, M. 1997, preprint gr-qc/9704009
curred too fast to notice, the MWI prediction is that |-̈ i            [10] Borel, E. 1909, Rend. Circ. Mat. Paleremo, 26, 247
will hear “click” with 100% certainty. When her assis-                 [11] Chung, K. L. 1974, A Course in Probability Theory (New
                                                                            York: Academic)
tant has completed his unenviable assignment, she will
                                                                       [12] Zeh, H. D. 1970, Found. Phys, 1, 69
have heard ten clicks, and concluded that collapse in-
                                                                       [13] Zurek, W. H. 1981, Phys. Rev. D, 24, 1516
terpretations of quantum mechanics are ruled out at a
                                                                            Zurek, W. H. 1982, Phys. Rev. D, 26, 1862
confidence level of 1 − 0.5n ≈ 99.9%. If she wants to rule                  Joos, E. & Zeh, H. D. 1985, Z. Phys. B, 59, 223
them out at “ten sigma”, she need merely increase n by                 [14] Zurek, W. H. 1991, Phys. Today, 44 (10), 36
continuing the experiment a while longer. Occasionally,                [15] Omnès, R. 1997, Phys. Rev. A, in press
to verify that the apparatus is working, she can move her              [16] Giulini, D., Joos, E., Kiefer, C., Kupsch, J., Stamatescu,
head away from the gun and suddenly hear it going off                       I. O. & Zeh, H. D. 1996, Decoherence and the Appear-
intermittently. Note, however, that almost all terms in                     ance of a Classical World in Quantum Theory (Berlin:
the final superposition will have her assistant perceiving                  Springer)
that he has killed his boss.

                                                                   5
[17] von Neumann, J. 1932, Matematische Grundlagen der
     Quanten-Mechanik (Berlin: Springer)
[18] Gottfried, K. 1989, contribution to Erice School “62
     Years of Uncertainty”, unpublished
[19] Tegmark, M. 1993, Found. Phys. Lett, 6, 571
[20] Nozick, R. 1981, Philosophical Explanations (Cambridge:
     Harvard Univ. Press)
[21] Nielsen, H. B. 1983, Phil. Trans. Royal Soc. London,
     A310, 1983
[22] Weinberg, S. 1995, The Quantum Theory of Fields (Cam-
     bridge: Cambridge Univ. Press)
[23] Tapster, P. R., Rarity, J. G. & Owens, P. C. M. 1994,
     Phys. Rev. Lett., 73, 1923
[24] Pritchard, D. et al. 1997, in these proceedings
[25] Schwab, K.,Bruckner, N. & Packard, R. E. 1997, Nature,
     386, 585
[26] Page, D. N. A 1995, preprint gr-qc/9507025
[27] Albert, D. 1997, private communication
[28] Vaidman, L. 1996, quant-ph/9609006, Int. Stud. Phil.
     Sci., in press
[29] Kent, A. 1990, Int. J. Mod. Phys A, 5, 1745
[30] Kent, A. 1997, preprint gr-qc/9703089
[31] Sakaguchi, T. 1997, preprint quant-ph/9704039
[32] Zeh, H. D. 1993, Phys. Lett. A, 172, 189
[33] Deutsch, D. 1986, in Quantum Concepts of Space and
     Time, ed. Penrose, R. & Isham, C. J. (Oxford: Caledonia)
[34] Lockwood, M. 1989, Mind, Brain & the Quantum (New
     York: Blackwell)
[35] Schrödinger, E. 1935, Naturwissenschaften, 23, 807

NOTE:
This paper and a number of related ones are available
online at h t t p://www.sns.ias.edu/˜max/everett.html

                                                                6

