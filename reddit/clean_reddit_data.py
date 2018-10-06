#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 21:41:30 2018

@author: fz
"""

import numpy as np
import pandas as pd
import sys
from pprint import pprint

# Read in data directly into pandas

# Output for Part1

def nullratio():    
    # Read in data directly into pandas
    df = pd.read_csv('reddit_api_data.csv' , sep=',', encoding='latin1')
    percent_missing = df.isnull().sum() / len(df)
    missing_value_df = pd.DataFrame({
            'percent_missing': percent_missing})
    outputFile=open("reddit_Datacleanliness.txt", "a")
    missing_value_df.to_csv(outputFile)
    outputFile.close()

def invalidratio():
    df = pd.read_csv('reddit_api_data.csv' , sep=',', encoding='latin1')
    valuelist = ['[removed]','[deleted]']
    frameWithValues = df[df["Comment_Content"].isin(valuelist)]
    outputFile=open("reddit_Datacleanliness.txt", "a")
    outputFile.write("\n\nNumber of rows that have a comment content that has been deleted or removed\n")
    outputFile.write(format(len(frameWithValues)))
    outputFile.close()

def cleandata():
    df = pd.read_csv('reddit_api_data.csv' , sep=',', encoding='latin1')
    df = df[df.Comment_Content != '[removed]']
    df = df[df.Comment_Content != '[deleted]']
    myFileName="reddit_cleaned_data.csv"
    df.to_csv(myFileName)

    
if __name__ == "__main__":
    nullratio()
    invalidratio()
    cleandata()
'''   


 outputFile=open("output_hw2_part1.txt", "w")
    
    # Print first 10 rows
    outputFile.truncate()
    outputFile.write("Data Frame first ten rows\n")
    (myDataFrame[:10]).to_csv(outputFile)

    # Find the latitude and longitude for Annapolis, MD
    mdRows = myDataFrame["City, State"] == "Annapolis, MD"
    outputFile.write("\n\nThe latitude and longitude for Annapolis, MD\n")
    (myDataFrame[mdRows][['Latitude', 'Longitude']]).to_csv(outputFile)
    
    # Find the number of unique Latitude
    latitudeRows = pd.unique(myDataFrame["Latitude"].ravel())
    outputFile.write("\n\nUnique Latitude\n")
    outputFile.write(str(len(latitudeRows)))
    
    # Find the number of unique City, State
    cityRows = pd.unique(myDataFrame["City, State"].ravel())
    outputFile.write("\n\nUnique City, State\n")
    outputFile.write(str(len(cityRows)))
        
    # Find the number of unique Longitude
    longitudeRows = pd.unique(myDataFrame["Longitude"].ravel())
    outputFile.write("\n\nUnique Longitude\n")
    outputFile.write(str(len(longitudeRows)))

    # Find the number of unique Ratings
    ratingRows = pd.unique(myDataFrame["User Ratings"].ravel())
    outputFile.write("\n\nUnique User Ratings\n")
    outputFile.write(str(len(ratingRows)))
    
    # Find the number of rows that have a user rating that is not 5.
    valuelist = ['2','3','4','-200','a']
    frameWithValues = myDataFrame[myDataFrame["User Ratings"].isin(valuelist)]
    outputFile.write("\n\nNumber of rows that have a user rating that is not 5\n")
    outputFile.write(str(len(frameWithValues)))

    # Find the number of missing values in Latitude
    ratingCounts = myDataFrame['Latitude'].value_counts()
    outputFile.write("\n\nThe number of missing values in Latitude\n")
    outputFile.write(str(len(myDataFrame)-sum(ratingCounts)))
    
    # Find the number of missing values in City, State
    ratingCounts = myDataFrame['City, State'].value_counts()
    outputFile.write("\n\nThe number of missing values in City, State\n")
    outputFile.write(str(len(myDataFrame)-sum(ratingCounts)))
    
    # Find the number of missing values in Longitude
    ratingCounts = myDataFrame['Longitude'].value_counts()
    outputFile.write("\n\nThe number of missing values in Longitude\n")
    outputFile.write(str(len(myDataFrame)-sum(ratingCounts)))
    
    # Find the number of missing values in User Ratings
    ratingCounts = myDataFrame['User Ratings'].value_counts()
    outputFile.write("\n\nThe number of missing values in User Ratings\n")
    outputFile.write(str(len(myDataFrame)-sum(ratingCounts)))
    
    outputFile.close()
    
#####################
# Clean the data
#####################
def part2():
    # Read in data directly into pandas
    myDataFrame = pd.read_csv('data.csv' , sep=',', encoding='latin1')
    # Zip is an iterator in a pandas data frame. Lambda is an anonymous function
    # This code uses an anonymous function to split the 'City, State' cell into two data series
    # and assigns them to new columns in the data frame
    myDataFrame['City'], myDataFrame['State'] = zip(*myDataFrame['City, State'].apply(lambda x: x.split(',')))
    print("\n\nNew DataFrame columns")
    pprint(myDataFrame[:10])
    
    # Fix the upper and lower case
    myDataFrame["City, State"] = myDataFrame["City, State"].str.lower()
    print("\n\nLower Case")
    pprint(myDataFrame[:10])
    
    # Delete a column from a data frame
    # Delete column from DataFrame
    del myDataFrame['City, State']
    print("\n\nRemove column")
    pprint(myDataFrame[:10])
    
    #Drop rows with missing observations. Print to the screen the number of rows I dropped
    DataFrame=myDataFrame.dropna()
    print("\n\nNumber of rows dropped for missing observations")
    pprint(len(myDataFrame)-len(DataFrame))
    
    #Remove rows with invalid user rating. Print to the screen the number of rows I dropped 
    #and the City and State for that row (if available).
    myDataFrame=DataFrame.drop(29)
    DataFrame=myDataFrame.drop(79)
    print("\n\nNumber of rows dropped for invalid user rating")
    print("2")
    
    # Sort data by latitude and longitude. Print to the screen the first 10 sorted results.
    myDataFrame = DataFrame.sort_values(by=['Latitude','Longitude'],ascending=[1,0])
    pprint(myDataFrame[:10])
    
    # Write the data to a csv file and a text file
    myFileName="output_hw2_part2.csv"
    myDataFrame.to_csv(myFileName)
    
    myFileName="output_hw2_part2.txt"
    myDataFrame.to_csv(myFileName, sep="|")
    
if __name__ == "__main__":
    # execute only if run as a script
    part1()
    part2()

'''