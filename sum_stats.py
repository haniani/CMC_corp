import pandas as pd
import csv

t2012 = pd.read_csv('Statistics_2012.csv')
t2013 = pd.read_csv('Statistics_2013.csv')
t2014 = pd.read_csv('Statistics_2014.csv')
t2015 = pd.read_csv('Statistics_2015.csv')
t2016 = pd.read_csv('Statistics_2016.csv')

sumTables = pd.concat([t2012, t2013], axis=1).reindex(t2012.index)
sumTables2 = pd.concat([sumTables, t2014], axis=1).reindex(sumTables.index)
sumTables3 = pd.concat([sumTables2, t2015], axis=1).reindex(sumTables2.index)
sumTables4 = pd.concat([sumTables3, t2016], axis=1).reindex(sumTables3.index)

with open("Sum_stat.csv", "w", newline='') as csv_file:
    sumTables4.to_csv(csv_file)
csv_file.close()

stat1000 = sumTables4.head(1000)

with open("Sum_stat_1000.csv", "w", newline='') as csv_file2:
    stat1000.to_csv(csv_file2)
csv_file2.close()