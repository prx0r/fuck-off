# Mit 10 Bildern

**source:** pdf · **section:** solutions
**file:** Rechnender_Raum
---

Rechnender Raum                                                                                            K. Zuse, Bad Hersfeld

Mit 10 Bildern

Z u s a m m e n fa s s u n g : Der Verfasser unternimmt denVersuch, informations- und automatentheoretisches Denken auf physi­
kalische Probleme anzuwenden. Neben einigen allgem einen Betrachtungen wird im wesentlichen der Gedanke einer D ig it a li­
sierung räum licher Beziehungen verfolgt, womit d ie Idee der Quantisierung der physikalischen Größen weiter verallgem einert
wird.

S u m m a ry : In the following contribution the author nies to apply an Information and automata theory approach to certain
Problems of physics. Besides some general considerations, the main thought discussed is the idea of d ig ita liz in g spatial relat-
ions whereby the.conception of quanticization of the physical quantities is generalized.

Es ist uns heute selbstverständlich, daß numerische Rechen-          sein. Das Z ie l ist erreicht, wenn überhaupt eine Diskussion
verfahren erfolgreich eingesetzt werden können, um physi­            zustande kommt und sich daraus Anregungen ergeben, d ie
kalische Zusammenhänge zu durchleuchten. Insbesondere                eines Tages zu Lösungen führen, d ie auch den Physikern
der Einsatz moderner Datenverarbeitungsanlagen hat die               akzeptabel erscheinen.
Anwendung numerischer Methoden enorm befruchtet. Bis­
                                                                     Im folgenden s o ll eine kurze Zusammenfassung dieser Ge­
her ist dabei stets davon ausgegangen worden, daß die Z ie l­
                                                                     danken gegeben werden, d ie in einer ausführlicheren Arbei
setzung einer numerischen Lösung darin bestehen muß, das
                                                                     näher behandelt werden sollen.
vom Physiker z.B. durch eine D ifferentialgleichung reprä­
sentierte M odell durch ein numerisches M odell (nämlich             Vergleicht man d ie durch die mathematischen Ansätze reprä­
der numerischen Lösung der Differentialgleichung) mög­
                                                                     sentierten M odelle der Physik und d ie zugehörigen nume­
lichst exakt anzunähern. Ein rückwirkender Einfluß der               rischen M odelle miteinander, so ergibt sich ein charakteri­
numerischen Lösungen auf d ie physikalische Theorie selbst
                                                                     stischer Unterschied: D ie physikalischen M odelle sind z.B.
besteht le d ig lic h indirekt in der bevorzugten Anwendung          durch D ifferentialgleichungen in Dimensionen definiert,
solcher physikalischer Methoden, d ie der numerischen
                                                                     welche durch kontinuierliche Größen dargestellt-werden,
Lösung besonders leicht-zugänglich sind.
                                                                     welche k e in e rle i Beschränkungen unterliegen. Hingegen
Im folgenden seien jedoch e inige Ideen entwickelt, d ie es          arbeiten d ie numerischen Lösungen insbesondere b e i ihrer ’
berechtigt erscheinen lassen, d ie Frage nach einer direkten         Durchführung m it programmgesteuerten Rechenmaschinen
Einflußnahme neuer Ideen der Datenverarbeitung auf physi­            m it Größen, d ie nur eine diskrete Z ahl von Werten zulassen.
kalische Probleme zu stellen. D ie Schwierigkeit besteht             Es g ib t Grenzwerte in Form von M in im a l- und Maxim alwer­
selbstverständlich darin, daß verschiedene Wissensgebiete            ten, und es lie g t eine Stufung der Werte vor, d ie es nicht e r­
miteinander in Beziehung gebracht werden müssen. Bereits             laubt, zwischen zwei gegebene Werte b e lie b ig v ie le Zwischen­
d ie heutige Physik selbst spaltet sich immer mehr in e in ­         werte einzuschalten. Hinzu kommen weitere Beschränkungen
zelne Spezialgebiete auf [ 1] . A lle in die mathematischen          dadurch, daß eine D ifferentialgleichung nur durch D ifferen­
Methoden der modernen Physik sind nicht einm al jedem                zengleichungen angenähert werden kann, was sich z.B. in
                                                                     der endlichen Schrittweite bei Integrationen auswirkt. W ir
Mathematiker geläufig und erfordern für ih r Verständnis ein
                                                                     können zwar durch Erhöhung der Stellenkapazität einer Rechen­
jahrelanges Spezialstudium.
                                                                     maschine und durch Verkleinerung der Schrittweite derartige
Aber auch die m it der Datenverarbeitung in Zusammenhang             numerische Lösungen im Prinzip b e lie b ig exakt an die gegebene
stehenden Theorien und Wissensgebiete spalten sich heute             D ifferentialgleichung annähern, jedoch ist dies praktischen
bereits in verschiedene Spezialzweige auf. Erwähnt seien             Grenzen unterworfen. D ie Automatentheorie lehrt dann auch,
d ie formale Logik, die Informationstheorie, die Automaten-          daß d ie praktisch benutzten programmgesteuerten Rechen­
theorie und die Theorie der Formelsprachen. Der Gedanke,             maschinen im allgem einen unter d ie finite n Automaten fallen
diese Gebiete, soweit sie betroffen sind, unter dem Namen            und somit nur eine endliche Z a hl von Zuständen erlauben und
"Kybernetik* zusammenzufassen, hat sich noch nicht durch­            also auch nur eine endliche Z ahl von diskreten Lösungen für
setzen können. Sehr fruchtbar ist jedoch unabhängig von den          ein gegebenes Problem.
verschiedenen D efinitionen des Begriffes im einzelnen die
                                                                     Diese diskreten Lösungen haben jedoch einen v ö llig anderen
Auffassung der Kybernetik als Brücke zwischen den Wissen­
schaften [ 2] .                                                      Charakter als diejenigen, die sich aus der Quantentheorie
                                                                     ergeben. Am bekanntesten ist d ie Beziehung zwischen Fre­
Der Verfasser hat in diesem Sinne als Fachmann der Daten­            quenz und Energie etwa eines Lichtquants, das der Formel
verarbeitung einige grundsätzliche Gedanken entwickelt,              E = h ■cd unterliegt, wobei h eine universelle Naturkonstante
die er für wert hält, zur Diskussion gestellt zu werden.             ist. Man spricht h ie r zwar gern von der Quantisierung der
Einige dieser Gedanken mögen in der vorliegenden noch                Energie, jedoch können diese Quanten jeden beliebigen Wert
unreifen Form nicht ohne weiteres m it bewährten Vor­                                                     E
stellungen der theoretischen Physik in Einklang zu bringen           annehmen, le d ig lic h der Quotient % ist durch einen diskreten

336
f

                                                                     'X ;

     Wert gekennzeichnet. Hs ist dies etwas anderes, als wenn in              analoge Charakter der gegenseitigen Beziehungen jedoch noch
     einer d ig ita le n Rechenmaschine die Energie aufgrund der be -         erhalten bleibt. D ie Quantenmechanik unterwirft weitere
     grenzten Stellenzahl nur eine diskrete Zahl von Werten an­               Größen einer Quantelung, was darauf hinausläuft, daß gewisse
     nehmen kann.                                                             Größen nur diskrete Werte annehmen können. Man könnte
                                                                              also m it einer gewissen Berechtigung von einem hybriden
     D ie Annahmen der Quantentheorie haben weitgehende Konse­
                                                                              System sprechen.
     quenzen in bezug auf die Quantisierung verschiedener physi­
     kalischer Größen. Auch der Gedanke, daß die Feinstruktur                 Über v o ll d ig ita le physikalische M odelle verfügen wir heute
     des Raumes gewissen Beschränkungen unterliegt, ist eine                  noch nicht. Bei v ö llig e r Unvoreingenommenheit erscheint d ie
     Konsequenz der Quantentheorie. In diesem Sinne läßt sich                 Frage berechtigt, ob b e lie b ig unterteilbare, also echt ko nti­
     auch die Heisenberg'sche Unbestimmtheitsrelation auffassen,              nu ie rlic h e Größen in der Natur überhaupt denkbar sind. Was
     welche die g leichzeitige Bestimmung von Impuls und Ort                  wären z. B. die Konsequenzen, wenn wir zur restlosen Quante­
     gewissen Grenzen unterwirft. Neben le ic h t meßbaren elem en­           lung der gesamten Naturgesetze übergehen würden und anneh­
     taren Größen, wie dem kleinsten elektrischen Quantum                     men würden, daß grundsätzlich jede Größe irgendeiner Quante­
     (durch das Elektron repräsentiert) wird der Begriff der k le in ­        lung unterliegt?
     sten Länge (ca 10*^“ cm) und der kleinsten Z eiteinheit
                                                                              Dieser Gedanke sei im folgenden etwas weiter verfolgt. Zu­
     bereits diskutiert. D ie Vorstellung des klassischen Kontinuums
                                                                              nächst seien e in ig e abstrakte Beispiele d ig ita le r M odelle be­
     wird zwar verlassen, jedoch nicht, indem anstelle des Kon­
                                                                              sprochen, die am Schreibtisch konstruiert sind. Sie haben nur
     tinuums etwa ein Gitter diskreter Werte tritt, sondern indem
                                                                              sehr entfernte Ä h n lic h ke it m it physikalischen Vorgängen, sind
     man zu grundsätzlich anderen Ansätzen übergeht, wie etwa
                                                                              jedoch geeignet, das Denken in d ig ita le n M odellen anzuregen.
     zum höherdimensionalen Konfigurationsraum, in dem Wahr-
    ^Ä ie in lic h ke its g rö ß e n definiert sind. (Z.B. Aufenthaltswahr­   Da es sich in diesem A rtik e l nur um eine kurze Zusammen­

     scheinlichkeit eines Partikels.) Auch b e i dieser Vorstellung           fassung handelt, können zum T e il nur einige charakteristische
     wird nicht von der Vorstellung des Kontinuums als solchem                Ergebnisse angeführt werden. In dem angekündigten Sonder­
                                                                              heft s o ll dann ausführlich auf diese und andere Beispiele einge­
     abgegangen, denn die Differentialgleichungen der Quanten­
     mechanik sind in bezug auf die Feldgrößen selbst ke in e rle i           gangen werden.

     Beschränkungen unterworfen.                                              Betrachten wir das klassische M odell der Thermodynamik, bei
     In diesem Zusammenhang erscheint es nützlich, die bei                    dem das Verhalten von Gasen durch Im Raum fre i bewegliche
                                                                              aufeinandentoßende G um m ibälle dargestellt w ird . Wegen der
     Rechengeräten übliche Unterscheidung zwischen analogen,
     d ig ita le n und hybriden Systemen zu betrachten. In einem              großen T eilchenzahl wird dieses Problem rechnerisch im a ll­

     analogen Gerät werden die Werte durch physikalische Größen               gemeinen statistisch behandelt. S te llt man sich jedoch die
     wie Spannungen, Position von mechanischen Gliedern, Ge­                  Aufgabe, das M odell direkt durch Nachrechnung der Flug­
     schwindigkeiten usw. dargestellt haben also im Prinzip einen             bahnen der einzelnen T eilchen zu sim ulieren, so kommt man
     kontinuierlichen Charakter. In bezug auf die dig ita le n Geräte         auf folgende Ergebnisse:
     wurde bereits festgestellt, daß diese nur diskrete, gestufte             Bel beiden M odellen (dem physikalischen und dem rechne­
     Werte zulassen. D ie Beschränkung auf die Größenordnung                  rischen) gehen im allgem einen geordnete Zustände in unge­
     (M inim al - und Maximalwerte) g ilt zum T e il auch für analoge         ordnete über (Zunahme der Entropie). Allerdings lassen sich
     Geräte, zumindest für die Maximalwerte. Hybride Systeme                  Ausnahmefälle konstruieren, b e i denen bestimmte Ordnungen
     stellen Kombinationen beider Systeme dar. Einm al können                 eihalten bleiben. Nehmen wir z. B. e in Gefäß m it genau
       teitale und analoge Geräte miteinander kombiniert werden,              parallelen Wänden an und eine Serie von T eilchen, deren
    f  obei an den Schnittstellen Wandler für die verschiedenen
     Darstellungsarten erforderlich sind. Zum anderen können aber
                                                                              Bahnen genau senkrecht auf einer dieser Ebenen stehen, wobei
                                                                              die Bahnen genügend weit auseinander liegen, um gegenseitige
     auch d ie Werte selbst in hybrider Form dargestellt werden,              Beeinflussung zu verhindern, so bleiben diese Bahnen im Sinne
     indem etwa die D ichte diskreter Impulse ein Maß für den zu              der klassischen Mechanik erhalten. Auch im Rechenmaschinen-
     repräsentierenden Wert ergibt.                                           m odell ist dies der F a ll, wenn das der Rechnung zugrunde
     Diese für technische Geräte sinnvolle Unterscheidung läßt sich           gelegte Koordinatensystem ebenfalb p a ra lle l bzw. orthogonal
     auch auf physikalische M odelle übertragen. Ist die Natur                zu den Wänden gelegt wird. Sicher lassen sich auch noch in te r­
     analog, d ig ita l oder hybrid? Beziehungsweise; Eignet sich             essante weitere S p e zia lfälle konstruieren, bei denen Stoß V o r ­
    . zur Formulierung der physikalischen Gesetze besser ein ana­             gänge zwischen den T eilchen stattfinden und trotzdem eine be­
      loges, ein digitales oder ein hybrides Modell?                          stimmte Ordnung erhalten bleib t (Bild 1).

     Das M odell der klassischen Mechanik ist zweifellos analog.
                                                                              Wir wissen nun, daß d ie moderne Physik dieses klassische B ild
     D ie auftretenden Größen (Koordinaten. Massen, Kräfte) sind              aufgelöst hat. D ie Stoßvorgänge der einzelnen T eilchen wer­
     ke ine rle i Beschränkungen unterworfen. Auch d ie R e lativitäts­
                                                                              den im Sinne der modernen Physik nicht streng determ iniert
     theorie arbeitet le d ig lic h m it einer oberen Grenze der G e­
                                                                              angenommen. Es gelten le d ig lic h Wahrscheinlichkeitsgesetze,
     schwindigkeit (Lichtgeschwindigkeit), im übrigen aber m it
                                                                              die im statbtischen Durchschnitt den Gesetzen der klassischen
     kontinuierlichen Werten.
                                                                              Mechanik entsprechen. Durch diesen Effekt tritt eine Streu­
     Durch d ie Einführung der Körnigkeit der Materie durch ihre              ung ein, welche bewirkt, daß auch in theoretisch ange­
     Auflösung in Moleküle, Atome und Elementarteilchen er­                   nommenen S pezialfällen m it der Z e it eine Auflösung der
     halten einige Größen einen diskreten Charakter, wobei der                Ordnung e in tritt und d ie Entropie des Systems steigt.

                                                                                                                                                337
W ie siebt in dieser Beziehung nun das rechnerische M o de ll aus?               Für d ie Untersuchung des Verhaltens m ehrerer Q uellen b ie te t
Solange w ir diesen Streueffekt n ic h t besonders in unser M o de ll            sich e in kartesisches Koordinatensystem an. Dadurch sind
                                                                                 neben der Stufung der Koordinaten zw ei ausgesprochene V or­
                                                                                 zugsrichtungen gegeben, d ie das Ausbreitungsbild beeinflussen.

                                                                                                                                                           X

B ild 1
B e isp ie l einer stabilen Ordnung von 8 in einem Quadrat m it
zurückwerfendah Kanten fre i bew eglichen B ällen . E in analoges
M o de ll würde unendliche G enauigkeit erfordern. In einem d l*
g ita le n M o de ll lÄfeibt d ie S ta b ilitä t erhalten. D ie S ta b ilitä t
g ilt jedoch nur für diskrete Seitenlängen des Quadrats.                         B ild 2                                    '
                                                                                 Ausbreitung eines Im pulses !f = 256 nach dem Gesetz

                                                                                 K ( / x - l, y ♦/ x + l.y + 5 fx ,y - l + /x,y+ l)»     9 xy
"einprogram m ieren", is t b e i den oben erwähnten sorgfältig
konstruierten S p e z ia lfä lle n ke in Streueffekt festzustellen.
Sobald aber durch eine geringfügige Streuung das System in
                                                                                 Wegen Sym m etrie braucht nur e in Sektor von 45°gezeichnet
bezug auf d ie sp e z ie lle Ordnung außer Takt kommt, haben                     zu werden. Es sind d ie Werte der F ro n tlin ie in den Zeitphasen
w ir es m it ähnlichem V erhalten zu tun w ie b e i den M odellen                I - V angegeben.
der modernen M echanik. Es ist im allgem einen n ic h t erfor­
d e rlic h , einen Streueffekt besonders zu berücksichtigen: d ie
m it der Rechnung verbundenen rechnerischen U ngenauigkeiten                     B ild 2 ze ig t e in einfaches B e isp ie l, b e i dem in jedem Z e it­
haben - von Sonderfällen abgesehen - dieselbe W irkung. Das                      takt der W ert eines jeden Gitterpunktes sich auf d ie 4 benach­
klassische M o de ll verlangt absolute Rechengenauigkeit, daher                  barten v e rte ilt. W ir haben eine n ic h t kreisförm ige A usbrei­
im rechnerischen M o de ll e in Rechnen m it unendlicher S te lle n ­            tung des Im pulses m it vorweglaufenden Spitzen u i den Koor­
zahl. Da dies praktisch n icht durchführbar is t, treten b e i den               dinatenachsen, Jedoch is t d ie V erteilung in der F ro n tlin ie
einzelnen Stoßvorgängen rechnerische Ungenauigkeiten auf,                        n ic h t g leichm ä ßig D ie vorweglaufenden Spitzen « reichen
d ie bew irken, daß - ä h n lic h dem M odell der modernen                       bald den unteren Grenzwert und sterben ab Je größer das V er­
M echanik - Abweichungen der Bahnen von den Theorien der                         h ä ltn is des Wertes im Q uellpunkt zu diesem Grenzwert is t,
klassischen M echanik auftreten. Man könnte auch diese A b­                      desto später tritt dieser Effekt e in . D ie Ausbreitung konver­
weichungen durch e in statistisches Gesetz summarisch e r­                       g ie rt dann gegen eine rotationssym m etrische Ausbreitung.
fassen. jedoch besteht e in w esentlicher Unterschied: Im                        D ies entspricht der an sich bekannten Tatsache, daß d ie physi­
M o dell der modernen M echanik handelt es sich um echte                         kalischen M odelle nur dann durch num erische Methoden gut
U nbestim m theit, b e i dem rechnerischen M o de ll geht a lles                 angenähert werden können, wenn m it feiner G ineistruktur
streng determ iniert zu, nur n ic h t im Sinne der klassischen                   und hoher S te lle n z a hl bzw, G enauigkeit gearbeitet w ird.
M echanik, sondern im Sinne bestim m ter rechnerischer A n­
sätze, d ie d ie klassische M echanik nur annähern. Beides be­
w irkt d ie Zunahme der Entropie,                                                Demgegenüber kann man d ie umgekehrte Frage stellen: W ie
                                                                                 stark lassen sich d ie num erischen Ansätze vergröbern, so daß
Als zweites B e isp ie l sei das Problem einer Q u e lle in einem
                                                                                 trotzdem noch etwas Sinnvolles herauskommt? Eine solche
zw eidim ensionalen Raum betrachtet. Das klassische M o dell
                                                                                 Untersuchung lä ß t sich im eindim ensionalen Raum zunächst
enthält k e in e rle i Beschränkungen in bezug auf d ie auftreten­
                                                                                 le ic h te r behandeln.
den Feld werte und lie fe rt som it eine rotationssymmetrische
Ausbreitung m it stetig abnehmender Intensität. E in d ig ita le s               A ls B e is p ie l sei d ie Fortpflanzung eines Druckim pulses in
M o de ll muß notwendigerweise m it d ig ita le n Koordinaten                    einer Rohrleitung behandelt. Das Problem s p ie lt z.B. eine
arbeiten. An sich bieten sich polare Koordinaten an, welche                      große praktische R o lle b e i der Untersuchung des Verhaltens
ebenfalls eine rotationssymmetrische Lösung ergeben. Jedoch                      von Erdölleitungen. D ie verschiedenen physikalischen M odelle,
erscheint d ie W ahl des Koordinatensystems m it der Q u e lle                   d ie h ie r zugrundegelegt werden, laufen auf d ie Lösung von
als M ittelpunkt zu sehr auf den sp e zie lle n F a ll zugeschnitten.            D iffe re ntia lgle ichu ng e n hinaus, Zwecks num erischer Lösung

338
dieser D iffe re ntia lgle ichu ng e n kann man zu Differenzen -           W ir nehmen entsprechend B ild 4 e in orthogonales G itternetz
gleichungen Ubergehen. Schränkt man d ie m öglichen Werte                  an und ordnen jedem Punkt Werte qx. qy zu. D er E in fachheit
der auftretenden V ariablen, z.B. Druck und G eschw indigkeit,             halber nehmen w ir zunächst an, daß d ie q-Werte d ie Werte
noch durch grobe D ig ita lis ie ru n g e in , so kommt man sc h lie ß ­    -, 0, + annehmen können. W ir können dann auch von
lic h zu einfachen Im pulsen, welche im Extrem nur d ie Werte              q-P feilen oder kurz P fe ile n sprechen. W ir legen zunächst
0 und 1 annehmen kam en und sich m it konstanter Geschwin­                 fest, daß e in is o lie rte r P fe il, d .h. e in solcher, der n icht
d ig k e it schrittw eise fortpflanzen. Es entspricht dies der Fort­        zusammen m it einem senkrecht zu ihm verlaufenden P fe il
pflanzung eines Impulses in einer Relaiskette.                             am g le iche n G itterpunkt a u ftritt, sich in seiner Richtung auf
                                                                           den nächsten G itterpunkt überträgt. S ie können sich selbst­
                                                                           verständlich nur orthogonal fortschalten.
                         ©
                                                                           W ir brauchen nun noch e in Gesetz für den F a ll sich kreuzen­
                                                                           der P fe ile . D ies is t in B ild 5 dem onstriert. Im Punkt A sind
                                                                           zur Zeitphase I zw ei sich kreuzende P fe ile vorhanden. Nach
                                                                           unserem bisherigen Gesetz würden diese sich unabhängig in
                                                                           ihre n Richtungen fortschalten. W ir legen nun fest, daß in
                                                                           diesem F a ll d ie P fe ile zwar auch in ihre n Richtungen nach
                                                 B ild 3
                                                                           den Punkten B und C fortgeschaltet werden, ih re Richtungen
                                                                           B.und C aber vertauscht werden. W ir « halten dann e in sta­
                                                                           b ile s T e ilc h e n m it der Periode 24 t, welches sich diagonal
B ild 3 ze ig t h ie rfü r e in einfaches B e isp ie l. W ir haben d ie
                                                                           fortschaltet.
beiden Funktionswerte v und p, w elche je d ie Werte +1, 0,
 -1 (N ullen werden der Einfachheit halber n ic h t geschrieben)
annehmen können. Der lin e a re Raum is t dabei in einzelne
                                                                             B ild 5
Sektoren u n te rte ilt. Es werden d ie Differenzw erte - Av und                                                                           O        o
                                                                           . Schaltgesetz für zw ei sich
- 4 p g e b ilde t. Aus diesen Werten werden in jedem Z eittakt
                                                                             kreuzende P fe ile qx, qy ent­
neue Werte y und p errechnet nach der Formel:
                                                                             sprechend B ild 4.                   O                        O        o
v    -4 p =* v                                                             Punkt A Phase 1: Kreuzende
p   - Av => p                                                              P fe ile                               o                        o        o
                                                                           Punkte B, C Phase II:
D ie Übertragung dieses Verfahrens der groben D ig ita lis ie ru n g
                                                                            Richtungen der P fe ile               q
auf m ehrdim ensionale Räume führt ebenfalls zu in teressanten                                                                             o        o
                                                                            werden vertauscht.
Ergebnissen. Jedoch is t es n icht so einfach, h ie r stabile
Strukturen zu erhalten. Den einzelnen Im pulsen in einer
Rohrleitung entsprechen W ellenfronten im Raum. Bei grober
D ig ita lis ie ru n g ze ig t sich, daß bevorzugte Richtungen für d ie
Fortpflanzung solcher W ellenftonten bestehen.

Interessant ist jedoch d ie Frage nach solchen Strukturen, d ie
sich n ic h t im Raum als W ellenfront, sondern in Form von
räu m lich begrenzten Strukturen fortpflanzen, d ie in eine
gewisse A nalogie zu Elem entarteilchen gesetzt werden können.              B ild 6
W ir w ollen solche G ebilde D ig ita lte ilc h e n nennen.                 D iagonal laufendes
                                                                            Elem entarteilchen
W ir verfugen jedoch Uber kein einfaches physikalisches M odell,
                                                                            entsprechend dem
welches beispielsw eise durch einen Satz von D iffe re n tia l­
                                                                            Gesetz von B ild 5.
gleichungen d ie Fortpflanzung eines solchen stabilen T e il­
chens repräsentiert. Das M o de ll des W ellenpaketes führt zu
in sta b ile n G ebilden, welche zerfließen. Es sei daher zunächst
davon abgesehen, solche D ig ita lte ilc h e n in Anlehnung an
                                                                            W ir haben nun T e ilche n , d ie sich in 8 diskreten Richtungen
physikalische M odelle zu entw ickeln; sondern es sei eine
                                                                            in der Ebene fortschalten können. Es lä ß t sich eine Reihe
reine Konstruktion auf dem Papier vorweggenommen.
                                                                            in teressanter B eispiele für d ie Begegnungen solcher T e ilche n
                                                                            b ild e n . W ir b leib e n dabei zunächst b e i der Festlegung, daß
                                                                            P fe ile nur d ie Werte -, 0, + annehmen können. Am g leiche n
y                                                                           G itterpunkt heben sich zw ei entgegengesetzte P fe ile a u f, und
                                                                            zw ei gleichg e richte te w irken w ie e in ein zeln er P fe il. B ild 7
                                           B ild 4
    o        o       o    o                                                 ze ig t e in B eispiel.
                                           Zw eidim ensionaler
                                           D ig ita lra u m m it            Es ze ig t sich, daß der V e rlau f der verschiedenen Begegnungen
        q*   |
    O - i —- o            o                Werten qx, qy pro Punkt.         zeitphasen- und abstandsphasenabhängig ist. D ie T e ilche n
             ■ q,t                                                         können durch einander durchlaufen oder sich vernichten oder
                                     X
    O        O       o    o                                                neue T e ilche n b ild e n .

                                                                                                                                                   339
Bei der Begegnung kommt es sehr darauf an, ob der Schnitt­
punkt der Teilchenbahnen auf einem definierten diskreten
Punkt des Koordinatensystems lie g t. In diesem F a ll findet
eine Reaktion statt.

                  A

   o                               o                              r
         o

                           o

   o      o     a |>       0       o
                                                                             B ild 9
  1
B -©—                              0                                         T eilchen entsprechend Gesetz von B ild 8. Pfeilverhältnis 5 : 2.
                                                                             D ie Bewegungsrichtung entspricht dem Pfeilverhältnis. Das
   o                                             B ild 7                     T e ilchen hat d ie Periode 7 A t und durchläuft periodisch 7
         o

                               f
                       f

                                                 Zwei sich schneidende       Phasen. D ie Teilchenbahn geht nur einm al pro Periode durch
                               -

                                                 T eilchen A, B ergeben      einen definierten diskreten Punkt des Koordinatensystems.
   o      o      o         -e—
                                                 ein neues T eilchen C,      (Nullphasenpunkt Q). Zwischendurch "z e rflie ß t" das Teilchen.
                                   t   c
                                                                             Man kann L inien g leicher Phase konstruieren (Phasenlinien).
                                                                             To-i-re
W ir können nun die M öglichkeiten dieses Systems erweitern,
indem wir P fe ile verschiedener absoluter Länge zulassen. Für               B ild 10 zeigt ein B eispiel für d ie Reaktion zweier D ig it a l-
P fe ile gleicher Richtung setzen w ir einfach das Additions­                teilchen A und B, welche sich zu einem T e ilchen C ver­
gesetz ein. Schwieriger wird es, das Gesetz von B ild 5 auf                  einigen. Eine solche Reaktion findet jedoch nur bei bestimm­
sich kreuzende P fe ile verschiedener Länge auszudehnen. W ir                ten Phasenlagen statt. In dem gewählten B eispiel schneiden
treffen folgende Festlegung:                                                 sich d ie idealisierten Teilchenbahnen zu g leicher Z e it in
                                                                             ihren Nullphasenpunkten. Man kann verschiedene Beispiele
Bei orthogonal zueinander stehenden Pfeilen wird der längere
                                                                             für solche Begegnungen konstruieren. Ohne Kenntnis der
in zwei T e lle zerlegt, der Betrag des einen ist g le ic h dem
                                                                             Feinstruktur des logischen Gesetzes, dem d ie D ig it a lt e il­
Betrag des orthogonal dazu laufenden Pfeiles und w irkt m it
                                                                             chen gehorchen, sind nur Wahrscheinlichkeitsaussagen Uber
diesem zusammen entsprechend B ild 5. Der Rest w irkt w ie e in
                                                                             d ie Reaktion solcher T e ilchen m öglich.
isolierter P f e il (Bild 8).
                                                                             D ie gezeigten Beispiele sind selbstverständlich noch weit da­
                                           B ild 8                           von entfernt, ab Ausgangspunkt für d ie Formulierung physi­
                                           Läßt man P fe ile verschiedener kalischer Gesetze zu dienen. Sie können jedoch e in rohes
                                           diskreter Längenwerte zu,       B ild von den M öglichkeiten geben, das Werkzeug der Auto­
                                           sp muß ein neues Gesetz         matentheorie auf physikalische Gesetze anzusetzen. An sich
                                           fa m u lie rt werden: Isolierte ist d ie Automatentheorie n icht auf d ig ita le Gesetzmäßigkei­
                                           P fe ile schalten sich in ihrer   ten beschränkt; jedoch ist d ie Behandlung von Automaten m it
                                           Richtung fort bei g le ic h -     nicht diskreten Zuständen recht schwierig, und d ie entspre­
                                   bleibender Länge. G leiche      chenden mathematischen Lösungen dürften sich nicht v ie l
oder entgegengesetzt gerichtete addieren bzw. subtrahieren sich. von den heute in der theoretischen Physik gebräuchlichen
Bei orthogonalen Pfeilen wird der längere in zwei T e ile zerlegt: unterscheiden. Jedenfalb scheint d ie Automatentheorie das
Oer eine ist g leich dem zugeordneten orthogonalen P fe il und     richtig e Werkzeug zu sein, wenn man d ie Frage nach der
wirkt m it diesem zusammen entsprechend B ild 5. Oer Rest                    restlosen Quantisierung a lle r physikalischer Größen stellt.
wirkt wie ein isolierter P fe il.                                            D ie D igitalisierung bedeutet dabei, daß man m it V ariablen
                                                                             arbeitet, d ie je nur eine begrenzte Z ahl von Werten an­
                                                                             nehmen können. Diese können im Extrem fall Ja-Nein-Werte
W ir können jetzt T eilchen verschiedener Fortpflanzungs-
                                                                             (Bits) sein; jedoch sind auch mehrwertige Variable m it ent­
richtung konstruieren. D ie Z a hl der verschiedenen m öglichen
                                                                             sprechender mehrweniger Logik verwendbar. Eine besondere
Richtungen hängt von der Zahl der m öglichen Werte für d ie
                                                                             R o lle spielt v ie lle ic h t d ie dreiwertige Logik, da m it den
Beträge der P fe ile ab.
                                                                             Werten +1, 0, -1 besonders günstig gearbeitet werden kann.
B ild 9 zeigt e in B eispiel m it dem Pfeilverhältnis 5 : 2. D ie            Eine sehr wesentliche Frage ist die, ob eine D igitalisierung
Bewegungsrichtung entspricht dem Pfeilverhältnis. D ie T e il­               zwangsläufig m it einer Gitterstruktur des Raumes verknüpft
chen durchlaufen verschiedene Phasen. Das T eilchen von                      ist. Diese hat weitgehende Konsequenzen, d ie nicht ohne
B ild 9 hat d ie Periode 7 h t. D ie T eilchen gehen pro Periode             weiteres im Einklang m it den heutigen Vorstellungen der
durch einen diskretenKoordinatenpunkt Q (Nullphasenpunkt).                   Physik stehen, z.B. der Isotropie des Raumes. D ie Benutzung
Zwischendurch "zerfließen* die Teilchen; Man kann Linien                     eines räum lichen und ze itlic h e n Gitters ist zunächst zweifels­
g leicher Phase (Phasenlinien Tq bis Tg) konstruieren.                       ohne d ie bequemste Lösung für eine D ig ita lisie run g . A lle r-
dings stehen außer dem durch kartesische Koordinaten gege­              von 10” 13 cm gew ählt werden müssen; denn d ie Größe 10*13
benen G itter auch andere M öglichkeiten zur Verfügung, z.B.            cm lie g t ja in der Größenordnung der Ausdehnung der Atom ­
kann man d ie dichteste Kugelpackung wählen.                            kerne bzw. deren einzelner P a rtik e l. D ie elektrostatische
                                                                        W echselwirkung steht zur W echselwirkung in fo lg e G ravita­
                                                                        tio n im V erhältnis von etwa 1040 : 1. D am it is t es auch k la r,
In a lle n diesen F ä lle n haben w ir es m it Automatentypen zu
                                                                        daß einfache M odelle z e llu la re r Automaten n ic h t ausreichen
tun, d ie unter dem Namen "z e llu la re Automaten" in der
                                                                        können, um zu brauchbaren Ergebnissen zu gelangen.
Literatur bereits behandelt worden sind [ 3] . Es handelt sich
dabei um d ie A ufteilung eines im P rin z ip unbegrenzten m ehr­       D ig ita lte ilc h e n kann man auch als sich selbst reproduzierende
dim ensionalen Feldes in periodisch sich w iederholende Z e lle n .     Systeme auffassen. Man kann von einem "Norm alzustand"
Jede Z e lle kann für sich als is o lie rte r Automat aufgefaßt wer­    des Gitters der z e llu la re n Automaten ausgehen, der durch e in
den. Er steht m it den N achbarzellen durch Austausch von               bestim mtes Muster gestartet w ird. Dieses Muster is t wand­
Inform ation in Verbindung. D ie Eingangsvariablen ste lle n d ie       lungsfähig und besteht z e itlic h gesehen aus einer Folge von
von den Nachbar z e lle n übertragenen Werte dar, während d ie          Zuständen, d ie sich periodisch w iederholen. D ie W ieder­
Ergebniswerte g le ic h den an d ie N achbarzellen abgegebenen          holung ist dabei jedoch n icht ö rtlic h gebunden, sondern das
Werten sind. Da der z e llu la re Automat nur einen begrenzten          Muster kann wandern und sich so gewissermaßen in einem

•
Umfang hat, hat er auch nur eine begrenzte Z a hl von Zustän­           Nachbargebiet w ieder selbst reproduzieren.
den.
                                                                        Dieses Fortschaltgesetz für Störungen des Normalzustandes ge­
D ie Größe einer solchen Z e lle muß dabei so gew ählt werden,          nügt jedoch noch n icht. Bei Annahme von Feldwerten muß d ie
daß das V erhalten des Gesamtsystems durch d ie Beschreibung            Ausbreitung dieser Felder selbst und das Zusammenspiel der
des Verhaltens einer einzelnen Z e lle vollständig erklärt ist.         D ig ita lfe ld e r m it den D ig ita lte ilc h e n durch das Schaltungsge­
B ei den besprochenen B eispielen besteht d ie Z e lle aus einem        setz z e llu la re r Automaten gegeben sein. D abei müssen d ie
einzelnen G itterpunkt (z.B .B ilde r 4 bis 10), der in u n m itte l­   einzelnen Vektoren, z.B. diejenigen der M axwellschen
baren Beziehungen zu den Nachbarpunkten steht. Für d ie Dar­            G leichungen, durch D ig ita lw erte innerhalb der z e llu la re n
stellung ko m plizierter Gesetze kann man sich in jedem G itte r­       Automaten repräsentiert werden. D ies bedingt, daß diese
punkt e in kleines Rechengerät vorstellen. Es is t le ic h t einzu-     n ic h t nur gestuft sind, sondern auch M in im a l- und M axim al­
sehen, daß d ie F ü lle der M öglichkeiten h ie r außerordentlich       werte aufweisen. Das bedeutet, daß Feldgrößen im d ig ita le n
groß ist.                                                               M o de ll weder b e lie b ig k le in noch b e lie b ig groß sein können.

Schw ierig is t es, solche Z e lle n zu konstruieren, d ie e in e r­    W ie bereits erwähnt, s te llt e in räu m lich und z e itlic h p e rio ­
seits e in Ausbreiten von Feldern, andererseits d ie Existenz           disches G itter zunächst nur d ie m athem atisch am einfachsten
bew eglicher Schaltungsmuster (D ig ita lte ilch e n ) zulassen.        zu behandelnde Lösung dar. Abweichungen hiervon bedeuten
D abei is t zu beachten, daß d ie Natur m it einer außerordent­         M odulationen der Gesetze, d ie auf gewisse Inhom ogenitäten
lic h e n F e in he it sowohl in der Raumstruktur als auch in der       hinauslaufen. Es g ib t z.B. d ie Theorie der wachsenden Auto­
Größenordnung der V ariablen arbeitet. D ie Fein struktur               maten. Ferner kann m it W ahrscheinlichkeitsw erten gearbeitet
eines solchen Gitters w ird sicher noch w esentlich feiner als          werden. Dieses Problem dürfte einer gründlichen Untersuchung
d ie von den Physikern heute angenommene kleinste Länge                 von berufener S te lle wert sein.
E in n ic h t isotroper durch Gitterstruktur repräsentierter Raum hat      der Lichtgeschw indigkeit nähert, desto kritische r w ird d ie d ig i­
selbstverständlich Vorzugsrichtungen in bezug auf d ie Aus­                ta le S im u latio n der Vorgänge, B ei energiereichen T e ilche n
breitung von Strahlen. Dies w iderspricht zunächst unseren E r­            müßte es zu Vorgängen kommen, d ie man gewissermaßen ab
fahrungen. Es is t bis jetzt ke in Experim ent bekannt, das auf            e in "sic h Verrechnen" des rechnenden Raumes bezeichnen
eine solche Richtungsdifferenzierung schließen lä ß t. A lte r­            kann. Dadurch könnte grundsätzlich anderes V erhalten von
dings is t auch noch n ic h t systematisch danach gesucht worden.          T e ilche n sehr hoher Energie (höhere G eschw indigkeit bzw.
Im Bereich der norm alen O ptik durfte eine solche Suche w ohl             höhere Frequenz) e rklärt werden.
auch vergeblich sein. Selbst b e i Röntgenstrahlen sind d ie
                                                                           Durch diese verschiedenen Betrachtungen » hält der B egriff
W ellenlängen noch sehr lang gegenüber der elem entaren
                                                                           der Inform ation eine w esentliche Bedeutung. D ie Inform ations­
Länge von 10"13 cm.
                                                                           theorie hat den B egriff des "Inform ationsgehaltes* in bezug auf
Wenn überhaupt, so könnten solche Effekte w ohl nur b e i außer­           Nachrichtenübertragungssysteme k la r fo rm uliert. Man neigt
o rdentlich energiereichen T e ilche n beobachtet worden. Nun              daher dazu, d ie Inform ationstheorie ab d ie T heorie der In ­
beginnt unsere heutige Experim entalphysik aber gerade erst,               form ation und v ie lle ic h t auch Inform ationsverarbeitung über­
dieses G ebiet zu erschließen. Nur e in Physiker kann eine Ant­            haupt zu halten. Das trifft jedoch n ic h t zu. D ie le ic h tfe rtig e
wort auf d ie Frage geben, ob derartige Experim ente erfolgver­            Übertragung der Begriffe der Inform ationstheorie auf Nachbar-
sprechend sein könnten. Wenn z.B. d ie Richtungsdifferenzie­      gebiete der Nachrichtenübertragung führt le id e r oft zu U nklar­
rung selbst b e i energiereichen T e ilc h e n noch feiner is t als d ie
                                                                  heiten . Auch b e i der vorliegenden Betrachtung müssen w ir
Auflösung beispielsw eise von Nebelkammeraufhahmen, so kann uns k la r werden, was unter Inform ationsgehalt usw. verstan­
sie n ic h t entdeckt werden. Außerdem wäre wegen der Erd-        den werden s o ll. B ei den re in physikalischen Prozessen kann
drehung eine,; z e itlic h e Sortierung und Ordnung der Aufnahmen man schlecht von Nachrichtenübertragung sprechen. D ies
erforderlich.                                                              wäre an sich nur interessant, sobald w ir den Menschen in d ie
                                                                           Betrachtung einbeziehen. B ei Annahme einer unendlich feinen
D ie Frage der Isotropie des Raumes erfordert selbstverständlich
                                                                           Ausbreitung unserer beispiebw eise durch elektrom agnetische
auch e in e Auseinandersetzung m it der R elativitätstheorie. D ie
                                                                           W elten ausgesandten N achrichten müßten diese ewig erhalten
für d ie sp e z ie lle R elativitätstheorie w esentlichen Lorentz-
                                                                           b le ib e n , sofern dem n ic h t d ie z e itlic h e E n d lic h k e it des W elt­
transformationen lassen sich selbstverständlich auch durch
                                                                           a lb Grenzen setzt. Im übertragenen S inne kann man dann
num erische Ansätze b e lie b ig annähem. A llerdin g s w ird es
                                                                           auch davon sprechen, daß d ie Strahlen, d ie aus dem W e lta ll
schwer sein, das M o de ll der R elativitätstheorie in der konse­
                                                                           von anderen Sternen zu uns kommen, für den Menschen N ach­
quenten Farm d ig it a l zu sim ulieren. Unsere physikalische
                                                                           richte n bedeuten, wodurch d ie Frage nach dem Inform ations­
Erfahrung sagt zunächst, daß ke in ausgezeichnetes Koordina­
                                                                           gehalt dieser Nachrichten s in n v o ll w ird. S ieht man von dieser
tensystem nachweisbar is t und daß w ir in unseren Berechnungen
                                                                           Bedeutung der Inform ation ab M itte l der Nachrichtenübertra­
berechtigt sind, jedes Koordinatensystem als g leichberechtigt
                                                                           gung ab, so kann man trotzdem auch b e i n ic h t belebten
dem anderen gegenüber anzunehmen, wobei d ie Lorentztrans-
                                                                           Systemen von einem Inform ationsgehalt sprechen, wenn man
form atianen d ie Beziehungen zwischen diesen Inertialsystem en
                                                                           d ie V ariationsbreite der m öglichen Gestaltungen eines Gegen­
form ulieren. D ie strenge Auslegung der R elativitätstheorie
                                                                           standes, Musters oder dergleichen betrachtet. So kann e in
zieht aber üen Schluß, daß es auch tatsächlich ke in ausge­
                                                                           Schlüssel aufgrund seiner V a ria b ilitä t einen bestimmten In fo r­
zeichnetes Koordinatensystem g ib t und es zwecklos is t, durch
                                                                           m ationsgehalt, in B it gemessen, enthalten. In diesem Sinne
Experim ente danach zu suchen, Bel der Auffassung des Kos­
                                                                           kann man den oben besprochenen D ig ita lte ilc h e n einen In fo r­
mos ah z e llu la re n Automaten kommt man jedoch an der An­
                                                                           m ationsgehalt zuordnen, der der Z a h l der m öglichen V a ria ­
nahme von ausgezeichneten Bezugssystemen wohl kaum vor­
                                                                           tionen dieser T e ilche n entspricht. B ei den in den B ebpielen     i
b e i. Man kann a lle rding s d ie Strukturen von z e llu la re n Auto­
                                                                           von B ildern 8, 9, 10 gezeigten D ig ita lte ilc h e n hängt dieser
maten so konstruieren, daß es m ehrere, aber e n d lich v ie le aus­
                                                                           Inform ationsgehalt von der m axim alen P feilgröße (ab ganze
gezeichnete Koordinatensysteme g ib t. D ie Konstanz der L ic h t­
                                                                           positive bzw. negative Zahl) ab.
geschw indigkeit in a lle n Inertialsystem en wäre durch d ie d ig i­
ta le S im ulierung der Lorentztransformationen und d ie dam it
zusammenhängenden Verkürzungen von Körpern darstellbar.                    Der Gedanke, daß d ie Inform ation b e i physikalischen Be­
A llerdings muß sich in einem solchen M o de ll eine Beziehung             trachtungen ein e w ichtige R o lle übernehmen kann, b t schon
zwischen der. Lichtgeschw indigkeit und der Übertragungsge­                verschiedentlich ausgesprochen worden [2] . D ie von
schw indigkeit zwischen den einzelnen Z e lle n des z e llu la re n        Z e m a n e k geäußerte Auffassung, daß d ie beiden elem en­
Automaten ergeben. Diese müssen n icht notwendigerweise                    taren Dim ensionen naturwissenschaftlicher Betrachtungswebe,
identisch sein. Im G egenteil is t anzunehmen, daß d ie Über­              n ä m lich Stoff und Energie, um d ie Elem entardim ension In fo r­
tragungsgeschwindigkeit von Z e lle zu Z e lle höher sein muß              m ation erw eitert werden könne, kann man a lle rding s etwas
ab d ie erst durch diese Übertragung zustandekommenden                     abwandeln: Eine gründliche Bearbeitung des Problems w ird
Signalfortpflanzungen. Diese höhere G eschw indigkeit hat je ­             w ohl eher zu dem Ergebnb führen, daß d ie bbher verwandten
doch nur lo k a le Bedeutung. S ie is t aufgrund der Anisotropie           Elem entardim ensionen m it H ilfe der Begriffe, d ie m it der
des rechnenden Raumes auch verschieden in verschiedenen                    Inform ation in Zusammenhang stehen, e rklärt werden müßten.
Richtungen. A llerding s ergibt das "d ig ita le * M o de ll im V er­      Inform ationsgehalt b t nur einer dieser Begriffe. H inzu kommen
g le ic h zum "analogen* M o dell der R elativitätstheorie einen           elem entare Informationsverarbeitungsprozesse und Begriffe
wesentlichen Unterschied; Je mehr sich d ie re la tiv e Geschwin­          der Schaltalgebra, w ie S ch a ltg lie d , Schaltvorgang, S chalt­
d ig k e it eines Inertialsystem s im V erhältnis zum Bezugssystem         z e it und dergleichen. Auch d ie Erhaltungssätze der Physik
 könnten dann in entsprechenden Begriffen der Inform ations­                 kaum standhalten können. Es is t auch n ic h t anzunehmen, daß
 theorie und Autom atentheorie ihren Ausdruck finden. Am                     sie w irk lic h begründet werden kann. Das Denken in ganzen
 nächstliegenden is t d ie Frage, ob w ir von einer Erhaltung                Zahlen und diskreten Zuständen erfordert e in Denken in un­
 der Inform ation im Kosmos sprechen können. Faßt man den                    stetigen Übergängen, b e i denen das Kausalgesetz durch A lg o ­
 Kosmos im Sinne des rechnenden Raumes als große Rechen­                     rithm en fa m u lie rt ist. Das A rbeiten m it diskreten Zuständen
 m aschine auf, d ie van außen n ic h t beeinflußbar is t, so g ilt          und Quantisierungen als solches bedingt n ic h t Notwendiger­
 im Sinne der Inform ationstheorie, daß d ie Inform ation dieses             weise einen V erzicht auf eine kausale Betrachtungsweise.
 Systems n ic h t vermehrt werden kann. Das g ilt auch für
 Systeme, in denen d ie Entropie im physikalischen Sinne zu­                 W ichtig is t d ie Frage, ob d ie D eterm ination in beiden Z e it­
 nim m t, selbst wenn d ie Inform ationstheorie le h rt, daß der             richtungen g ilt . Das klassische M o de ll der M echanik e rfü llt
 Inform ationsgehalt eines Machrichtensystems m it seiner                    diese Forderung nach z e itlic h e r Sym m etrie bekanntlich in
 Entropie steigt.                                                            id e a le r W eise. D ie statistische Quantenm echanik führt den
                                                                             B egriff der W ahrscheinlichkeit e in und siebt in der Zunahme
 B ei d ig ita le r Auffassung des Kosmos is t notwendigerweise der
                                                                             der Entropie e in Abweichen von der z e itlic h e n Sym m etrie.
 Inform ationsgehalt in einem abgeschlossenen Raumbereich
                                                                             F in ite Automaten folgen im allgem einen nur den in positiver
 begrenzt, was e in ig e K onsequenzen nach sich zieht. Ebenso
                                                                             Z eitrichtung determ inierten Gesetzen. Der Algorithm us setzt
 is t der Inform ationsgehalt eines D ig ita lte ilc h e n s begrenzt.
                                                                             nur fest, w elcher folgende Zustand sich aus dem gegebenen
 A llerding s ze ig t e in B lic k auf d ie Natur, daß dieser sehr hoch
                                                                             ergibt, n ic h t umgekehrt. Es lassen sich zwar Automaten kon­
 sein muß. Betrachten w ir e in Photon, so muß d ie Richtung
                                                                             struieren, b e i denen auch der vorhergehende Zustand durch
 seiner Fortpflanzung und d ie W ellenlänge in dieser Inform ation
                                                                             den folgenden bestim m t is t, was jedoch n ic h t notw endiger­
 ihre n Ausdruck finden. Beide Größen müßten jedoch b e i d ig i­
                                                                             weise Sym m etrie der Gesetze in z e itlic h e r Richtung bedeutet.
 ta le r Auffassung so fe in gestuft sein, daß eine solche Stufung
                                                                             E in B lic k auf Rechenmaschinen möge dies veranschaulichen.
 bisher durch k e in e rle i Experim ent entdeckt weiden konnte.
                                                                             E ine Rechenmaschine is t - einwandfreies A rbeiten vorausge­
 Schw ieriger w ird d ie Frage nach dem Inform ationsgehalt von              setzt - in positiver Z eitrichtung determ iniert. Im a llg e m e i­
 T e ilche n , wenn man d ie Beeinflussung durch Felder betrach­             nen sind Rechenvorgänge n icht um kehrbar, was sich schon
 tet. D ie Beschleunigung eines T eilchens erfolgt dann auf­                 daraus ergibt, daß d ie logischen Grundoperationen, w elche d ie
 grund einer Inform ationsverarbeitung. Ebenso is t d ie Frage               elem entaren Bausteine a lle r höheren Rechenoperationen dar-
 nach der Inform ationsbilanz b e i der Reaktion zwischen                    ste lle n , n ic h t umkehrbar sind (z.B. a vb=>c). E in Zählw erk
 T e ilche n interessant.                                                    s te llt e in B e is p ie l einer Rechenmaschine dar, w elche im
                                                                             Effekt in beiden Richtungen determ iniert is t, da es in der
 M it inform atlons- und automatentheoretischen Betrachtungen
                                                                             einen Z eitrichtung vorwärts und in der anderen rückwärts
 in engem Zusammenhang steht d ie Frage der D eterm ination
                                                                             z ä h lt, sofern man nur d ie Zustandstabelle betrachtet und d ie
 und K ausalität. D ie Auto m atentheorie arbeitet m it dem Be­
                                                                             Vorgänge im einzelnen n ic h t analysiert.
 g riff des Zustandes eines Automaten. F in ite Automaten
 können eine begrenzte A nzahl von Zuständen einnehm en.
 L ie g t k e in Eingangssignal vor, so e rg ib t sich aufgrund des          W ill man das M o d e ll der klassischen M echanik durch Rechen­
 dem Automaten zugrunde liegenden Algorithm us aus dem ge­                   geräte sym bolisieren, so sind d ie M ög lichkeiten durch den be­
 gebenen Zustand der folgende. Das Gesetz eines Automaten                    grenzten Inform ationsgehalt der Geräte beschränkt. Das Mo­
 kann daher durch eine Zustandstabelle dargestellt werden. Da                d e ll der klassischen M echanik setzt auch einen unendlichen
 d ie Autom atentheorie m it abstrakten Begriffen arbeitet, er-              Inform ationsgehalt n ic h t nur des Kosmos im Ganzen, sondern
1fo lg t dieser Übergang von einem Zustand in den anderen in                 auch b e lie b ig k le in e r Raum teile voraus. Dieser Umstand
 der T heorie ohne Zwischenstufen. D abei fragt d ie Automa­                 scheint bisher n ic h t genügend in Betracht gezogen worden zu
 tentheorie n ic h t danach, w ie b e i einem technisch tatsächlich          sein.
 ausgeführten Automaten e in solcher Übergang erfolgt. Es
                                                                             D ie in den B eispielen angeführten D ig ita lte ilc h e n unter­
 interessiert le d ig lic h , daß z.B. e in F lip - F lo p innerhalb einer
                                                                             lie g e n , is o lie rt betrachtet, einem z e itlic h symmetrischen
 gewissen Z e it, d a T aktzeit, von einem stabilen Zustand in
                                                                             Gesetz. E in sich g e ra d lin ig fortschaltendes T e ilc h e n kann in
den anderen übergeht. Daß man diesen Vorgang des Um ­
                                                                             beiden Zeitrichtungen determ iniert verfolgt werden. B ei Re­
schlagens selbstverständlich technologisch analysieren kann,
                                                                             aktionen von T e ilche n untereinander lie g t nur D eterm ination
lie g t außerhalb der Betrachtungsweise der Autom atentheorie,
                                                                             in positiver'Z eitrichtung vor. Es w ird sicher schw ierig sein,
solange diese sich n ic h t ausdrücklich bemüht, solche E in z e l­
                                                                             e in Gesetz für D ig ita lte ilc h e n zu finden, das in beiden Z e it­
heiten m it zu erfassen.
                                                                             richtungen determ inierte Beziehungen festlegt. K ritis c h is t
 Von Physikern w ird m itunter d ie Ansicht vertreten, daß der               dabei d ie Frage der Auslösung der Aufspaltung eines T e il­
 stufenlose Übergang eines Atoms von einem stabilen Zustand                  chens in zw ei neue T e ilc h e n , w elche der Umkehrung der V er­
 in den anderen m it dem Kausalgesetz schlecht in Einklang                   einigung zw eier T e ilche n entspricht.
 zu bringen ist; z.B. Arthur M a r c h "D ie physikalische
 Erkenntnis und ih re Grenzen", Seite 19 [4] . Er versteht                   D ie Frage der z e itlic h e n Sym m etrie der physikalischen Ge­
 dort den B egriff der K ausalität so, daß der Übergang von                  setze w ird neuerdings v ie lfa ch in Zusammenhang m it den
 einem abgeschlossenen System zum nächsten e in ko ntin uie r­               Spiegelungseigenschaften des Raumes diskutiert. Eine auto­
 liches Geschehen voraussetzt. Diese Auffassung w ird einer                  matentheoretische Betrachtungsweise könnte diese Dis kussion
 automatentheoretischen Betrachtung physikalischer Prozesse                  v ie lle ic h t w esentlich befruchten.

                                                                                                                                                  343
B ild lic h wäre der rechnende Raum als Relaiskosmos deutbar,       natürlich verschiedene Verhaltensweisen m öglich. Man kann
wobei wir uns allerdings von irgendwelchen konkreten Vor­           sagen, d ie Idee des rechnenden Raumes stehe im Widerspruch
stellungen bezüglich der Relaistechnik selbst v ö llig frei         zu einigen heute anerkannten Sätzen der Physik (z.B. Isotropie
machen müssen. Auch müßten d ie bereits angedeuteten M ög-,         des Raumes), infolgedessen könne es ih n nicht geben. Diese
llchke ite n wachsender bzw. variabler Automaten m it in Be­        Auffassung wird heute vielfach von Physikern vertreten, ohne
tracht gezogen werden.                                              daß man sich wohl Uber d ie Konsequenzen ernsthaft Gedanken
                                                                    gemacht hat. Man kann aber auch den Versuch machen, d ie
Wenn auch d ie vorhergehenden Betrachtungen noch nicht zu
                                                                    Gesetze des rechnenden Raumes so zu modulieren, daß diese
handgreiflichen Lösungen führen, so dürfte doch gezeigt sein,
                                                                    Widersprüche verschwinden. S c h lie ß lic h kann man auch die
daß der vorgeschlagene Weg e inige neue Perspektiven eröff­
                                                                    durch d ie Idee des rechnenden Raumes in Frage gestellten Vor­
net, welche wert sind, weiterverfolgt zu werden. D ie Einbe­
                                                                    stellungen kritisch betrachten und ihre G ü ltig ke it nach neuen
ziehung von Begriffen der Informations- und Automatentheorie
                                                                    Gesichtspunkten untersuchen.
in physikalische Betrachtungen wird umso d rin g liche r werden,
je mehr ml£ ganzen Zahlen, diskreten Zuständen und der­             Im folgenden sei noch eine Gegenüberstellung der m öglichen
gleichen gearbeitet wird. Angesichts der Konsequenzen sind          Auffassungen versucht.

Klassische Physik                        Quantenphysik                               Rechnender Raum

Punktmechaidk                            W ellenm echanik                            Automaten theorie
                                                                                     Schaltalgebra

Korpuskel                                W elle - Korpuskel                          Scbaltzustand, D ig ita lte ilc h e n

analog                                   hybrid                                      d ig it a l

Analysis                                 Differentialgleichungen                     Boolesche Algebra

A lle Größen ko ntinuierlich             Einige Größen gequantelt                    A lle Größen nehmen nur diskrete Werte an

Keine Grenzwerte                         Außer Lichtgeschwindigkeit                 . M in im a l- und Maximalwerte sämtlicher
              ?                          keine Grenzwerte                            Größen

U nendlich genau                         Unbestimmtheitsrelation                     Begrenzte Rechengenauigkeit

Kausalität in beiden Z eit-              Nur statistische Kausalität                 Kausalität nur in positiver Zeltrichtung,
richtungen                               Auflösung in W ahrscheinlichkeit            Einführung von Wahrscheinlichkeitstermen
                                                                                     m öglich, aber n ic ht nötig

                                          Klassische Mechanik wird                   Wahrscheinlichkeitsgesetze der Quanten -
                                          statistisch angenähert                     physik durch determ inierte Raumstruktur
                                                                                      erklärbar

                                          Urformei                                   Urschaltung

Es sei noch betont, daß d ie bisherigen Untersuchungen des
Verfassen rein auf dem Papier durchgefuhrt worden sind.
Weitere Untenuchungen müßten unter Zuhilfenahme moder­
ner Rechengeräte vorgenommen werden.                                L ite ra tu r

Anhang
                                                                    [1]   C .-F. Frhr. von Weizsäcker, Hamburg, * D ie E inheit
D ie Idee des Gitterraumes wurde in letzter Z elt in mehreren
                                                                          der Physik", Physiker-Tagung 1966, Plenarvortxäge I
Aufsätzen durch Fritz B o p p behandelt [5]. Diese A rbei­
                                                                          Verlag Teubner, Stuttgart.
ten und d ie Arbeit des Verfassers erfolgten v ö llig unabhängig
voneinander. Bopp geht als Physiker von anderen Vorstellungen
                                                                     [2] H.Zemanek, Wien, " D i e Kybernetik als interfakulta­
aus und wendet eine etwas andere Betrachtungsweise an. Es
                                                                         tive Formalwissenschaft*, Physiker-Tagung 1966,
ist jedoch zu hoffen, daß eine gegenseitige Befruchtung der
                                                                         Plenarvorträge I, Verlag Teubner, Stuttgart.
beiden Standpunkte (des physikalischen und des automaten­
theoretischen) zu wertvollen Erkennmissen führt. Für den
                                                                     [3] John von Neumann, "Theory of Self-Reproducing
physikalischen Laien ist es allerdings schwer verständlich,
                                                                         Automata", University of Illin o is Press.
warum dem fiktiven Gravitationsradius (6,7 •10-5S cm)
eine solche Bedeutung beigelegt wird. Ein derartig feines
                                                                     [4] Arthur March, Innsbruck, " D ie physikalische Erkenntnis
Gitter würde bedeuten, daß im Raum von der Größenordnung
                                                                          und ihre Grenzen", Frledr.Vieweg&Sohn,Braunschweig.
der Elementarlänge von 10-13 cm noch einm al ein ganzer
Kosmos untergebracht werden könnte, was vom automaten­
                                                                     [ 5] Fritz Bopp, Zeitschrift für Physik, Band 200, Heft 2.
theoretischen Standpunkt wenig plausibel erscheint.

