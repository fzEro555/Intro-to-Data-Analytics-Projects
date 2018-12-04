  # !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 21:36:03 2018

@author: fz
"""
import plotly

plotly.tools.set_credentials_file(username='fzEro555', api_key='Whlfx48mu0VA1EjW9GVL')
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd

# Maria
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


def stack_barchart_sentiment(data_frame: pd.core.frame.DataFrame, file_name

):
# Maria
df = data_frame
df1 = df[df["date"].isin(dateList1)]
data = [
    go.Bar(
        x=df1['date'],  # assign x as the dataframe column 'x'
        y=-df1['neg'],
        name='neg'
    ),
    go.Bar(
        x=df1['date'],
        y=df1['pos'],
        name='pos'
    )
]

layout = go.Layout(
    barmode='overlay',
    title='Overlay bar for ' + file_name + ' hurricane maria'
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename=file_name + ' for hurricane maria')

# Harvey
df2 = df[df["date"].isin(dateList2)]
data = [
    go.Bar(
        x=df2['date'],  # assign x as the dataframe column 'x'
        y=-df2['neg'],
        name='neg'
    ),
    go.Bar(
        x=df2['date'],
        y=df2['pos'],
        name='pos'
    )
]

layout = go.Layout(
    barmode='overlay',
    title='Overlay bar for ' + file_name + ' hurricane harvey'
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename=file_name + ' for hurricane harvey')

# Irma
df3 = df[df["date"].isin(dateList3)]
data = [
    go.Bar(
        x=df3['date'],  # assign x as the dataframe column 'x'
        y=-df3['neg'],
        name='neg'
    ),
    go.Bar(
        x=df3['date'],
        y=df3['pos'],
        name='pos'
    )
]

layout = go.Layout(
    barmode='overlay',
    title='Overlay bar for ' + file_name + ' hurricane irma'
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename=file_name + ' for hurricane irma')

# Irene
df4 = df[df["date"].isin(dateList4)]
data = [
    go.Bar(
        x=df4['date'],  # assign x as the dataframe column 'x'
        y=-df4['neg'],
        name='neg'
    ),
    go.Bar(
        x=df4['date'],
        y=df4['pos'],
        name='pos'
    )
]

layout = go.Layout(
    barmode='overlay',
    title='Overlay bar for ' + file_name + ' hurricane irene'
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename=file_name + ' for hurricane irene')

if __name__ == "__main__":
    # reddit
    df1 = pd.read_csv("reddit_sentiment_date.csv")
    stack_barchart_sentiment(df1, "reddit_sentiment_date.csv")

    # guardian
    df2 = pd.read_csv("guardian_sentiment_date.csv")
    stack_barchart_sentiment(df2, "guardian_sentiment_date.csv")

    # nytimes
    df3 = pd.read_csv("nytimes_sentiment_date.csv")
    stack_barchart_sentiment(df3, "nytimes_sentiment_date.csv")