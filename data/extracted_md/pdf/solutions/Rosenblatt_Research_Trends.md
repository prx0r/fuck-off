# COPY

**source:** pdf · **section:** solutions
**file:** Rosenblatt_Research_Trends
---

Vol. VI, No, 2, Summer 1958

                  “research
                                                                  trends
                         CORNELL       AERONAUTICAL            LABORATORY,      INC.,    BUFFALO      21,   NEW    YORK

The Design of an

                     f

                                                by FRANK ROSENBLATT                              a
                                                                                             4

                         Introducing the perceptron — A machine                 which senses,
                         recognizes, remembers, and responds like the human mind.

cise about the creation of machines having                          First, in recent years our knowledge of the function-
human qualities have long been a fascinating province          ing of individual cells in the central nervous system has
in the realm of science fiction. Yet we are now about to       vastly increased.
witness the birth of such a machine — a machine capable             Second, large numbers of engineers and mathema-
of perceiving, recognizing, and identifying its surround-      ticians are, for the first time, undertaking serious study
ings without any human training or control.                    of the mathematical basis for thinking, perception, and
    Development of that machine has stemmed from a             the handling of information by the central nervous sys-
search for an understanding of the physical mechanisms         tem, thus providing the hope that these problems may
which underlie human experience and intelligence. The          be within our intellectual grasp.
question of the nature of these processes is at least as           Third, recent developments in probability theory
ancient as any other question in western science and           and in the mathematics of random processes provide
philosophy, and, indeed, ranks as one of the greatest          new tools for the study of events in the nervous system,
scientific challenges of our time.                             where only the gross statistical organization is known
     Our understanding of this problem has gone perhaps        and the precise cell-by-cell “wiring diagram” may never
as far as had the development of physics before Newton.        be obtained.
We have some excellent descriptions of the phenomena
to be explained, a number of interesting hypotheses, and       Receives Navy Support
a little detailed knowledge about events in the nervous           In July, 1957, Project PARA (Perceiving and Recog-
system. But we lack agreement on any integrated set of         nizing Automaton), an internal research program which
principles by which the functioning of the nervous             had been in progress for over a year at Cornell Aero-
system can be understood.                                      nautical Laboratory, received the support of the Office
    We believe now that this ancient problem is about          of Naval Research. The program had been concerned
to yield to our theoretical investigation for three reasons:   primarily with the application of probability theory to
                                                                                                                             *
                                                                                                                                                                                                                            |
      the problem of memory and perception. In undertaking                                                                                  Area (Outer               Area (Deeper           Cortex
                                                                                                                                                                                                                            |
      this investigation, the author assumed at the outset that                                            Projection   Area                layer)                    layers)

      the organization of the sensory world of light, sound,                                                                                                                                          Raise
                                                                                                                                                                                                                            |

      temperature, pressure, etc., is learned, rather than being                                                                                                                                      Arm

     immediately self-evident to the perceiving system.
         In other words, an organism fully equipped with
     visual apparatus, and exposed to an environment of,
     say, squares and circles, would not be able to tell these
     forms apart unless it has specifically learned to do so.
     This means in the fullest sense that the two kinds of
                                                                                                                                                                                                                            |
                                                                                                                                                                                                                            |

     forms would be indistinguishable at the outset, i.e., that
     two squares, chosen at random, would appear to be no                           FIG. 1 — Organization of a biological brain.                                                (Red areas indicate
                                                                                                  active cells, responding to the letter X.)
     more alike than a square and circle, similarly chosen at
     random. Inasmuch as people are unable to report their
                                                                                                                                                           Association
                                                                                             Mosaic of                    Projection area
                                                                                                                                                               (A-units)               Units                            4
     experiences as infants, experimental observations have
                                                                                            Sensory                       (in some models)
                                                                                            Points

     been unable to establish a definite case for or against the                                                               ID
                                                                                                                                                                      <
                                                                                                                                                                                               |        Output Signal
     theory that perception of “similarity” must be learned.                                                                                              ce

                                                                                                                                                                 ee

                                                                                                                                                          coe

                                                                                                                                                                       e                Rs
     Problem of Perceptual Generalization
                                                                                                                                                     NG
          For the engineer or mathematician attempting to                                                                                                 je

     construct a system which will “learn to perceive” (i.e. a                                           Topographic                    Random

     system which, in the environment of squares and circles,
                                                                                                         Connections                    Connections                                     R
                                                                                                                                                                 Feedback                      |
                                                                                                                                                                 Circuits
     will spontaneously arrive at the conclusion that there
     are two classes of forms present), the principal difficulty
                                                                                                      FIG. 2 — Organization of a perceptron.
     is the problem known as “perceptual generalization.”
     If a square always appeared in the same position, at the
     same angular orientation, and reduced to the same size,                        limited sample of forms from a given class, the per-
     and if all other geometrical forms were similarly reduced                      ceiving system is able to recognize any member of that
                                                                                    class (e.g., a man in any posture, angular orientation, or
     to some standard transformation, it would be a relatively
                                                                                    costume), even if it has never seen the particular image
     simple matter to distinguish among such forms, and to
     assign a new form to its appropriate class by simply                           before. While the problem is here stated in terms of the
                                                                                    visual sense, it is clear that the same problem exists when
     matching it against all members of a library of stored
     images.                                                                        other senses are used. One of the most interesting forms
         A system which will perform this reduction to                             of this problem is in speech recognition.
     standard position, size, etc., is extremely cumbersome,
                                                                                       The design of a physical system which can recognize
     however, and still leaves the more baffling problem of                        “similarities” in our complex environment, where
     how non-rigid forms, such as a man or an ocean wave,                          countless demands are made on all of our senses, and
     can be recognized. The problem of perceptual general-                         which tends, spontaneously, to form meaningful class-
     ization is concerned with how, after exposure to a                            ifications of stimuli in such an environment, has been                                                                               |
                                                                                   the main objective of Project PARA.

                                                                                    Understanding the Perceptron
                                                                                        To understand the proposed machine — or percep-                                                                                 |
                                       THE
                                       COVER
                                                                                    tron — it is necessary first to understand something of
                                                                                    the nature of the brain and how it works. Figure 1                                                                                  |
                                                                                    represents the basic organization of the human brain,
                                                                                   including the motor cortex, which controls physical
                                                                                   responses. This organization has been well established
                                       Resistance thermometers for                 through physiological and anatomical studies. The con-
                                      emeasuring heat transfer rates in
                                       shock tunnels have been success-            nections from the retina to the visual projection area
                                       fully developed by CAL in con-              provide a sort of map of the visual field in the brain.
                                       junction with its hypersonic re-            Beyond this point, however, connections appear to be-
                                       search. Here, the skilled hands
                                       of a technician insert a glass but-         come increasingly random, so that in the association
                                      ton    with   a resistance     thermom-      areas (which appear to be mainly responsible for learn-
                                      eter mounted on it into a slender
                                      wedge. Five such wedges are
                                                                                   ing and memory) it is no longer possible to relate a
                                      used    in    a   rake,   or   series   of   particular point to some specific location in the retina.
                                    probes, to calibrate flow in a                 The association cells of the brain are likely to respond
hypersonic shock tunnel.   Each wedge has a resistance thermometer
on both faces.   Thus, by measuring    the heat transfer        rate on both       to any one of a vast number of different stimuli from
sides of the wedge, it is possible to measure both flow angularity and             any of the five senses.
flow Mach number. Resistance thermometers are fabricated in the                        Inputs to the association area tend to arrive at the
Materials Department for the hypersonic research activities of the
Aerodynamic Research Department.                                                   surface layers of cells, while outputs emanate from the
                                                                                   deeper layers. Feedback circuits between these layers
2|
        |

            are so organized that a cell in a deeper layer is more       concept, or abstraction, in terms of which the environ-
            likely to feed back to the same outer layer cells which      ment is organized.
        |
            caused its activity than to cells which take no part in          At the outset, when a perceptron is first exposed to
                                                                                                                                        ‘

            its stimulation. When impulses arrive at the motor           stimuli, the responses which occur will be random, and
            cortex, an intelligible order appears to have been re-       no meaning can be assigned to them. As time goes on,
    |
            stored. The motor cortex apparently contains a kind          however, changes which occur in the association system
            of map of the body surface, so that stimulation of a         cause individual responses to become more and more
            particular location will lead to a specific muscular         specific to such particular, well-differentiated classes of
            response. Thus the confusion of connections through          forms as squares, triangles, clouds, trees, or people.
    |       the association area has somehow “recognized” the                 In order to clarify the foregoing process, it is neces-
            visual stimulus, and developed an output signal which        sary first to point out a fundamental feature of the per-
            is constrained to particular, relevant channels.             ceptron — a feature whose biological counterpart has
                                                                         not yet been demonstrated. When an A-unit of the
            Mystery Still Exists                                         perceptron has been active, there is a persistent after-
    |
                The channels into and out of the central nervous         effect which serves the function of a “memory trace.”
            system have been rather well mapped. We know what            The assumed characteristic of this memory trace is a
            points in the projection area will respond, say, to a ray    simple one: whenever a cell is active, it gains in
            of light in the lower right quadrant of the visual field,    “strength,” so that its output signals (in response to a
            and we know where in the motor cortex the signal             fixed stimulus) become stronger, or gain in frequency
            which causes a man to raise his left arm originates. The     or probability. The strength of an A-unit is measured
            big mystery is how the apparently unintelligible tangle      in units of “value” (v), a hypothetical quantity. All
            of connections in the association area manages to record     theoretical attempts to account for learning in the
            the fact that a beam of light (or a dog, or a landscape)     nervous system have ultimately been forced to assume
            is actually seen, and how the impulses from the visual       some functional change which serves the same purpose
            stimulus are interpreted in such a manner as to select       as V.
            the single appropriate response channel.
                In Figure 2 is shown the organization of a system        Simple Memory Hypothesis
            whose “anatomy” is completely known — the percep-                The variable v appears to be the simplest, and in
            tron. This system is capable of the same functions of        some ways the most plausible, memory hypothesis ad-
|
|
            sensing, recognition,   retention, and response selection    vanced to date. Further, the perceptron is the first system
            as its biological counterpart. Although the similarity of    proven to be workable with so simple a memory mechan-
            organization to the biological brain is clearly evident,     ism. An examination of the behavior of A-unit values in
            certain differences and simplifications should be noted.     more advanced models of the perceptron makes it clear
|              First, the projection area, which is found in all ad-     that such a variable would be exceedingly difficult to             .

            vanced biological systems, is not essential for the per-     detect, physiologically. The values of the A-units tend to
            ceptron. In simplified models, the retinal points are        a terminal equilibrium condition, from which they may
}           assumed to be connected directly to randomly selected        fluctuate slightly, either positively or negatively. It is
            units (A-units) in the association system. In other words,   not surprising, therefore, that such an erratic variable
|

            each sensory point may be connected to one or more           has escaped detection in physiological experiments.
            A-units chosen at random from all possible units in the      Nonetheless, such slight fluctuations exert a mass sta-
|
            system.                                                      tistical effect which can be demonstrated to enable the
                Second, the responses (R-units) of the perceptron        perceptron to form new associations, to “store” mem-
            are typically binary devices which are either on or off,     ories, and to select appropriate responses.
            or which may sometimes have a third “neutral” con-                A simple perceptron is shown in detail in Fig. 3. The
            dition. Little attention has been given to responses which   circles in this figure represent sets of units, and there
            must vary in intensity, the R-units of the perceptron
            being used to signal the state of the system.
                Third, the R-units of the perceptron actually com-                                                   Reinforce
            bine the functions of the second association layer with
            those of the motor cortex. The R-units transmit feed-
            back signals to the same A-units which are responsible
            for activating the unit in the first place.

            Meaning of Responses
                These response units of the perceptron are more like
            special association cells whose activity represents the                                                                             Pe

            brain’s recognition response to various stimuli, rather
            than cells in the motor cortex which regulate speech or
            movement. The activation of a particular response for
            the perceptron might mean, for example, that a triangle                                                  Reinforce “0”

            is present, or that a man’s voice is being heard. Each
            response is thus capable of representing a particular             FIG. 3 — Detailed organization of a single perceptron.
    might be hundreds or thousands of units in each set. as a test figure, one of the identical stimuli used during
    This perceptron has only a single response unit, which the training period, as in Part B of the example.
    has three possible states: “1”, “O”, or “neutral”.* In          The solid curves show the “probability of correct
    the absence of any signal, the response unit is in a generalization.” This is the probability that the percep-
    neutral state, and delivers no output. In the presence tron will give the appropriate response for any member
    of a signal it tends to oscillate between the neutral state of the stimulus class picked at random, as in Part D of
    and the “1” or “0” condition.                               the example.
        The association system is di-                                                     It can be seen from Fig. 5 that
    vided into two subjects, or “source                                               a perceptron with 100 A-units in
    sets”, one of which tends to activate                            EDITOR’S NOTE                    each source set, which has been
                                                           Because of the unusual        signifi-     trained with 100 squares and 100
    a 1-response, while the other tends
                                                        cance of Dr. Rosenblatt’s        article,     circles, should have a probability
    to activate a O-response. If the                    Research Trends is proud to devote
    total output signal from the 1-                                                                   of 0.92 of giving the correct re-
                                                        this entire issue to it.
    source set is greater than the total                   In the Fall issue, we will return to
                                                                                                      sponse if it is shown one of the
    output signal from the 0-source                    our policy of presenting two articles          squares (or circles) that it has seen
    set, the response      R = 1 tends to              highlighting trends in the Labora-             before. It should also have a prob-
    occur. If the total signal from the                tory’s research.                               ability of 0.85 of giving the correct
    “0” set is greater, the response                                                                  response to a completely random
    R = O tends to occur.                                                                             square or circle which it may never
       In a more elaborate perceptron there may be a large                     have seen before.    If learning experience is continued
    number of such responses, and the source sets for these                    indefinitely, both probabilities converge to the same limit,
    responses will typically cross-cut one another, so that                    in this case 0.887. Thus, in the limit, it makes no differ-
    the same A-unit may be in the source sets of a number                      ence whether the perceptron has seen the particular
    of responses. It can be shown that such multiple func-                     stimulus before or not; it does equally well in either
    tioning of the A-units does not interfere excessively with
                                                          case.
  their performance.                                           The mathematical proof of the foregoing statement
                                                          constitutes a proof of this machine’s ability to form
 Feedback Signals                                         perceptual generalizations.
      The R response causes a feedback signal to be sent       As the number of association units in the perceptron
  back to the members of its own source set. These feed- is increased, the probabilities of correct performance
 back signals have the effect of multiplying the rate of approach unity. From Fig. 5 it is clear that with an
 activity of the A-units which receive them. Thus if amazingly small number of units — in contrast with
 the response should happen to be “1,” each unit in the the human brain’s 10’° nerve cells — the perceptron is
  1-source set might have its rate of activity doubled, capable of highly sophisticated activity.
 while the members of the 0-source set remain unaffected.
 This not only increases the slight original tendency to Can Recognize Patterns
 maintain the response R = 1, it also means that the          It is important to recognize that the mode of opera-
 A-units in the 1-source set will gain in value at a tion of this system does not limit it to such simple, rigid
 greater rate than the units in the O-source set. The in- forms as geometrical figures. Any classes of forms,
 crease in value is referred to as a “reinforcement.” An which meet certain conditions of similarity, can be dis-
 example series of pertinent experiments is shown in tinguished by the perceptron, including such diverse
 Fig. 4.                                                                      patterns as the letters of the alphabet, human profiles,
      It should be emphasized that the condition shown in                     or types of aircraft. With some very slight modifications,
 Part D (Fig. 4 Example) could easily be reversed, if the                     it can be shown that the perceptron should be capable
 perceptron were “trained” with only a single square and                      of recognizing patterns in time (such as speech and
 circle, prior to testing. In order to make this perform-                     movement) as well as patterns in space. A large increase
 ance reliable, the perceptron must first see a sample of                     in the “vocabulary” of the perceptron can be obtained
 squares (say, 100-200 squares in various positions and                       with a relatively slight increase in the number of binary
angular orientations) and a sample of circles, being                          response units.
forced by the experimenter to give the appropriate                                These results were well established, theoretically, by
response to each.                                                             the Fall of 1957 (Ref. 3). At this time a simulation pro-
      The predicted performance of typical perceptrons                        gram was started, using the IBM 704 computer, to de-
with 100, 200, and 500 association ‘cells in each source                      termine how well the theory would hold up in practice.
set, in learning to discriminate two figures which are                        While no digital computer can approach the perceptron
about as “similar” as a square and a circle, is shown in                      in speed and flexibility of performance, such a computer
Fig. 5. The broken curves show the probability that the                       can examine each connection and A-unit of the system
perceptron will give the correct response if it is shown,                     in turn, can then compute the appropriate signals which
                                                                              would be transmitted in a physical network, and can
*The “neutral” state shown in these R-units is introduced in order to avoid
                                                                              next calculate the performance of a perceptron in re-
excessive complexities in the discussion. In the proposed perceptron, the     sponse to a series of visual forms. Many such simulation
R-units will actually be simple binary devices with no intermediate neutral   experiments are now complete, and all main predictions
condition.                                                                    of the theory are substantiated.
4
                                                        FIG.       4 — EXAMPLE         EXPERIMENT

                                                       Reinforce “1”

             Stimulus

         7                                                             R=1
         Wy
                                                                       Neutral                                                                               Neutral

                                                                       R=0

                                                                                                                                           Reinforce   “0”

(A)   Associate square to            R =    1. Red indicates active sets           (B) Associate circle to R = 0. Black shading shows residual
and connections.                                                                   reinforcement from previous experience.

                                                         Strong                                                                           Strong
                                                                                                                                                               R=1
                                                         Signal                         '

                                                                       Neutral                                                                                 Neutral

                                                                                                      !                                                        R=0
                                                        Week _         R= 0
                                                        “signal

                                            Y
                                                                                                                                                                         |

(C)          Test with original square. Solid red areas show effect                                       (D)   Test with random square.
of previous reinforcement.

  In Part A the perceptron           illustrated in Fig. 3 is responding           reinforcement picked up in the I-source set is greater than the
with R =          1 to the image of a square,     in the upper part of the         total reinforcement picked up in the O-source set, so that the
visual field. The red connections are active. Note that an equal                   appropriate     resp         is   expected to occur.
subset of A-units tends to respond to the stimulus in each of the                    But the foregoing experiment is, in a sense, a trivial one, since
two source sets (small red circles). It is assumed that either by                  we clearly cannot pre-train the perceptron on every possible
chance, or because of “forcing” by the experimenter, the response                  square and circle, so as to guarantee that it will give the proper
unit goes to the state R = 1. Consequently, the 1-source set is                    response in a particular case. The critical question is asked in
reinforced at a rapid rate, relative to the O-source set. The re-                  Part D. What happens when we show the perceptron, which
inforcement is indicated by the solid red area, in the set of A-                   was trained in parts A and B, a new square, picked at random,
units responding to the square. At this point, it is clear that if                 which may or may not coincide in size and position with the
the same square were to be repeated, the signal from the 1-source                  square which was previously seen? Will the perceptron still show
set would be stronger than the signal from the O-source set, so                    any tendency to prefer the correct response, or will its choice
that R = 1 would almost certainly be repeated.                                     of response be entirely random?
  In Part B a second stimulus (circle) is shown to the perceptron,                   Now,   if a new square is picked at random,             it can     be demon-
which still curries the residual effects of its previous experience.               strated that it is likely to activate a set of A-units in each source
It is assumed that the response R = 0 occurs, either spontaneously,                set which has more members in common with the sets of A-units
or because of forcing by the experimenter. The added reinforce-                    responding to other squares, than with the sets of A-units
ment is shown by the solid red area in the O-source set.                     The   responding to circles. Consequently, the condition shown in Part
question now is: will the perceptron still give the “appropriate”                  D is most likely to result. Under these circumstances, while some
response (R = 1) if it is again shown the original square?                         reinforcement is expected to be picked up from both the previous
  Part       C shows    that while   some   fraction   of the reinforcement        square-circle reinforcement, the total reinforcement (solid red area)
due to the circle is expected to carry over to the square, because                 in the l-source set remains greater, and the appropriate response
of the intersections of the responding sets of A-units, the total                  should occur.
                                                                                                          biological system known to be capable of classifying,
               Broken curves (Pr) = probability of correct response to training stimulus
              Solid curves(Pg) probability ofcorrectgeneralizotion.
                                                                                                     j
                                                                                                          conceptualizing, and symbolizing its environment —
                                                                                                          particularly a completely new and unanticipated en-
                                                                                                     H
                                                                                                          vironment — in the absence of any human training or
                                                                                                          control.
                                    7
      2                                                                                                   Perceptron Being Built
                 Ye
                                        7
                                                                                                              A working model of a Class C' perceptron is
                    Xx                                                                                    scheduled for completion within the next year. Although
                                                                                                          the economical design of such a system presents several
      6                                                                                                   difficult problems, considerable headway has already
                                                                                                          been made in the design of suitable components. Mean-
                                                                                                          while, the predictions as to the terminal states of a Class
                                                                             RANDOM LEVEL
                                                                                                          C perceptron have already been tested, using the 704
          '                10                     100                    1000               10,000
                                                                                                          as a simulator, and a program to investigate the Class C'
                                        WUMBER
                                           OF STIMULI IN EACH CLASS                                       perceptrons in a similar fashion is in operation.
    FIG. 5 —        Learning curves for three typical perceptrons.                                           There have, of course, been many theoretical brain
                                                                                                         models before the perceptron. We might profitably
    Now although the perceptron developed to that point                                                  summarize the main points which set the perceptron off
could be shown to have an impressive capacity for learn-                                                 from other attempts.
ing and remembering those concepts imposed on it by                                                          (1) The perceptron is the first system which appears
an experimenter, it soon became clear that it could not                                                  to be economical, in the sense that it can operate success-
spontaneously form meaningful classes. In fact, such                                                     fully on non-trivial problems, with a smaller number
a perceptron, turned loose in an environment with no                                                     of units than are present in the human nervous system.
intervention on the part of the experimenter, tends                                                      All previous system designs, which are in any way com-
toward a terminal condition in which it gives either the                                                 parable, are of a completely prohibitive size and cost.
response R = 1 universally, to everything it sees, or                                                         (2) The perceptron is not built to rigid logical speci-
the response R = 0, equally universally, without any                                                     fications, in which the failure of a particular unit is
discrimination between stimulus classes. The responses                                                   likely to cause a breakdown of operation. The design of
of such a perceptron clearly give no information about                                                   the system is based on a small number of statistical
the environment. Such perceptrons are referred to as                                                     parameters and some general logical constraints, but
Class C perceptrons.                                                                                     within these limits the actual connections can be drawn
                                                                                                         from a table of random numbers.
Proof Found                                                                                                  (3) The perceptron does not recognize forms by
     Recently, a proof was found for a second theorem                                                    matching them against a stored inventory of similar
which indicates that with a seemingly trivial modifica-                                                  images, or by performing a mathematical analysis of
tion, a perceptron having strikingly different properties                                                characteristics. The recognition is direct and essentially
results. The modification required is simply that the                                                    instantaneous, since the “memory” is in the form of
values of the A-units should be allowed to decay at a                                                    new pathways through the system, rather than a coded
rate proportional to their present magnitude. The re-                                                    representation of the original stimuli. There is no way
sulting exponential decay is characteristic of practically                                               of reconstructing the original stimuli from the memory
all biological quantities which require the continued                                                    with any absolute certainty. Nonetheless, the probability
application of energy for their persistence; and it is                                                   of obtaining an appropriate recognition response,        or
probable that a similar rule must hold for biological                                                    “naming response,” can be made virtually perfect.
memory traces.                                                                                               (4) As a model for the biological brain, the per-
     The effect of introducing a decay component is that,                                                ceptron does not violate any known information about
instead of growing indefinitely, the values of the A-units                                               the central nervous system. Its size, the logic of its
tend toward a terminal equilibrium condition which                                                       connections, the degree of reliability required of indi-
depends on the input signals and activity of the unit.                                                   vidual units, the permissible random variation in its
Perceptrons organized in this way are members of the                                                     “wiring diagram,” and the kinds of signals employed
class C’. The characteristics of this class are stated in an                                             are all consistent with current anatomical and physio-
“existence theorem;” which is of such fundamental im-                                                    logical data or the latest assumptions of these character-
portance that it seems worth stating here in simplified                                                  istics. The differences from the nervous system are
form:                                                                                                    generally in the direction of simplification, rather than
         A class C' perceptron can be expected to divide                                                 complication, since it is often possible to achieve effects
    the stimuli of any arbitrary environment into classes,                                               in an electronic model which would require many cells
    without any assistance or training by a human                                                        and connections in a biological system. At only one
    operator. The system will form its own concepts                                                      point — the assumed “value” of the A-units — is there
    and these concepts will tend to be meaningful; that                                                  an assumption which does not have a clearly identifiable
    is, they represent an organization of the environment                                                counterpart in the biological brain, and this appears to
   on the basis of similarity and dissimilarity.                                                         be due to difficulties of measurement, rather than in-
   In brief, a Class C* perceptron is the first non-                                                     compatibility of the concept.
                                                                                                              e

            (5) The perceptron is the first system which has                       tems of every variety might make use of the perceptron.
       proved capable of spontaneous organization and sym-                         Finally, coming at a time when the scientific exploration
       bolization of its environment, along lines which bear                       of outer space is just getting started, the possibility of a
       some definite relationship to the human concept of                          robot passenger, capable of describing and classifying
       similarity. While statistical schemes for the correlation                   new environments, may make possible the completion
       and differentiation of patterns have been proposed pre-                     of many useful explorations under difficult environ-
       viously, and might be implemented by a digital com-                         mental conditions.
       puter, the perceptron       appears to be the only system
      which inherently operates in this fashion, as a property                     Extend Theory
      of its organization, rather than through the execution                            Such speculation, however, cannot really be evaluated
      of a logical program.                                                        at this time. We must first extend the basic theory of
                                                                                   the perceptron, which is still in its infancy. We must
      Applications                                                                 lower the cost of an A-unit to a few hundredths the
          The ultimate applications of a system such as the                        cost of units which can now be built with conventional
      perceptron, if such a system can indeed be built economi-                    components. We must study the behavior of laboratory
      cally, open possibilities which still seem difficult to                      models in environments ranging from the simple mix-
      imagine. In principle, the perceptron can not only read                      tures of geometrical forms, which are simulated in our
      print and script, but can respond to verbal commands                         current programs, to such complex problems as the dis-
      as well.                                                                     crimination of speech and human faces. We must develop
           One stage beyond the level which now seems attain-                      sensing devices suitable for providing visual and auditory
      able by the perceptron, is the possibility of an automatic                   inputs to the system.
      translator which can receive spoken inputs in one                                This program is a major undertaking, and we can-
      language and produce written or verbal outputs in                            not expect practical applications in the immediate future.
      another language. And it is possible that ultimately the                     Nonetheless, whether the next stage takes two years or
      coupling of a perceptron with a conventional digital                         ten years, it now seems clear that with the perceptron, a
      computer may carry us over the remaining obstacles                           new field of research, both for engineering and for the
      of grammar and syntax.                                                       theory of intelligent systems, has come of age.                                    S
          The application of such a system to library research
      and data gathering, for scientific purposes, is a definite                                                                REFERENCES
      possibility. In this application, the perceptron might                              ‘           .                      A. The Sensory Order. Univ. of Chicago
                                                                                              ress,       Chicago,
      be expected to digest and prepare abstracts of relevant                                         2. HEBB, D. O. The Organization of Bebavior. John Wiley
      material, as well as to locate references.                                          & Sons, New                York,   1949.
          In the more distant future, automatic navigation and                                   3. ROSENBLATT, F. The Perceptron: A Theory of Sta-
                                                                                          tistical Separability in Cognitive Systems. CAL Report No.
      landing systems, automatic pilots, and recognition sys-                             VG-1196-G-1,               January,    1958.

                     FRANK ROSENBLATT, author of “The Design of an
                     Intelligent Automaton,” became interested in the prob-
    ABOUT            lems of measurement and data analysis which appeared to
|
                     be fundamental to scientific progress in psychopathology
     THE             six or seven years ago. He was at that time a Fellow of the
                     U.S. Public Health Service and was engaged in research
    AUTHOR           on schizophrenia. Subsequently, his doctoral thesis dealt
                     with the application of an analysis technique to problems
      ;              of personality measurement. At the same time, however,
                     Dr. Rosenblatt nurtured a growing conviction that the
                     main content of psychology will become amenable to
                     sound theoretical treatment only after a more secure basis
                     is established, through an improved understanding of the                                                                    a
                     biophysical processes in memory and cognition. With this
                     thought in mind, Dr. Rosenblatt had already increased his
                     emphasis on physiological problems and mathematical
                     brain models.
                        His training in electronics and computer design stems
                     largely from the construction of a special digital computer,
                     the EPAC, which he built as an aid to the data analysis
                     required for his thesis. Employed for the last three years
                     as a Research Psychologist at Cornell Aeronautical Lab-
                     oratory, Dr. Rosenblatt has made contributions to the
                     design of information processing and weapon control sys-
                     tems, in addition to his work as Project Engineer respon-
                  sible for the perceptron program.
                 oe      Dr.   Rosenblatt   was   born   in New   Rochelle,   N. Y., in
                  _   1928. He attended the Bronx (N. Y.) High School of
                      Science and graduated from Cornell University, where
                      he majored in social psychology, in 1950. He received his
                      PhD in Psychology, also from Cornell, in 1956.

