﻿  # !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 22:28:11 2018

@author: fz
"""

import plotly

plotly.tools.set_credentials_file(username='fzEro5', api_key='JW2fEOORvG6eByCT2TfG')
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import cufflinks as cf

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


def bubblechart():
    # cf.set_config_file(offline=True, world_readable=True, theme='pearl')
    df = pd.read_csv("../basic_analysis/combined_data.csv", sep=',')

    # Maria
    df1 = df[df["date"].isin(dateList1)]
    sizeref = 2. * max(df1['amount for maria']) / (100 ** 2)

    trace0 = go.Scatter(
        x=df1['date'],
        y=df1['number of contract for maria'],
        text=df1['amount for maria'],
        mode='markers',
        marker=dict(
            size=df1['amount for maria'],
            sizeref=sizeref,
            sizemode='area',
            color='rgb(255, 144, 14)'
            # sizemin=4
        )
    )
    data = [trace0]
    layout = go.Layout(
        xaxis=dict(
            title='date',

        ),
        yaxis=dict(
            title='number of cantracts for maria',

        ),
        title='amount spent for hurricane maria'
    )
    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig, filename='bubble for maria', auto_open=True)
    # Harvey
    df2 = df[df["date"].isin(dateList2)]
    sizeref = 2. * max(df2['amount for harvey']) / (100 ** 2)

    trace0 = go.Scatter(
        x=df2['date'],
        y=df2['number of contract for harvey'],
        text=df2['amount for harvey'],
        mode='markers',
        marker=dict(
            size=df2['amount for harvey'],
            sizeref=sizeref,
            sizemode='area',
            color='rgb(93, 164, 214)'
            # sizemin=4
        )
    )
    data = [trace0]
    layout = go.Layout(
        xaxis=dict(
            title='date',

        ),
        yaxis=dict(
            title='number of cantracts for harvey',

        ),
        title='amount spent for hurricane harvey'
    )
    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig, filename='bubble for harvey', auto_open=True)

    # Irma
    df3 = df[df["date"].isin(dateList3)]
    sizeref = 2. * max(df3['amount for irma']) / (100 ** 2)

    trace0 = go.Scatter(
        x=df3['date'],
        y=df3['number of contract for irma'],
        text=df3['amount for irma'],
        mode='markers',
        marker=dict(
            size=df3['amount for irma'],
            sizeref=sizeref,
            sizemode='area',
            color='rgb(44, 160, 101)'
            # sizemin=4
        )
    )
    data = [trace0]
    layout = go.Layout(
        xaxis=dict(
            title='date',

        ),
        yaxis=dict(
            title='number of cantracts for irma',

        ),
        title='amount spent for hurricane irma'
    )
    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig, filename='bubble for irma', auto_open=True)

    # Irene
    df4 = df[df["date"].isin(dateList4)]

    sizeref = 2. * max(df4['amount for irene']) / (100 ** 2)

    trace0 = go.Scatter(
        x=df4['date'],
        y=df4['number of contract for irene'],
        text=df4['amount for irene'],
        mode='markers',
        marker=dict(
            size=df4['amount for irene'],
            sizeref=sizeref,
            sizemode='area',
            color='rgb(255, 65, 54)'
            # sizemin=4
        )
    )
    data = [trace0]
    layout = go.Layout(
        xaxis=dict(
            title='date',

        ),
        yaxis=dict(
            title='number of cantracts for irene',

        ),
        title='amount spent for hurricane irene'
    )
    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig, filename='bubble for irene', auto_open=True)


if __name__ == "__main__":
    bubblechart()
