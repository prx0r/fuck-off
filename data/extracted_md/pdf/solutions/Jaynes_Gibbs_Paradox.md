# gibbs, 7/8/1996

**source:** pdf · **section:** solutions
**file:** Jaynes_Gibbs_Paradox
---


                                  THE GIBBS PARADOXy
                                           E. T. Jaynes
                          Department of Physics. Washington University,
                                 St. Louis, Missouri 63130 USA.

Abstract : We point out that an early work of J. Willard Gibbs (1875) contains a correct analysis
of the \Gibbs Paradox" about entropy of mixing, free of any elements of mystery and directly
connected to experimental facts. However, it appears that this has been lost for 100 years, due to
some obscurities in Gibbs' style of writing and his failure to include this explanation in his later
Statistical Mechanics. This \new" understanding is not only of historical and pedagogical interest;
it gives both classical and quantum statistical mechanics a di erent status than that presented in
our textbooks, with implications for current research.

                                           CONTENTS
    1. INTRODUCTION                                                                           2
    2. THE PROBLEM                                                                            3
    3. THE EXPLANATION                                                                        4
    4. DISCUSSION                                                                             6
    5. THE GAS MIXING SCENARIO REVISITED                                                      7
    6. SECOND LAW TRICKERY                                                                    9
    7. THE PAULI ANALYSIS                                                                    10
    8. WOULD GIBBS HAVE ACCEPTED IT?                                                         11
    9. GIBBS' STATISTICAL MECHANICS                                                          13
    10. SUMMARY AND UNFINISHED BUSINESS                                                      17
    11. REFERENCES                                                                           18

y In Maximum Entropy and Bayesian Methods , C. R. Smith, G. J. Erickson, & P. O. Neudorfer, Editors,
Kluwer Academic Publishers, Dordrecht, Holland (1992); pp. 1{22.
2                                           1. Introduction                                            2
1. Introduction
J. Willard Gibbs' Statistical Mechanics appeared in 1902. Recently, in the course of writing a
textbook on the subject, the present writer undertook to read his monumental earlier work on
Heterogeneous Equilibrium (1875{78). The original purpose was only to ensure the historical accu-
racy of certain background remarks; but this was superseded quickly by the much more important
unearthing of deep insights into current technical problems.
     Some important facts about thermodynamics have not been understood by others to this
day, nearly as well as Gibbs understood them over 100 years ago. Other aspects of this \new"
development have been reported elsewhere (Jaynes 1986, 1988, 1989). In the present note we
consider the \Gibbs Paradox" about entropy of mixing and the logically inseparable topics of
reversibility and the extensive property of entropy.
     For 80 years it has seemed natural that, to nd what Gibbs had to say about this, one should
turn to his Statistical Mechanics. For 60 years, textbooks and teachers (including, regrettably, the
present writer) have impressed upon students how remarkable it was that Gibbs, already in 1902,
had been able to hit upon this paradox which foretold { and had its resolution only in { quantum
theory with its lore about indistinguishable particles, Bose and Fermi statistics, etc.
     It was therefore a shock to discover that in the rst Section of his earlier work (which must
have been written by mid{1874 at the latest), Gibbs displays a full understanding of this problem,
and disposes of it without a trace of that confusion over the \meaning of entropy" or \operational
distinguishability of particles" on which later writers have stumbled. He goes straight to the heart
of the matter as a simple technical detail, easily understood as soon as one has grasped the full
meanings of the words \state" and \reversible" as they are used in thermodynamics. In short,
quantum theory did not resolve any paradox, because there was no paradox.
     Why did Gibbs fail to give this explanation in his Statistical Mechanics ? We are inclined to
see in this further support for our contention (Jaynes, 1967) that this work was never nished.
In reading Gibbs, it is important to distinguish between early and late Gibbs. His Heterogeneous
Equilibrium of 1875{78 is the work of a man at the absolute peak of his intellectual powers; no
logical subtlety escapes him and we can nd no statement that appears technically incorrect today.
In contrast, his Statistical Mechanics of 1902 is the work of an old man in rapidly failing health,
with only one more year to live. Inevitably, some arguments are left imperfect and incomplete
toward the end of the work.
     In particular, Gibbs failed to point out that an \integration constant" was not an arbitrary
constant, but an arbitrary function. But this has, as we shall see, nontrivial physical consequences.
What is remarkable is not that Gibbs should have failed to stress a ne mathematical point in almost
the last words he wrote; but that for 80 years thereafter all textbook writers (except possibly Pauli)
failed to see it.
     Today, the universally taught conventional wisdom holds that \Classical mechanics failed to
yield an entropy function that was extensive, and so statistical mechanics based on classical the-
ory gives qualitatively wrong predictions of vapor pressures and equilibrium constants, which was
cleared up only by quantum theory in which the interchange of identical particles is not a real
event". We argue that, on the contrary, phenomenological thermodynamics, classical statistics,
and quantum statistics are all in just the same logical position with regard to extensivity of en-
tropy; they are silent on the issue, neither requiring it nor forbidding it.
     Indeed, in the phenomenological theory Clausius de ned entropy by the integral of dQ=T over
a reversible path; but in that path the size of a system was not varied, therefore the dependence
of entropy on size was not de ned. This was perceived by Pauli (1973), who proceeded to give the
correct functional equation analysis of the necessary conditions for extensivity. But if this is required
already in the phenomenological theory, the same analysis is required a fortiori in both classical
3                                                                                                     3
and quantum statistical mechanics. As a matter of elementary logic, no theory can determine the
dependence of entropy on the size N of a system unless it makes some statement about a process
where N changes.
     In Section 2 below we recall the familiar statement of the mixing paradox, and Sec. 3 presents
the explanation from Gibbs' Heterogeneous Equilibrium in more modern language. Sec. 4 discusses
some implications of this, while Sections 5 and 6 illustrate the points by a concrete scenario. Sec.
7 then recalls the Pauli analysis and Sec. 8 reexamines the relevant parts of Gibbs' Statistical
Mechanics to show how the mixing paradox disappears, and the issue of extensivity of entropy is
cleared up, when the aforementioned minor oversight is corrected by a Pauli type analysis. The
 nal result is that entropy is just as much, and just as little, extensive in classical statistics as in
quantum statistics. The concluding Sec. 9 points out the relevance of this for current research.
2. The Problem
We repeat the familiar story, already told hundreds of times; but with a new ending. There are
n1 moles of an ideal gas of type 1, n2 of another noninteracting type 2, con ned in two volumes
V1; V2 and separated by a diaphragm. Choosing V1=V2 = n1 =n2 , we may have them initially at the
same temperature T1 = T2 and pressure P1 = P2 = n1 RT=V1. The diaphragm is then removed,
allowing the gases to di use through each other. Eventually we reach a new equilibrium state
with n = n1 + n2 moles of a gas mixture, occupying the total volume V = V1 + V2 with uniform
composition, the temperature, pressure and total energy remaining unchanged.
     If the gases are di erent, the entropy change due to the di usion is, by standard thermody-
namics,
                   S = Sf inal , Sinitial = nR log V , (n1 R log V1 + n2 R log V2 )
or,
                              S = ,nR[f log f + (1 , f ) log(1 , f )]                       (1)
where f = n1 =n = V1 =V is the mole fraction of component 1. Gibbs [his Eq. (297)] considers
particularly the case f = 1=2, whereupon
                                           S = nR log 2:
What strikes Gibbs at once is that this is independent of the nature of the gases, \: : : except that
the gases which are mixed must be of di erent kinds. If we should bring into contact two masses
of the same kind of gas, they would also mix, but there would be no increase of entropy." He then
proceeds to explain this di erence, in a very cogent way that has been lost for 100 years. But to
understand it, we must rst surmount a diculty that Gibbs imposes on his readers.
     Usually, Gibbs' prose style conveys his meaning in a suciently clear way, using no more
than twice as many words as Poincare or Einstein would have used to say the same thing. But
occasionally he delivers a sentence with a ponderous unintelligibility that seems to challenge us to
make sense out of it. Unfortunately, one of these appears at a crucial point of his argument; and
this may explain why the argument has been lost for 100 years. Here is that sentence:
    \Again, when such gases have been mixed, there is no more impossibility of the separation
     of the two kinds of molecules in virtue of their ordinary motions in the gaseous mass
     without any especial external in uence, than there is of the separation of a homogeneous
     gas into the same two parts into which it has once been divided, after these have once
     been mixed."
The decipherment of this into plain English required much e ort, sustained only by faith in Gibbs;
but eventually there was the reward of knowing how Champollion felt when he realized that he had
4                                        3. The Explanation                                          4
mastered the Rosetta stone. Suddenly, everything made sense; when put back into the surrounding
context there appeared an argument so clear and simple that it seemed astonishing that it has not
been rediscovered independently dozens of times. Yet a library search has failed to locate any trace
of this understanding in any modern work on thermodynamics or statistical mechanics.
     We proceed to our rendering of that explanation, which is about half direct quotation from
Gibbs, but with considerable editing, rearrangement, and exegesis. For this reason we call it \the
explanation" rather than \Gibbs' explanation". We do not believe that we deviate in any way from
Gibbs' intentions, which must be judged partly from other sections of his work; in any event, his
original words are readily available for comparison. However, our purpose is not to clarify history,
but to explain the technical situation as it appears today in the light of this clari cation from
history; therefore we carry the explanatory remarks slightly beyond what was actually stated by
Gibbs, to take note of the additional contributions of Boltzmann, Planck, and Einstein.
3. The Explanation
When unlike gases mix under the conditions described above, there is an entropy increase S =
nR log 2 independent of the nature of the gases. When the gases are identical they still mix, but
there is no entropy increase. But we must bear in mind the following.
     When we say that two unlike gases mix and the entropy increases, we mean that the gases could
be separated again and brought back to their original states by means that would leave changes in
external bodies. These external changes might consist, for example, in the lowering of a weight, or
a transfer of heat from a hot body to a cold one.
     But by the \original state" we do not mean that every molecule has been returned to its
original position, but only a state which is indistinguishable from the original one in the macroscopic
properties that we are observing. For this we require only that a molecule originally in V1 returns
to V1 . In other words, we mean that we can recover the original thermodynamic state, de ned
for example by specifying only the chemical composition, total energy, volume, and number of
moles of a gas; and nothing else. It is to the states of a system thus incompletely de ned that the
propositions of thermodynamics relate.
     But when we say that two identical gases mix without change of entropy, we do not mean
that the molecules originally in V1 can be returned to V1 without external change. The assertion
of thermodynamics is that when the net entropy change is zero, then the original thermodynamic
state can be recovered without external change. Indeed, we have only to reinsert the diaphragm;
since all the observed macroscopic properties of the mixed and unmixed gases are identical, there
has been no change in the thermodynamic state. It follows that there can be no change in the
entropy or in any other thermodynamic function.
     Trying to interpret the phenomenon as a discontinuous change in the physical nature of the
gases (i. e., in the behavior of their microstates) when they become exactly the same, misses
the point. The principles of thermodynamics refer not to any properties of the hypothesized mi-
crostates, but to the observed properties of macrostates; there is no thought of restoring the original
microstate. We might put it thus: when the gases become exactly the same, the discontinuity is in
what you and I mean by the words \restore" and \reversible".
     But if such considerations explain why mixtures of like and unlike gases are on a di erent
footing, they do not reduce the signi cance of the fact that the entropy change with unlike gases is
independent of the nature of the gases. We may, without doing violence to the general principles
of thermodynamics, imagine other gases than those presently known, and there does not appear
to be any limit to the resemblance which there might be between two of them; but S would be
independent of it.
5                                                                                                     5
     We may even imagine two gases which are absolutely identical in all properties which come
into play while they exist as gases in the di usion cell, but which di er in their behavior in some
other environment. In their mixing an increase of entropy would take place, although the process,
dynamically considered, might be absolutely identical in its minutest details (even the precise path
of each atom) with another process which might take place without any increase of entropy. In
such respects, entropy stands strongly contrasted with energy.
     A thermodynamic state is de ned by specifying a small number of macroscopic quantities such
as pressure, volume, temperature, magnetization, stress, etc. { denote them by fX1 ; X2 ; : : :; Xng
{ which are observed and/or controlled by the experimenter; n is seldom greater than 4. We may
contrast this with the physical state, or microstate, in which we imagine that the positions and
velocities of all the individual atoms (perhaps 1024 of them) are speci ed.
     All thermodynamic functions { in particular, the entropy { are by de nition and construction
properties of the thermodynamic state; S = S (X1 ; X2 ; : : :; Xn ). A thermodynamic variable may
or may not be also a property of the microstate. We consider the total mass and total energy to
be \physically real" properties of the microstate; but the above considerations show that entropy
cannot be.
     To emphasize this, note that a \thermodynamic state" denoted by X  fX1 : : :Xn g de nes a
large class C (X ) of microstates compatible with X . Boltzmann, Planck, and Einstein showed that
we may interpret the entropy of a macrostate as S (X ) = k log W (C ), where W (C ) is the phase
volume occupied by all the microstates in the chosen reference class C . From this formula, a large
mass of correct results may be explained and deduced in a neat, natural way (Jaynes, 1988). In
particular, one has a simple explanation of the reason for the second law as an immediate conse-
quence of Liouville's theorem, and a generalization of the second law to nonequilibrium conditions,
which has useful applications in biology (Jaynes, 1989).
     This has some interesting implications, not generally recognized. The thermodynamic entropy
S (X ) is, by de nition and construction, a property not of any one microstate, but of a certain
reference class C (X ) of microstates; it is a measure of the size of that reference class. Then if two
di erent microstates are in C , we would ascribe the same entropy to systems in those microstates.
But it is also possible that two experimenters assign di erent entropies S; S 0 to what is in fact the
same microstate (in the sense of the same position and velocity of every atom) without either being
in error. That is, they are contemplating a di erent set of possible macroscopic observations on
the same system, embedding that microstate in two di erent reference classes C; C 0 .
     Two important conclusions follow from this. In the rst place, it is necessary to decide at the
outset of a problem which macroscopic variables or degrees of freedom we shall measure and/or
control; and within the context of the thermodynamic system thus de ned, entropy will be some
function S (X1; : : :; Xn ) of whatever variables we have chosen. We can expect this to obey the second
law TdS  dQ only as long as all experimental manipulations are con ned to that chosen set. If
someone, unknown to us, were to vary a macrovariable Xn+1 outside that set, he could produce what
would appear to us as a violation of the second law, since our entropy function S (X1; : : :; Xn ) might
decrease spontaneously, while his S (X1; : : :; Xn ; Xn+1) increases. [We demonstrate this explicitly
below].
     Secondly, even within that chosen set, deviations from the second law are at least conceivable.
Let us return to the mixing of identical gases. From the fact that they mix without change of
entropy, we must not conclude that they can be separated again without external change. On the
contrary, the \separation" of identical gases is entirely impossible with or without external change.
If \identical" means anything, it means that there is no way that an \unmixing" apparatus could
determine whether a molecule came originally from V1 or V2 , short of having followed its entire
trajectory.
6                                           4. Discussion                                           6
     It follows a fortiori that there is no way we could accomplish this separation reproducibly by
manipulation of any macrovariables fXi g. Nevertheless it might happen without any intervention
on our part that in the course of their motion the molecules which came from V1 all return to it at
some later time. Such an event is not impossible; we consider it only improbable.
     Now a separation that Nature can accomplish already in the case of identical molecules, she
can surely accomplish at least as easily for unlike ones. The spontaneous separation of mixed unlike
gases is just as possible as that of like ones. In other words, the impossibility of an uncompensated
decrease of entropy seems to be reduced to improbability.
4. Discussion
The last sentence above is the famous one which Boltzmann quoted twenty years later in his
reply to Zermelo's Wiederkehreinwand and took as the motto for the second (1898) volume of
his Vorlesungen uber Gastheorie. Note the superiority of Gibbs' reasoning. There is none of the
irrelevancy about whether the interchange of identical particles is or is not a \real physical event",
which has troubled so many later writers { including even Schrodinger. As we see, the strong
contrast between the \physical" nature of energy and the \anthropomorphic" nature of entropy,
was well understood by Gibbs before 1875.
      Nevertheless, we still see attempts to \explain irreversibility" by searching for some entropy
function that is supposed to be a property of the microstate, making the second law a theorem of
dynamics, a consequence of the equations of motion. Such attempts, dating back to Boltzmann's
paper of 1866, have never succeeded and never ceased. But they are quite unnecessary; for the
second law that Clausius gave us was not a statement about any property of microstates. The
di erence in S on mixing of like and unlike gases can seem paradoxical only to one who supposes,
erroneously, that entropy is a property of the microstate.
      The important constructive point that emerges from this is that thermodynamics has a greater
  exibility in useful applications than is generally recognized. The experimenter is at liberty to
choose his macrovariables as he wishes; whenever he chooses a set within which there are experi-
mentally reproducible connections like an equation of state, the entropy appropriate to the chosen
set will satisfy a second law that correctly accounts for the macroscopic observations that the
experimenter can make by manipulating the macrovariables within his set.
      We may draw two conclusions about the range of validity of the second law. In the rst place,
if entropy can depend on the particular way you or I decide to de ne our thermodynamic states,
then obviously, the statement that entropy tends to increase but not decrease can remain valid only
as long as, having made our choice of macrovariables, we stick to that choice.
      Indeed, as soon as we have Boltzmann's S = k log W , the reason for the second law is seen
immediately as a proposition of macroscopic phenomenology, true \almost always" simply from
considerations of phase volume. Two thermodynamic states of slightly di erent entropy S1 , S2 =
10,6 =393 cal/deg, corresponding to one microcalorie at room temperature, exhibit a phase volume
ratio
                              W1 =W2 = exp[(S1 , S2 )=k] = exp[1016 ]:                          (2)
Macrostates of higher entropy are sometimes said to `occupy' overwhelmingly greater phase volumes;
put more accurately, macrostates of higher entropy may be realized by an overwhelmingly greater
number, or range, of microstates. Because of this, not only all reproducible changes between
equilibrium thermodynamic states, but the overwhelming majority of all the macrostate changes
that could possibly occur { equilibrium or nonequilibrium { are to ones of higher entropy, simply
because there are overwhelmingly more microstates to go to, by factors like (2). We do not see why
any more than this is needed to understand the second law as a fact of macroscopic phenomenology.
7                                                                                                    7
      However, the argument just given showing how entropy depends, not on the microstate, but
on human choice of the reference class in which it is to be embedded, may appear so abstract that
it leaves the reader in doubt as to whether we are describing real, concrete facts or only a particular
philosophy of interpretation, without physical consequences.
      This is so particularly when we recall that after the aforementioned paper of 1866, Boltzmann
spent the remaining 40 years of his life in inner turmoil and outward controversy over the second
law, repeatedly changing his position. The details are recounted by Klein (1973). In the end this
degenerated into nit{picking arguments over the exact conditions under which his H {function did
or did not decrease. But none of this was ever settled or related to the real experimental facts
about the second law { which make no reference to any velocity distribution! It behooves us to be
sure that we are not following a similar course.
      Fortunately, the concrete reality and direct experimental relevance of Gibbs' arguments is easily
shown. The actual calculation following is probably the most common one found in elementary
textbooks, but the full conditions of its validity have never, to the best of our knowledge, been
recognized. The scenario in which we set it is only slightly fanciful; the discovery of isotopes was
very nearly a realization of it. As examination of several textbooks shows, that discovery prompted
a great deal of confusion over whether entropy of mixing of isotopes should or should not be included
in thermodynamics.
5. The Gas Mixing Scenario Revisited.
Presumably, nobody doubts today that the measurable macroscopic properties of argon (i.e. equa-
tion of state, heat capacity, vapor pressure, heat of vaporization, etc.) are described correctly by
conventional thermodynamics which ascribes zero entropy change to the mixing of two samples of
argon at the same temperature and pressure. But suppose that, unknown to us today, there are two
di erent kinds of argon, A1 and A2, identical in all respects except that A2 is soluble in Whifnium,
while A1 is not (Whifnium is one of the rare superkalic elements; in fact, it is so rare that it has
not yet been discovered).
      Until the discovery of Whifnium in the next Century, we shall have no way of preparing argon
with controllably di erent proportions of A1 and A2. And even if, by rare chance, we should
happen to get pure A1 in volume V 1, and pure A2 in V 2, we would have no way of knowing
this, or of detecting any di erence in the resulting di usion process. Thus all the thermodynamic
measurements we can actually make today are accounted for correctly by ascribing zero entropy of
mixing to argon.
      Now the scene shifts to the next Century, when Whifnium is readily available to experimenters.
What could happen before only by rare chance, we can now bring about by design. We may, at
will, prepare bottles of pure A1 and pure A2. Starting our mixing experiment with n1 = fn moles
of A1 in the volume V1 = fV , and n2 = (1 , f )n moles of A2 in V2 = (1 , f )V , the resulting actual
di usion may be identical in every detail, down to the precise path of each atom, with one that
could have happened by rare chance before the discovery of Whifnium; but because of our greater
knowledge we shall now ascribe to that di usion an entropy increase S given by Eq (1), which
we write as:
                                          S = S1 + S2                                          (3)
where
                                         S1 = ,nRf log f                                        (4a)
                                    S2 = ,nR(1 , f ) log(1 , f )                                (4b)
But if this entropy increase is more than just a gment of our imagination, it ought to have
observable consequences, such as a change in the useful work that we can extract from the process.
8                              5. The Gas Mixing Scenario Revisited.                                  8
      There is a school of thought which militantly rejects all attempts to point out the close relation
between entropy and information, claiming that such considerations have nothing to do with energy;
or even that they would make entropy \subjective" and it could therefore could have nothing to do
with experimental facts at all. We would observe, however, that the number of sh that you can
catch is an \objective experimental fact"; yet it depends on how much \subjective" information
you have about the behavior of sh.
      If one is to condemn things that depend on human information, on the grounds that they are
\subjective", it seems to us that one must condemn all science and all education; for in those elds,
human information is all we have. We should rather condemn this misuse of the terms \subjective"
and \objective", which are descriptive adjectives, not epithets. Science does indeed seek to describe
what is \objectively real"; but our hypotheses about that will have no testable consequences unless
it can also describe what human observers can see and know. It seems to us that this lesson should
have been learned rather well from relativity theory.
      The amount of useful work that we can extract from any system depends { obviously and
necessarily { on how much \subjective" information we have about its microstate, because that tells
us which interactions will extract energy and which will not; this is not a paradox, but a platitude.
If the entropy we ascribe to a macrostate did not represent some kind of human information about
the underlying microstates, it could not perform its thermodynamic function of determining the
amount of work that can be extracted reproducibly from that macrostate.
      But if this is not obvious, it is easily demonstrated in our present scenario. The di usion will
still take place without any change of temperature, pressure, or internal energy; but because of
our greater information we shall now associate it with a free energy decrease F = ,T S . Then,
according to the principles of thermodynamics, if instead of allowing the uncontrolled irreversible
mixing we could carry out the same change of state reversibly and isothermally, we should be able
to obtain from it the work
                                            W = ,F = T S:                                          (5)
Let us place beside the diaphragm a movable piston of Whifnium. When the diaphragm is removed,
the A2 will then di use through this piston until its partial pressure is the same on both sides,
after which we move the piston slowly (to maintain equal A2 pressure and to allow heat to ow in
to maintain constant temperature), in the direction of increasing V1 . From this expansion of A1
we shall obtain the work                  ZV
                                   W1 = P1 dV = n1 RT log(V=V1)
                                         V1

or from (4a),
                                              W1 = T S1                                         (6)
The term S1 in the entropy of mixing therefore indicates the work obtainable from reversible
isothermal expansion of component A1 into the full volume V = V1 + V2 . But the initial di usion
of A2 still represents an irreversible entropy increase S2 from which we obtain no work.
     Spurred by this partial success, the other superkalic element Whafnium is discovered, which
has the opposite property that it is permeable to A1 but not to A2. Then we can make an apparatus
with two superkalic pistons; the Whifnium moves to the right, giving the work W1 = T S1 , while
the Whafnium moves to the left, yielding W2 = T S2 . We have succeeded in extracting just
the work W = T S predicted by thermodynamics. The entropy of mixing does indeed represent
human information; just the information needed to predict the work available from the mixing.
     In this scenario, our greater knowledge resulting from the discovery of the superkalic elements
leads us to assign a di erent entropy change to what may be in fact the identical physical process,
down to the exact path of each atom. But there is nothing \unphysical" about this, since that
9                                                                                                  9
greater knowledge corresponds exactly to { because it is due to { our greater capabilities of control
over the physical process. Possession of a superkalic piston gives us the ability to control a new
thermodynamic degree of freedom Xn+1 , the position of the piston. It would be astonishing if this
new technical capability did not enable us to extract more useful work from the system.
     This scenario has illustrated the aforementioned greater versatility of thermodynamics { the
wider range of useful applications { that we get from recognizing the strong contrast between the
natures of entropy and energy, that Gibbs pointed out so long ago.
     To emphasize this, note that even after the discovery of superkalic elements, we still have the
option not to use them and stick to the old macrovariables fX1 : : :Xn g of the 20'th Century. Then
we may still ascribe zero entropy of mixing to the interdi usion of A1 and A2, and we shall predict
correctly, just as was done in the 20'th Century, all the thermodynamic measurements that we can
make on Argon without using the new technology. Both before and after discovery of the superkalic
elements, the rules of thermodynamics are valid and correctly describe the measurements that it is
possible to make by manipulating the macrovariables within the set that we have chosen to use.
     This useful versatility { a direct result of, and illustration of, the \anthropomorphic" nature
of entropy { would not be apparent to, and perhaps not believed by, someone who thought that
entropy was, like energy, a physical property of the microstate.
6. Second Law Trickery.
Our scenario has veri ed another statement made above; a person who knows about this new degree
of freedom and manipulates it, can play tricks on one who does not know about it, and make him
think that he is seeing a violation of the second law. Suppose there are two observers, one of whom
does not know about A1; A2, and superkalic elements and one who does, and we present them with
two experiments.
      In experiment 1, mixing of a volume V1 of A1 and V2 of A2 takes place spontaneously, without
superkalic pistons, from an initial thermodynamic state Xi to a nal one Xf without any change
of temperature, pressure, or internal energy and without doing any work; so it causes no heat ow
between the di usion cell and a surrounding heat bath of temperature T . To both observers, the
initial and nal states of the heat bath are the same, and to the ignorant observer this is also true
of the argon; nothing happens at all.
      In experiment 2 we insert the superkalic pistons and perform the same mixing reversibly,
starting from the same initial state Xi . Again, the nal state Xf of the argon has the same
temperature, pressure, and internal energy as does Xi . But now work W is done, and so heat
Q = W ows into the di usion cell from the heat bath. Its existence and magnitude could be
veri ed by calorimetry. Therefore, for both observers, the initial and nal states of the heat bath
are now di erent. To the ignorant observer, an amount of heat Q has been extracted from the heat
bath and converted entirely into work: W = Q, while the total entropy of the system and heat
bath has decreased spontaneously by S = ,Q=T , in agrant violation of the second law!
      To the informed observer, there has been no violation of the second law in either experiment.
In experiment 1 there is an irreversible increase of entropy of the argon, with its concomitant loss
of free energy; in experiment 2, the increase in entropy of the argon is exactly compensated by the
decrease in entropy of the heat bath. For him, since there has been no change in total entropy, the
entire process of experiment 2 is reversible. Indeed, he has only to move the pistons back slowly to
their original positions. In this he must give back the work W , whereupon the argon is returned
to its original unmixed condition and the heat Q is returned to the heat bath.
      Both of these observers can in turn be tricked into thinking that they see a violation of the
second law by a third one, still better informed, who knows that A2 is actually composed of two
components A2a and A2b and there is a subkalic element Whoofnium { and so on ad in nitum.
10                                     7. The Pauli Analysis                                      10
A physical system always has more macroscopic degrees of freedom beyond what we control or
observe, and by manipulating them a trickster can always make us see an apparent violation of the
second law.
     Therefore the correct statement of the second law is not that an entropy decrease is impossible
in principle, or even improbable; rather that it cannot be achieved reproducibly by manipulating the
macrovariables fX1 ; : : :; Xng that we have chosen to de ne our macrostate. Any attempt to write
a stronger law than this will put one at the mercy of a trickster, who can produce a violation of it.
     But recognizing this should increase rather than decrease our con dence in the future of the
second law, because it means that if an experimenter ever sees an apparent violation, then instead of
issuing a sensational announcement, it will be more prudent to search for that unobserved degree of
freedom. That is, the connection of entropy with information works both ways; seeing an apparent
decrease of entropy signi es ignorance of what were the relevant macrovariables.
7. The Pauli Analysis
Consider now the phenomenological theory. The Clausius de nition of entropy determines the
di erence of entropy of two thermodynamic states of a closed system (no particles enter or leave)
that can be connected by a reversible path:
                                                  Z 2 dQ
                                        S2 , S1 =      T                                      (7)
                                                     1
Many are surprised when we claim that this is not necessarily extensive; the rst reaction is:
\Surely, two bricks have twice the heat capacity of one brick; so how could the Clausius entropy
possibly not be extensive?" To see how, note that the entropy di erence is indeed proportional
to the number N of molecules whenever the heat capacity is proportional to N and the pressure
depends only on V=N ; but that is not necessarily true, and when it is true it is far from making
the entropy itself extensive.
     For example, let us evaluate this for the traditional ideal monoatomic gas of N molecules and
consider the independent thermodynamic macrovariables to be (T; V; N ). This has an equation
of state PV = NkT and heat capacity Cv = (3=2) Nk, where k is Boltzmann's constant. From
this all elementary textbooks nd, using the thermodynamic relations (@S=@V )T = (@P=@T )V and
T (@S=@T )V = Cv :
                                                     Z 2  @S       @S       
                  S (T2; V2; N ) , S (T1; V1 ; N ) =        @V dV + @T dT
                                                 1           T               V
                                                                                                 (8)
                                              = Nk log VV2 + 32 Nk log TT2
                                                         1               1
It is evident that this is satis ed by any entropy function of the form
                                                               
                                                       3
                            S (T; V; N ) = k N log V + 2 N log T + kf (N )                       (9)

where f (N ) is not an arbitrary constant, but an arbitrary function. The point is that in the
reversible path (7) we varied only T and V ; consequently the de nition (7) determines only the
dependence of S on T and V . Indeed, if N varied
                                              R on our reversible path, then (7) would not be
correct (an extra `entropy of convection' term dN=T would be needed).
11                                                                                                  11
     Pauli (1973) noticed this incompleteness of (7) and saw that if we wish entropy to be extensive,
then that is logically an additional condition, that we must impose separately. The extra condition
is that entropy should satisfy the scaling law
                            S (T; qV; qN ) = qS (T; V; N );    0<q<1                              (10)
Then, substituting (9) into (10), we nd that f (N ) must satisfy the functional equation
                                    f (qN ) = qf (N ) , qN log q                                   (11)
Di erentiating with respect to q and setting q = 1 yields a di erential equation Nf 0 (N ) = f (N ),N ,
whose general solution is
                                     f (N ) = Nf (1) , N log N :                              (12)
[alternatively, just set N = 1 in (11) and we see the general solution]. Thus the most general
extensive entropy function for this gas has the form
                                               V 3                      
                           S (T; V; N ) = Nk log N    + 2 log T + f (1) :                     (13)
It contains one arbitrary constant, f (1), which is essentially the chemical constant. This is not
determined by either the Clausius de nition (7) or the condition of extensivity (10); however, one
more fact about it can be inferred from (13). Writing f (1) = log(Ck3=2), we have
                                                                3=2 
                                S (T; V; N ) = Nk log   CV (kT )       :                      (14)
                                                             N
The quantity in the square brackets must be dimensionless, so C must have the physical dimensions
of (volume),1(energy ),3=2 = (mass)3=2 (action),3 . Thus on dimensional grounds we can rewrite
(13) as
                                             V 3  mkT 
                           S (T; V; N ) = Nk log N + 2 log  2        :                      (15)
where m is the molecular mass and  is an undetermined quantity of the dimensions of action.
It might appear that this is the limit of what can be said about the entropy function from phe-
nomenological considerations; however, there may be further cogent arguments that have escaped
our attention.
8. Would Gibbs Have Accepted It?
Note that the Pauli analysis has not demonstrated from the principles of physics that entropy
actually should be extensive ; it has only indicated the form our equations must take if it is. But
this leaves open two possibilities:
     (1) All this is a tempest in a teapot; the Clausius de nition indicates that only entropy
         di erences are physically meaningful, so we are free to de ne the arbitrary additive
         terms in any way we please. This is the view that was taught to the writer, as a
         student many years ago.
     (2) The variation of entropy with N is not arbitrary; it is a substantive matter with
         experimental consequences. Therefore the Clausius de nition of entropy is logically
12                               8. Would Gibbs Have Accepted It?                                     12
         incomplete, and it needs to be supplemented either by experimental evidence or fur-
         ther theoretical considerations.
The original thermodynamics of Clausius considered only closed systems, and was consistent with
conclusion (1). Textbooks for physicists have been astonishingly slow to move beyond it; that of
Callen (1960) is almost the only one that recognizes the more complete and fundamental nature of
Gibbs' work.
     In the thermodynamics of Gibbs, the variation of entropy with N is just the issue that is
involved in the prediction of vapor pressures, equilibrium constants, or any conditions of equilibrium
with respect to exchange of particles. His invention of the chemical potential  has, according to
all the evidence of physical chemistry, solved the problem of equilibrium with respect to exchange
of particles, leading us to conclusion (2); chemical thermodynamics could not exist without it.
     Gibbs could predict the nal equilibrium state of a heterogeneous system as the one with
maximum total entropy subject to xed total values of energy, mole numbers, and other conserved
quantities. All of the results of his Heterogeneous Equilibrium follow from this variational principle.
He showed that by a mathematical (Legendre) transformation this could be stated equally well
as minimum Gibbs free energy subject to xed temperature and chemical potentials, which form
physical chemists have generally found more convenient (however, it is also less general; in exten-
sions to nonequilibrium phenomena there is no temperature or Gibbs free energy, and one must
return to the original maximum entropy principle, from which many more physical predictions may
be derived).
     This preference for one form of the variational principle over the other is largely a matter of
our conditioning from previous training. For example, from our mechanical experience it seems
intuitively obvious that a liquid sphere has a lower energy than any other shape with the same
entropy; yet to most of us it seems far from obvious that the sphere has higher entropy than any
other shape with the same energy.
     It is interesting to note how the various classical textbooks deal with the question of extensivity;
and then how Gibbs dealt with it. Planck (1926, p. 92), Epstein (1937; p. 136) and Zemansky (1943;
p. 311) do not give the scaling law (10), but simply write entropy as extensive from the start,
apparently considering this too obvious to be in need of any discussion. Callen (1960; p. 26) does
write the scaling law, but does not derive it from anything or derive anything from it; thereafter
he proceeds to write entropy as extensive without further discussion.
     In other words, all of these works simply assume entropy to be extensive without investigating
the question whether that extensivity follows from, or is even consistent with, the Clausius de nition
of entropy. More recent textbooks tend to be even more careless in the logic; the only exception
known to us is that of Pauli. But let us note how much is lost thereby:
(a) The question of extensivity cannot have any universally valid answer; for there are systems,
for example some spin systems and systems with electric charge or gravitational forces, for which
the scaling law (10) does not hold because of long{range interactions; yet the Clausius de nition
of entropy is still valid as long as N is held constant. Such systems cannot be treated at all by a
formalism that starts by assuming extensivity.
(b) This reminds us that for any system extensivity of entropy is, strictly speaking, only an ap-
proximation which can hold only to the extent that the range of molecular forces is small compared
to the dimensions of the system. Indeed, for virtually all systems small deviations from exact
extensivity are observable in the laboratory; the experimentalist calls them \surface e ects" and
we note that Gibbs' Heterogeneous Equilibrium gives beautiful treatments of surface tension and
electrocapillarity, all following from his single variational principle.
13                                                                                                   13
     Obviously, then, Gibbs did not assume extensivity as a general property, as did the others noted
above. But of course, Gibbs was in agreement with them, that entropy is very nearly extensive for
most single homogeneous systems of macroscopic size. But he is careful in saying this, adding    P the
quali cation \- - - , for many substances at least, - - -". Then he gives such relations as G = i ni
which hold in the cases where entropy can be considered extensive to sucient accuracy.
     But Gibbs never does give an explicit discussion of the circumstances in which entropy is or
is not extensive! He appears at rst glance to evade the issue by the device of talking only about
the total entropy of a heterogeneous system, not the entropies of its separate parts. Movement of
particles from one part to another is disposed of by the observation that, if it is reversible, then the
total entropy is unchanged; and that is all he needs in order to discuss all his phenomena, including
surface e ects, fully.
     But on further meditation we realize that Gibbs did not evade any issue; rather, his far
deeper understanding enabled him to see that there was no issue. He had perceived that, when
two systems interact, only the entropy of the whole is meaningful. Today we would say that the
interaction induces correlations in their states which makes the entropy of the whole less than the
sum of entropies of the parts; and it is the entropy of the whole that contains full thermodynamic
information. This reminds us of Gibbs' famous remark, made in a supposedly (but perhaps not
really) di erent context: \The whole is simpler than the sum of its parts." How could Gibbs have
perceived this long before the days of quantum theory?
     This is one more example where Gibbs had more to say than his contemporaries could absorb
from his writings; over 100 years later, we still have a great deal to learn by studying how Gibbs
manages to do things. For him, entropy is not a local property of the subsystems; it is a \global"
property like the Lagrangian of a mechanical system; i.e. it presides over the whole and determines,
by its variational properties, all the conditions of equilibrium { just as the Lagrangian presides over
all of mechanics and determines, by its variational properties, all the equations of motion.
     Up to this point we have been careful to consider only the phenomenology and experimental
facts of thermodynamics, in order to make their independent logical status clear. Most discussions
of these matters mix up the statistical and phenomenological aspects from the start, in a way
that we think generates and perpetuates confusion. In particular, this has obscured the fact that
the fundamental operational de nitions of such terms as equilibrium, temperature, and entropy
{ and the statements of the rst and second laws { involve only the macrovariables observed in
the laboratory. They make no reference to microstates, much less to any velocity distributions,
probability distributions, or correlations. As Helmholtz and Planck stressed, this much of the eld
has a validity and usefulness quite independent of whether atoms and microstates exist.
9. Gibbs' Statistical Mechanics
Now we turn to the nal work of Gibbs, which appeared 27 years after his Heterogeneous Equilib-
rium, and examine the parts of it which are relevant to these issues. We expect that a statistical
theory might supplement the phenomenology in two ways. Firstly, if our present microstate theory
is correct, we would get a deeper interpretation of the basic reason for the phenomenology, and a
better understanding of its range of validity; if it is not correct, we might nd contradictions that
would provide clues to a better theory. Secondly, the theoretical explanation would predict gen-
eralizations; the range of possible nonequilibrium conditions is many orders of magnitude greater
than that of equilibrium conditions, so if new reproducible connections exist they would be almost
impossible to nd without the guidance of a theory that tells the experimenter where to look.
     It is generally supposed that Gibbs coined the term \Statistical Mechanics" for the title of this
book. But in reading Gibbs' Heterogeneous Equilibrium we slowly developed a feeling, from the
above handling of entropy and other incidents in it, that his thermodynamic formalism corresponds
14                                 9. Gibbs' Statistical Mechanics                                    14
so closely to that of Statistical Mechanics { in particular, the grand canonical ensemble { that he
must have known the main results of the latter already while writing the former.
      This suspicion was con rmed in part by the discovery that the term \Statistical Mechanics"
appears already in an Abstract of his dated 1884, of a paper read at a meeting but which, to the best
of our knowledge, was never published and is lost. The abstract states that he will be concerned
with Liouville's theorem and its applications to astronomy and thermodynamics; presumably, the
latter is what appears in the rst three Chapters of his Statistical Mechanics, 18 years later.
      It seems likely, then, that Gibbs found the main results of his Statistical Mechanics very early;
perhaps even as early as his attending Liouville's lectures in 1867. But he delayed nishing the
book for many years, probably because of mysteries concerning speci c heats that he kept hoping
to resolve, but could not before the days of quantum mechanics; his remarks in the preface indicate
how much this bothered him. The parts that seemed unsatisfactory would have been left unwritten
in nal form until the last possible moment; and those parts would be the ones where we are most
likely to nd small errors or incomplete statements.
      Gibbs' concern about speci c heats is no longer an issue for us today, but we want to understand
why classical statistical mechanics appeared (at least to readers of the book) to fail badly in
the matter of extensivity of entropy. He introduces the canonical ensemble in Chapter IV, as a
probability density P (p1 : : :qn ) in phase space, and writes (his Eq. 90; hereafter denoted by SM.90,
etc.):

                                           = ,  = log P                                     (SM:90)
where  = (p1 : : :qn ) is the Hamiltonian (same as the total energy, since he considers only con-
servativeR forces),  is the \modulus" of the distribution, and is a normalization constant chosen
so that Pdp1 ; : : :; dqn = 1. He notes that  has properties analogous to those of temperature,
and strengthens the analogy by introducing externally variable coordinates a1 ; a2 with the mean-
ing of volume, strain tensor components, height in a gravitational eld, etc. with their conjugate
forces Ai = ,@=@ai . On an in nitesimal change (i.e., comparing two slightly di erent canonical
distributions) he nds the identity
                                                      X
                                       d = ,d , Ai dai                                 (SM:114)
where the bars denote canonical ensemble averages. He notes that this is identical in form with a
thermodynamic equation if we neglect the bars and consider (,) as the analog of entropy, which
he denotes, incredibly, by  .
     Here Gibbs anticipates { and even surpasses { the confusion caused 46 years later when Claude
Shannon used H for what Boltzmann had called (,H ). In addition, the prospective reader is warned
that from p. 44 on, Gibbs uses the same symbol  to denote both the \index of probability" as in
(SM.90), and the thermodynamic entropy, as in (SM.116); his meaning can be judged only from
the context. In the following we deviate from Gibbs' notation by using Clausius' symbol S for
thermodynamic entropy.
     Note that Gibbs, writing before the introduction of Boltzmann's constant k, uses , with the
dimensions of energy, for what we should today call kT ; consequently his thermodynamic analog
of entropy is what we should today call S=k, and is dimensionless.?
? In this respect Gibbs' notation is really neater formally { and more cogent physically { than ours; for
Boltzmann's constant is only a correction factor necessitated by our custom of measuring temperature in
arbitrary units derived from the properties of water. A really fundamental system of units would have
k  1 by de nition.
15                                                                                                 15
     The thermodynamic equation analogous to (SM.114) is then
                                               X
                                   d = TdS , Ai dai                                       (SM:116)
Now Gibbs notes that in the thermodynamic equation, the entropy S \is a quantity which is
only de ned by the equation itself, and incompletely de ned in that the equation only determines
its di erential, and the constant of integration is arbitrary. On the other hand, the  in the
statistical equation has been completely de ned." Then interpreting (,) as entropy leads to the
familiar conclusion, stressed by later writers, that entropy is not extensive in classical statistical
mechanics.
      Right here, we suggest, two ne points were missed, but the Pauli analysis conditions us to
recognize them at once. The rst is that normalization requires that P has the physical dimen-
sions (action),n , while the argument of a logarithm should be dimensionless. To obtain a truly
dimensionless  , we should rewrite (SM.90) as  = log( n P ) where  is some quantity of the
dimensions of action. This point has, of course, been noted before many times.
      The second ne point is more serious and does not seem to have been noted before, even by
Pauli; the question whether , is the proper statistical analog of thermodynamic entropy cannot
be answered merely by examination of (SM.114). Let us denote by  the correct (dimensionless)
statistical analog of entropy that Gibbs was seeking. The trouble is again that in (SM.114) we are
varying only  and the ai ; consequently it determines only how  varies with  and the ai . As in
(9), from Gibbs' (SM.114) we can infer only that the correct statistical analog of entropy must have
the form
                                           = , + g (N );                                        (16)
where N = n=3 denotes as before the number of particles. Again, the \constant of integration" is
not an arbitrary constant, but an arbitrary function g (N ). Clearly, no de nite \statistical analog"
of entropy has been de ned until the function g (N ) is speci ed.
     However, in defense of Gibbs, we should note that at this point he is not discussing extensivity
of entropy at all, and so he could reply that he is considering only xed values of N , and so is in
fact concerned only with an arbitrary constant. Thus one can argue whether it was Gibbs or his
readers who missed this ne point (it is only 160 pages later, in the nal two paragraphs of the
book, that Gibbs turns at last to the question of extensivity).
     In any event, a point that has been missed for so long deserves to be stressed. For 60 years, all
scientists have been taught that in the issue of extensivity of entropy we have a fundamental failure,
not just of classical statistics, but of classical mechanics, and a triumph of quantum mechanics.
The present writer was caught in this error just as badly as anybody else, throughout most of his
teaching career. But now it is clear that the trouble was not in any failure of classical mechanics,
but in our own failure to perceive all the freedom that Gibbs' (SM.114) allows. If we wish entropy
to be extensive in classical statistical mechanics, we have only to choose g (N ) accordingly, as was
necessary already in the phenomenological theory. But  R curiously, nobody seems to have noticed,
much less complained, that Clausius' de nition S  dQ=T also failed in the matter of extensivity.
     But exactly the same argument will apply in quantum statistical mechanics; in making the
connection between the canonical ensemble and the phenomenological relations, if we follow Gibbs
and use the Clausius de nition of entropy as our sole guide in identifying the statistical analog of
entropy, it will also allow an arbitrary additive function h(N ) and so it will not require entropy to
be extensive any more than does classical theory. Therefore the whole question of in what way { or
indeed, whether { classical mechanics failed in comparison with quantum mechanics in the matter
of entropy, now seems to be re{opened.
16                                9. Gibbs' Statistical Mechanics                                  16
      Recognizing this, it is not surprising that entropy has been a matter of unceasing confusion
and controversy from the day Clausius discovered it. Di erent people, looking at di erent aspects
of it, continue to see di erent things because there is still un nished business in the fundamental
de nition of entropy, in both the phenomenological and statistical theories.
      In the case of the canonical ensemble, the oversight about extensivity is easily corrected, in
a way exactly parallel to that indicated by Pauli. In the classical case, considering a gas de ned
by the thermodynamic variables A1 = p = pressure, a1 = V = volume, Gibbs' statistical analog
equation (SM.114) may be written
                                           d = ,d , pdV                                       (17)
The statistical analog of entropy must have the form (16); and if we want it to be extensive, it must
also satisfy the scaling law (10). Now from the canonical ensemble for an ideal gas, with phase
space probability density
                                                          X p2 
                                             1
                               P = (2m)3N=2V N exp , 2mi                                      (18)
(which we note is dimensionally correct and normalized, although it does not contain Planck's
constant), we have from the dimensionally corrected (SM.90),

                          , = N log V + 32N [log(2m) + 1] , 3N log                           (19)
Then, substituting (19) and (16) into (10), we nd that g (N ) must satisfy the same functional
equation (11), with the same solution (13). The Gibbs statistical analog of entropy (16) is now
                                                                   
                            = N log N V + 3 log 2m + 3 + g (1) :                           (20)
                                            2      2      2
The extensive property (9) now holds, and the constants g (1) and  combine to form essentially the
chemical constant. This is not determined by the above arguments, just as it was not determined
in the phenomenological arguments.
      Therefore it might appear that the shortcoming of classical statistical mechanics was not any
failure to yield an extensive entropy function, but only its failure to determine the numerical value
of the chemical constant. But even this criticism is not justi ed at present; the mere fact that
it is believed to involve Planck's constant is not conclusive, since e and c are classical quantities
and Planck's constant is only a numerical multiple of e2 =c. We see no reason why the particular
number 137.036 should be forbidden to appear in a classical calculation. Since the problem has not
been looked at in this way before, and nobody has tried to determine that constant from classical
physics, we see no grounds for con dent claims either that it can or cannot be done.
      But the apparent involvement of e and c suggests, as Gibbs himself noted in the preface
to his Statistical Mechanics, that electromagnetic considerations may be important even in the
thermodynamics of electrically neutral systems. Of course, from our modern knowledge of the
electromagnetic structure of atoms, the origin of the van der Waals forces, etc., such a conclusion is
in no way surprising. Electromagnetic radiation is surely one of the mechanisms by which thermal
equilibrium is maintained in any system whose molecules have dipole or quadrupole moments,
rotational/vibrational spectrum lines, etc. and no system is in true thermal equilibrium until it is
bathed in black{body radiation of the same temperature.
      At this point the reader may wonder: Why do we not turn to the grand canonical ensemble, in
which all possible values of N are represented simultaneously? Would this enable us to determine
17                                                                                                   17
by physical principles how entropy varies with N ? Unfortunately, it cannot do so as long as we try
to set up entropy
              R in statistical mechanics by nding a mere analogy with the Clausius de nition of
entropy, S = dQ=T . For the Clausius de nition was itself logically incomplete in just this respect;
the information needed is not in it.
     The Pauli correction was an important step in the direction of getting \the bulk of things" right
pragmatically; but it ignores the small deviations from extensivity that are essential for treatment
of some e ects; and in any event it is not a fundamental theoretical principle. A truly general
and quantitatively accurate de nition of entropy must appeal to a deeper principle which is hardly
recognized in the current literature, although we think that a cogent special case of it is contained
in some early work of Boltzmann, Einstein, and Planck.
10. Summary and Un nished Business.
We have shown here that the Clausius de nition of entropy was incomplete already in the phe-
nomenological theory; therefore it was inadequate to determine the proper analog of entropy in
the statistical theory. The phenomenological theory, classical statistical mechanics, and quantum
statistical mechanics, were all silent on the question of extensivity of entropy as long as one tried to
identify the theoretical entropy merely by analogy with the Clausius empirical de nition. The Pauli
type analysis is a partial corrective, which applies equally well and is equally necessary in all three
cases, if we wish entropy to be extensive.
     It is curious that Gibbs, who surely recognized the incompleteness of Clausius' de nition, did
not undertake to give a better one in his Heterogeneous Equilibrium; he merely proceeded to use
entropy in processes where N changes and never tried to interpret it in such terms as phase volume,
as Boltzmann, Planck, and Einstein did later. In view of Gibbs' performance in other matters, we
cannot suppose that this was a mere oversight or failure to understand the logic. More likely, it
indicates some further deep insight on his part about the diculty of such a de nition.
     A consequence of the above observations is that the question whether quantum theory really
gave an extensive entropy function and determined the value of the chemical constant, also needs
to be re{examined. Before a quantum theory analog of entropy has been de ned, one must consider
processes in which N changes. If we merely apply the scaling law as we did above, the quantum
analog of entropy will have the form (20) in which  is set equal to Planck's constant; but a new
arbitrary constant  fq (1) is introduced that has not been considered heretofore in quantum
statistics. If we continue to de ne entropy by the Clausius de nition (7), quantum statistics does
not determine .
     This suggests that, contrary to common belief, the value of the chemical constant is not
determined by quantum statistics as currently taught, any better than it was by classical theory.
It seems to be a fact of phenomenology that quantum statistics with = 0 accounts fairly well
for a number of measurements; but it gives no theoretical reason why should be zero. The
Nernst Third Law of Thermodynamics does not answer this question; we are concerned rather
with the experimental accuracy of such relations as the Sackur{Tetrode formula for vapor pressure.
Experimental vapor pressures enable us to determine the di erence gas , liquid . Therefore we
wonder how good is the experimental evidence that is not needed, and for how many substances
we have such evidence.
     For some 60 years this has not seemed an issue because one thought that it was all settled
in favor of quantum theory; any small discrepancies were ascribed to experimental diculties and
held to be without signi cance. Now it appears that the issue is reopened; it may turn out that
is really zero for all systems; or it may be that giving it nonzero values may improve the accuracy
of our predictions. In either case, further theoretical work will be needed before we can claim to
understand entropy.
18                                        REFERENCES                                               18
     There is a conceivable simple resolution of this. Let us conjecture that the present common
teaching is correct; i.e., that new precise experiments will con rm that present quantum statistics
does, after all give the correct chemical constants for all systems. If this conjecture proves to be
wrong, then some of the following speculations will be wrong also.
     We should not really expect that a phenomenological theory, based necessarily on a nite
number of observations that happened to feasible in the time of Clausius { or in our time { could
provide a full de nition of entropy in the greatest possible generality. The question is not an
empirical one, but a conceptual one; and only a de nite theoretical principle, that rises above all
temporary empirical limitations, can answer it. In other words, it is a mistake to try to de ne
entropy in statistical mechanics merely by analogy with the phenomenological theory. The only
truly fundamental de nition of entropy must be provided directly by the statistical theory itself;
and comparison with observed phenomenology takes place only afterward.
     This is how relativity theory was constituted: empirical results like the Michelson{Morley
experiment might well suggest the principle of relativity; but the deduction of the theory from
this principle was made without appeal to experiment. After the theory was developed, one could
test its predictions on such matters as abberation, time dilatation, and the orbits of fast charged
particles.
     The answer is rather clear; for both Clausius and Gibbs the theoretical principles that were
missing did not lie in quantum theory (that was only a quantitative detail). The fundamental
principles were the principles of probability theory itself; how does one set up a probability distri-
bution over microstates { classical or quantum { that represents correctly our information about a
macrostate? If that information includes all the conditions needed in the laboratory to determine
a reproducible result { equilibrium or nonequilibrium { then the theory should be able to predict
that result.
     We suggest that the answer is the following. For any system the entropy is a property of
the macrostate (more precisely, it is a function of the macrovariables that we use to de ne the
macrostate), and it is de ned by a variational property: it is the upper bound of ,k Tr( log )
over all density matrices that agree with those macrovariables. This will agree with the Clausius
and Pauli prescriptions in those cases where they were valid; but it automatically provides the
extra terms that Gibbs needed to analyze surface e ects, if we apply it to the nite sized systems
that actually exist in the laboratory.
     When thermodynamic entropy is de ned by this variational property, the long confusion about
order and disorder (which still clutters up our textbooks) is replaced by a remarkable simplicity
and generality. The conventional Second Law follows a fortiori : since entropy is de ned as a
constrained maximum, whenever a constraint is removed, the entropy will tend to increase, thus
paralleling in our mathematics what is observed in the laboratory. But it provides generalizations
far beyond that, to many nonequilibrium phenomena not yet analyzed by any theory.
     And, just as the variational formalism of Gibbs' Heterogeneous Equilibrium could be used
to derive useful rules of thumb like the Gibbs phase rule, which were easier to apply than the full
formalism, so this generalization leads to simple rules of thumb like the phase volume interpretation
S = k log W of Boltzmann, Einstein, and Planck, which are not limited to equilibrium conditions
and can be applied directly for very simple applications like the calculation of muscle eciency in
biology (Jaynes, 1989).
                                         REFERENCES
Callen, H. B. (1960), Thermodynamics, J. Wiley & Sons, Inc., New York.
Epstein, P. S. (1937), Textbook of Thermodynamics, J. Wiley & Sons, Inc., New York.
19                                                                                                 19
Gibbs, J. Willard (1875{78) \On the Equilibrium of Heterogeneous Substances", Connecticut Acad.
    Sci. Reprinted in The Scienti c Papers of J. Willard Gibbs, by Dover Publications, Inc., New
    York (1961).
Gibbs, J. Willard (1902), Elementary Principles in Statistical Mechanics, Yale University Press,
    New Haven, Conn. Reprinted in The Collected Works of J. Willard Gibbs, Vol. 2 by Dover
    Publications, Inc., New York (1960).
Jaynes, E. T. (1965), \Gibbs vs Boltzmann Entropies", Am. Jour. Phys. 33, 391{398.
Jaynes, E. T. (1967), \Foundations of Probability Theory and Statistical Mechanics", in Delaware
    Seminar in Foundations of Physics, M. Bunge, Editor, Springer{Verlag, Berlin. Reprinted in
    Jaynes (1983).
Jaynes, E. T. (1983), Papers on Probability, Statistics, and Statistical Physics, D. Reidel Publishing
    Co., Dordrecht, Holland, R. D. Rosenkrantz, Editor. Reprints of 13 papers.
Jaynes, E. T. (1986) \Macroscopic Prediction", in Complex Systems { Operational Approaches, H.
    Haken, Editor; Springer{Verlag, Berlin.
Jaynes, E. T. (1988), \The Evolution of Carnot's Principle", in Maximum Entropy and Bayesian
    Methods in Science and Engineering , Vol. 1, G. J. Erickson and C. R. Smith, Editors; Kluwer
    Academic Publishers, Dordrecht, Holland.
Jaynes, E. T. (1989), \Clearing up Mysteries; the Original Goal", in Proceedings of the 8'th Inter-
    national Workshop in Maximum Entropy and Bayesian Methods, Cambridge, England, August
    1{5, 1988; J. Skilling, Editor; Kluwer Academic Publishers, Dordrecht, Holland.
Klein, M. J. (1973), \The Development of Boltzmann's Statistical Ideas", in E. C. D. Cohen & W.
    Thirring, eds., The Boltzmann Equation , Springer{Verlag, Berlin; pp. 53{106
Pauli, W. (1973), Thermodynamics and the Kinetic Theory of Gases , (Pauli Lectures on Physics,
    Vol. 3); C. P. Enz, Editor. MIT Press, Cambridge MA.
Planck, M. (1926), Treatise on Thermodynamics, Dover Publications, Inc., N. Y.
Zemansky, M. W. (1943) Heat and Thermodynamics , McGraw{Hill Book Co., New York.

