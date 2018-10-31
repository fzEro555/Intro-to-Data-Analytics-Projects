# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 12:32:04 2018

@author: subha
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from apyori import apriori

def cleanup(myDataframe):
    myDataframe.drop(myDataframe.columns[[0]], axis = 1, inplace = True)
    #we remove all the columns which are uninteresting for association rules
    newDataframe = myDataframe[['Contracting Agency Name','Vendor Address State Name',
               'National Interest Action']].copy()
    return newDataframe

def make_list(myDataframe):
    #we convert the data into a list of lists as required by apyori library
    myDataframe = cleanup(myDataframe)
    records = []  
    for i in range(len(myDataframe)):  
        records.append([str(myDataframe.values[i,j]) for j in range(0, 3)])
    return records

def association_rules(myDataframe,min_sup,min_conf,min_l,min_len):
    records = make_list(myDataframe)
    association_rules = apriori(records, min_support=min_sup, min_confidence=min_conf, 
                            min_lift=min_l, min_length=min_len)  
    association_results = list(association_rules) 
    return association_results

if __name__ == "__main__":
    myData = pd.read_csv('FPDS_final.csv')
    association_results = association_rules(myData,0.005,0.1,2,3)
    for item in association_results:
        pair = item[0] 
        items = [x for x in pair]
        print("Rule: " + items[0] + " -> " + items[1])
        print("Support: " + str(item[1]))
        print("Confidence: " + str(item[2][0][2]))
        print("----------------------------------------------------")
    