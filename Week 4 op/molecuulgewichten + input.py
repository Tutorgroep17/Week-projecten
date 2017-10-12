#geef eiwit sequentie in
seq = input("Voer een eiwit sequentie in: \n")
#moleculaire massa in g/mol
A = 89
R = 174
N = 132
D = 133
C = 121
F = 146
Q = 147
E = 75
G = 155
H = 131
I = 131
L = 146
K = 149
M = 165
P = 115
S = 105
T = 119
W = 204
Y = 181
V = 117
#tel het aantal keer dat elk aminozuur voorkomt
aantalA = seq.count("A")
aantalR = seq.count("R")
aantalN = seq.count("N")
aantalD = seq.count("D")
aantalC = seq.count("C")
aantalF = seq.count("F")
aantalQ = seq.count("Q")
aantalE = seq.count("E")
aantalG = seq.count("G")
aantalH = seq.count("H")
aantalI = seq.count("I")
aantalL = seq.count("L")
aantalK = seq.count("K")
aantalM = seq.count("M")
aantalP = seq.count("P")
aantalS = seq.count("S")
aantalT = seq.count("T")
aantalW = seq.count("W")
aantalY = seq.count("Y")
aantalV = seq.count("V")
#aantal voorkomen X massa
gewichtA = aantalA * A
gewichtR = aantalR * R
gewichtN = aantalN * N
gewichtD = aantalD * D
gewichtC = aantalC * C
gewichtF = aantalF * F
gewichtQ = aantalQ * Q
gewichtE = aantalE * E
gewichtG = aantalG * G
gewichtH = aantalH * H
gewichtI = aantalI * I
gewichtL = aantalL * L
gewichtK = aantalK * K
gewichtM = aantalM * M
gewichtP = aantalP * P
gewichtS = aantalS * S
gewichtT = aantalT * T
gewichtW = aantalW * W
gewichtY = aantalY * Y
gewichtV = aantalV * V
#tel de massa's op
gewichteiwit = gewichtA + gewichtR + gewichtN + gewichtD + gewichtC + gewichtF + gewichtQ + gewichtE + gewichtG + gewichtH + gewichtI + gewichtL + gewichtK + gewichtM + gewichtP + gewichtS + gewichtT + gewichtW + gewichtY + gewichtV
#geef uitslag
print (gewichteiwit, "Da")


