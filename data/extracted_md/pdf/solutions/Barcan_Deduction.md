# The Deduction Theorem in a Functional Calculus of First Order Based on Strict Implication

**source:** pdf · **section:** solutions
**file:** Barcan_Deduction
---

Author(s): Ruth C. Barcan
Source: The Journal of Symbolic Logic, Vol. 11, No. 4 (Dec., 1946), pp. 115-118
Published by: Association for Symbolic Logic
Stable URL: http://www.jstor.org/stable/2268309
Accessed: 29-04-2016 01:55 UTC

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at
http://about.jstor.org/terms

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted
digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about
JSTOR, please contact support@jstor.org.

                     Association for Symbolic Logic, Cambridge University Press are collaborating with JSTOR to
                     digitize, preserve and extend access to The Journal of Symbolic Logic

                                       This content downloaded from 128.103.149.52 on Fri, 29 Apr 2016 01:55:57 UTC
                                                        All use subject to http://about.jstor.org/terms
T1h JOURNAL OF STUBoLIc LOGIC
Volume 11, Number 4, Dec. 1946

    THE DEDUCTION THEOREM IN A FUNCTIONAL CALCULUS OF
               FIRST ORDER BASED ON STRICT IMPLICATION

                                       RUTH C. BARCAN

   In a previous paper, a functional calculus based on strict implication was
developed. That system will be referred to as S2'. The system resulting from
the addition of Becker's2 axiom "'O OA--3 OA" will be referred to as S41. In
the present paper3 we will show that a restricted deduction theorem is provable
in S41 or more precisely in a system equivalent to S4'. We will also show that
such a deduction theorem is not provable in S2'.

   The following theorems not derived in Symbolic logic will be required for
the fundamental theorems XXVIII* and XXIX* of this paper. We will state
most of them without proofs.

96. F(A D (B D E)) -3 ((A D B) D (A D E))

97. F ((A D B) D (A D E)) -3 (A D (B DE))
98. F (A D (B D E)) ((A D B) D (AD E))

99. F (A D (B -E)) m ((A D B) (AD E))
          ((A D (B D E))(A D (E D B))) _ (((A D B) D (A D E))((A D
                                   E) D (A D B))) 98, adj, 80, mod pon
                    (A D (B E)) ((A D B) (A D E)) 16.8, subst, def

100. FA DA

101. F((A D B)(A D (B -3 E))) -3 (A D E)

XXV. If FA -3 B then F (AE) -3 B.

XXVI. IfF E -3 (A _ B) then F ((H D E)(H D A)) -3 (H D B)
                                           and F ((HI D E)(H D B)) -3 (H -3 A).
                    (,H v E) -3 (-%JH v (A B))
                                                         hyp, 19.64, mod pon, 13.11, subst
                    (H D E) -3 ((H D A) - (H D B))
                                                               14.2, 99, subst, def, 2, VIII
                    ((H D E)(H D A)) 3 (H D B)) 14.26, subst
            Similarly,
                    ((H D E)(H D B)) -3 (H D A)

  Received September 17, 1946.
  1 A functional calculus of first order based orn strict implication, this JOURNAL, vol. 11
(1946), pp. 1-16.
  2 See Lewis and Langford, Symbolic logic, pp. 497-502.
  3 Part of this paper was included in a dissertation written in partial fulfillment of the
requirements for the Ph.D. degree in Philosophy at Yale University. I am grateful to
Professor Frederic B. Fitch for his criticisms and suggestions.
                                               115

           This content downloaded from 128.103.149.52 on Fri, 29 Apr 2016 01:55:57 UTC
                            All use subject to http://about.jstor.org/terms
 116       RUTH            C.     BARCAN

102. F (H - (A B)) -3 ((H -3 A) D (H -3 B)) and
         (HQ (A-B)) -3 ((H -3B) D (H -A)).
XXVII. If F E -3 (A-B) then ((H -3 E)(H -3 A)) -3 (H -3 B) and
                                   F ((H -3 E) (H -3 B)) -3 (H -3 A).
               (-H v E) -3 (,IH v (A B)) hyp, 19.64, mod pon, 13.11, subst
               (H -3 E) -3 (H -3 (A --B)) 14.2, VII, 18.7, subst
               ((H -3 E)(H -3 A)) -3 (H -3 B) 102, VIII, 14126, subst
           Similarly,
               ((H -3 E)(I1 -3 B)) -3 (H -3 A).
  The axiom which distinguishes S41 is 103*. Theorems derivable in S4' but
not in S21 will be marked by an asterisk.
  104* and 105* are required in the proof of XIX*.

103*. OOA -3 OA
104*. F IOA =CIA
105*. F CA -3 (B -3 CIA)
   S21eq and S41eq. A consideration of the deduction theorem requires a
definition on "proof on hypotheses." Such a definitionisfacilitated if we formu-
late it in terms of a system equivalent to S21 which will be referred to as S21eq.
   Every axiom of S21 is an axiom of S21eq. The rule for generalization in S2'
is replaced by the following rule for axioms: If A is an axiom then (,B)B is an
axiom where B is the result of replacing all free occurrences of a in A by ,B. The
rule for adjunction is like that of S21 extended to include the following: If (a,) (a2)
... (am)A and (al) (a2)B * * (am) are provable then (a,) (a2) ... (am) (AB) is prov-
able. The substitution rule of S21 is extended so as to read exactly like XVI.
Modus ponens is retained.
  The rule for axioms gives the effect of generalization since we can prove the
following: If A1, A2, - - *, A. are the steps of a proof of B where B is An then we
can construct a corresponding proof such that (a)B is provable. Suppose Ai
is an axiom, then replace Ai by (a)Ai . If Ai is not an axiom then it follows from
some previous Ai, and Ai2 by modus ponens, adjunction or substitution. Sup-
pose Ai follows by modus ponens. Let Ai2 be Ai, -3 Ai. One of the theorems
derivable in S21eq is (a) (A -3 B) -3 ((a)A -3 (a)B) the proof of which is the same
as 19 of S2' since the rule of generalization is not employed. Replace Ai by
the sequence (a)(Ai -3 Ai) -3 ((ca)A, -3 (a)Aj), (a)Aj, -3 (a)Ai , (a)Ai . If Ai
follows from some preceding Ai, and Ai2 by substitution or adjunction then
replace Ai by (a)Ai.
  It is obvious that S21 is equivalent to S21eq. The axioms of S21 and the gen-
eralization rule give us the axioms of S21eq. Modus ponens is retained. The
extended adjunction rule follows directly from 29 and modus ponens. XVI is
the same as the extended rule of substitution.
  S41eq is the system which results from the addition of axiom 103* to S21eq
and it is of course equivalent to S41.
  Proof on hypotheses. Let B be said to be provable on the hypotheses A1,
A2, I. *, A, in S21eq and S41eq if there is a finite list of formulas B1, B2, * , B8
where B8 is B, satisfying the following conditions:

         This content downloaded from 128.103.149.52 on Fri, 29 Apr 2016 01:55:57 UTC
                          All use subject to http://about.jstor.org/terms
          DEDUCTION THEOREM IN CALCULUS WITH STRICT IMPLICATION 117

  For each i (1 < i ? s)
          1. Bi is one of Al, A2, ,An or
          2. Bi is an axiom or
          3. Bi results by one of the rules of inference from Bi1 and Bi,
                                                      where ii < i and i2 < i.
  B is provable on the hypotheses Al, A2, , A, will be abbreviated: Al, A2,
 ... F B.
  In S21eq we cannot prove either
          1. Al ,A2, I ,An-1 F A, D B
or 2. Al, A2, ,A 1 A, , B
from 3. Al, A2, ,An - B.
 This can be shown if we use an eight element matrix of Parry4 which satisfies
the axioms and rules of S2. This matrix also satisfies S21eq if we regard the
domain of individuals as consisting of a single individual a.5 Every expression
of the form (a)A would then be replaced by B where B results from substituting
all free occurrences of a in A by a. Neither (A -3 B) D (OA -3 OB) nor (A -3
B) -3 (OA --3 OB) are satisfied by this matrix although ((OA -3( OB) is provable
on the hypothesis (A -3 B) in S21eq. (Rule VI.)
  In S41eq, 1 always follows from 3 and 2 follows from 3 if each Ar (1 ? r ? n)
can be transformed into an equivalent expression El r.

XXVIII*. If Al, A2, , A, [ B then Al, A2, , An,,1 F An D B.
  Proof: Let us assume that A, D Bm has been proved for every Bm in the list
B1, B2, , B. of the definition of proof on hypotheses where m < i. We will
show that H An D B4 .
  Case (1). Bi is an axiom.
               Bi -3 (An, D B4) 15.2
               A, D Bi mod pon
  Case (2). Bi is An -
               A,, D Bi 100
  Case (3). Bi is one of Al, A2, A,, ,.
               Proof like Case (1).
  Case (4). Bi follows by modus ponens from a previous Bi, and Bi2 where let
us say Bi2 is Bi1 -3 Bi 4
                ((An D Bil)(An D (Bil -3 Bi))) -3 (An D B4) 101
                (An D Bil)(An D (Bil -3 Bi)) hyp, adj
               (An D B ) mod pon
  Case (5). Bi follows from adjunction of a previous Bi1 and Bi2 .
               ((An :D Bil) (Av D Bi2)) -3 (An D (BjjBi)
                                                                  16.8, def, 12.17, mod pon
  Where the extended rule is used we have
                ((An D (a1)(a2) . . . (am)Bij)(AN D (a1)(a2) . . . (am) )Bi2)) 3
                (A. D (a1)(a2) ... (am)(BiBi2)) Like step 1 using 29 and
                                                                                         subst.

  4V. T. Parry, The postulates for "strict implication," Mind, vol. 43 (1934), pp. 78-80.
  6 This method for interpreting the quantifiers was suggested by the referee.

          This content downloaded from 128.103.149.52 on Fri, 29 Apr 2016 01:55:57 UTC
                           All use subject to http://about.jstor.org/terms
  118       RUTH            C.     BARCAN

                Anl D B. hyp, adj, mod pon
   Case (6). B. follows by substitution from a previous Bi, and By2 where let
us say Bi2 is (al)(aO2) * (ca.)(r _ E) and Cil, Ct2 a ,. is a complete list of
the free variables in r and E.6
                (al) (a2) ... (a,)(r E) 3 (Bil B1) XIX*, 14.1, IX, VIII
                ((An D (al)(Ca2) ... (cam)(rF E))(An DBj1)) -3 (Anf DBI) XXVI
                An D B. hyp, adj. mod pon

 XXIX*. If AA , * , An B and if F Alir, FA2 F2,. * *,
                      An _2 o rn 2 then Al, A2 X***XAn-l An -3 B.
   Proof: Let us assume that An -3 Bm has been proved for every Bm in the list
B1, B2, ... * B, of the definition of proof on hypotheses where m < i. We will
show that F An -3 B. .
  Case (1). B. is an axiom. Since every axiom of S4'eq is of the form E -3 H
or (al) (a2) ... (a,,)(E -3 H) it follows from 18.7, 39 and substitution that if
M is an axiom then F M =CI r.
            Bi -3 (An -3 B1) 105*
            An -3 Bi mod pon
   Case (2). B, is An
                Aft -3 Bi 12.1
   Case (3). Bi is one of Al, A2, ---,An
               An -3 B. 105*, hyp, mod pon
   Case (4). Bi follows from a previous Bi1 and Bi2 by modus ponens where let
us say Bi. is Bil -3 Bi.
               ((An. D Bil)(An D (Bil 3 Bi))) (Anf D B1) 101
              ((An -3 Bil) (An -3 (Bil 3 Bi))) 3 (An -3 B)
                                                                     VII, 19.81, 18.7, subst
                (An -3 Bi)(An -3 (Bi1 -3 Bc)) hyp, adj
                An -3 B. mod pon
   Case (5). Bi follows from adjunction of a previous B1 and Bi2.
                ((An -3 Bil) (An -3 Bi2)) -3 (An -3 (B;1Bi2)) 19.61
            An -3 Bi hyp, adj, mod pon
  Where the extended rule is used employ 29 and substitution as in XXVIII*.
  Case (6). Bi follows from a previous B1 and Bi2 by substitution where let
us say B i is (a1) (a02) ... (aem) (r F E) and al, Ca2 X * a,, is a complete list of
the free variables in r and E.6
                (ail)(aO2) ... (a,,)(r E) -3 (Bil Bj) XIX*
                ((An -3 (a1) (a2) ... (a.) (F r E)) (An -3 B1)) -3 (An -3 Bi) XXVII
                An -3 Bi hyp, adj. mod pon7

  YALE UNIVERSITY

    6 If r F E is provable then (al)(al) .** (arm) (r E E) is provable where al , Ct2 X a
is a complete list of the free variables in r and E. We will assume that wherever B. follows
by substitution, the variables in r and E have been generalized upon.
    7 A slightly stronger theorem than XXIX* could be proved as an immediate corollary
of XXVIII* if we introduced the following lemma: If F A D B then F OA D OB. We
would then need only to assume that F An or, where i < n. This alternative proof was
suggested by the referee.

          This content downloaded from 128.103.149.52 on Fri, 29 Apr 2016 01:55:57 UTC
                           All use subject to http://about.jstor.org/terms

