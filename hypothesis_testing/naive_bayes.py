# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 17:33:19 2018

@author: subha
"""
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import numpy as np
import pandas as pd


def naive_bayes(X, Y):
    #Create a Gaussian Classifier
    model = GaussianNB()
    # Train the model using the training sets 
    model.fit(X, Y)
    return model

def confusionMatrix(predict,actual):
    df_confusion = confusion_matrix(actual, predict)
    print(df_confusion)

def load_data():
    myData = pd.read_csv('./count_ranges.csv')
    # attributes in x are the predictors and y will be the response
    X = myData[['irma_count','harvey_count','maria_count','irene_count']]
    max_amount = myData['total_amount'].max() - myData['total_amount'].min()
    myData['amount_range'] = myData['total_amount'].apply(lambda x: '-1.0' 
        if x < max_amount/71 else '1.0')
    Y = myData[['amount_range']].values.reshape(-1,)
    #we use the numerical data to predict but we validate using the text data
    return X,Y
    

def main():
    X, Y = load_data()
    #splitting the dataset into train and test
    test_size = 0.20
    seed = 7
    X_train, X_validate, Y_train, Y_validate = train_test_split(X, Y, test_size=test_size, random_state=seed)
    #training the model
    model = naive_bayes(X_train,Y_train)
    #Predict Output 
    Y_predict= model.predict(X_validate)
    #print ()
    print("The confusion matrix will be: ")
    confusionMatrix(Y_predict,Y_validate)


if __name__ == "__main__":
    main()
