from textblob import TextBlob
import csv

with open('./global_warming.csv', 'rU') as csvfile:
    readCSV = csv.DictReader(csvfile, delimiter=',')
    next(readCSV)
    try:
        for d in readCSV:
            analysis = TextBlob(d['tweet'])
            print(analysis.sentiment)
    except:
        print("")
        