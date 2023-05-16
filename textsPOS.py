import os,re
from os.path import join
import nltk
from nltk.tokenize import word_tokenize
from pymystem3 import Mystem

m = Mystem()

POS2016 = open("POS2016.txt", 'w')

f = open("textVK2016.txt", "r")
file = f.readlines()
text = ''.join(file)
f.close()
tokens = word_tokenize(text,language="russian")
for k in tokens:
    h = m.analyze(k)
    j = re.findall('(\'\w{1,4}\,)',str(h))
    jk = re.sub("\[|\'|\,|\"", '', str(j))
    jk = re.sub("\]", ' ', str(jk))
    POS2016.write(jk)

POS2016.close()
