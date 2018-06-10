from textblob import TextBlob
import csv

with open('global_warming.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        analysis = TextBlob(row[0])
        print(analysis.sentiment)
        print("")
    print("")