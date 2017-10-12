#Sequentie RNA van het organisme
print("voer sequentie RNA in, in fasta format:")
seq = input()

#Geeft tekenlengte RNA sequentie weer
print("aantal basen: ",len(seq))

#Telt de hoeveelheden Cytosine en Guanine in het RNA en geeft deze weer
aantalC = seq.count('C')
aantalG = seq.count('G')
print("aantal Cytosine: ",aantalC)
print("aantal Guanine: ",aantalG)

#telt de hoeveelheden Cytosine en Guanine in het RNA bij elkaar op en geeft dit weer
GC = (aantalC+aantalG)
print("aantal Cytosine en Guanine: ",GC)

#geeft het GC% in het RNA weer ten opzichte van de complete lengte
GCP = GC/len(seq)
print("GC percentage: ",GCP*100,"%")

#Sequentie DNA van het organisme
print("voer sequentie DNA in, in fasta format:")
DNA = input()

#Geeft tekenlengte DNA sequentie weer
print("aantal basen: ",len(DNA))

#Telt de hoeveelheden Cytosine en Guanine in het DNA en geeft deze weer
aantalC = DNA.count('C')
aantalG = DNA.count('G')
print("aantal Cytosine: ",aantalC)
print("aantal Guanine: ",aantalG)

#telt de hoeveelheden Cytosine en Guanine in het DNA bij elkaar op en geeft dit weer
GCDNA = (aantalC+aantalG)
print("aantal Cytosine en Guanine: ",GCDNA)

#geeft het GC% van het DNA weer ten opzichte van de complete lengte
GCPDNA = GCDNA/len(DNA)
print("GC percentage: ",GCPDNA*100,"%")

DNALV = len(DNA)-len(seq)
print("lengte verschil DNA RNA:", DNALV)

#verschil in GC% tussen DNA en RNA
print("Verschil in GC% tussen DNA en RNA sequentie: ",((GCP-GCPDNA)*100),"%")
print("Als het verschil in GC% <0 dan is het GC% hoger dan in het DNA.")


