import os,re

A = 0 #прилагательное
ADV = 0 #наречие
ADVPRO = 0  #местоименное наречие
ANUM = 0    #числительное-прилагательное
APRO = 0    #местоимение-прилагательное
COM = 0 #часть композита - сложного слова
CONJ = 0    #союз
INTJ = 0    #междометие
NUM = 0 #числительное
PART = 0    #частица
PR = 0  #предлог
S = 0   #существительное
SPRO = 0    #местоимение-существительное
V = 0   #глагол

f = open("POS2016.txt", "r")
file = f.readlines()
text = ''.join(file)
f.close()

a = re.findall("\w{1,4}", str(text))
for i in a:
    if "S" == i:
        S +=1
    elif "A" == i:
        A +=1
    elif "ADV" == i:
        ADV +=1
    elif "ADVPRO" == i:
        ADVPRO +=1
    elif "ANUM" == i:
        ANUM +=1
    elif "APRO" == i:
        APRO +=1
    elif "COM" == i:
        COM +=1
    elif "CONJ" == i:
        CONJ +=1
    elif "INTJ" == i:
        INTJ +=1
    elif "NUM" == i:
        NUM +=1
    elif "PART" == i:
        PART +=1
    elif "PR" == i:
        PR +=1
    elif "SPRO" == i:
        SPRO +=1
    elif "V" == i:
        V +=1

print(S, "\n", A, "\n", ADV, "\n", ADVPRO, "\n", ANUM, "\n", APRO, "\n", COM, "\n", CONJ, "\n", INTJ, "\n", NUM, "\n", PART, "\n", PR, "\n", SPRO, "\n", V)




