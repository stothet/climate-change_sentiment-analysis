from textblob import TextBlob
import csv,sys
reload(sys)
sys.setdefaultencoding("ISO-8859-1")

POLARITY_THRESHOLD = 0.55;
SUBJECTIVENESS_THRESHOLD = 0.55;

with open('./analysed_tweets.csv', 'wb') as resultExport:
    with open('./global_warming.csv', 'rU') as source:
        readCSV = csv.DictReader(source, delimiter=',')
        next(readCSV)
        headers = ['Tweet', 'Sentiment', 'Opinionated']
        outCSV = csv.DictWriter(resultExport, fieldnames=headers);
        outCSV.writeheader();

        for d in readCSV:
            analysis = TextBlob(d['tweet'])
            print(d['tweet'],analysis.sentiment)
            outCSV.writerow({'Tweet': d['tweet'],
                             'Sentiment':  'Positive' if analysis.sentiment[0]>POLARITY_THRESHOLD else 'Negative',
                             'Opinionated': 'Yes' if analysis.sentiment[1]>SUBJECTIVENESS_THRESHOLD else 'No'})