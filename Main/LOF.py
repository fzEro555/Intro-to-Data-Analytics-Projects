
import pandas as pd
import numpy as np
from sklearn.neighbors import LocalOutlierFactor


def LOF(myDataframe, k):
    # removing date attribute because that is irrelevant
    del myDataframe['date']
    clf = LocalOutlierFactor(n_neighbors=k, contamination=0.1)
    prediction = clf.fit_predict(myDataframe)
    Scores = clf.negative_outlier_factor_
    return (-Scores)


def output(myDataframe, Scores):
    # printing the first 6 rows of outliers
    j = 0
    for i in range(len(myDataframe)):
        if Scores[i] > 4:
            print(myDataframe.loc[[i]])
            j = j+1
        if j==5:
            break


def clean(myDataframe, Scores):
    # deleting the outliers
    length = len(myDataframe)
    for i in range(0,length):
        if Scores[i] > 4:
            myDataframe.drop([i],axis=0, inplace=True)
    return myDataframe


def main():
    myData = pd.read_csv("./combined_data.csv")
    # selecting columns of interest
    cols_of_interest = ['date', 'number of titles for irma in reddit',
                        'number of titles for harvey in reddit',
                        'number of titles for maria in reddit',
                        'number of titles for irene in reddit',
                        'number of titles for irma in nytimes',
                        'number of titles for harvey in nytimes',
                        'number of titles for maria in nytimes',
                        'number of titles for irene in nytimes',
                        'number of titles for irma in guardian',
                        'number of titles for harvey in guardian',
                        'number of titles for maria in guardian',
                        'number of titles for irene in guardian']
    news_Data = myData[cols_of_interest]
    
    # should try different values of k
    Scores = LOF(news_Data,30) 
    # printing a few examples of outliers
    output(news_Data,Scores)
    # cleanup the outliers
    myData = clean(myData,Scores)
    # this should actually be our data file but I will not be overwriting our data
    # myData.to_csv('combined_data.csv')
    
    
if __name__ == "__main__":
    main()
