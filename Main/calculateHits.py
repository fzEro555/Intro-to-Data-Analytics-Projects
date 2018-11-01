import csv
import pandas as pd


def dateZone(date):
    dateList = ['2011-08-21', '2011-08-28', '2017-08-17', '2017-08-21',
                '2017-08-28', '2017-08-30', '2017-09-03', '2017-09-13']

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
    if date > dateList[4] and date < dateList[5]:
        return 1
    if date >= dateList[5] and date <= dateList[6]:
        return 2
    if date > dateList[6] and date <= dateList[7]:
        return 1
    if date > dateList[7]:
        return 0


def calhits(data):
    for index, row in data.iterrows():
        data['hitsCount'] = data.apply(lambda row: dateZone(row['date']), axis=1)


if __name__ == "__main__":
    data = pd.read_csv("./reddit.csv")

    calhits(data)
    data.to_csv("reddit.csv")