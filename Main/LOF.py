
import pandas as pd
import numpy as np
from sklearn.neighbors import LocalOutlierFactor

def LOF(myDataframe, k):
    #removing date attribute because that is irrelevant
    del myDataframe['date']
    clf = LocalOutlierFactor(n_neighbors=k, contamination=0.1)
    prediction = clf.fit_predict(myDataframe)
    Scores = clf.negative_outlier_factor_
    return (-Scores)

    
if __name__ == "__main__":
    news_data = pd.read_csv("./counts_combined.csv")
    #print(LOF(news_data, 20))
    #print(LOF(news_data,25))
    print(LOF(news_data,30))
    
    
