import csv
import pandas as pd
import numpy as np
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def reddit_sentiment_date():
    datelist = []
    df = pd.read_csv("../reddit/reddit.csv")
    for time in df["time"]:
        time = time[0:10]
        datelist.append(time)
    df['date'] = datelist
    dateList = np.unique(datelist)

    sent_analyzer = SentimentIntensityAnalyzer()

    score_dict = []
    # calculate sentiment score for every day
    for date in dateList:
        score_list = []
        neg_total = 0
        pos_total = 0
        neutral_total = 0
        total = 0
        for index, row in df.loc[df['date'] == date].iterrows():
            # if row['date'] == date :
            score = sent_analyzer.polarity_scores(str(row['comment']))
            score_list.append((row['comment'], score))
            neg_total += score['neg']
            pos_total += score['pos']
            neutral_total += score['neu']
            total += 1
            score_date = [date, neg_total / total, pos_total / total, neutral_total / total]
            score_dict.append(score_date)
    header = ['date', 'neg', 'pos', 'neu']
    score_dict.insert(0, header)
    # write sentiment data to file
    with open("reddit_sentiment_date.csv", 'w') as reddit_file:
        writer = csv.writer(reddit_file, delimiter=',')
        writer.writerows(score_dict)


def guardian_sentiment_date():
    datelist = []
    df = pd.read_csv("../basic_analysis/guardian_data.csv")
    for time in df["article date"]:
        time = time[0:10]
        datelist.append(time)
    df['date'] = datelist
    dateList = np.unique(datelist)

    sent_analyzer = SentimentIntensityAnalyzer()

    score_dict = []
    # calculate sentiment score for every day
    for date in dateList:
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
            score_date = [date, neg_total / total, pos_total / total, neutral_total / total]
            score_dict.append(score_date)
    header = ['date', 'neg', 'pos', 'neu']
    score_dict.insert(0, header)
    # write sentiment data to file
    with open("guardian_sentiment_date.csv", 'w') as guardian_file:
        writer = csv.writer(guardian_file, delimiter=',')
        writer.writerows(score_dict)


def nytimes_sentiment_date():
    datelist = []
    df = pd.read_csv("../basic_analysis/nytimes_data.csv")
    for time in df["article date"]:
        time = time[0:10]
        datelist.append(time)
    df['date'] = datelist
    dateList = np.unique(datelist)

    sent_analyzer = SentimentIntensityAnalyzer()

    score_dict = []
    # calculate sentiment score for every day
    for date in dateList:
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
            score_date = [date, neg_total / total, pos_total / total, neutral_total / total]
            score_dict.append(score_date)
    header = ['date', 'neg', 'pos', 'neu']
    score_dict.insert(0, header)
    # write sentiment data to file
    with open("nytimes_sentiment_date.csv", 'w') as nytimes_file:
        writer = csv.writer(nytimes_file, delimiter=',')
        writer.writerows(score_dict)


if __name__ == "__main__":
    reddit_sentiment_date()
    guardian_sentiment_date()
    nytimes_sentiment_date()