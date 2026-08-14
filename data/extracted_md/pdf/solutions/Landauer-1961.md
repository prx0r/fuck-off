# r

**source:** pdf · **section:** solutions
**file:** Landauer-1961
---


                                                                    R. Landauer

    Irreversibility and Heat Generation
    in the Computing P rocess

    Abstract: It is argued that computing machines inevitably involve devices which perform logical functions
    that do not have a single-valued inverse. This logical irreversibility is associated with physical irreversibility
    and requires a minimal heat generation, per machine cycle, typically of the order of kT for each irreversible
    function. This dissipation serves the purpose of standardizing signals and making them independent of their
    exact logical history. Two simple, but representative, models of bistable devices are subjected to a more
    detailed analysis of switching kinetics to yield the relationship between sp eed and energy dissipation, and
    to estimate the effects of errors induced by thermal fluctuations.

    1. Introduction
    The search for faster and more compact computing cir­           degree of freedom associated with the information. Clas­
    cuits leads directly to the question; What are the ultimate     sically a degree of freedom is associated with kT oJ
    physical limitations on the progress in this direction? In      thermal energy. Any switching signals passing between
    practice the limitations are likely to be set by the need for   devices must therefore have this much energy to override
    access to each logical element. At this time, however, it is    the noise. This argument does not make it clear that the
    still hard to understand what physical requirements this        signal energy must actually be dissipated. An alternative
    puts on the degrees of freedom which bear information.          way of anticipating our conclusions is to refer to the argu­
    The existence of a storage medium as compact as the             ments by Brillouin and earlier authors, as summarized by
    genetic one indicates that one can go very far in the           Brillouin in his book, Science and Information Theory/
    direction of compactness, at least if we are prepared to        to the effect that the measurement process requires a
    make sacrifices in the way of speed and random access.          dissipation of the order of kT. The computing process,
       Without considering the question of access, however,         where the setting of various elements depends upon the
    we can show, or at least very strongly suggest, that infor­     setting of other elements at previous times, is closely akin
    mation processing is inevitably accompanied by a certain        to a measurement. It is difficult, however, to argue out
    minimum amount of heat generation. In a general way             this connection in a more exact fashion. Furthermore,
    this is not surprising. Computing, like all processes pro­      the arguments concerning the measurement process are
    ceeding at a finite rate, must involve some dissipation.        based on the analysis of specific models (as will some of
    Our arguments, however, are more basic than this, and           our arguments about computing), and the specific models
    show that there is a minimum heat generation, independ­         involved in the measurement analysis are rather far from
    ent of the rate of the process. Naturally the amount of         the kind of mechanisms involved in data processing. In
    heat generation involved is many orders of magnitude            fact the arguments dealing with the measurement process
    smaller than the heat dissipation in any practically con­       do not define measurement very well, and avoid the very
    ceivable device. The relevant point, however, is that the       essential question: When is a system A coupled to a sys­
    dissipation has a real function and is not just an unneces­     tem B performing a measurement? The mere fact that
    sary nuisance. The much larger amounts of dissipation in        two physical systems are coupled does not in itself require
    practical devices may be serving the same function.             dissipation.
       Our conclusion about dissipation can be anticipated in           Our main argument will be a refinement of the follow­
    several ways, and our major contribution will be a tight­       ing line of thought. A simple binary device consists of a
    ening of the concepts involved, in a fashion which will         particle in a bistable potential well shown in Fig. 1. Let
    give some insight into the physical requirements for logi­      us arbitrarily label the p irticle in the left-hand well as the
    cal devices. The simplest way of anticipating our conclu­       z e r o state. When the particle is in the right-hand well,
    sion is to note that a binary device must have at least one     the device is in the o n e state. Now consider the operation      183

                                                                                                                   IBM JOURNAL •JULY 1961
         r e s t o r e t o on e, which leaves the particle in the o n e                                                                                            v
         state, regardless of its initial location. If we are told that
         the particle is in the o n e state, then it is easy to leave it in
         the o n e state, without spending energy. If on the other
         hand we are told that the particle is in the z e r o state, we
         can apply a force to it, which will push it over the barrier,
         and then, when it has passed the maximum, we can apply
         a retarding force, so that when the particle arrives at on e,
         it will have no excess kinetic energy, and we will not have
         expended any energy in the whole process, since we ex­
         tracted energy from the particle in its downhill motion.
         Thus at first sight it seems possible to r e s t o r e t o o n e
         without any expenditure of energy. Note, however, that
         in order to avoid energy expenditure we have used two
         different routines, depending on the initial state of the                        x is a generalized coordinate representing
         device. This is not how a computer operates. In most                             quantity which is switched.
         instances a computer pushes information around in a
         manner that is independent of the exact data which are
         being handled, and is only a function o f the physical
         circuit connections.                                                    v
             Can we then construct a single time-varying force,                  4
         F(r), which when applied to the conservative system of
         Fig. 1 will cause the particle to end up in the o n e state,
         if it was initially in either the o n e state or the z e r o state?
         Since the system is conservative, its whole history can be
         reversed in time, and we will still have a system satisfying
         the laws of motion. In the time-reversed system we then
         have the possibility that for a single initial condition                                                     •                                                                                                                          •
                                                                                                                      0                                                                                                                           1
                                                                                               --------------------   ------------------------------------------------------------------------------------------------------------------------   ---------------------

          (position in the o n e state, zero velocity) we can end up                           POSITION                                                                                                                  POSITION
                                                                                  ------ ► X
         in at least two places: the z e r o state or the o n e state.
         This, however, is impossible. The laws of mechanics are               Figure 2   Potential well in which ze ro and one state
         completely deterministic and a trajectory is determined
                                                                                          are not separated by barrier.
         by an initial position and velocity. (An initially unstable                      Information is preserved because random
         position can, in a sense, constitute an exception. We can                        motion is slow.
          roll away from the unstable point in one of at least two
         directions. Our initial point o n e is, however, a point of
         stable equilibrium.) Reverting to the original direction              or being processed. The simplest class and the one to
          of time development, we see then that it is not possible to          which all the arguments of subsequent sections will be
          invent a single F(t) which causes the particle to arrive at          addressed consists of devices which can hold information
          o n e regardless of its initial state.                               without dissipating energy. The system illustrated in
             If, however, we permit the potential well to be lossy,            Fig. 1 is in this class. Closely related to the mechanical
         this becomes easy. A very strong positive initial force               example of Fig. 1 are ferrites, ferroelectrics and thin
          applied slowly enough so that the damping prevents oscil­            magnetic films. The latter, which can switch without
          lations will push the particle to the right, past on e, re­          domain wall motion, are particularly close to the one-
          gardless of the particle’  s initial state. Then if the force is     dimensional device shown in Fig. 1. Cryotrons are also
          taken away slowly enough, so that the damping has a                  devices which show dissipation only when switching. They
          chance to prevent appreciable oscillations, the particle is          do differ, however, from the device o f Fig. 1 because the
          bound to arrive at on e. This example also illustrates a             z e r o and o n e states are not particularly favored ener­
          point argued elsewhere2 in more detail: While a heavily              getically. A cryotron is somewhat like the mechanical
          overdamped system is obviously undesirable, since it is              device illustrated in Fig. 2, showing a particle in a box.
          made sluggish, an extremely underdamped one is also not              Two particular positions in the box are chosen to repre­
          desirable for switching, since then the system may bounce            sent z e r o and on e, and the preservation of information
          back into the wrong state if the switching force is applied          depends on the fact that Brownian motion in the box is
          and removed too quickly.                                             very slow. The reliance on the slowness of Brownian
                                                                               motion rather than on restoring forces is not only charac­
          2. Classification                                                    teristic of cryotrons, but of most of the more familiar
          Before proceeding to the more detailed arguments we                  forms of information storage: Writing, punched cards,
          will need to classify data processing equipment by the               microgroove recording, etc. It is clear from the literature
184       means used to hold information, when it is not interacting           that all essential logical functions can be performed by

IBM JOURNAL •JULY 1961
           I                                                         discussed for the latter in detail by Swanson.5 The dissi­
                                                                     pative device, such as the single tunnel diode, will in
                                                                     general be an analog, strictly speaking, to an unsym-
                                                                     metrical potential well, rather than the symmetrical well
                                                                     shown in Fig. 1. We can therefore expect that of the two
                                                                     possible states for the negative resistance device only one
                                                                     is really stable, the other is metastable. An assembly of
                                                                     bistable tunnel diodes left alone for a sufficiently long
                                                                     period would eventually almost all arrive at the same state
                                                                     of absolute stability.
                                                                        In general when using such latching devices in com ­
                                                                     puting circuits one tries hard to make the dissipation in
                                                                     the two allowed states small, by pushing these states as
Figure 3       Negative resistance characteristic (solid             closely as possible to the voltage or current axis. If one
               line) with load line (dashed).                        were successful in eliminating this dissipation almost
               z e r o and o n e are stable states, U is unstable.
                                                                     completely during the steady state, the device would
                                                                     become a member of our first class. Our intuitive expecta­
                                 F                                   tion is, therefore, that in the steady state dissipative device
                                                                     the dissipation per switching event is at least as high as in
                                                                     the devices of the first class, and that this dissipation per
                                                                     switching event is supplemented by the steady state
                                                                     dissipation.
                                                                        The third and remaining class is a “catch-all”; namely,
                                                                     those devices where time variation is essential to the rec­
                                                                     ognition of information. This includes delay lines, and
                                                                     also carrier schemes, such as the phase-bistable system
                                                                     of von Neumann.6 The latter affords us a very nice illus­
                                                                     tration of the need for dissipative effects; most other
                                                                     members of this third class seem too complex to permit
                                                                     discussion in simple physical terms.
Figure 4       Force versus distance for the bistable well              In the von Neumann scheme, which we shall not
                                                                     attempt to describe here in complete detail, one uses a
               of Fig. 1.
               z e r o and o n e are the stable states, U the        “pump”signal of frequency o>0, which when applied to a
               unstable one.                                         circuit tuned to a>o/2, containing a nonlinear reactance,
                                                                     will cause the spontaneous build-up of a signal at the
                                                                     lower frequency. The lower frequency signal has a choice
devices in this first class. Computers can be built that             of two possible phases (180° apart at the lower fre­
contain either only cryotrons, or only magnetic cores.3’   4         quency) and this is the source of the bistability. In the
   The second class of devices consists of structures which          von Neumann scheme the pump is turned off after the
are in a steady (time invariant) state, but in a dissipative         subharmonic has developed, and the subharmonic sub­
one, while holding on to information. Electronic flip-flop           sequently permitted to decay through circuit losses. This
circuits, relays, and tunnel diodes are in this class. The           decay is an essential part of the scheme and controls the
latter, whose characteristic with load line is shown in              direction in which information is passed. Thus at first
Fig. 3, typifies the behavior. Two stable points of opera­           sight the circuit losses perform an essential function. It
tion are separated by an unstable position, just as for the          can be shown, however, that the signal reduction can be
device in Fig. 1. It is noteworthy that this class has no            produced in a lossless nonlinear circuit, by a suitably
known representatives analogous to Fig. 2. All the active            phased pump signal. Hence it would seem adequate to
bistable devices (latches) have built-in means for restora­          use lossless nonlinear circuits, and instead of turning the
tion to the desired state. The similarity between Fig. 3             pump off, change the pump phase so that it causes signal
and the device of Fig. 1 becomes more conspicuous if we              decay instead of signal growth. The directionality of
represent the bistable well of Fig. 1 by a diagram plotting          information flow therefore does not really depend on the
force against distance. This is shown in Fig. 4. The line            existence of losses. The losses do, however, perform
F = 0 intersects the curve in three positions, much like             another essential function.
the load line (or a line of constant current), in Fig. 3.               The von Neumann system depends largely on a cou­
This analogy leads us to expect that in the case of the              pling scheme called majority logic, in which one couples
dissipative device there will be transitions from the                to three subharmonic oscillators and uses the sum of their
desired state, to the other stable state, resulting from             oscillations to synchronize a subharmonic oscillator
thermal agitation or quantum mechanical tunneling,                   whose pump will cause it to build up at a later time than
much like for the dissipationless case, and as has been              the initial three. Each of the three signals which are            185

                                                                                                                    IBM JOURNAL •JULY 1961
         added together can have one of two possible phases. At            ble. Then the machine cycle maps the 2N possible initial
         most two of the signals can cancel, one will always sur­          states of the machine onto the same space of 2N states,
         vive, and thus there will always be a phase determined            rather than just a subspace thereof. In the 2N possible
         for the build-up of the next oscillation. The synchroniza­        states each bit has a o n e and a z e r o appearing with equal
         tion signal can, therefore, have two possible magnitudes.         frequency. Hence the reversible computer can utilize
         If all three of the inputs agree we get a synchronization         only those truth functions whose truth table exhibits equal
         signal three times as big as in the case where only two           numbers of o n e s and z e r o s. The admissible truth func­
         inputs have a given phase. If the subharmonic circuit is          tions then are the identity and negation, the e x c lu s iv e o r
         lossless the subsequent build-up will then result in two dif­     and its negation. These, however, are not a complete sets
         ferent amplitudes, depending on the size of the initial syn­      and do not permit a synthesis o f all other truth functions.
         chronization signal. This, however, will interfere with the           In the third level of our argument we permit more
         basic operation of the scheme at the next stage, where we         general devices. Consider, for example, a particular three-
         will want to combine outputs of three oscillators again,          input, three-output device, i.e., a small special purpose
         and will want all three to be of equal amplitude. We thus         computer with three bit positions. Let p, q, and r be the
         see that the absence of the losses gives us an output am­         variables before the machine cycle. The particular truth
         plitude from each oscillator which is too dependent on            function under consideration is the one which replaces
         inputs at an earlier stage. While perhaps the deviation           r by p * q if r^O, and replaces r by p •q if r= 1. The vari­
         from the desired amplitudes might still be tolerable after        ables p and q are left unchanged during the machine
         one cycle, these deviations could build up, through a             cycle. We can consider r as giving us a choice of pro­
         period of several machine cycles. The losses, therefore,          gram, and p, q as the variables on which the selected
         are needed so that the unnecessary details of a signal’     s     program operates. This is a logically reversible device,
         history will be obliterated. The losses are essential for         its output always defines its input uniquely. Nevertheless
         the standardization of signals, a function which in past          it is capable of performing an operation such as and
         theoretical discussions has perhaps not received adequate         which is not, in itself, reversible. The computer, however,
         recognition, but has been very explicitly described in a          saves enough o f the input information so that it supple­
         recent paper by A. W. Lo.7                                        ments the desired result to allow reversibility. It is inter­
                                                                           esting to note, however, that we did not “             save” the
         3. Logical irreversibility
                                                                           program; we can only deduce what it was.
         In the Introduction we analyzed Fig. 1 in connection                  Now consider a more general purpose computer, which
         with the command r e s t o r e t o o n e and argued that this     usually has to go through many machine cycles to carry
         required energy dissipation. We shall now attempt to               out a program. At first sight it may seem that logical
         generalize this train of thought, r e s t o r e t o o n e is an   reversibility is simply obtained by saving the input in
         example o f a logical truth function which we shall call          some corner of the machine. We shall, however, label a
         irreversible. We shall call a device logically irreversible if     machine as being logically reversible, if and only if all its
         the output of a device does not uniquely define the inputs.        individual steps are logically reversible. This means that
         We believe that devices exhibiting logical irreversibility        every single time a truth function of two variables is
         are essential to computing. Logical irreversibility, we           evaluated we must save some additional information
         believe, in turn implies physical irreversibility, and the         about the quantities being operated on, whether we need
         latter is accompanied by dissipative effects.                      it or not. Erasure, which is equivalent to r e s t o r e t o one,
            We shall think of a computer as a distinctly finite array       discussed in the Introduction, is not permitted. We will,
         of N binary elements which can hold information, with­             therefore, in a long program clutter up our machine bit
         out dissipation. We will take our machine to be synchro­           positions with unnecessary information about intermedi­
         nous, so that there is a well-defined machine cycle and at         ate results. Furthermore if we wish to use the reversible
         the end of each cycle the N elements are a complicated             function of three variables, which was just discussed, as
         function o f their state at the beginning of the cycle.            an and, then we must supply in the initial programming
            Our arguments for logical irreversibility will proceed          a separate z e r o for every an d operation which is subse­
         on three distinct levels. The first-level argument consists        quently required, since the “    bias”which programs the
         simply in the assertion that present machines do depend            device is not saved, when the a n d is performed. The
         largely on logically irreversible steps, and that therefore        machine must therefore have a great deal of extra ca­
         any machine which copies the logical organization of               pacity to store both the extra “     bias”bits and the extra
         present machines will exhibit logical irreversibility, and         outputs. Can it be given adequate capacity to make all
         therefore by the argument of the next Section, also physi­         intermediate steps reversible? If our machine is capable,
         cal irreversibility.                                               as machines are generally understood to be, of a non­
            The second level of our argument considers a particu­           terminating program, then it is clear that the capacity
         lar class of computers, namely those using logical func­           for preserving all the information about all the inter­
         tions of only one or two variables. After a machine cycle          mediate steps cannot be there.
         each of our N binary elements is a function of the state               Let us, however, not take quite such an easy way out.
         of at most two of the binary elements before the machine           Perhaps it is just possible to devise a machine, useful in
186      cycle. Now assume that the computer is logically reversi­          the normal sense, but not capable of embarking on a

IBM JOURNAL •JULY 1961
non term inating program. Let us take such a machine as it       one of 2N states (for N bits in the assembly) and there­
normally comes, involving logically irreversible truth           fore the entropy can increase by kN \oge 2 as the initial
functions. An irreversible truth function can be made            information becomes thermalized.
into a reversible one, as we have illustrated, by “ embed­          Note that our argument here does not necessarily
ding”it in a truth function of a large number of variables.      depend upon connections, frequently made in other writ­
The larger truth function, however, requires extra inputs        ings, between entropy and information. We simply think
to bias it, and extra outputs to hold the information which      of each bit as being located in a physical system, with
provides the reversibility. What we now contend is that          perhaps a great many degrees of freedom, in addition to
this larger machine, while it is reversible, is not a useful     the relevant one. However, for each possible physical
computing machine in the normally accepted sense of the          state which will be interpreted as a z e r o , there is a very
word.                                                            similar possible physical state in which the physical sys­
   First of all, in order to provide space for the extra         tem represents a on e. Hence a system which is in a o n e
inputs and outputs, the embedding requires knowledge of          state has only half as many physical states available to it
the number of times each of the operations of the origi­         as a system which can be in a o n e or z e r o state. (We
nal (irreversible) machine will be required. The useful­         shall ignore in this Section and in the subsequent con­
ness of a computer stems, however, from the fact that it         siderations the case in which the o n e and z e r o are rep­
is more than just a table look-up device; it can do many         resented by states with different entropy. This case
programs which were not anticipated in full detail by the        requires arguments of considerably greater complexity
designer. Our enlarged machine must have a number of             but leads to similar physical conclusions.)
bit positions, for every embedded device of the order                In carrying out the r e s t o r e t o o n e operation we are
of the number of program steps and requires a number of          doing the opposite of the thermalization. We start with
switching events during program loading comparable to            each bit in one of two states and end up with a well-
the number that occur during the program itself. The             defined state. Let us view this operation in some detail.
setting of bias during program loading, which would                 Consider a statistical ensemble of bits in thermal
typically consist of restoring a long row of bits to say         equilibrium. If these are all reset to on e, the number of
ze ro , is just the type of nonreversible logical operation      states covered in the ensemble has been cut in half. The
we are trying to avoid. Our unwieldy machine has there­          entropy therefore has been reduced by k loge 2 = 0.6931 k
fore avoided the irreversible operations during the run­         per bit. The entropy of a closed system, e.g., a computer
ning of the program, only at the expense of added com ­          with its own batteries, cannot decrease; hence this entropy
parable irreversibility during the loading of the program.       must appear elsewhere as a heating effect, supplying
                                                                 0.6931 kT per restored bit to the surroundings. This is,
4. Logical irreversibility and entropy generation
                                                                 of course, a minimum heating effect, and our method of
The detailed connection between logical irreversibility          reasoning gives no guarantee that this minimum is in fact
and entropy changes remains to be made. Consider again,          achievable.
as an example, the operation r e s t o r e t o on e. The gen­        Our reset operation, in the preceding discussion, was
eralization to more complicated logical operations will          applied to a thermal equilibrium ensemble. In actuality
be trivial.                                                      we would like to know what happens in a particular com ­
   Imagine first a situation in which the r e s t o r e opera­   puting circuit which will work on information which has
tion has already been carried out on each member of an           not yet been thermalized, but at any one time consists
assembly of such bits. This is somewhat equivalent to an         of a well-defined z e r o or a well-defined on e. Take first
assembly of spins, all aligned with the positive z-axis. In       the case where, as time goes on, the reset operation is
thermal equilibrium the bits (or spins) have two equally          applied to a random chain of o n e s and z e r o s . We can,
favored positions. Our specially prepared collections             in the usual fashion, take the statistical ensemble equiva­
show much more order, and therefore a lower tempera­             lent to a time average and therefore conclude that the
ture and entropy than is characteristic of the equilibrium       dissipation per reset operation is the same for the time-
state. In the adiabatic demagnetization method we use            wise succession as for the thermalized ensemble.
such a prepared spin state, and as the spins become dis­             A computer, however, is seldom likely to operate on
oriented they take up entropy from the surroundings and           random data. One of the two bit possibilities may occur
thereby cool off the lattice in which the spins are em­           more often than the other, or even if the frequencies are
bedded. An assembly of ordered bits would act similarly.          equal, there may be a correlation between successive bits.
As the assembly thermalizes and forgets its initial state         In other words the digits which are reset may not carry
the environment would be cooled off. Note that the impor­         the maximum possible information. Consider the extreme
tant point here is not that all bits in the assembly initially    case, where the inputs are all on e, and there is no need
agree with each other, but only that there is a single,          to carry out any operation. Clearly then no entropy
well-defined initial state for the collection of bits. The       changes occur and no heat dissipation is involved. Alter­
well-defined initial state corresponds, by the usual statis­     natively if the initial states are all z e r o they also carry no
tical mechanical definition of entropy, S = k logc W, to         information, and no entropy change is involved in reset­
zero entropy. The degrees of freedom associated with the         ting them all to on e. Note, however, that the reset opera­
information can, through thermal relaxation, go to any           tion which sufficed when the inputs were all o n e (doing           187

                                                                                                                 IBM JOURNAL •JULY 1961
              nothing) will not suffice when the inputs are all z e r o .           BEFORE     CYCLE                    AFTER C Y C L E
                                                                                                                                               final
              When the initial states are z e r o , and we wish to go to            P      q       r                   Pi      q,              STATE
              o n e , this is analogous to a phase transformation between
              two phases in equilibrium, and can, presumably, be done
              reversibly and without an entropy increase in the uni­
              verse, but only by a procedure specifically designed for
              that task. We thus see that when the initial states do not
              have their fullest possible diversity, the necessary entropy
              increase in the r e s e t operation can be reduced, but only
              by taking advantage of our knowledge about the inputs,
              and tailoring the reset operation accordingly.
                 The generalization to other logically irreversible oper­
              ations is apparent, and will be illustrated by only one            F ig u re s    Three input - three output device which
              additional example. Consider a very small special-purpose                         maps eight possible states onto only four
              computer, with three binary elements p, q , and r. A ma­                          different states.
              chine cycle replaces p by r, replaces q by r, and replaces
              r by p •q. There are eight possible initial states, and in
              thermal equilibrium they will occur with equal proba­              pared to kT. Let us, furthermore, assume that switching
              bility. How much entropy reduction will occur in a                 is accomplished by the addition of a force which raises
              machine cycle? The initial and final machine states are            the energy of one well with respect to the other, but still
              shown in Fig. 5. States a and p occur with a probability           leaves a barrier which has to be surmounted by thermal
              of Vs each: states y and S have a probability of occur­            activation. (A sufficiently large force will simply elimi­
              rence of % each. The initial entropy was                           nate one of the minima completely. Our switching forces
                                                                                 are presumed to be smaller.) Let us now consider a
              Si = k log,           —k%p log, p                                  statistical ensemble of double well systems with a non­
                = —k ^ i log, i = 3k log, 2 .                                    equilibrium distribution and ask how rapidly equilibrium
                                                                                 will be approached. This question has been analyzed in
              The final entropy is                                               detail in an earlier paper,2 and we shall therefore be satis­
              *S'/™ kXp log, p                                                   fied here with a very simple kinetic analysis which leads
                                                                                 to the same answer. Let nA and nB be the number of en­
                 - —k ( i log i + i log i + i log f + i log %).                  semble members in Well A and Well B respectively. Let
              The difference Si—Sf is 1,18 k. The minimum dissipation,            Ua and Ub be the energies at the bottom of each well and
              if the initial state has no useful information, is therefore       U that of the barrier which has to be surmounted. Then
              3.18 kT.                                                           the rate at which particles leave Well A to go to Well B
                 The question arises whether the entropy is really re­           will be of the form vnAexp[—(£/—UA)/ kT]. The flow
              duced by the logically irreversible operation. If we really        from B to A will be vnB exp[~- (E/—UB)/kT]. The two
              map the possible initial z e r o states and the possible initial   frequency factors have been taken to be identical. Their
              o n e states into the same space, i.e., the space of o n e
                                                                                 differences are, at best, unimportant compared to the
              states, there can be no question involved. But, perhaps,           differences in exponents. This yields
              after we have performed the operation there can be some            driA
              small remaining difference between the systems which               — —= - nAv exp[—(U—Uyi)/kT]
                                                                                  at
              were originally in the o n e state already and those that
                                                                                      + nBv exp[—■
                                                                                                 (£/ —UB)/kT~\ ,
              had to be switched into it. There is no harm in such
              differences persisting for some time, but as we saw in the         dn B
              discussion of the dissipationless subharmonic oscillator,                        nAv exp[~ (£/—UA)/kT~}
                                                                                  dt
              we cannot tolerate a cumulative process, in which dif­                           nBv exp[ —(U —Ub )/kT]                           (5.1)
              ferences between various possible o n e states become
              larger and larger according to their detailed past histories.      We can view Eqs. (5.1) as representing a linear trans
              Hence the physical “    many into one”mapping, which is
                                                                                                                             dnA dnB
              the source of the entropy change, need not happen in full          formation on (nA, nB), which yields { —— > — — i - What
              detail during the machine cycle which performed the logi­                                                        dt         dt
              cal function. But it must eventually take place, and this          are the characteristic values of the transformation? They
              is all that is relevant for the heat generation argument.          are:
              5. Detailed analysis of bistable well                              Ai = 0, A2= - v exp[(£/—UA)/kT]
               To supplement our preceding general discussion we shall                           —v e x p [ - ( U —UB)/kT] .
               give a more detailed analysis of switching for a system
               representable by a bistable potential well, as illustrated,       The eigenvalue Ai=0 corresponds to a time-independent
188            one-dimensionally, in Fig. 1, with a barrier large com-           well population. This is the equilibrium distribution

I B M J O U R N A L •J U L Y 1961
                                                                 time. (This model is probably closer to the behavior of
rtA= nB exp — [UB—Ua] •                                          ferrites and ferroelectrics, when the switching occurs by
            kT
                                                                 domain wall motion, than our preceding bistable well
   The remaining negative eigenvalue must then be asso­          model. The energy differences between a completely
ciated with deviations from equilibrium, and exp( —A20           switched and a partially switched ferrite are rather small
gives the rate at which these deviations disappear. The          and it is the existence of a low domain-wall mobility
relaxation time r is therefore in terms of a quantity t/o,       which keeps the particle near its initial state, in the ab­
which is the average of UA and UB                                sence of switching forces, and this initial state can almost
1                                                                equally well be a partially switched state, as a completely
- = A 2= v exp[— ( 17— Uo)/kT                                    switched one. On the other hand if one examines the
T
                                                                 domain wall mobility on a sufficiently microscopic scale
             •{ ex p [ - ( U o- U A)k T ]+ exp[(U o-U B)kT]} .
                                                                 it is likely to be related again to activated motion past
                                                         (5.2)   barriers.) In that case, particles will diffuse a typical dis­
                                                                 tance s in a time t ~ s 2/ 2 D . D is the diffusion constant.
The quantity U0 in Eq. (5.2) cancels out, therefore the
                                                                 The distance which corresponds to information loss is
validity of Eq. (5.2) does not depend on the definition of
                                                                 s-a, the associated relaxation time is ro~a2/2D. In the
Uo. Letting A = i( U A—UB), Eq. (5.2) then becomes
                                                                 presence of a force F the particle moves with a velocity
1                                                                ju,F, where the mobility p is given by the Einstein relation
- -2v ex p [ - (U - Uo)/AT]cosh A/AJ .                   (5.3)   as D /k T . T o move a particle under a switching force F
r
                                                                 through a distance 2a requires a time t8 given by
To first order in the switching force which causes UA and
UB to differ, (t/—Uo) will remain unaffected, and there­         juFr* = 2a,                                             (5.5)
fore Eq. (5.3) can be written                                    or
1          1                                                     rs = 2a/fiF.                                            (5.6)
—         — cosh A/AT ,                                  (5.4)
T         TO
                                                                 The energy dissipation 2A, is a 2aF. This gives us the
where r0 is the relaxation time for the symmetrical poten­       equations
tial well, when A =0. This equation demonstrates that the
device is usable. The relaxation time r0 is the length of        T«= 2a2//jtA,                                           (5.7)
time required by the bistable device to thermalize, and          t8/ to=4AT/A,                                           (5.8)
represents the maximum time over which the device is
usable, r on the other hand is the minimum switching             which show the same direction of variation of r«with A
time. Cosh A/AT therefore represents the maximum num­            as in the case with the barrier, but do not involve an expo­
ber of switching events in the lifetime of the information.      nential variation with A/AT. If all other considerations
Since this can be large, the device can be useful. Even if       are ignored it is clear that the energy bistable element of
A is large enough so that the first-order approximation          Eq. (5.4) is much to be preferred to the diffusion stabil­
needed to keep U —Uo constant breaks down, the expo­             ized element of Eq. (5.8).
nential dependence of cosh A/AT on A, in Eq. (5.3) will             The above examples give us some insight into the need
far outweigh the changes in exp[(t/~ Uo)kT], and to/t            for energy dissipation, not directly provided by the argu­
will still be a rapidly increasing function of A.                ments involving entropy consideration. In the r e s t o r e t o
   Note that A is one-half the energy which will be dissi­       o n e operation we want the system to settle into the o n e
pated in the switching process. The thermal probability          state regardless of its initial state. We do this by lowering
distribution within each well will be about the same             the energy of the o n e state relative to the z e r o state.
before and after switching, the only difference is that the      The particle will then go to this lowest state, and on the
final well is 2A lower than the initial well. This energy        way dissipate any excess energy it may have had in its
difference is dissipated and corresponds to the one-half         initial state.
hysteresis loop area energy loss generally associated with
                                                                 6. Three sources of error
switching. Equation (5.4) therefore confirms the em­
pirically well-known fact that increases in switching            We shall in this section attempt to survey the relative
speed can only be accomplished at the expense of in­             importance of several possible sources o f error in the
creased dissipation per switching event. Equation (5.4)          computing process, all intimately connected with our pre­
is, however, true only for a special model and has no            ceding considerations. First of all the actual time allowed
really general significance. T o show this consider an           for switching is finite and the relaxation to the desired
alternative model. Let us assume that information is             state will not have taken place completely. If Ts is the
stored by the position of a particle along a line, and that      actual time during which the switching force is applied
x ±a correspond to z e r o and on e, respectively. No
    * =                                                          and t 8 is the relaxation time of Eq. (5.4) then exp
barrier is assumed to exist, but the random diffusive            ( — T s/ t 8) is the probability that the switching will not

motion of the particle is taken to be slow enough, so that       have taken place. The second source of error is the one
positions will be preserved for an appreciable length of         considered in detail in an earlier paper by J. A. Swanson,5       189

                                                                                                                IBM JOURNAL •JULY 1961
         and represents the fact that t 0 is finite and information        mitted by Eq. (5.4), is small compared to unity.
         will decay while it is supposed to be sitting quietly in its         Consider now, instead, the diffusion stabilized element
         initial state. The relative importance of these two errors        of Eq. (5.8). For it, we can find instead of Eq. (6.4) the
         is a matter of design compromises. The time TSi allowed           relationship
         for switching, can always be made longer, thus making
                                                                           exp(—T s/ ts) > exp[(—A/4&T)exp( - 2A/kT) ],          (6.5)
         the switching relaxation more complete. The total time
         available for a program is, however, less than t o , the relax­   and the right-hand side is again large compared to the
         ation time for stored information, and therefore increas­         Boltzmann error, exp(-~2A/&r). The alternative argu­
         ing the time allowed for switching decreases the number           ment in terms of the accumulated Boltzmann error exists
         of steps in the maximum possible program.                         also in this case.
            A third source of error consists of the fact that even if         When we attempt to consider a more realistic machine
         the system is allowed to relax completely during switching        model, in which switching forces are applied to coupled
         there would still be a fraction of the ensemble of the            devices, as is done for example in diodeless magnetic
         order exp( —2A/kT) left in the unfavored initial state.           core logic,4 it becomes difficult to maintain analytically a
         (Assuming A»/cT.) For the purpose of the subsequent               clean-cut breakdown of error types, as we have done here.
         discussion let us call this Boltzmann error. We shall show        Nevertheless we believe that there is still a somewhat
         that no matter how the design compromise between the              similar separation which is manifested.
         first two kinds of errors is made, Boltzmann error will
         never be dominant. We shall compare the errors in a
         rough fashion, without becoming involved in an enumera­
                                                                           Summary
         tion of the various possible exact histories of information.
            To carry out this analysis, we shall overestimate Boltz­       The information-bearing degrees of freedom of a com­
         mann error by assuming that switching has occurred in             puter interact with the thermal reservoir represented by
         every machine cycle in the history of every bit. It is this       the remaining degrees of freedom. This interaction plays
         upper bound on the Boltzmann error which will be shown            two roles. First of all, it acts as a sink for the energy
         to be negligible, when compared to other errors. The              dissipation involved in the computation. This energy dis­
         Boltzmann error probability, per switching event is               sipation has an unavoidable minimum arising from the
         exp( —2A/kT). During the same switching time bits                 fact that the computer performs irreversible operations.
         which are not being switched are decaying away at the             Secondly, the interaction acts as a source of noise causing
         rate exp( —t/ro). In the switching time Ts, therefore,            errors. In particular thermal fluctuations give a supposedly
         unswitched bits have a probability T 8/ tq of losing their        switched element a small probability of remaining in its
         information. If the Boltzmann error is to be dominant             initial state, even after the switching force has been ap­
                                                                           plied for a long time. It is shown, in terms of two simple
         Ts/ to < exp( - 2A/kT) .                                 (6.1)
                                                                           models, that this source of error is dominated by one of
         Let us specialize to the bistable well of Eq. (5.4). This         two other error sources:
         latter equation takes (6.1) into the form
                                                                           1) Incomplete switching due to inadequate time allowed
         2T                                                                   for switching.
         — -exp( —A /& r)<exp( —2A/&T) ,                          (6-2)
          t8                                                               2) Decay of stored information due to thermal fluctua­
         or equivalently                                                      tions.
                                                                              It is, of course, apparent that both the thermal noise
         — —< £ e x p ( —A/&T) .                                  (6.3)    and the requirements for energy dissipation are on a scale
          TS
                                                                           which is entirely negligible in present-day computer com­
         Now consider the relaxation to the switched state. The er­        ponents. The dissipation as calculated, however, is an
         ror incurred due to incomplete relaxation is exp(—7 V t s),       absolute minimum. Actual devices which are far from
         which according to Eq. (6.3) satisfies                            minimal in size and operate at high speeds will be likely
                                                                           to require a much larger energy dissipation to serve the
         exp( —Tb/ t 8) > ex p [ —iexp( —A/&T) ].                 (6.4)
                                                                           purpose of erasing the unnecessary details of the com­
         The right-hand side of this inequality has as its argument        puter’ s past history.
         iexp( —A/kT) which is less than i. Therefore the right-
         hand side is large compared to exp( —2A/kT), the Boltz­
         mann error, whose exponent is certainly larger than unity.
                                                                           Acknowledgments
         We have thus shown that if the Boltzmann error domi­
         nates over the information decay, it must in turn be              Some of these questions were first posed by E. R. Piore
         dominated by the incomplete relaxation during switching.          a number of years ago. In its early stages2’5 this project
           A somewhat alternate way of arguing the same point              was carried forward primarily by the late John Swanson.
         consists in showing that the accumulated Boltzmann error,         Conversations with Gordon Lasher were essential to the
190      due to the maximum number of switching events per­                development of the ideas presented in the paper.

IBM JOURNAL •JULY 1961
References                                                          room temperature, if the activation energy for its motion is
                                                                    sufficiently large (~ several electron volts).
1. L. Brillouin, Science and Information Theory, Academic
   Press Inc., New York, New York, 1956.                            (2) Swanson’ s optimum volume is, generally, not very
                                                                    different from the common sense requirement on U,
2. R. Landauer and J. A. Swanson, Phys. Rev., 121, 1668             namely: vt exp( —l/AT)<$0, which would be found with­
   (1961).                                                          out the use of information theory. This indicates that the
                                                                    use of redundancy and complicated coding methods does
3. K. Mendelssohn, Progress in Cyrogenics, Yol. 1, Academic         not permit much additional information to be stored. It is
   Press Inc., New York, New York, 1959. Chapter I by               obviously preferable to eliminate these complications, since
   D. R. Young, p. 1.                                               by making each element only slightly larger than the
4. L. B. Russell, IRE Convention Record, p. 106 (1957).             “optimum”value, the element becomes reliable enough to
                                                                    carry information without the use of redundancy.
5. J. A. Swanson, IBM Journal, 4, 305 (1960).
   We would like to take this opportunity to amplify two          6. R. L. Wigington, Proceedings of the IRE, 47, 516 (1959).
   points in Swanson’  s paper which perhaps were not ade­
   quately stressed in the published version.                     7. A. W. Lo, Paper to appear in IRE Transactions on Elec­
                                                                     tronic Computers.
  (1) The large number of particles (~100) in the optimum
  element are a result of the small energies per particle         8. D. Hilbert and W. Ackermann, Principles of Mathematical
  (or cell) involved in the typical cooperative phenomenon           Logic, Chelsea Publishing Co., New York, 1950, p. 10.
  used in computer storage. There is no question that infor­
  mation can be stored in the position of a single particle, at   Received October 5,1960

                                                                                                                                   191

                                                                                                                IBM JOURNAL •JULY 1961

