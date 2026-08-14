# 2

**source:** pdf · **section:** solutions
**file:** Weber_DePew
---


Growth of Order in the Universe
David Layzer

2.1 History
In 1834 a French engineer, Sadi Carnot, laid the foundation for the science
of thermodynamics by proving that every ideal reversible heat engine
operating between two heat reservoirs at given temperatures has the same
efficiency. Carnot believed that heat is an indestructible substance. Under
this assumption, he showed that if two ideal reversible heat engines operat­
ing between a given pair of heat reservoirs had different efficiencies, they
could be hooked together to form a machine that would generate mechan­
ical energy. By 1840 rigorous experiments by James Joule in England and
Robert Mayer in Germany had established that, contrary to Carnot's as­
sumption, heat is not an indestructible substance. Rather, heat and mechan­
ical energy are interconvertible at a fixed rate of exchange. This is the First
Law of thermodynamics. Around 1850 Rudolf Clausius in Germany and
William Thomson in England independently revised Carnot's theory in the
light of the First Law. They proved that his theorem— that all reversible
heat engines operating between reservoirs at given temperatures have the
same efficiency— remains valid if one introduces a new postulate. This
postulate, the Second Law of thermodynamics, has two equivalent forms:
(1) It is impossible to construct a device whose only effect is to convert
heat from a single reservoir at uniform temperature entirely into work. (2)
It is impossible to construct a device whose only effect is to transfer heat
from a colder to a hotter reservoir.
    In the 1850s and 1860s Clausius and Thomson developed the implica­
tions of this postulate. Thomson showed that ideal reversible heat engines
can be used to define temperature in a manner that does not rely on the
properties of any physical substance such as an ideal gas. Using this new
definition of temperature, Clausius showed that the Second Law implies the
existence of a new physical property, which he called entropy. This quantity
remains constant in reversible changes of an isolated thermodynamic
system but increases in every nonreversible change. Thus the Second Law
implies that all natural processes generate entropy.
    During the 1850s and 1860s Clausius, James Clerk Maxwell, Ludwig
24    David Layzer

Boltzmann, and others sought to relate the thermodynamic properties of
macroscopic bodies, especially gases, to the dynamical behavior of their
constituent molecules. At that time, molecules were still hypothetical ob­
jects, and some physicists— notably Ernst Mach— objected on method­
ological grounds to basing explanations of observable phenomena on a
theoretical description of unobserved objects. However, the dynamical
theory of gases, as it was then called, proved to have a lot of explanatory
power. For a modest investment in assumptions about the properties of
molecules, it yielded large returns in predictions about the macroscopic
behavior of gases. Entropy, however, and with it the Second Law, remained
outside the scope of the theory until Boltzmann introduced his famous
 statistical definition of entropy in the 1870s. Boltzmann also succeeded in
 deriving a special case of the Second Law from plausible statistical assump­
 tions. Boltzmann's definition makes entropy a measure of disorder at the
molecular level. The Second Law implies, therefore, that the molecular
 disorder of an isolated gas tends to increase until it is as large as possible.
 The state of maximum molecular disorder corresponds to thermodynamic
 equilibrium.
    In 1946 Claude Shannon, following up work by Leo Szilard and others
 in the 1920s, explicitly freed Boltzmann's definition of entropy from its
 thermodynamic context and used it to construct a mathematical theory
 of communication. Shannon's work inspired several people to apply in­
 formation theory to biological problems. These efforts were not very
 productive, however. Some biologists argued that the approach was wrong
 in principle— that neither information (as it is defined in communication
 theory) nor negative entropy has much to do with biological order. One of
 the things I hope to do in this talk is to clarify the connection between
 information and biological order.

2.2 What Is Entropy?
Consider a gas. Its macroscopic states are defined by variables such as
temperature, density, and chemical composition, all of which represent
average properties of the gas. Many different molecular configurations, or
microstates, have the same average properties and hence represent the same
macroscopic state, or macrostate. We may think of a macrostate as the set of
all microstates that have a given set of average properties. Boltzmann
defined the entropy of a macrostate as the logarithm of the number of its
microstates. If H denotes the entropy of a given macrostate and W the
number of microstates that belong to it— the number of ways in which the
macrostate can be realized— then Boltzmann's definition reads
      H = log W.                                                             (1 )
                                       Growth of Order in the Universe    25

  If the microstates have unequal weights wt (where the wt are positive
numbers that add up to 1), the entropy is given by
     H = X H*log(l/H*),                                                   U)
which reduces to the preceding formula when wt = 1/W.
    To apply Boltzmann's definition to communication theory, we identify
microstates with strings of characters, and macrostates with sets of strings
that share specified properties. Consider, for example, strings of English
letters that have a certain length. The entropy of this set of strings is the
logarithm of the number of its members. If the letters are weighted ac­
cording to their frequency in some sample of English prose, we may use
formula (2) to calculate the entropy. For a string of given length, this will
yield a smaller value of the entropy. If we require our strings to consist of
English words, we obtain a still smaller value of the entropy. And if we
require the strings to be meaningful English sentences, the entropy is again
smaller.
    In the last example it is probably impossible to assign a precise value
to the entropy, because competent judges are likely to disagree about
whether certain strings of words are meaningful. But if doubtful cases con­
stitute a small fraction of the total number of candidates the definition is
still useful.
    Let us now consider a biological example: the entropy of a set of
variants of some biomolecule— hemoglobin, say. We may define a variant
of hemoglobin as a molecule that performs the biological function of
hemoglobin well enough to enable an individual that synthesizes this
molecule to survive and reproduce. This definition, like the definition of
a meaningful English sentence in our earlier example, is not absolutely
precise. It depends on the population and the range of environments one
chooses to consider. Even when these are specified it will probably be
impossible to draw a line separating functional from nonfunctional mole­
cules, just as it is impossible to draw a line separating meaningful from
nonmeaningful English sentences. Here again, however, the borderline
cases constitute a negligible fraction of the whole.

2.3 What Is Information?
The class of meaningful English sentences containing 100 or fewer char­
acters is much smaller than the class of word-strings with 100 or fewer
characters, and its members are more orderly. Reducing the entropy of a
class increases the orderliness of its members. But we have to be careful.
The entropy of the class of character-strings of length 5 is much smaller
than the entropy of the class of English sentences of length 100 or less, but
its members are less orderly. In the scientific contexts I wish to consider
26    David Layzer

it is useful to define information not as negative entropy but as the difference
between potential entropy and actual entropy.
    By potential entropy I mean the largest possible value that the entropy can
assume under specified conditions. In thermodynamics one usually specifies
the values of conserved quantities such as the total energy and the number
of molecules or molecular building blocks. In communication theory we
may choose the specified conditions in various ways, each of which yields
a different value for the potential entropy and hence a different value for
the information. For example, we may choose to consider strings of English
characters or strings of English words. The value we assign to meaningful
English sentences of a given length will obviously depend on this choice.
Analogously, in calculating the potential entropy of a gene, we may con­
sider strings of DNA bases or strings of codons.
    Potential entropy is also potential information, because the largest value
that the entropy can assume under specified conditions is also the largest
value that the information can assume. We can express this symmetry by
writing the relation between entropy and information in the form
     H + I = Hmax = /max = J.                                                (3)

2.4 Information and Order
The relation between biological organization and thermodynamic order has
been warmly debated for at least half a century. In the late 1930s and early
1940s Erwin Schroedinger (1944) popularized the thesis that biological
organization is created and maintained at the expense of thermodynamic
order, while Joseph Needham (1941) argued that "the two concepts are
quite different and incommensurable. We should distinguish [Needham
said] between Order and Organization." Needham's view has been endorsed
and elaborated by many biologists, including Peter Medawar (1969) and
Andre Lwoff (1968).
   The conflict between the two points of view involves several distinct
issues that have not always been clearly separated.
   1.     Are order and organization "different and incommensurable" at the level of
physics and chemistry? Needham and Medawar argued that they are, because
when hydrogen and oxygen combine to form liquid water or when a
supercooled liquid crystallizes, the thermodynamic order of the system of
molecules decreases while its degree of organization increases.
   This argument overlooks the fact that the thermodynamic order of a
collection of molecules refers to their distribution (or, more precisely, the
distribution of their representative points) in six-dimensional phase space.
When a supercooled liquid crystallizes, the increase in its spatial order is
more than offset by a decrease in the order associated with the distribution
                                         Growth of Order in the Universe      27

of its representative points in velocity space. Crystallization releases
energy and allows the distribution to spread in velocity space. Anal­
ogously, the increase in organization that accompanies the folding of a
protein or the spontaneous self-assembly of a ribosome is more than offset
by the decrease in the order of the surrounding water molecules.
    In short, spatial organization represents one aspect of thermodynamic
order, but there are other aspects as well. The relation between spatial
organization and thermodynamic order is analogous to the relation be­
tween kinetic energy and total energy.
    2.    Does biological order transcend spatial organization? For a biologist, the
order of a protein is intimately bound up with its structure. A single change
in the amino-acid sequence of a protein may destroy its function and hence
its biological order, but from a purely chemical standpoint the protein and
its nonfunctional mutant are equally orderly. Does it follow that Boltz­
mann's definition of order does not apply to biological order? I think not.
    Consider a gas composed of oxygen-16 and oxygen-18 molecules. Is the
thermodynamic order of the gas larger when the two isotopes are spatially
separated than when they are mixed? The answer depends on the context.
In purely chemical contexts the degree of mixing of the isotopes does not
affect the entropy, because both isotopes have the same chemical prop­
erties. The order associated with the degree of mixing of the two isotopes
is a separate additive component of the total thermodynamic order of the
gas. Symbolically,
     I      C hem +       ^m ix in g '                                       (4 )

where the first term on the right is the part of the information that depends
only on properties of the gas that do not discriminate between the two
isotopes.
   Analogously, we may express the information content of a functional
hemoglobin molecule as the sum of a chemical contribution, which does
not depend on the sequence of amino-acid residues, and a biological con­
tribution, which does:
     I      f c h e m ~ F I b io '                                           (5 )

According to our earlier discussion, the biological contribution to the
information is given by the formula
     ^bio        /       -f^bio

            = log W - log Wbi0                                               (6)
            = log(W/Wbio),
where W is the number of distinct polypeptides of the same length as
28    David Layzer

a functional hemoglobin molecule and Wbio is the number of functional
variants.
   We can define biological order more precisely and more generally in
terms of fitness. Population geneticists assume that every variant of a trait
can be assigned a definite (multiplicative) fitness— a measure of how effec­
tively that trait contributes to its possessor's expectation of reproductive
success under given conditions. In the preceding formula we now set Wbio
equal to the number of variants that are at least as fit as the variant under
consideration. Natural selection always increases the proportion of rela­
tively fit variants in a population and decreases the proportion of relatively
unfit variants. Hence, as I shall discuss in more detail presently, natural
selection always generates biological order.
   3.     Some writers have argued that thermodynamic order and biological
order must be fundamentally different because thermodynamic order is
continually decreasing while biological order is continually increasing.
Others have argued that the growth of biological order is driven by the
growth of thermodynamic entropy, much as the regular oscillations of the
pendulum in a grandfather clock are driven by a falling weight. Both
arguments are based on a false premise: that the thermodynamic order
of the universe is continually decaying. But the growth of entropy does
not imply the decay of order. Remember that information, the measure
of thermodynamic order, is the difference between potential and actual
entropy:
     H + I = J.
In thermodynamic contexts ], the potential information or entropy, is
constant, but in astronomical and biological contexts it may increase with
time. If ] increases faster than H, information will be generated.
   This point is worth emphasizing. When Eddington wrote about the
"running down" of the universe, he assumed that because all natural pro­
cesses generate entropy, a measure of disorder, the universe must have
been more orderly in the past than it is today. Many later writers have
drawn the same fallacious conclusion. The reason it is fallacious is that
information, the measure of order, is not simply negative entropy. It is the
difference between potential entropy or potential information (the quantity
denoted above by ]) and entropy (H). All natural processes generate
entropy; but some processes— astronomical and biological processes in
particular— also generate potential entropy. As I shall discuss presently,
the universe could well have begun to expand from a state of zero entropy
and zero information.
   Let us now take a closer look at the processes that create and destroy
order.
                                           Growth of Order in the Universe     29

  2.5 Growth of Entropy
  Entropy is a measure of the spread of a discrete frequency distribution. In a
  gas of classical particles, the distribution is over blocks of equal size in
  phase space. In evolutionary contexts the distribution is over a genotype
  space. In a genotype space every point represents a genotype or a segment
  of a genotype. For example, the variants of a single gene are represented
  by points in a space whose dimension is equal to the number of codons.
      Molecular interactions in a gas or liquid normally generate entropy. That
  is, they tend to distribute molecules (or rather, their representative points)
  as broadly as possible over phase space, if they are not so distributed to
  begin with. The Second Law of thermodynamics asserts that this is so.
  Kinetic theories, the first of which was invented by Boltzmann, seek to
  explain why and under what circumstances molecular interactions generate
  entropy.
      One might suppose that any very large collection of interacting mole­
  cules would evolve toward its state of maximum entropy, but numerical
  simulations have shown that this is not the case. A classic example is the
  work of Fermi, Pasta, and Ulam, who used a computer to simulate the
  behavior of a long chain of coupled anharmonic oscillators. They found
  that the system did not relax into its state of maximum entropy but
  oscillated irregularly between states of high and low entropy. Thus size
  and complexity do not guarantee entropic behavior. On the other hand, it
  is easy to prove that a system of randomly interacting molecules evolves
  irreversibly toward its state of maximum entropy, provided the individual
  interactions are time reversible. Randomness or quasi-randomness of the
  underlying microscopic processes seems to be a necessary condition for
  entropic macroscopic behavior. The technical difficulties of kinetic theories,
■
— which need not concern us here, center on elucidating the notion of quasi­
  randomness in systems that are in fact completely deterministic.
      Mutation and genetic recombination play a role in biological evolution
  analogous to the role of molecular interactions in the evolution of a
  gas. The central dogma of molecular biology, that information flows uni-
  directionally from the genotype to the phenotype, guarantees that genetic
  variation is blind to its phenotypic consequences. In this sense genetic
  variation is random. Accordingly we may expect that genetic variation
  always generates entropy. Although I believe this to be true, it is only part of
  the truth. As I will discuss presently, genetic variation may also generate
  potential entropy/information.
      Let me try to be more concrete. Consider the genotype space corres­
  ponding to a particular trait or group of closely related traits in a given
  population. Genetic variation always tends to increase the spread of geno­
  types in this genotype space. It does this in two ways: (a) It makes the
30    David Layzer

distribution of genotypes flatter, more uniform, (b) In addition, it may
allow the population to colonize previously uninhabited regions of the
genotype space. The first process generates entropy but not potential
entropy. Hence it necessarily destroys information. The second process
generates potential entropy as well. It does not necessarily generate en­
tropy. More important, it is an essential preliminary to the generation of
information by differential reproduction, as I shall discuss shortly.

2.6 Growth of Potential Entropy/Information in Astronomical Contexts
In thermodynamic systems the potential entropy has a fixed value that
depends on the values of appropriate conserved quantities such as the total
energy. Hence the growth of entropy leads to a decline of order. In other
contexts, however, the potential entropy is not fixed but may increase. If it
increases faster than the entropy itself, information is generated.
   Astronomy offers many examples. Let us look at a few.
   1. In a star composed initially of pure hydrogen, thermonuclear reactions
gradually convert hydrogen to helium in the core. The potential mixing
entropy of the star thereby increases. A star of the sun's mass is stable
against convection, so mixing occurs very slowly. Helium accumulates in
the core, so order and information are generated.
   2. In self-gravitating systems, contraction releases energy that appears
partly as kinetic energy of random motions. For example, a self-gravitating
gas cloud contracts and gets hotter as it radiates away energy. Thus a self-
gravitating gas cloud has negative specific heat. This is a sign that it does
not have a stable state of maximum entropy. (The specific heat of a system
in a stable state of maximum entropy is necessarily positive.) As the gas
cloud contracts, its molecules colonize new regions of velocity space. This
example also illustrates how entropy growth can result in increased spatial
order. As the cloud contracts, its spatial order increases, but it occupies an
increasing volume of velocity space.
   3. Cosmology offers the most important astronomical examples of the
growth of potential entropy. In the early universe, thermodynamic equi­
librium prevails locally. As the universe expands, the rates of equilibrium-
maintaining reactions fall below the expansion rate and nonequilibrium
conditions are frozen in. To quote from an earlier paper (1970):
     Expansion or contraction from an initial state of thermodynamic equilibrium
     generates both specific entropy and specific information. This conclusion
     obviously applies under much more general assumptions about the
     state and composition of the cosmic medium. The essential elements
     of the argument are (a) that the 'initial' state is one of maximum
     specific entropy (zero information), and (b) that the rate of cosmic
                                        Growth of Order in the Universe      31

     expansion or contraction ... may be comparable to or greater than the
     rates of processes that tend to produce the state of local thermo­
     dynamic equilibrium. Because the cosmic expansion or contraction is
     not quasi-static, it generates departures from local thermodynamic
     equilibrium and hence generates information. At the same time, ir­
     reversible processes generate entropy.
   Consider, for example, a uniform mixture of blackbody radiation and gas
in an expanding universe. So long as the radiation and the gas exchange
energy sufficiently rapidly, they remain at the same temperature, which
decreases as the universe expands. Eventually, the rate of energy exchange
becomes too small to keep the gas and the radiation at the same tempera­
ture. (In an initially hot universe filled with hydrogen, this happens when
the hydrogen recombines, at a temperature of a few thousand degrees
Kelvin, Neutral hydrogen interacts very weakly with blackbody radiation
at this temperature.) Thereafter, the gas cools faster than the radiation. If
there is no interaction at all between the two components, the specific
entropy of each one remains constant. But because the gas and the radia­
tion are at different temperatures, their combined entropy is smaller than it
could be, given their combined energy density. In other words, the po­
tential entropy of the cosmic medium exceeds the actual entropy, and the
difference increases as the universe expands. Thus the cosmic expansion
generates information.
   What is going on in this example? Linear scales are increasing like a.
Momentum is decreasing like 1i a. For energy there are three possibilities:
for relativistic particles E cc p. For nonrelativistic particles E cc p2. For
internal energy, E is constant. Hence the rate at which energy per unit mass
decreases depends on the degree of equilibration between the gas and the
radiation.
   Consider a relativistic and a nonrelativistic gas initially in equilibrium at
the same temperature. If they remain in equilibrium as the universe expands
(or contracts), their common temperature varies as (a, /a)q, where a is the
cosmic scale factor, a1 is its initial value, and q is between 1 and 2. If
equilibration does not occur, a temperature difference between the two
gases develops. Thus the expansion (or contraction) generates thermo­
dynamic order.
   What happens to the entropy? If equilibration is instantaneous, the
entropy per unit mass stays constant. If the two gases do not interact at all,
the entropy also remains constant! If equilibration occurs subsequently, the
resulting common temperature is higher than it would have been if equili­
bration had been instantaneous. (This is true in a contracting as well as in
an expanding universe.) Thus the energy is higher than it would be if
equilibration were instantaneous, and the potential entropy is also higher.
32    David Layzer

The rate of entropy generation is actually greatest at some intermediate
(finite, nonzero) rate of equilibration.
   A simple example will illustrate this conclusion. Consider two disks
spinning at different rates on a common axis, as in a clutch assembly. If the
disks are not in contact or if they are in contact but there is no slippage,
there is no frictional dissipation. The dissipation is greatest when the disks
are in contact but there is some slippage.
   Because the energy per unit volume in our expanding mixture of gas and
radiation is greater than it would be if equilibration were instantaneous, the
cosmic expansion increases the accessible volume of phase space. If equili­
bration were instantaneous, the accessible volume would remain constant,
the accessible region of momentum space contracting at a rate that just
compensates for the expansion of physical space.
   Does the growth of potential entropy distinguish between cosmic
expansion and cosmic contraction? No. The preceding discussion applies
equally well to a contracting universe.
   Note that what drives the growth of chemical and structural order is
the cosmic expansion (or contraction), not the tendency toward random­
ization. The Second Law has nothing to do with the growth of potential
entropy. This illustrates an important general proposition:
     Processes that generate order are in no sense driven by the growth of entropy.
In particular, biological evolution is not driven by the growth of entropy.
   4.    In the preceding example, the cosmic expansion generates a tem­
perature difference between two homogeneous components of the cosmic
medium. This temperature difference could in principle be used to run a
heat engine. Thus it is a potential source of free energy. By far the most
important practical source of free energy on earth is sunlight. Sunlight is a
by-product of the burning of hydrogen into helium in the deep interior of
the sun. Hydrogen, in turn, was produced by chemical (more specifically,
nuclear) reactions in the early universe. Let us look more closely at this
process.
   The rate of a two-body reaction is inversely proportional to the density
and increases with increasing temperature. The cosmic expansion rate is
proportional to the square root of the mass density and is independent of
temperature (except insofar as thermal energy contributes to the mass
density). Hence two-body reaction rates increase relative to the expansion
rate as we look back in time. At sufficiently early times, the rate of any
given two-body reaction will exceed the cosmic expansion rate. Con­
versely, the rate of any given two-body reaction eventually falls below the
cosmic expansion rate.
   Now consider a specific chemical equilibrium— for example, the equi­
librium between neutrons, protons, electrons, positrons, neutrinos,
                                       Growth of Order in the Universe   33

and antineutrinos. Sufficiently early in the history of the universe, the
equilibrium-maintaining reactions (e.g., the capture of an electron by a
proton to give a neutron and a neutrino, and the reverse reaction) will
proceed rapidly enough to keep the ratio of neutrons to protons at its
equilibrium value. Eventually, however, the relevant reaction rates fall be­
low the expansion rate. The relative abundances of the reactants are then
frozen in. They retain the values appropriate to earlier values of the cosmic
density and temperature.
    As the cosmic density and temperature diminish, chemical equilibrium
favors the formation of compound particles with progressively larger
binding energies. If the expansion took place slowly enough, and if the
cosmic medium remained uniform, nearly all of the matter in the universe
would eventually be in the form of iron, the element with the largest
binding energy per nucleon and thus the ultimate product of nuclear
reactions at low temperatures and densities. In fact, chemical equilibrium is
frozen in at an epoch when most of the matter is in the form of protons.
That is why hydrogen is still available to produce starlight— and to sup­
port life on earth.
    5.    The cosmic expansion generates two important kinds of order:
chemical order, which we have just discussed, and structural order. Struc­
tural order manifests itself in the dumpiness of the cosmic mass distribu­
tion— in the fact that matter is not uniformly distributed in space but is
concentrated in a hierarchy of self-gravitating systems. Most cosmologists
believe that a satisfactory cosmological theory must explain how this
complicated kind of dumpiness has evolved from an initially uniform
distribution of mass. Most cosmologists assume that the cosmic microwave
background, a blackbody radiation field whose present temperature is 3K,
is the remnant of a primeval fireball. This assumption has not so far led to a
satisfactory theory for the evolution of dumpiness. The alternative cos­
mological assumption, that the universe began to expand from a uniform
state at zero temperature, forms the starting point for a theory that predicts
the gradual emergence of structure in the course of the cosmic expansion.
Whether or not this theory proves to be correct, it serves to illustrate
how structural order can evolve in an initially structureless universe.

2.7 Growth of Organization in Biological Evolution
Evolutionary change results from the interplay of two elementary pro­
cesses: genetic variation and differential reproduction (natural selection).
Molecular biology has strongly confirmed the neo-Darwinian postulate
that there is no feedback of specific information from the living organism's
life experience to variations in the genes it passes on to its descendants.
34    David Layzer

Thus genetic variation and differential reproduction are independent
processes.
   In the 1940s and 1950s I. I. Schmalhausen, using evidence from com­
parative embryology, elaborated the important thesis that evolution is a
process of hierarchic construction. This process has two complementary
aspects: differentiation, the increasing specialization and diversification of
parts; and integration, the formation of new aggregates in which the struc­
ture and function of the parts are subordinated to and regulated by the
structure and function of the aggregate as a whole, in the manner of cells in
a tissue, tissues in an organ, or organs in an organ system. (Individual
development, including psychological development, is also largely a pro­
cess of hierarchic construction. This is the central idea in the work of Heinz
Werner and of Jean Piaget.)
    Hierarchic construction has given rise to what Stebbins, in The Basis of
 Progressive Evolution, calls a "hierarchy of complexity." Stebbins distin­
 guishes eight major levels of overall organization in this hierarchy, rep­
 resented by "free-living viroids," procaryotes, eucaryotes, sponges and
 fungi, flatworms and higher plants, arthropods and vertebrates, mammals
 and birds, and man. Each level in this hierarchy is distinguished from the
 preceding level by a major evolutionary innovation, and organisms on each
 level retain the innovations that distinguish earlier levels. Thus flatworms
 and higher plants are not only multicellular organisms; they also have
  differentiated tissues and organs. Arthropods and vertebrates have, in
  addition, a central nervous system and sense organs. Mammals and birds
  are warm-blooded, and man has the capacity for language and culture.
     The "strategy" of hierarchic construction must itself be a consequence of
  the more elementary processes of genetic variation and differential repro­
  duction. I have discussed the implications of this requirement elsewhere
  (1980). The chief implication (I have argued) is that genetic variation
  cannot be a completely random process, though of course it must be blind
  to its phenotypic consequences. For hierarchic construction to evolve as an
  evolutionary strategy, genetic regulation must be regulated by a genetic
  system that has evolved along with the genetic system that specifies an
  organism's development. When this idea was put forward, in 1977, several
  examples of genetically regulated mutation and recombination rates were
  known. Since then, movable genetic elements (transposons) that regulate
  mutation and recombination rates have been found to be ubiquitous in both
  procaryotes and eucaryotes.

 2.8 Hierarchic Construction and the Growth of Information
 To understand how evolution generates biological information, let us con­
 sider some elementary evolutionary processes.
                                        Growth of Order in the Universe      35

    1. Mutation. Consider a population whose members all carry the same
variant of a gene that codes for a certain protein. Now suppose that a
mutation causes a new variant of this gene to appear in some fraction of the
population. The biological information associated with the new variant
may be greater or less than that associated with the original one. There are
two cases: (a) If the original variant is as fit as possible— if its representa­
tive point in genotype space is at a fitness peak— then any mutation
decreases fitness and destroys biological information, (b) If the original
variant is not as fit as possible, a mutation may increase or decrease fitness,
or leave it unchanged. But the average effect of the mutation in a large
population will ordinarily be to decrease fitness or to leave it nearly
unchanged. Conclusion: Mutations either diminish the average biological in­
formation associated with a given trait or leave it unchanged.
    2. Differential reproduction always increases the relative abundance of the
fitter variants in a population and decreases the relative abundance of the
less fit variants. Hence differential reproduction always increases the average
 biological information associated with a given trait in a given population.
    3. Gene duplication. Because the duplicated genetic material is redundant,
 this process by itself alters neither the potential information nor the actual
information associated with the template. But it is a necessary preliminary
 to the two following processes.
    4. Differentiation. Mutations may alter copies of a duplicated segment of
 genetic material. Thus if A denotes a segment of genetic material, duplica­
 tion may replace A by the sequence AA, and mutations may then alter this
 sequence to AA'. If A' were nonfunctional, this process would leave the
 information unchanged but would increase the potential information and
 the entropy (by the same factor). In reality, however, differentiation is
 always accompanied by
    5. Integration. Suppose that the segment A and A! jointly take over the
 function of A. Among the segments AA' there may be some that are fitter
 than A. Natural selection now has an enlarged region of genotype space in
 which to act. As the frequency of the fitter variants increases, the average
 biological information associated with the segment AA' and its variants
 also increases. Gene duplication and differentiation jointly open up new
 regions of genotype space for colonization by an evolving population. In
 so doing, they create potential information. Natural selection converts this
 potential information into actual information.

2.9 What Drives Evolution?
It seems clear that evolution must be driven by something. Nonliving
matter does not organize itself, except under very special circumstances.
Even then the degree of organization attained is quite modest compared
36    David Layzer

with even the simplest examples of biological organization. What is so
special about living matter?
   Before the advent of molecular biology, many people, including some
outstanding biologists, answered this question by positing a “life force."
Molecular biology and biochemistry have convincingly demonstrated that
no such postulate is necessary. What distinguishes living matter from
nonliving matter is "just" its organization. A virus synthesized in the
laboratory would be indistinguishable from its natural template. But that
does not answer the question.
   A common modem answer is the growth of entropy. Evolution, on this
view, is driven by the tendency of order to decay into chaos. To explain
how order can result from a general tendency toward the dissolution of
order, people often use the example of two unequal weights hanging on
opposite sides of a pulley. As the center of mass of the two weights
descends, the lighter weight rises. Analogously, protein molecules that
have been denatured and then returned to their normal cellular envi­
ronment spontaneously refold; the diminished entropy of the protein
molecules is more than compensated by the increased entropy of the sur­
rounding water molecules.
    But we are still in the realm of analogy. To see what drives evolution we
need to analyze a true evolutionary process. Consider, for example, the
evolution of self-replicating strands of RNA in the well-known experiments
of Sol Spiegelman. The "driving force" here is just the "Malthusian in­
stability," the tendency of any population of self-replicators to grow ex­
ponentially so long as the supplies of building blocks and fuel molecules
hold out. If two populations competing for the same building blocks and
the same source of free energy have different exponential growth rates, the
population with the larger growth rate will eventually take over com­
pletely. Of course, free energy and building blocks must be constantly
supplied. But it would be misleading to regard the flow of free energy or of
molecular building blocks as driving the evolutionary process. On the
contrary, the ability of living organisms to mobilize free energy and or­
ganize matter is an evolutionary adaptation— a consequence of the repro­
ductive instability of genetic material.
    The notion that evolution is driven by the "Malthusian instability" was,
of course, Darwin's key idea. If we need to be reminded of it, it is partly
because generations of population geneticists have focused their studies
not on instability but on statistical equilibrium. Yet, as Ernst Mayr has
persuasively argued, significant evolutionary changes probably occur only,
 or at least primarily, in populations far from equilibrium— small, peripheral
 "founder" populations, where the tendency toward exponential growth
is not held in check by a limited food supply, by competition, or by
predation.
                                       Growth of Order in the Universe     37

   There is another reason why many people have been tempted to iden­
tify the driving force in evolution with the growth of entropy. We have all
encountered the following argument. "Evolution, like all natural processes,
rests ultimately on physical laws. All physical laws, with one exception, fail
to distinguish between the two directions of time. The one exception is the
Second Law of thermodynamics, which states that all physical processes
generate entropy. Hence evolution, which more than any other natural
phenomenon distinguishes between the direction of the past and the direc­
tion of the future, must ultimately derive its 'arrow' from the Second Law."
   This argument is flawed because the Second Law is not the same kind of
law as the time-reversible laws that govern elementary particles and their
interactions. Those laws are independent of initial and boundary condi­
tions. By contrast, the Second Law depends in an essential way on initial
and boundary conditions. This was explicitly recognized by Maxwell, who
invented a famous thought experiment to demonstrate it. Maxwell had a
demon opening and shutting a trap door in a partition down the middle of
a box of gas. The demon let fast molecules pass from right to left, slow
molecules from left to right. Thus the temperature of the left half of the box
gradually increased, while the temperature of the right half decreased, in
violation of the Second Law. Half a century later, Leo Szilard pointed out
that information has its price in entropy. In order to gain information about
individual molecules, the demon must interact with them, and each interac­
tion generates entropy. Szilard showed that the entropy of the system (gas
molecules + demon) would increase with time, as the Second Law predicts.
    It is not difficult, however, to construct a version of Maxwell's thought
experiment that illustrates his original point, namely, that the Second Law
presupposes certain initial (and boundary) conditions. Replace the demon
by a tiny robot programmed to open and close the trap door according to
the results of a calculation carried out before the start of the experiment.
The calculation predicts the positions and velocities of all the molecules in
the gas at any moment after the initial moment, and the robot's program
allows it to use this information to do the demon's job. Of course, such
a calculation would need to be based on an immense quantity of data about
a still earlier state of the gas and its container, but that is all right in a
thought experiment. In this experiment, the entropy of the system (gas
molecules + robot) does decrease with time. Thus the Second Law fails if
certain kinds of microscopic information about the initial state are present.
This is just the sort of constraint on the Second Law that Maxwell had in
mind.
    Thus the Second Law presupposes the absence of certain kinds of micro­
 scopic order in the initial states of natural systems. Why these kinds of
 order are absent is a question that lies beyond the scope of this lecture
(Layzer, 1970, 1976). The point I wish to make now is that biological
38     David Layzer

           STRUCTURES,INITIAL CONDITIONS         ORDER-GENERATING PROCESSES
                            ij'                                   ^

Figure 2.1
[Reproduced by permission of The MIT Press from D. Layzer, "Quantum Mechanics,
Thermodynamics, and the Strong Cosmological Principle," in A. Shimony and H. Feshbach,
eds.. Physics as Natural Philosophy, Cambridge, MA: MIT Press, 1982]
                                                Growth of Order in the Universe             39

evolution obviously has nothing to do with the absence of microscopic
order in natural systems. Indeed, none of the order-generating processes I
have discussed in this lecture depends directly on the Second Law. There is
a single universal law governing processes that dissipate order, but order is
generated by several hierarchically linked processes. Figure 2.1, taken from
an earlier publication (Layzer, 1982), illustrates how these processes are
related to each other, to the processes that generate entropy, and to a
cosmic symmetry condition that I call the Strong Cosmological Principle,
which supplies the initial conditions needed to derive the Second Law from
the time-reversible laws of microscopic physics (Layzer, 1976).

References
Layzer, D., 1970. Pure and Applied Chemistry 22:457.
Layzer, D., 1976. The arrow of time. Scientific American December; Astrophysical Journal
206:559.
Layzer, D„ 1980. American Naturalist 115:809.
Layzer, D., 1982. Quantum mechanics, thermodynamics, and the strong cosmological prin­
ciple. In Physics as Natural Philosophy, A. Shimony and H. Feshbach, eds., Cambridge, MA:
MIT Press.
Layzer, D., 1984. Constructing the Universe. Scientific American Illustrated Library, chapter 8.
Lwoff, A., 1968. Biological Order. Cambridge, MA: MIT Press.
Medawar, P. B., 1969. The Art of the Soluble. London: Methuen, pp. 99-100.

Needham, J., 1941. Evolution and thermodynamics. In Moulds of Understanding, New York:
St. Martin's Press.

Schroedinger, E., 1967. What Is Life? Cambridge: Cambridge University Press.

