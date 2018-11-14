#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 21:41:30 2018

@author: fz
"""


import pandas as pd


# get the fraction value for each attributes.
def nullratio():
    # Read in data directly into pandas
    df = pd.read_csv('reddit_api_data.csv' , sep=',', encoding='latin1')
    percent_missing = df.isnull().sum() / len(df)
    missing_value_df = pd.DataFrame({
            'percent_missing': percent_missing})
    outputFile = open("reddit_Datacleanliness.txt", "a")
    missing_value_df.to_csv(outputFile)
    outputFile.close()


# get the fraction of noise in attribute Comment_Content
def invalidratio():
    df = pd.read_csv('reddit_api_data.csv' , sep=',', encoding='latin1')
    valuelist = ['[removed]','[deleted]']
    frameWithValues = df[df["Comment_Content"].isin(valuelist)]
    outputFile = open("reddit_Datacleanliness.txt", "a")
    outputFile.write("\n\nNumber of rows that have a comment content that has been deleted or removed\n")
    outputFile.write(format(len(frameWithValues)/len(df)))
    outputFile.close()


# delete the noise in Comment_Content
def cleandata():
    df = pd.read_csv('reddit_api_data.csv' , sep=',', encoding='latin1')
    df = df[df.Comment_Content != '[removed]']
    df = df[df.Comment_Content != '[deleted]']
    myFileName = "reddit_cleaned_data.csv"
    df.to_csv(myFileName)


if __name__ == "__main__":
    nullratio()
    invalidratio()
    cleandata()
