# entropy

**source:** pdf · **section:** solutions
**file:** Tsirelson_Bound
---

Article
Why the Tsirelson Bound?
Bub's Question and Fuchs' Desideratum
William Stuckey1*'* , Michael Silberstein 2/3 , Timothy M cDevitt4 and Ian Kohler1
 1   Department of Physics, Elizabethtown College, Elizabethtown, PA 17022, USA
 2   Department of Philosophy, Elizabethtown College, Elizabethtown, PA 17022, USA
 3   Department of Philosophy, University of Maryland, College Park, MD 20742, USA
 4   Department of Mathematical Sciences, Elizabethtown College, Elizabethtown, PA 17022, USA
 *   Correspondence: stuckeym@etown.edu

 Received: 30 June 2019; Accepted: 12 July 2019; Published: 15 July 2019                        © check for
                                                                                                  updates

 Abstract: To answer Wheeler's question "Why the quantum?" via quantum information theory
 according to Bub, one must explain both why the world is quantum rather than classical and why
 the world is quantum rather than superquantum, i.e., "Why the Tsirelson bound?" We show that
 the quantum correlations and quantum states corresponding to the Bell basis states, which uniquely
 produce the Tsirelson bound for the Clauser-Horne-Shimony-Holt (CHSH) quantity, can be derived
 from conservation per no preferred reference frame (NPRF). A reference frame in this context
 is defined by a measurement configuration, just as with the light postulate of special relativity.
 We therefore argue that the Tsirelson bound is ultimately based on NPRF just as the postulates
 of special relativity. This constraint-based/principle answer to Bub's question addresses Fuchs'
 desideratum that we "take the structure of quantum theory and change it from this very overt
 mathematical speak ... into something like [special relativity]." Thus, the answer to Bub's question
 per Fuchs' desideratum is, "the Tsirelson bound obtains due to conservation per NPRF".

 Keywords: Tsirelson bound; Bell-CHSH inequality; superquantum correlations; quantum
 information theory

1. Introduction
      Wheeler's opening statement in his 1986 paper, "How Come the Quantum?" holds as true today
as it did then [1]
     The necessity of the quantum in the construction of existence: out of what deeper requirement
     does it arise? Behind it all is surely an idea so simple, so beautiful, so compelling that
     when—in a decade, a century, or a millennium—we grasp it, we will all say to each other,
     how could it have been otherwise? How could we have been so stupid for so long?
The problem is, as Hardy points out, "The standard axioms of [quantum theory] are rather ad hoc.
Where does this structure come from?" [2]. Concerning quantum mechanics, Fuchs writes ([3], p. 285).

     Compare that to one of our other great physical theories, special relativity. One could make
     the statement of it in terms of some very crisp and clear physical principles: The speed of
     light is constant in all inertial frames, and the laws of physics are the same in all inertial
     frames. And it struck me that if we couldn't take the structure of quantum theory and
     change it from this very overt mathematical speak—something that didn't look to have
     much physical content at all, in a way that anyone could identify with some kind of physical
     principle—if we couldn't turn that into something like this, then the debate would go on

Entropy 2019, 21, 692; doi:10.3390/e21070692                                w w w .m dpi.com /journal/entropy
Entropy 2019, 21, 692                                                                                 2 of 17

      forever and ever. And it seemed like a worthwhile exercise to try to reduce the mathematical
      structure of quantum mechanics to some crisp physical statements.
      Special relativity is a principle theory, i.e., its postulates are constraints, so quantum information
theory (QIT) seeks "the reconstruction of quantum theory" via a constraint-based/principle approach [4]
in answering Wheeler's "Really Big Question", "Why the quantum?" [5,6]. Indeed, QIT has produced
several different sets of axioms, postulates, and "physical requirements" in terms of quantum
information (five noted by Fuchs, for example [3]) which all reproduce quantum theory. Bub has
successfully recast Wheeler's question as, "why is the world quantum and not classical, and why is it
quantum rather than superquantum, i.e., why the Tsirelson bound for quantum correlations?" [7-9].
      That is, classical correlations produce a Clauser-Horne-Shimony-Holt (CHSH) quantity [10]
between —2 and 2 (the Bell inequality [11]), quantum correlations produce a CHSH quantity between
—2y/2 and 2y/2 (the Tsirelson bound [12]), and superquantum correlations produce a maximum CHSH
quantity of 4 (the Popescu-Rohrlich (PR) correlations [13]). Classical and quantum correlations exist
in Nature, but superquantum correlations have not been observed. All three correlations satisfy
relativistic causality (the no-signaling condition [14]), so "Why the quantum?" meaning "Why the
quantum correlations?" means answering Bub's question, "Why the Tsirelson bound?"
      An interesting information-theoretic derivation of the Tsirelson bound has been produced via
"information causality" [15], thus it would seem QIT is making great strides in both reconstructing
quantum theory and recasting and answering Wheeler's question. Bub writes, "It's a significant sea
change in the foundations of physics that information-theoretic principles of this sort are investigated
as possible constraints on physical processes" ([9], p. 183).
      Despite all the success of QIT, the community does not find any of the reconstructions compelling.
Cuffaro, for example, argues that information causality needs to be justified in some physical sense [16].
Furthermore, as Hardy states, "When I started on this, what I wanted to see was two or so obvious,
compelling axioms that would give you quantum theory and which no one would argue with" [17].
Fuchs quotes Wheeler, "If one really understood the central point and its necessity in the construction
of the world, one ought to state it in one clear, simple sentence" ([3], p. 302). Asked if he had such a
sentence, Fuchs responded, "No, that's my big failure at this point" ([3], p. 302).
      Herein, we propose a constraint-based answer to QIT's version of "Why the quantum?" that we
can state in "one clear, simple sentence"
      The Tsirelson bound obtains because of conservation per no preferred reference frame.
Assuming the reader is willing to suspend their anthropocentric bias against constraint-based
explanation [18,19], Section 2 shows how the phenomena described by two Bell basis
states, the spin singlet state ^ ^ j ( |+ l —1)— | —1 + 1))^ and the "Mermin photon state"
 (-— (| +1 + 1)+ | —1 —1))^, satisfy conservation of angular momentum [20] per no preferred
reference frame (NPRF) [21]. The term "reference frame" has many meanings in physics related
to microscopic and macroscopic phenomena, Galilean versus Lorentz transformations, relatively
moving observers, etc. Here, a measurement configuration constitutes a reference frame, as with the
light postulate of special relativity. This constraint, conservation per NPRF, reproduces the quantum
correlation function for the Bell-basis-states phenomena whence the Tsirelson bound. We then show
how the quantum states themselves follow from this constraint and NPRF proper. Thus, violations
of the Bell inequality up to the Tsirelson bound follow from quantum correlations obtained from the
conservation of angular momentum per NPRF [22,23]. It is then easy to generalize this constraint to
conservation per NPRF for phenomena described by any of the Bell basis states. Since the quantum
correlations and quantum states associated with the Bell-basis-states phenomena both follow from
the constraint and NPRF, and the Bell basis states uniquely establish the Tsirelson bound [12,24,25],
the Tsirelson bound is ultimately grounded in NPRF, just as special relativity [26].
     Finally, using the Popescu-Rohrlich (PR) correlations, we show how superquantum correlations
that satisfy the no-signaling condition and exceed the Tsirelson bound can violate conservation per
Entropy 2019, 22, 692                                                                                        3 of 17

NPRF. Thus, this result shows explicitly how the quantum correlations responsible for the Tsirelson
bound satisfy conservation per NPRF while both classical and superquantum correlations can violate
this constraint (Figure 1).

                                       Why the quantum? = Why the Tsirelson bound?

                                                      CHSH Quantity

                               -2~2                   - 2V2 <->2V2          PR correlations -> 4

                        Satisfy Bell inequality      Tsirelson bound          No-signaling max

                        Classical Correlations     Quantum Correlations   Superquantum Correlations

                         Violate Constraint         Satisfy Constraint       Violate Constraint

       Figure 1. Summary of the result. The "constraint" is conservation per no preferred reference frame.

     Our explanation of the Tsirelson bound does not require a map from 3N-dimensional Hilbert space
to some "causal influence" in spacetime, e.g., a dynamical interpretation a la Bohmian mechanics,
and it does not require hidden variables (e.g., [27]). That is, the + 1/—1 outcomes (dropping factors of
h/2) for the spin singlet or "Mermin photon" states [28] and the angle between Stern-Gerlach (SG)
magnets or polarizers are all that appear in the quantum correlations uniquely producing the Tsirelson
bound and they are all that is required for our constraint-based explanation.
     Thus, we see explicitly in this result how quantum mechanics conforms statistically to a
conservation principle without need of a "causal influence" or hidden variables acting on a trial-by-trial
basis to account for that conservation. There are many attempts to add such classical mechanisms,
but they are superfluous as far as the physics is concerned. The light postulate of special relativity is a
good analogy for our proposed constraint.
     In special relativity, Alice is moving at velocity Va relative to a light source and measures the
speed of light from that source to be c. Bob is moving at velocity V&relative to that same light source
and measures the speed of light from that source to be c. Here, "reference frame" refers to the relative
motion of the observer and source which then defines a specific measurement of a specific quantity in
the context of all its alternatives. NPRF in this context thus means all measurements produce the same
outcome c. As a consequence of this constraint and NPRF proper (giving the relativity postulate of
special relativity), special relativity is a constraint-based/principle theory.
     In quantum mechanics, Alice orients her SG magnet at a relative to a source of spin entangled
particles and measures +1 or —1 (|). Bob orients his SG magnet at /3 relative to that same source of spin
entangled particles and measures +1 or —1 (|). Here, "reference frame" refers to the relative orientation
of the SG magnets and source which then defines a specific measurement of a specific quantity in
the context of all its alternatives. NPRF in this context means all measurements produce the same
outcome +1 or —1 (|). As a consequence of this constraint, we can only conserve angular momentum
on average between different reference frames, i.e., it cannot be conserved on a trial-by-trial basis
unless the SG magnets or polarizers are co-aligned (Figure 2). As we show below, this constraint
plus NPRF proper (giving P^_= P__ |_) then produce the quantum state, i.e., probability for each
possible measurement outcome. This is quite unlike classical physics (Figures 3 and 4); in fact, it is
what uniquely distinguishes the quantum joint distribution from its classical counterpart [29]. Thus,
NPRF here leads to quantum outcomes (+1/—1 only) and "average-only" conservation (Figure 5),
a constraint-based/principle answer to Bub's question. Thus, our answer to Bub's question satisfying
Fuchs' desideratum is
      The Tsirelson bound obtains because of conservation per no preferred reference frame.
    We do acknowledge that our explanation of the Tsirelson bound lies outside the QIT enterprise
devoted to explaining quantum probability theory via information-theoretic principles over all possible
Entropy 2019, 21,692                                                                                             4 of 17

probability structures [2,3,30]. In the parlance of metaphysics, we have not ruled out some "possible
world" in which superquantum correlations exist, we have only ruled them out on empirical grounds
for our world in accord with physics. However, the result is not without relevance for QIT. From an
information-theoretic perspective, what is actually being conserved in this fashion is the fundamental
unit of binary information, e.g., on-off(ness), on-on(ness), yes-no(ness), etc.
     This is not conservation of information a la information causality; our constraint does not deal
with signals sent between Alice and Bob, but with the spatiotemporal correlations in their measurement
settings and results. Accordingly, we concur with the QIT approach to view quantum mechanics in
terms of spacetime constraints on par with a principle theory such as special relativity (Figure 5),
rather than dynamical laws or processes. Therefore, we feel this constraint-based explanation of
the Tsirelson bound does contribute to the desideratum of QIT. Again, we emphasize that this is
a constraint-based explanation of the Tsirelson bound per physics, so it cannot satisfy any grander
extra-physical expectations, i.e., pure information-theoretic constraints, of some in QIT.

                                                +1 -l           -1 +1
                                                Result          Result

      Figure 2. Outcomes (yellow dots) in the same reference frame, i.e., outcomes for the same measurement
      (blue arrows represent SG magnet orientations), for the spin singlet state explicitly conserve
      angular momentum.

   01 02 03            04 05 06            07      08     09       10      11     12      13 14         15 16
      Figure 3. A spatiotemporal ensemble of 16 experimental trials for the spin singlet state. Angular
     momentum is not conserved in any given trial, because there are two different measurements being
     made, i.e., outcomes are in two different reference frames, but it is conserved on average for all 16 trials.
     It is impossible for angular momentum to be conserved explicitly in each trial since the measurement
     outcomes are binary (quantum) with values of +1 (up) or —1 (down)              Per no preferred reference
     frame. The conservation principle at work here assumes Alice and Bob's measured values of angular
     momentum are not mere components of some hidden angular momentum, e.g., oppositely oriented S/\
     and Sb so that Alice and Bob's + 1 /—1 results are always components of those hidden         and Sg with
     variable magnitudes. That is, the measured values of angular momentum are the angular momenta
     contributing to this conservation principle.
Entropy 2019, 21, 692                                                                                               5 of 17

      Figure 4. Reading from left to right, as Bob rotates his SG magnets relative to Alice's SG magnets for
      her +1 outcome, the average value of his outcome varies from —1 (totally down, arrow bottom) to
      0 to +1 (totally up, arrow tip). This obtains per conservation of angular momentum on average in
      accord with no preferred reference frame. Bob can say exactly the same about Alice's outcomes as
      she rotates her SG magnets relative to his SG magnets for his +1 outcome. That is, their outcomes
      can only satisfy conservation of angular momentum on average, because they only measure + 1 /—1
      ^ | n e v e r a fractional result. Thus, just as with the light postulate of special relativity, we see that no
      preferred reference frame requires quantum (+1/—1) outcomes for all measurements and that leads to
      a constraint-based/principle answer to Bub's question.

                                   Special Relativity                 Quantum Mechanics
                          Empirical Fact: Alice and Bob both   Empirical Fact: Alice and Bob both
                          measure c, regardless of their       measure +1/-1 Q ) , regardless of
                          relative motion
                                                               the ir relative SG orientation
                         Alice(Bob) says of Bob(Alice): Time Alice(Bob) says of Bob(Alice): Must
                         dilation and length contraction     average results
                          NPRF: Relativity of simultaneity     NPRF: 'Average-only' conservation
                         Violate NPRF: Posit empirically       Violate NPRF: Posit empirically
                         unverifiable ether constituting a     unverifiable HV residing in a
                         preferred frame                       preferred frame

      Figure 5. Comparing special relativity with quantum mechanics according to no preferred reference
      frame. Because Alice and Bob both measure the same speed of light c regardless of their relative motion,
      Alice (Bob) may claim that Bob's (Alice's) length and time measurements are erroneous and need to be
      corrected (length contraction and time dilation). Likewise, because Alice and Bob both measure the
      same values for angular momentum + 1 /—1 (j^J regardless of their relative SG magnet orientation,
      Alice (Bob) may claim that Bob's (Alice's) individual + 1 /—1 values are erroneous and need to be
      corrected (averaged). It is possible that Alice and Bob's outcomes are equally valid, i.e., neither need to
      be corrected, per no preferred reference frame. In special relativity, the apparently inconsistent results
      can be reconciled via relativity of simultaneity. In quantum mechanics, the apparently inconsistent
      results can be reconciled via "average-only" conservation. It is also possible that Alice (Bob) is
      actually correct and Bob's (Alice's) outcomes need to be corrected, or that some other frame is actually
      preferred and both Alice and Bob need to correct their outcomes or understand them in the context
      of that preferred frame. In special relativity, we can do that using an empirically unverifiable ether.
      In quantum mechanics, we can do that using empirically unverifiable hidden variables (Figure 3).

2. The Tsirelson Bound from a Conservation Principle
      We assume at this point the reader is prepared to consider a constraint-based/principle
explanation [18,19] of the phenomena responsible for the Tsirelson bound. We present the physics
that is germane to our argument though much of it is doubtless familiar to the reader. The deeper point
is to look at the physics via constraints (Figures 3 and 4), so as to remove the mystery of entanglement
created by dynamical bias (Section 3). While the following analysis itself does not require it, we urge
Entropy 2019, 6 9 2                                                                                 6 of 17

the reader to take seriously the possibility that quantum entanglement is explained not by some
dynamical/causal process in Hilbert space or spacetime, but by constraints on events in spacetime a
la a principle theory
       We start with a specific case, viz., conservation of angular momentum per NPRF,
before generalizing that to conservation per NPRF. More specifically, we consider the spin singlet
state (total anti-correlation) and the "Mermin state" [28] for photons (total correlation) since they
are examples of two Bell basis states with obvious physical meaning. After our presentation of this
transparent conservation principle, we show how it and NPRF proper give the quantum states. We can
then show how conservation of angular momentum per NPRF generalizes to conservation per NPRF
for Bell-basis-states phenomena.
       In principle, the creation of an entangled state due to conservation of angular momentum
is not difficult to imagine, e.g., the dissociation of a spin-zero diatomic molecule [31] or the
decay of a neutral pi meson into an electron-positron pair [32]. In reality, creating a spin singlet
state or the Mermin photon state in a controlled experimental situation is nontrivial [33,34],
i.e., the preparation fragment of the circuit would contain many operations and wires, so we will
suppress the preparation into a spatially localized region which we will call "the source" per
convention (Hardy calls this an "equivalence class of preparations" [30]). The spin singlet state
(total angular momentum equals zero ([35], pp. 29-30)) is            (| ud)— \ ) ) where u/d means the
outcome is displaced upwards/downwards relative to the north-south pole alignment of the SG
magnets. This state obtains due to conservation of angular momentum at the source as represented by
momentum exchange in the spatial plane orthogonal to the source collimation (binary information is
"up or down" transverse).
       The Mermin state for photons (a Bell basis state in the triplet space with total angular momentum
of 1 ([35], pp. 29-30)) is ^ (| VV) + | HH)) where V ("vertical") means the there is an outcome
(photon detection) behind one of the co-aligned polarizers and H ("horizontal") means there is no
outcome behind one of the co-aligned polarizers. This state obtains due to conservation of angular
momentum at the source as represented by momentum exchange along the source collimation (binary
information is "yes or no" longitudinal). At this point, we focus the discussion on the spin singlet state
for total anti-correlation, since everything said of that state can be easily transferred to the Mermin
photon state.
       We wire the preparation to a pair of transformations then wire those to a pair of results, i.e., we
orient the emission directions of the source towards SG magnets and detectors (Figure 6).

                                Alice

     Figure 6.   Alice and Bob making spin measurements with their Stern-Gerlach (SG) magnets
     and detectors.

     The circuits of QIT represent a series of operations in space and time (Figure 7) in accord with
our attempt to explain the spatiotemporal ensemble of spatiotemporal experimental trials for the spin
singlet and Mermin photon states (Figure 3). In this way, we move the discussion from time-evolved
state vectors in 3N-dimensional Hilbert space to the computation of probabilities for circuits in
spacetime using the Feynman path integral. We can obtain the following probability amplitudes for
Entropy 2019, 21, 692                                                                                         7 of 17

the various correlated outcomes of the circuits associated with our spin singlet state using the path
integral method [36,37]
                                        A ,d = - A i ,, = A    - ^   + e'?)                                       (1)

                                        A „, = - A u =            (<■"> - <A)                                     (2)

where a and ji are the SG magnet orientation angles in space (Figure 6). The corresponding probabilities
are then
                               r„i = lA ,/ = IAjbI2= p* = icos2                                                   0)

and
                               p«« = |b4„„|2 = \Add\2 = PM = -sin 2 ( y - ^ j                                     (A

Equations (3) and (4) constihite the "quanhun state" for the spin singlet state. We derive these from
our constraint and NPRF proper below. Likewise, the probabilities for the Mermin photon state are

                                          P vv = Ph h = ^cos2 (a - ft)                                            (5)

and
                                          Pv h = Ph v = ^ S in 2 (a -   0)                                        (6)

Equations (5) and (6) constihite the quanhun state for the Mermin photon state. We also derive these
from our constraint and NPRF proper below. Each probability for a particular circuit is spatiotemporal
in that it is the probability for a source emission event with its corresponding orientations of the two
SG magnets (tx and /3) and two outcomes (till, dd, lid, or du), as represented by each trial in Figure 3.
Let us investigate what Alice and Bob discover about this preparation in the various spatiotemporal
classical contexts of their transformations and results.

      Figure 7. "It is always possible to provide a complete foliation for a circuit" ([30], p. 20). Reproduced
      with permission from the author.

      Alice's detector responds up and down with equal frequency regardless of the orientation ci of her
SG magnet, i.e., she obtains the same outcome regardless of her measurement per NPRF. Bob observes
the same regarding his SG magnet orientation /3. Thus, the source is rotationally invariant in the
spatial plane orthogonal to the source collimation in this spacetime context per NPRF. When Bob and
Alice compare their outcomes, they find that their outcomes are perfectly anti-correlated (ud and du
with equal frequency) when a —ft = 0, i.e., when making the same measurement. This is consistent
with conservation of angular momentum per classical mechanics between the pair of detection events
(this fact defines the state). The degree of that anti-correlation diminishes as a —ft —» j until it is
equal to the degree of correlation (uu and dd) when their SG magnets are at right angles to each other.
 Entropy 2019, 21, 692                                                                               8 of 17

 In other words, whenever the SG magnets are orthogonal to each other, anti-correlated and correlated
 outcomes occur with equal frequency, i.e., conservation of angular momentum in one direction is
 independent of the angular momentum changes in any orthogonal direction. Thus, we would not
 expect to see more correlation or more anti-correlation based on conservation of angular momentum
 for transverse results in the spatial plane orthogonal to the source collimation when the SG magnets
 are orthogonal to each other. Notice that once their SG magnets are not co-aligned, the conservation
 between them obtains in a purely statistical sense, since we can no longer have explicit cancellation of
 Alice and Bob's measured values (Figure 4).
       As we continue to increase the angle oc —ft beyond j the anti-correlations continue to diminish
 until we have totally correlated outcomes when the SG magnets are anti-aligned. This is also consistent
 with conservation of angular momentum, since the totally correlated results when the SG magnets are
 anti-aligned represent momentum exchanges in opposite directions in the spatial plane orthogonal to
 the source collimation just as when the SG magnets are aligned, it is now simply the case that what
 Alice calls up. Bob calls down and vice-versa.
       The counterpart for the Mermin photon state is simply that angular momentum conservation
 is evidenced by VV or HH outcomes for co-aligned polarizers (again, this fact defines the state),
 i.e., when making the same measurement. When the polarizers are at right angles you have only VH
 and HV outcomes, which is still totally consistent with conservation of angular momentum as "not H"
 implies 1/ and vice-versa [34]. In other words, a polarizer does not have a "north-south" distinction
 (longitudinal rather than transverse momentum exchange). In particular, having rotated either or both
 polarizers by n one should obtain precisely 1/1/ or HH outcomes again.
       One might then ask (rhetorically for this audience) whether or not it is possible to explain the
 conservation of angular momentum per NPRF for this spin singlet circuit using classical probability
 theory. Of course, that would be a hidden variable theory amenable to counterfactual definiteness
 (Mermin's "instruction sets" [28,38]) on a trial-by-trial basis. This possibility is explored using
 correlations where the probability of outcomes i and j for settings a and b is written p(i,j \ a, b) [16].
 We start with the fact that Alice's outcomes are not influenced by Bob's settings and vice-versa

                                        p(A | a ,b )
                                                       II

                                        p(A \ a',b )
                                                       II

                                                                                                        (7)
                                        p(B\ a ,b )
                                                       II

                                        p(B\ a ,b')
                                                       II

 This is the no-signaling condition alluded to above. Next, we write the average of outcomes i •; for
 settings a and b as
                                      («/&> = E (* -;)-p (» //l« /& )                             (8)
 and construct the Clauser-Horne-Shimony-Holt (CHSH) quantity

b)+                                             (a,b') + (   b) - (   b')                               (9)

 If one attempted to instantiate the momentum exchanges of the spin singlet circuit using instruction
 sets/ counterfactual definiteness/hidden variables per classical probability theory in accord with
 no-signaling. Equation (9) would give a value between 2 and —2 (CHSH version of Bell's
 inequality [11]). However, Equations (3) and (4) per quantum mechanics put into Equations (8)
 and (9) give
                         —cos {a —b ) —cos {a —bf) —cos (a1—b) + cos (a1—bf)                     (10)
 Choosing a = tt/4, af = —7t / 4 , b = 0, and bf = n / 2 minimizes Equation (10) at —2y/l (the
 Tsirelson bound).
Entropy 2019, 21, 692                                                                                 9 of 17

     Everything said here concerning angular momentum conservation per anti-correlated outcomes
of the spin singlet state applies for angular momentum conservation per correlated outcomes of the
Mermin photon state, which gives

                        cos 2 (a —b) + cos 2 (a —bf) + cos 2 {a! —b ) —cos 2 {a! —bf)                   (11)

for Equation (9). Using a = n / 8, a' = —n / 8, b = 0, and bf = n / 4 maximizes Equation (11) at 2y/2
(the Tsirelson bound). Experiments show that the quantum results can be achieved (violating the
Bell inequality), ruling out an explanation of these correlated momentum exchanges via classical
probability theory We now derive these quantum correlations using the conservation of angular
momentum [20] per NPRF. Using that result and NPRF proper, we then be able to derive the quantum
states and generalize the constraint to conservation per NPRF.
     It is easy to see how this follows by starting with total angular momentum of zero for binary
(quantum) outcomes +1 and —1. (This argument is for the spin singlet state and, again, we are
suppressing the factor of h/2. "Binary" entails "quantum" so we stop qualifying it as such.) Alice and
Bob both measure +1 and —1 results with equal frequency for any SG magnet angle (NPRF) and when
their angles are equal they obtain totally anti-correlated outcomes giving total angular momentum of
zero (this is a defining factor). Now, divide Alice's results into two subsets of +1 and —1, each occurring
N /2 times when the total number of measurements is N (the argument is symmetric with respect to
Bob, obviously). Contrary to classical mechanics, conservation of angular momentum per NPRF does
not allow us to make a definitive prediction about a particular outcome at Bob's location based on a
particular corresponding outcome at Alice's location when Bob's SG magnet is rotated by 6 relative to
Alice's, because Bob only ever measures +1 or —1 per NPRF, i.e., no fractions (again, this fact alone
distinguishes the quantum joint distribution from its classical counterpart [29]) (Figure 3).
     By definition, the correlation function for these N pairs of results is

                        ^ ^ _ (+ 1) a ( - 1)b + (+ 1) a (+ 1)b + ( - 1) a (~ 1)b + -                    ^ 2)

Now, organize the numerator into two equal subsets; the first is that of all Alice's +1 results (+1 )a and
the second is that of all Alice's —1 results (—1)a

                                ■       (+1) a (EBA+) + (-1 ) a (EBA-)
                                                                                                        (13)
                                ‘ /P) ~              N
where EBA+ is the sum of all of Bob's results corresponding to Alice's result (+1)a and EBA- is
the sum of all of Bob's results corresponding to Alice's result (—1)^. Again, we could just as well
have used Bob's results (+1) b and (—1)g and obtained averages over Alice's results instead, since the
situation is symmetric (NPRF). Now, rewrite Equation (13) as

                                        — -(+ 1 )a BA+ + - ( —1)a BA—                                   (14)

with the overline denoting average. To obtain the quantum correlation function, we need some
principle that specifies BA+ and BA—, and we propose that principle is our particular form of
conservation. Here is how one might argue for the principle using classical reasoning applied to the
quantum exchange of momentum.
     The projection of the angular momentum vector of Alice's particle              = +1 oc along jS is    •
/3 = + cos 0 where again 0 is the angle between the unit vectors oc and jS. From Alice's perspective,
when Bob makes the same measurement, i.e., jS = oc, he finds the angular momentum vector of his
particle is Sp = —1oc, so that   + Sg = Sjotai = 0. When he does not make the same measurement,
he should obtain a fraction of the length of Sg, i.e., Sb • /3 = —lcc • jS = —cos 0 (this also follows from
counterfactual spin measurements on the single-particle state [39]). Of course, per NPRF, Bob only
  Entropy 2019, 21, 692                                                                              10 of 17

  ever obtains +1 or —1, so we posit that Bob will average the required —cos 6 (Figures 3 and 4), which
  means
                                             BA+ = - cos0                                           (15)
  Likewise, for Alice's (—1)a results, we have

                                                      BA— = cos 0                                       (16)

  Putting these into Equation (14), we obtain

                               («/jS) = ^ ( + 1 ) a ( - cos0) + i ( —1) a (cos0) =   cos                (17)

  which is precisely the correlation function given by quantum mechanics. This derivation of the
  quantum correlation function is independent of the formalism of quantum mechanics, instead it
  follows from a compelling and simple physical principle, the conservation of angular momentum
  per NPRF. Now, let us use this result and derive the corresponding quantum state, i.e.. Equations (3)
  and (4).
       We need to find Puu, Ppp, Pluj, and P^u/ thus we need four independent conditions.
  Normalization gives
                                        Puu + Pud + Pdu + pdd = l                                 (18)
  and our correlation function

               M > = (+ 1) a (+ 1 ) b Puu + ( + 1 ) a ( - 1                                ) BPud+              +

  along with our constraint represented by Equations (14)-(16) give

                                                  Puu ~ Pud = ~ 2 cos ^                                 (20)

  and
Pdu                                                      - Pdd =2 COS0                                  (21)
  Finally, NPRF gives Pu^ = P^u/ since Pu^ is Alice's up results paired with Bob's down results and Pdu
  is Bob's up results paired with Alice's down results. Solving these four equations for Puu, P^, Pu^,
  and Pfa gives precisely Equations (3) and (4).
        Notice that since the angle between SG magnets oc — ft is twice the angle between Hilbert
  space measurement bases, this result easily generalizes to conservation per NPRF of whatever the
  measurement outcomes represent when unlike outcomes entail conservation. All one need do is
  let 0     20 in the above analysis, understanding that 0 now represents the angle between Hilbert
  space measurement bases. The origin of the more general conservation principle is transparent in
  the next example where the angle between polarizers oc —ft equals the angle between Hilbert space
  measurement bases.
        For the Mermin photon state, conservation of angular momentum is established by pass
  (designated by +1) and no pass (designated by —1) results through a polarizer. When the polarizers
  are co-aligned, Alice and Bob get the same results, half pass and half no pass. Thus, conservation of
  angular momentum is established by the intensity of the electromagnetic radiation applied to binary
  outcomes for various polarizer orientations. Again, grouping Alice's results into +1 and —1 outcomes
  we see that she would expect [cos20 —sin20] at 6 for her +1 results and [sin20 —cos20] for her —1
  results. Since Bob measures the same thing as Alice for conservation of angular momentum, we posit
Entropy 2019, 21, 692                                                                                               11 of 17

that those are Bob's averages when his polarizer deviates from Alice's by 6. Therefore, the correlation
(oc, jS) of results for conservation of angular momentum per Equation (14) is

                          i(+ l)^ (c o s 20 —sin20) + i ( —l)^(sin20 —cos20) = cos 26                                  (22)

which is precisely the correlation function given by quantum mechanics. Now, let us use this result
and derive the corresponding quantum state, i.e.. Equations (5) and (6).
    As before, we need to find P y y , Ph h , Pv h , and Ph v s o we need four independent conditions.
Normalization and Pyu = Phv are the same as for the spin singlet case. The correlation function

          (#/0) = (+ 1 ) a (+ 1 ) b £ W + (+ 1 ) a (- 1 )b * V h + ( —1) a (+1) b Ph v + ( ~ ^ ) a ( ~ ^ ) b Ph h      (23)

along with our constraint represented by Equation (22) give

                                         P w - Pv h = - - ( s in 20 - cos20)                                           (24)

                                          Ph v ~ Ph h = ^(sin20 - cos20)                                               (25)

Solving these four equations for P y y , Ph h , Pv h , and Ph v gives precisely Equations (5) and (6).
     Notice that, since the angle between polarizers oc —ft equals the angle between Hilbert space
measurement bases, this result immediately generalizes to conservation per NPRF of whatever the
outcomes represent when like outcomes entail conservation. (We expand on the general conservation
principle below.) Consequently, the CHSH quantity that obtains using correlations derived by
demanding strict (each measurement pair) conservation for like settings (same reference frame,
defining the entangled state) and average conservation for unlike settings (different reference frames)
is exactly that of quantum mechanics. That explains the Tsirelson bound per conservation of binary
information over a spatiotemporal ensemble, i.e., conservation per NPRF. Accordingly, expecting
the Bell inequality to be satisfied per classical probability theory means selectively abandoning the
conservation principle proposed here.
     We can now show how superquantum correlations in accord with the no-signaling condition
that can exceed the Tsirelson bound, violate our spacetime symmetry group constraint. We already
know that superquantum correlations must violate this constraint, since the constraint yields quantum
correlations and superquantum correlations exceed quantum correlations. This merely serves as an
example for clarity. The Popescu-Rohrlich (PR) correlations [13]

                                      p (l,l I a,b) = p ( - l , - l | a,b) = ^

                                      p (l,l | a,b') = p(—1, —1 | a,b') = ^
                                                                                 \                                     (26 )
                                      p (l,l | a',b) = p(—1, —1 | a',b) = -

                                      p ( l , - l I a',b') = p ( - 1,1 | a',b') = ^

produce a value of 4 for Equation (9), the largest of any no-signaling possibilities. To explicitly relate
quantum and superquantum correlations, we bring Equation (26) to bear on our spin singlet and
Mermin photon states. Again, we focus the discussion on the spin singlet state and allude to the
obvious manner by which the analysis carries over to the Mermin photon state.
    The last PR correlation certainly makes sense if ar = V, i.e., the total anti-correlation implying
conservation of angular momentum, so let us start there. The third PR correlation makes sense for
b = 7i + bf, where we have conservation of angular momentum with Bob having flipped his coordinate
Entropy 2019, 21, 692                                                                             12 of 17

directions. Likewise, then, the second PR correlation makes sense for a = n + a', where we have
conservation of angular momentum with Alice having flipped her coordinate directions. All of this is
perfectly self-consistent with our constraint, since af and bf are arbitrary per rotational invariance in
the spatial plane orthogonal to the source collimation. However, now, the first PR correlation is totally
at odds with conservation of angular momentum. Both Alice and Bob simply flip their coordinate
directions, so we should be right back to the fourth PR correlation with af a and bf b. Instead,
the PR correlations say that we have total correlation (maximal violation of conservation of angular
momentum) rather than total anti-correlation per conservation of angular momentum, which violates
every other observation. In other words, the set of PR observations violates conservation of angular
momentum in a maximal sense. To obtain the corresponding argument for angular momentum
conservation per the correlated outcomes of the Mermin photon state, simply start with the first PR
correlation and show the last PR correlation maximally violates angular momentum conservation.
     To show the spectrum on which superquantum correlations violate our constraint in this context,
replace the first PR correlation with

                                         p (l,l | a,b) = C
                                         p ( - 1 ,-1 | a,b) = D
                                         p( 1 ,-1 | a,b)= E                                          (27)
                                         p ( - l , l \a ,b )= F

The no-signaling condition in Equation (7) in conjunction with the second and third PR correlations
gives C = D and E = E. That in conjunction with normalization C + D + E + E = 1 and
p (anti-correlation) + p (correlation) = 1 means total anti-correlation is the conservation of angular
momentum per the quantum case while total correlation is the max violation of conservation of
angular momentum per the PR case. Thus, we have a spectrum of superquantum correlations all
violating conservation of angular momentum. The take-home message is that if the correlation is
stronger than that of quantum mechanics, it violates conservation of angular momentum per NPRF.
     Using Equation (27) with the second, third, and fourth PR correlations, we obtain a CHSH
quantity of
                                           3+ C+ D - E - E                                        (28)
As pointed out above, the PR correlations in Equation (26) have C = D = 1/2 and E = E = 0 giving
a CHSH quantity of 4. Furthermore, the angular-momentum-conserving quantum correlations are
C = D = 0 and E = E = 1/2 giving a CHSH quantity of 2. Thus, in this case, the superquantum
correlations violate conservation of angular momentum when the quantum correlation is below the
Tsirelson bound.
     This conclusion also follows from the Mermin photon state by replacing the last PR correlation in
analogous fashion, again with 6 = n. We let a af and b — bf in Equation (27) to replace the fourth
PR correlation and the CHSH quantity becomes

                                          3 - C - D + E+ E                                           (29)

Now, the max violation of conservation of angular momentum occurs for E = E = 1/2 (PR case)
and total conservation of angular momentum occurs for C = D = 1/2 (quantum case). Again,
the quantum correlation gives a CHSH quantity of 2 for this case, satisfying the Bell inequality. Thus,
again, the superquantum correlations violate conservation of angular momentum when the quantum
correlation is below the Tsirelson bound. What is important to see is that correlations stronger than
those of quantum mechanics violate conservation of angular momentum. Since we have not observed
such violations of conservation of angular momentum (CHSH quantity in excess of the the quantum
prediction [40]), we can rule out superquantum correlations on empirical grounds (Figure 1).
Entropy 2019, 21, 692                                                                                      13 of 17

     This spin singlet and Mermin photon state analysis generalizes to any measurement associated
with any of the four Bell basis states
                                           1
                                             ( I + 1 - 1 > - I - 1 + 1))
                                          V2
                                           1
                                             (1 + 1 - 1 ) + 1 - 1 + 1))
                                          Vi
                                           1                                                                  (30)
                                             (1 +1 + 1)+ 1- 1 - 1 »
                                          Vi
                                           1
                                             (1 +1 + 1)-1 - 1 - 1 »
                                          Vi

The eigenvalues for any 2 x 2 Hermitian matrix can be written +1 and —1, so whatever Alice and Bob
are measuring it gives outcomes of +1 or —1 (NPRF). All the states are rotationally invariant in Hilbert
space, so whatever the various measurement settings represent. Bob and Alice always measure unlike
results in like settings for the first two states ("unlike states") and like results for like settings for the last
two states ("like states") as required for explicit conservation of binary information, e.g., on-on(ness),
on-off(ness) or yes-no(ness), when Alice and Bob make the same measurement (general form of our
defining factor). Further, Bob and Alice measure +1 and —1 with equal frequency regardless of their
settings (NPRF), so Alice's results can be split into two equal sets of +1 and —1 outcomes. For her
+1 results, conservation dictates Bob's outcomes will average [cos20 —sin20] for the two like states
and [sin20 —cos20] for the two unlike states where 6 is now the angle between eigenbases in Hilbert
space representing whatever the relative difference in settings means in spacetime. For Alice's —1
results, the two equations are flipped, so we have correlations of =bcos 26 for like and unlike states,
respectively, which give the Tsirelson bound. Of course. Bob can make the same claim about Alice's
outcomes satisfying conservation on average with his +1 and —1 outcomes.
      For the spin singlet case, 6 between bases in Hilbert space is half the angle oc —ft between the SG
magnets while the angle between the polarizers oc —ft in the Mermin photon case is equal to the angle 6
between bases in Hilbert space. Thus, the derivations of the quantum correlations and quantum states
using our constraint and NPRF proper for the spin singlet and Mermin photon cases immediately
generalize to any Bell basis state analysis in Hilbert space. Consequently, our constraint in a very
general sense is conservation per NPRF.
      Classical correlations violate the constraint by not reaching the upper limit of the quantum
correlations (Tsirelson bound) as usual, and superquantum correlations violate the constraint by
exceeding the quantum correlations. Specifically, the probability of measuring unlike results for the
unlike states is cos20 and the probability of measuring like results is sin20 (generalized spin singlet
case). Similarly, the probability of measuring like results for the like states is cos20 and the probability
of measuring unlike results is sin20 (generalized Mermin photon case).
      Start with the unlike states. The last PR correlation says that a' and bf must be parallel (cos20 = 1,
Figure 8). The third PR correlation says a' and b must be perpendicular (sin20 = 1, Figure 8).
Furthermore, the second PR correlation says a and bf must be perpendicular (sin20 = 1, Figure 8).
Thus, these three PR correlations in total say a'/bf is perpendicular to a/b (Figure 8). Thus, we need
the first PR correlation to say a and b are parallel, but of course it says that a and b must also be
perpendicular (sin20 = 1). Therefore, the PR correlations violate our constraint in a maximal fashion
for the unlike states.
Entropy 2019, 21, 692                                                                                         14 of 17

                                                    a' or b'

                                                                       a or b

      Figure 8. Relative eigenbases configuration for the unlike states of Equation (30) satisfying the last
      three PR correlations.

      Now, for the like states: The last PR correlation says that a' and b' must be perpendicular
(sin2# = 1, Figure 9). The third PR correlation says a' and b must be parallel (cos26 = 1, Figure 9).
Furthermore, the second PR correlation says a and b' must be parallel (cos2# = 1, Figure 9). Thus,
these three PR correlations in total say                                             a' ib/s perpendicular to a / b ' (Figure 9).
first PR correlation to say a and b are perpendicular, but of course it says a and b must also be parallel
(cos 29 =1). Therefore, the PR correlations also violate our constraint in a maximal fashion for the
like states.

                                                   a' or b

                                                                      a or b'

      Figure 9. Relative eigenbases configuration for the like states of Equation (30) satisfying the last three
      PR correlations.

     Again, replacing the first PR correlation with Equation (27) and using the no-signaling condition
Equation (7) in conjunction with the second and third PR correlations gives C — D and
The CHSH quantity is 3 +C + D —E —fFor both the unlike and like states. We just showed that,
for both like and unlike states, we need C = D = 0 and                 1/2 to satisfy conservation per
NPRF, but the PR correlations are just the opposite, C = D = 1/2 and                0. This shows how
superquantum correlations violate our constraint in a very general sense.

3. Discussion
     Given the widely recognized fundamental importance of conservation principles following from
the spacetime symmetry group, this spin singlet state and Mermin photon state analysis suggests
that our constraint-based approach provides a "motivated principle" requested by Cuffaro [16].
Furthermore, just as the light postulate of special relativity is in accord with NPRF, the Bell basis states
producing the Tsirelson bound are also in accord with NPRF. Alice and Bob each measure +1 and
—1 with equal frequency for all measurement settings, they confirm conservation in all trials where
their measurement settings (reference frames) are the same, and Alice (Bob) can argue that Bob (Alice)
averages less than 1 to satisfy conservation in her (his) choice of measurement setting when the settings
(reference frames) are not the same (Figures 3 and 4).
Entropy 2019, 21, 692                                                                              15 of 17

     Thus, our constraint-based/principle answer to Bub's question, "Why the Tsirelson bound?" [7-9],
the QIT counterpart to Wheeler's "Really Big Question", "Why the quantum?", can be summed up in
"one clear, simple sentence"
      The Tsirelson bound obtains because of conservation per NPRF.
in accord with Fuchs' desideratum (Figure 5).
       The bottom line is that a compelling constraint ("who would argue with conservation per NPRF?")
answers "Why the Tsirelson bound?" without a corresponding "dynamical/causal influence" or
hidden variables to account for the results on a trial-by-trial basis. By accepting the constraint-based
explanation as fundamental, the lack of a compelling, consensus dynamical interpretation is not a
problem. This is just one of many mysteries in physics created by dynamical thinking and resolved by
constraint-based thinking [19].
       Since the Tsirelson bound follows more generally from the mathematical form of any Bell basis
state, regardless of what that state represents physically, one could argue that the Tsirelson bound
results more generally or more fundamentally from a conservation of binary information. That is,
from an information-theoretic perspective, the Tsirelson bound results from a frame independent
conservation of on-on(ness), on-off (ness), yes-no(ness), etc. However, this conservation of binary
information is not information exchanged from Alice (Bob) to Bob (Alice) as in information causality,
but information distributed among both Alice and Bob via a spatiotemporal ensemble. Nonetheless,
the constraint-based approach certainly negates the need for dynamical interpretation, which is a
QIT desideratum.
       One of the many motivations for the QIT approach is the suspicion that realism about the formal
machinery of ordinary textbook quantum mechanics is not warranted. For example, the measurement
problem is driven by taking seriously the unitary evolution of quantum states in Hilbert space.
Likewise, quantum entanglement is thought to require nonlocal causal influences, inexplicable
non-separability/holism, backwards causation, etc., precisely because it is assumed there must be some
dynamical or causal explanation of some sort. However, as we have shown herein, without invoking
mere instrumentalism or deflationary tactics, one can explain quantum entanglement and the Tsirelson
bound without any of that dynamical baggage and without realism about Hilbert space. As the QIT
community hypothesized, the explanation is a constraint-based/principle one.
       Therefore, we believe our constraint-based answer to "Why the Tsirelson bound?" not only
justifies the spirit of the QIT constraint-based approach, but provides a physical model of the quantum
in spacetime per the interpretation-project (Figures 2-4), albeit not a dynamical model. As things stand
now, there is no obvious connection between the interpretation-project and the QIT-project [41]. In this
regard, keep in mind that the postulates of special relativity are about the physical world in spacetime;
thus, in keeping with this analogy, QIT must eventually make such correspondence to reach their lofty
goals and escape the clever, but inherent instrumentalism of ordinary quantum. Our explanation of
the Tsirelson bound precisely addresses the need for QIT to make correspondence with phenomena
in spacetime.
       The resistance to Einstein's light postulate was immense because he posited something as
axiomatic that most people wanted to have explained. We understand the resistance to our constraint,
conservation per NPRF, will be at least as fierce even though it satisfies QIT's stated desideratum,
i.e., they wanted to answer "Why the Tsireslon bound?" per postulates such as those of special relativity.
Thus, ironically, some in QIT may not be satisfied with our constraint-based/principle explanation of
the Tsirelson bound precisely because it posits conservation per NPRF without further explanation;
they desire some "extra-physical" explanation for this constraint, e.g., information causality. In the
parlance of metaphysics, the complaint is that we have not ruled out some "possible world" in which
superquantum correlations exist, we have only ruled them out on empirical grounds for our world.
On this way of thinking, superquantum correlations can only be ruled out via mathematical or logical
necessity from some extra-physics basis.
Entropy 2019, 21, 692                                                                                       16 of 17

      Herein, we have answered Bub's question within the purview of physics in precise analogy with
the light postulate of special relativity in accord with Fuchs' desideratum, i.e., the Tsirelson bound
ultimately obtains because of conservation in accord with no preferred reference frame. Accordingly,
there is nothing mysterious about the physics we have discovered so far, it points unambiguously to
a physical reality governed fundamentally by constraints. Just as the QIT community suspected,
mysteries in quantum mechanics arise solely from the misplaced dynamical expectations of its
practitioners. Once we recognize the power of constraints to dispel the mysteries of physics, "we will
all say to each other, how could it have been otherwise? How could we have been so stupid for so
long?" [1].

Author Contributions: Conceptualization, W.S. and M.S.; software, T.M.; formal analysis, all authors;
writing—original draft preparation, W.S.; writing—review and editing, all authors; visualization, T.M.;
and supervision, W.S. and M.S.
Funding: This research received no external funding.
Conflicts of Interest: The authors declare no conflict of interest.

References and Notes
1.    Wheeler, J. How Come the Quantum? New Tech. Ideas Quantum Meas. Theory 1986, 480, 304-316. [CrossRef]
2.    Hardy, L. Reconstructing Quantum Theory. In Quantum Theory: Informational Foundations and Foils;
      Chiribella, G., Spekkens, R., Eds.; Springer: Dordrecht, The Netherlands, 2016; pp. 223-248. Available online:
      https://arxiv.org/abs/1303.1538 (accessed on 13 July 2019).
3.    Fuchs, C.; Stacey, B. Some Negative Remarks on Operational Approaches to Quantum Theory. In Quantum
      Theory: Informational Foundations and Foils; Chiribella, G., Spekkens, R., Eds.; Springer: Dordrecht,
      The Netherlands, 2016; pp. 283-305.
4.    Chiribella, G.; Spekkens, R. Introduction. In Quantum Theory: Informational Foundations and Foils;
      Chiribella, G., Spekkens, R., Eds.; Springer: Dordrecht, The Netherlands, 2016; pp. 1-18.
5.    Wheeler, J.A. Information, Physics, Quantum: The Search for Links. In Proceedings III International Symposium
      on Foundations of Quantum Mechanics; Physical Society of Japan: Tokyo, Japan, 1989; pp. 354-358.
6.    Barrow, J.D.; Davies, P.C.W.; Charles L. Harper, J. (Eds.) Science and Ultimate Reality: Quantum Theory,
      Cosmology, and Complexity; Cambridge University Press: New York, NY, USA, 2004.
7.    Bub, J. Why the Quantum? Stud. Hist. Philos. Modern Phys. 2004, 35B, 241-266. [CrossRef]
8.    Bub, J. Why the Tsirelson bound? In The Probable and the Improbable: The Meaning and Role of Probability in
      Physics; Hemmo, M., Ben-Menahem, Y., Eds.; Springer: Dordrecht, The Netherlands, 2012; pp. 167-185.
      Available online: h ttp s://arxiv.org/abs/1208.3744 (accessed on 13 July 2019).
9.    Bub, J. Bananaworld: Quantum Mechanics for Primates; Oxford University Press: Oxford, UK, 2016.
10.   Clauser, J.F.; Horne, M.A.; Shimony, A.; Holt, R.A. Proposed Experiment to Test Local Hidden-Variable
      Theories. Phys. Rev. Lett. 1969, 23, 880-884. [CrossRef]
11.   Bell, J. On the Einstein-Podolsky-Rosen paradox. Physics 1964,1, 195-200. [CrossRef]
12.   CireTson, B. Quantum Generalizations of Bell's Inequality. Lett. Math. Phys. 1980, 4, 93-100. [CrossRef]
13.   Popescu, S.; Rohrlich, D. Quantum nonlocality as an axiom. Found. Phys. 1994, 24, 379-385. [CrossRef]
14.   Buhrman, H.; Massar, S. Causality and Tsirelson's bounds. Phys. Rev. A 2005, 72, 052103. [CrossRef]
15.   Pawlowski, M.; Paterek, T.; Kaszlikowski, D.; Scarani, V.; Winter, A.; Zukowski, M. Information Causality as
      a Physical Principle. Nature 2009, 461,1101-1104. [CrossRef] [PubMed]
16.   Cuffaro, M.E. Information Causality, the Tsirelson Bound, and the 'Being-Thus' of Things. Available online:
      http://philsci-archive.pitt.edU/14027/l/tbound.pdf (accessed on 13 July 2019).
17.   Ball, P. Physicists Want to Rebuild Quantum Theory from Scratch. Wired 2017. Available online:
      https://www.wired.com/story/physicists-want-to-rebuild-quantum-theory-from-scratch/amp (accessed on
      13 July 2019).
18.   Silberstein, M.; Stuckey, W. Quantum Mechanics and the Consistency of Conscious Experience. 2019.
      Available online: https://arxiv.org/abs/1901.10825 (accessed on 13 July 2019).
19.   Silberstein, M.; Stuckey, W.; McDevitt, T. Beyond the Dynamical Universe: Unifying Block Universe Physics and
      Time as Experienced; Oxford University Press: Oxford, UK, 2018.
Entropy 2019, 21, 692                                                                                         17 of 17

20.   Unnikrishnan, C.S. Correlation functions. Bell's inequalities and the fundamental conservation laws.
      Europhys. Lett. 2005, 69,489-495. [CrossRef]
21.   We cite and use Unnikrishnan's result for the spin singlet state, but his analysis is for spin angular momentum
      only, which he generalizes to higher spin states, while our constraint is generalized for the conservation of
      anything represented by the Bell basis states. He also makes no mention of the Tsirelson bound, no preferred
      reference frame, special relativity, or superquantum correlations, so our analysis is a decidedly different
      application of this conceptual example.
22.    It is possible for subsets of an entangled collection of particles to violate the Tsirelson bound [23], but of
      course these would not necessarily satisfy conservation of angular momentum and do not violate the
      Tsirelson inequality.
23.   Cabello, A. Violating Bell's inequality beyond Cirel'son's bound. Phys. Rev. Lett. 2002,88,060403. [CrossRef]
      [PubMed]
24.   Landau, L.J. On the violation of Bell's inequality in quantum theory. Phys. Lett. A 1987,120,54-56. [CrossRef]
25.   Khalfin, L.A.; Tsirelson, B.S. Quantum/Classical Correspondence in the Light of Bell's Inequalities.
      Pound. Phys. 1992, 22, 879-948. [CrossRef]
26.    In this analysis, we are merely pointing out how certain empirical and mathematical facts associated with
      the Tsirelson bound lend themselves to a parallel with a principle approach to special relativity, precisely per
      Fuchs' desideratum. Therefore, our analysis does not and cannot rule out any particular interpretation of
      quantum mechanics. This includes any particular interpretation of quantum probability
27.   Ghirardi, G.; Romano, R. Arbitrary violation of the Tsirelson bound. Phys. Rev. A 2012,86,022116. [CrossRef]
28.   Mermin, N. Quantum mysteries refined. Am. }. Phys. 1994, 62, 880-887. [CrossRef]
29.   Garg, A.; Mermin, N. Bell Inequalities with a Range of Violation that Does Not Diminish as the Spin Becomes
      Arbitrarily Large. Phys. Rev. Lett. 1982, 49, 901-904. [CrossRef]
30.   Hardy, L. Reformulating and Reconstructing Quantum Theory. 2011. Available online: h ttp s://arxiv.org/
      abs/1104.2066 (accessed on 13 July 2019).
31.   Bohm, D. Quantum Theory; Prentice-Hall: New Jersey, NJ, USA, 1952.
32.   La Rosa, A. Introduction to Quantum Mechanics, Lecture 12, Quantum Entanglement. Available online: https:
      / / www.pdx.edu/nanogroup/sites/www.pdx.edu.nanogroup/files/QUANTUMENTANGLEMENT_18.
      pdf (accessed on 13 July 2019).
33.   Hensen, B. Experimental Loophole-Free Violation of a Bell Inequality Using Entangled Electron Spins
      Separated by 1.3 km. 2015.          Available online: https://arxiv.org/pdf/1508.05949.pdf (accessed on
      13 July 2019).
34.   Dehlinger, D.; Mitchell, M. Entangled photons, nonlocality, and Bell inequalities in the undergraduate
      laboratory. Am. }. Phys. 2002, 70, 903-910. [CrossRef]
35.   Renes, J. Quantum Information Theory. 2015. Available online: http://edu.itp.phys.ethz.ch/hsl5/Q IT /
      renes_lecture_notesl4.pdf (accessed on 13 July 2019).
36.   Sinha, S.; Sorkin, R. A Sum-over-histories Account of an EPR(B) Experiment. Pound. Phys. Lett. 1991,
      4, 303-335. [CrossRef]
37.   Wharton, K.; Miller, D.; Price, H. Action duality: A constructive principle for quantum foundations.
      Symmetry 2011, 3, 524-540. [CrossRef]
38.   Mermin, N. Bringing home the atomic world: Quantum mysteries for anybody. Am. J. Phys. 1981,
      49, 940-943. [CrossRef]
39.   Boughn, S. Making Sense of Bell's Theorem and Quantum Nonlocality. 2017. Available online: https:
      //arxiv.org/abs/1703.11003 (accessed on 13 July 2019).
40.   Poh, H.S.; Joshi, S.K.; Cere, A.; Cabello, A.; Kurtsiefer, C. Approaching Tsirelson's Bound in a Photon Pair
      Experiment. Phys. Rev. Lett. 2015,115,180408. [CrossRef] [PubMed]
41.   Timpson, C.G. Quantum Information Theory & the Foundations of Quantum Mechanics; Oxford University Press:
      Oxford, UK, 2013.

                         (c) 2019 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access
                         article distributed under the terms and conditions of the Creative Commons Attribution
                         (CC BY) license (http://creativecommons.Org/licenses/by/4.0/).

