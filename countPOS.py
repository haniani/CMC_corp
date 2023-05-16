import pandas as pd
import csv

df = pd.read_csv('exampleNOUMtext2016.csv')
res = df.Lex.value_counts()
a = res.head(100)

with open("Statistics_2016.csv", "w", newline='') as csv_file:
    res.to_csv(csv_file)

csv_file.close()

