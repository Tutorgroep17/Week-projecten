#Sequentie RNA van het organisme
print("voer sequentie RNA in, in het formaat fasta:")
seq = input()

#Geeft tekenlengte RNA sequentie weer
print("aantal basen: ",len(seq))

#Telt de hoeveelheden Cytosine en Guanine en geeft deze weer
aantalC = seq.count('C')
aantalG = seq.count('G')
print("aantal Cytosine: ",aantalC)
print("aantal Guanine: ",aantalG)

#telt de hoeveelheden Cytosine en Guanine bij elkaar op en geeft dit weer
GC = (aantalC+aantalG)
print("aantal Cytosine en Guanine: ",GC)

#geeft het GC% weer ten opzichte van de complete lengte
GCP = GC/len(seq)
print("GC percentage: ",GCP*100)


