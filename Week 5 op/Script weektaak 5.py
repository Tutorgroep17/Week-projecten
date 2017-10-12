aantal = 0
file1= input('eiwit sequentie 1:\n')
file2= input('eiwit sequentie 2:\n')

seq1=''
for i in open(file1).readlines()[1:]:
    seq1+=i.replace('\n','')

seq2=''
for i in open(file2).readlines()[1:]:
    seq2+=i.replace('\n','')

print("Sequentie 1: ",seq1,"\n \nSequentie 2: ",seq2,"\n")

lengte1 = len(seq1)
lengte2 = len(seq2)

if lengte1>lengte2:
    print("opgelet de bestanden zijn gewisseld! ivn met stack overflow")
    seq2=''
    for i in open(file1).readlines()[1:]:
        seq2+=i.replace('\n','')
    seq1=''
    for i in open(file2).readlines()[1:]:
        seq1+=i.replace('\n','')
    lengte1 = len(seq2)
    lengte2 = len(seq1)

for i in range(len(seq1)):
    if seq1[i]==seq2[i]:
        aantal+=1

identity = (aantal / lengte1 *100)


print("aantal afwijkend:\n",aantal,"\n")

print("Identity percentage:\n",identity,"%")

