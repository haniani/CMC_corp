import os,re, csv, json, nltk
from os.path import join
from nltk.tokenize import word_tokenize
from pymystem3 import Mystem

m = Mystem()

f = open("textVK2016.txt", "r")
file = f.readlines()
text = ''.join(file)
f.close()

with open("exampleNOUMtext2016.csv", "w", newline='') as csv_file:
    fieldnames = ['Lex', 'POS']
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(fieldnames)

    tokens = word_tokenize(text,language="russian")
    for k in tokens:
        h = m.analyze(k)  #анализ текста
        try:
            mystJson = json.dumps(h) #делаем json
            mystJson2 = json.loads(mystJson)
            word = mystJson2[0]['analysis'][0]['lex'] #вынимаем лексемы
            pos = mystJson2[0]['analysis'][0]['gr'] #вынимаем граммемы
            posREG = re.findall('^[A-Z]{1,4}',str(pos))
            j = ('[%s]' % ', '.join(map(str, posREG)))
            jk = re.sub("\[|\'|\,|\"", '', str(j))
            jk = re.sub("\]", ' ', str(jk))
            jk = re.sub(" ", '', str(jk))
            if jk == "S" or jk == "SPRO":
                textPOS = (word, jk)
                writer.writerow(textPOS)
            else:
                continue
        except:
            continue

csv_file.close()