#Sequentie RNA van het organisme
seq = input("voer sequentie RNA in, in fasta format:\n")

#Geeft tekenlengte RNA sequentie weer
print("aantal basen: ",len(seq))
RNAL = len(seq)

#Telt de hoeveelheden Cytosine en Guanine in het RNA en geeft deze weer
aantalC = seq.count('C') + seq.count('c')
aantalG = seq.count('G') + seq.count('g')
aantalT = seq.count('T') + seq.count('t')
aantalA = seq.count('A') + seq.count('a')
print("aantal Cytosine: ",aantalC)
print("aantal Guanine: ",aantalG)

#telt de hoeveelheden Cytosine en Guanine in het RNA bij elkaar op en geeft dit weer
GC = (aantalC+aantalG)
print("aantal Cytosine en Guanine: ",GC)

#geeft het GC% in het RNA weer ten opzichte van de complete lengte
GCP = GC/len(seq)
print("GC percentage: ",GCP*100,"%")

#Voer onbekende sequentie in
SAMP = input("Voer een Sequentie in, infasta format:\n")
SAMPA = SAMP.count('A') + SAMP.count('a')
SAMPT = SAMP.count('T') + SAMP.count('t')
SAMPG = SAMP.count('G') + SAMP.count('g')
SAMPC = SAMP.count('C') + SAMP.count('c')
aantalD = SAMP.count('D') + SAMP.count('d')
aantalE = SAMP.count('E') + SAMP.count('e')
aantalR = SAMP.count('R') + SAMP.count('r')
aantalK = SAMP.count('K') + SAMP.count('k')
aantalN = SAMP.count('N') + SAMP.count('n')
aantalF = SAMP.count('F') + SAMP.count('f')
aantalQ = SAMP.count('Q') + SAMP.count('q')
aantalH = SAMP.count('H') + SAMP.count('h')
aantalI = SAMP.count('I') + SAMP.count('i')
aantalL = SAMP.count('L') + SAMP.count('l')
aantalM = SAMP.count('M') + SAMP.count('m')
aantalP = SAMP.count('P') + SAMP.count('p')
aantalS = SAMP.count('S') + SAMP.count('s')
aantalW = SAMP.count('W') + SAMP.count('w')
aantalY = SAMP.count('Y') + SAMP.count('y')
aantalV = SAMP.count('V') + SAMP.count('v')

DREK = aantalD+aantalE+aantalR+aantalK+SAMPA+SAMPT+SAMPG+SAMPC
ATCG = SAMPA+SAMPG+SAMPT+SAMPC
int(DREK)
int(ATCG)
print("Lengte van ingevoerde sample: ",len(SAMP))
DREKC = aantalD+aantalE+aantalR+aantalK
MASSA = (aantalN*132)+(aantalF*146)+(aantalQ*147)+(aantalH*131)+(aantalI*131)+(aantalL*146)+(aantalM*165)+(aantalP*115)+(aantalS*105)+(aantalW*204)+(aantalY*181)+(aantalV*117)
MASSADREK = (aantalD*133)+(aantalE*75)+(aantalR*174)+(aantalK*149)
MASSAATCG = (SAMPA*89)+(SAMPT*119)+(SAMPC*121)+(SAMPG*155)
MASSATOT = MASSA+MASSADREK+MASSAATCG
RNAMASSA = (aantalC*121)+(aantalT*119)+(aantalG*155)+(aantalA*89)
if DREKC>0:
    print("Het is een eiwit.")
else:
    print("Het is DNA.")

#if statemant voor DNA
if int(DREK)!=(ATCG):
    print("aantal D,R,E,K: ",DREKC)
    print("totale lengte: ",DREK)
    VERGRNAEI = (DREK/RNAL)
    if VERGRNAEI<1:
        print("Het eiwit is met een factor",VERGRNAEI,"groter.")
    elif VERGRNAEI == 1:
        print("Het eiwit is even groot als het RNA.")
    else:
        print("Het eiwit is met een factor",VERGRNAEI,"groter.")
    print("Massa eiwit:",MASSATOT,"Da")
    print("Massa RNA:",RNAMASSA,"Da")
else:
    int(DREK)==int(ATCG)
    #Telt de hoeveelheden Cytosine en Guanine in het DNA en geeft deze weer
    print("aantal Cytosine: ",SAMPC)
    print("aantal Guanine: ",SAMPG)

    #telt de hoeveelheden Cytosine en Guanine in het DNA bij elkaar op en geeft dit weer
    GCDNA = (SAMPC+SAMPG)
    print("aantal Cytosine en Guanine: ",GCDNA)

    #geeft het GC% van het DNA weer ten opzichte van de complete lengte
    GCPDNA = GCDNA/ATCG
    print("GC percentage: ",GCPDNA*100,"%")

    DNALV = ATCG-RNAL
    print("lengte verschil DNA RNA:", DNALV)
    
    #verschil in GC% tussen DNA en RNA
    print("Verschil in GC% tussen DNA en RNA sequentie: ",((GCP-GCPDNA)*100),"%")
    if DNALV < 0:
        print("Het GC% is hoger in het RNA.")
    elif DNALV == 0:
        print("Het GC% is in het RNA gelijk aan het GC% van het DNA.")
    else:
        print("Het GC% is hoger in het DNA.")
    print("Massa DNA:",MASSAATCG,"Da")
    print("Massa RNA:",RNAMASSA,"Da")

        







