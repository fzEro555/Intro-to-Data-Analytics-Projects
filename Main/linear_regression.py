# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 16:57:53 2018

@author: subha
"""


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
  
def estimate_coef(x, y): 
    # number of observations/points 
    n = np.size(x) 
  
    # mean of x and y vector 
    m_x, m_y = np.mean(x), np.mean(y) 
  
    # calculating cross-deviation and deviation about x 
    SS_xy = np.sum(y*x - n*m_y*m_x) 
    SS_xx = np.sum(x*x - n*m_x*m_x) 
  
    # calculating regression coefficients 
    b_1 = SS_xy / SS_xx 
    b_0 = m_y - b_1*m_x 
  
    return(b_0, b_1) 
def plot_regression_line(x, y, b): 
    # plotting the actual points as scatter plot 
    plt.scatter(x, y, color = "m", 
               marker = "o", s = 30) 
    # predicted response vector 
    y_pred = b[0] + b[1]*x 
    # plotting the regression line 
    plt.plot(x, y_pred, color = "g") 
    # putting labels 
    plt.xlabel('x') 
    plt.ylabel('y') 
    # function to show plot 
    plt.show() 
    
def load_data():
    myData = pd.read_csv('./count_ranges.csv')
    # attributes in x are the predictors and y will be the response
    X = myData[['total_mentions']].values.reshape(-1,)
    #X.drop(X.index[[0]])
    Y = myData[['total_amount']].values.reshape(-1,)
    #Y.drop(Y.index[[0]])
    return X,Y  
  
if __name__ == "__main__": 
    # observations 
    X, Y = load_data()
    #splitting the dataset into train and test
    test_size = 0.20
    seed = 7
    X_train, X_validate, Y_train, Y_validate = train_test_split(X, Y, test_size=test_size, random_state=seed)
    # estimating coefficients 
    b = estimate_coef(X_train, Y_train) 
    print("Estimated coefficients:\nb_0 = {}  nb_1 = {}".format(b[0], b[1])) 
  
    # plotting regression line 
    plot_regression_line(X_train, Y_train, b) 