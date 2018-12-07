import csv
import pandas as pd
import numpy as np
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Maria
date_list = []
index = []
dateList1 = ['2017-09-02', '2017-09-03', '2017-09-04', '2017-09-05', '2017-09-06',
             '2017-09-07', '2017-09-08', '2017-09-09', '2017-09-10', '2017-09-11',
             '2017-09-12', '2017-09-13', '2017-09-14', '2017-09-15', '2017-09-16',
             '2017-09-17', '2017-09-18', '2017-09-19', '2017-09-20', '2017-09-21',
             '2017-09-22', '2017-09-23', '2017-09-24', '2017-09-25', '2017-09-26',
             '2017-09-27', '2017-09-28', '2017-09-29', '2017-09-30', '2017-10-01',
             '2017-10-02', '2017-10-03', '2017-10-04', '2017-10-05', '2017-10-06',
             '2017-10-07', '2017-10-08', '2017-10-09', '2017-10-10', '2017-10-11',
             '2017-10-12', '2017-10-13', '2017-10-14', '2017-10-15', '2017-10-16',
             ]

# Harvey
dateList2 = ['2017-08-03', '2017-08-04', '2017-08-05', '2017-08-06', '2017-08-07',
             '2017-08-08', '2017-08-09', '2017-08-10', '2017-08-11', '2017-08-12',
             '2017-08-13', '2017-08-14', '2017-08-15', '2017-08-16', '2017-08-17',
             '2017-08-18', '2017-08-19', '2017-08-20', '2017-08-21', '2017-08-22',
             '2017-08-23', '2017-08-24', '2017-08-25', '2017-08-26', '2017-08-27',
             '2017-08-28', '2017-08-29', '2017-08-30', '2017-08-31', '2017-09-01',
             '2017-09-02', '2017-09-03', '2017-09-04', '2017-09-05', '2017-09-06',
             '2017-09-07', '2017-09-08', '2017-09-09', '2017-09-10', '2017-09-11',
             '2017-09-12', '2017-09-13', '2017-09-14', '2017-09-15', '2017-09-16',
             '2017-09-17']

# Irma
dateList3 = ['2017-08-16', '2017-08-17', '2017-08-18', '2017-08-19', '2017-08-20',
             '2017-08-21', '2017-08-22', '2017-08-23', '2017-08-24', '2017-08-25',
             '2017-08-26', '2017-08-27', '2017-08-28', '2-17-08-29', '2017-08-30',
             '2017-08-31', '2017-09-01', '2017-09-02', '2017-09-03', '2017-09-04',
             '2017-09-05', '2017-09-06', '2017-09-07', '2017-09-08', '2017-09-09',
             '2017-09-10', '2017-09-11', '2017-09-12', '2017-09-13', '2017-09-14',
             '2017-09-15', '2017-09-16', '2017-09-17', '2017-09-18', '2017-09-19',
             '2017-09-20', '2017-09-21', '2017-09-22', '2017-09-23', '2017-09-24',
             '2017-09-25', '2017-09-26', '2017-09-27']

# Irene
dateList4 = ['2011-08-07', '2011-08-08', '2011-08-09', '2011-08-10', '2011-08-11',
             '2011-08-12', '2011-08-13', '2011-08-14', '2011-08-15', '2011-08-16',
             '2011-08-17', '2011-08-18', '2011-08-19', '2011-08-20', '2011-08-21',
             '2011-08-22', '2011-08-23', '2011-08-24', '2011-08-25', '2011-08-26',
             '2011-08-27', '2011-08-28', '2011-08-29', '2011-08-30', '2011-08-31',
             '2011-09-01', '2011-09-02', '2011-09-03', '2011-09-04', '2011-09-05',
             '2011-09-06', '2011-09-07', '2011-09-08', '2011-09-09', '2011-09-10',
             '2011-09-11']
date_list = [dateList1, dateList2, dateList3, dateList4]

hurricane = ['hurricane maria', 'hurricane harvey', 'hurricane irma', 'hurricane irene']


def reddit_sentiment_date():
    datelist = []
    df = pd.read_csv("./reddit/reddit.csv")
    for time in df["time"]:
        time = time[0:10]
        datelist.append(time)
    df['date'] = datelist

    sent_analyzer = SentimentIntensityAnalyzer()

    score_dict = []
    index = [0, 1, 2, 3]
    # for i in index:
    rows = df["hurricane name"] == 'hurricane maria'
    df = df[rows]

    # calculate sentiment score for every day
    for date in dateList1:
        score_list = []
        neg_total = 0
        pos_total = 0
        neutral_total = 0
        total = 0
        for index, row in df.loc[df['date'] == date].iterrows():
            score = sent_analyzer.polarity_scores(str(row['comment']))
            score_list.append((row['comment'], score))
            neg_total += score['neg']
            pos_total += score['pos']
            neutral_total += score['neu']
            total += 1
        if total == 0:
            score_date = ['hurricane maria', date, 0, 0, 0]
        else:
            score_date = ['hurricane maria', date, neg_total / total, pos_total / total, neutral_total / total]
        score_dict.append(score_date)
    header = ['hurricane name', 'date', 'neg', 'pos', 'neu']
    score_dict.insert(0, header)
    # write sentiment data to file
    with open("./sentiment_analysis/reddit_sentiment_date.csv", 'w') as reddit_file:
        writer = csv.writer(reddit_file, delimiter=',')
        writer.writerows(score_dict)


def guardian_sentiment_date():
    datelist = []
    df = pd.read_csv("./basic_analysis/guardian_data.csv")
    for time in df["article date"]:
        time = time[0:10]
        datelist.append(time)
    df['date'] = datelist
    rows = df["search query"] == "hurricane maria"
    df = df[rows]

    sent_analyzer = SentimentIntensityAnalyzer()

    score_dict = []
    # calculate sentiment score for every day
    for date in dateList1:
        score_list = []
        neg_total = 0
        pos_total = 0
        neutral_total = 0
        total = 0
        for index, row in df.loc[df['date'] == date].iterrows():
            score = sent_analyzer.polarity_scores(str(row['article summary']))
            score_list.append((row['article summary'], score))
            neg_total += score['neg']
            pos_total += score['pos']
            neutral_total += score['neu']
            total += 1
        if total == 0:
            score_date = ['hurricane maria', date, 0, 0, 0]
        else:
            score_date = ['hurricane maria', date, neg_total / total, pos_total / total, neutral_total / total]
        score_dict.append(score_date)
    header = ['hurricane name', 'date', 'neg', 'pos', 'neu']
    score_dict.insert(0, header)
    # write sentiment data to file
    with open("./sentiment_analysis/guardian_sentiment_date.csv", 'w') as guardian_file:
        writer = csv.writer(guardian_file, delimiter=',')
        writer.writerows(score_dict)


def nytimes_sentiment_date():
    datelist = []
    df = pd.read_csv("./basic_analysis/nytimes_data.csv")
    for time in df["article date"]:
        time = time[0:10]
        datelist.append(time)
    df['date'] = datelist
    rows = df["search query"] == "hurricane maria"
    df = df[rows]

    sent_analyzer = SentimentIntensityAnalyzer()

    score_dict = []
    # calculate sentiment score for every day
    for date in dateList1:
        score_list = []
        neg_total = 0
        pos_total = 0
        neutral_total = 0
        total = 0
        for index, row in df.loc[df['date'] == date].iterrows():
            score = sent_analyzer.polarity_scores(str(row['article summary']))
            score_list.append((row['article summary'], score))
            neg_total += score['neg']
            pos_total += score['pos']
            neutral_total += score['neu']
            total += 1
        if total == 0:
            score_date = ['hurricane maria', date, 0, 0, 0]
        else:
            score_date = ['hurricane maria', date, neg_total / total, pos_total / total, neutral_total / total]
        score_dict.append(score_date)
    header = ['hurricane name', 'date', 'neg', 'pos', 'neu']
    score_dict.insert(0, header)
    # write sentiment data to file
    with open("./sentiment_analysis/nytimes_sentiment_date.csv", 'w') as nytimes_file:
        writer = csv.writer(nytimes_file, delimiter=',')
        writer.writerows(score_dict)


def main():
    reddit_sentiment_date()
    guardian_sentiment_date()
    nytimes_sentiment_date()


if __name__ == "__main__":
    main()
