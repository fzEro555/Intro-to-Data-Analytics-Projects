import csv
import pandas as pd
from scipy import stats
from scipy.stats import levene

def dateZone(date):
    dateList = ['2011-08-21', '2011-08-28', '2017-08-17', '2017-08-30',
                '2017-09-03', '2017-09-13', '2017-09-16', '2017-10-02']

    if date < dateList[0]:
        return 0
    if date >= dateList[0] and date <= dateList[1]:
        return 1
    if date > dateList[1] and date < dateList[2]:
        return 0
    if date >= dateList[2] and date < dateList[3]:
        return 1
    if date >= dateList[3] and date <= dateList[4]:
        return 2
    if date > dateList[4] and date <= dateList[5]:
        return 1
    if date > dateList[5] and date < dateList[6]:
        return 0
    if date >= dateList[6] and date <= dateList[7]:
        return 1
    if date > dateList[7]:
        return 0


def hurricaneTime(date):
    datelist = ['2011-08-21', '2011-08-28', '2017-08-17', '2017-08-30',
                '2017-09-03', '2017-09-13', '2017-09-16', '2017-10-02']
    if date >= datelist[0] and date <= datelist[1]:
        return 'Irene'
    if date >= datelist[2] and date < datelist[3]:
        return 'Harvey'
    if date >= datelist[3] and date <= datelist[4]:
        return 'Harvey, Irma'
    if date > datelist[4] and date <= datelist[5]:
        return 'Irma'
    if date >= datelist[6] and date <= datelist[7]:
        return 'Maria'


def calhits(data):
    for index, row in data.iterrows():
        data['hitsCount'] = data.apply(lambda row: dateZone(row['date']), axis=1)


def hurricaneName(data):
    for index, row in data.iterrows():
        data['hurricaneName'] = data.apply(lambda row: hurricaneTime(row['date']), axis=1)


def anova(data):
    data1 = data[data['hurricaneName'].str.contains('Harvey', na=False)]['number of titles for harvey']
    data2 = data[data['hurricaneName'].str.contains('Irma', na=False)]['number of titles for irma']
    args = [data1, data2]
    f, p = stats.f_oneway(*args)
    # do levene test , the result is ﻿LeveneResult(statistic=3.003859284143726, pvalue=0.09589834933076798)
    # p is bigger than 0.05
    print(levene(data1, data2))
    # result is ﻿   0.8119993264991475 0.3764839982630388, so the hypothesis is correct.
    print(f, p)


def main():
    data = pd.read_csv("reddit_anova.csv")
    anova(data)


if __name__ == "__main__":
    main()
