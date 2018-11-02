# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 17:47:01 2018

@author: subha
"""

import numpy as np
import pandas as pd

#making simpler, more relevant columns
def new_columns(myData):
    myData['irma_count'] = (myData['number of titles for irma in reddit'] 
                            + myData['number of titles for irma in nytimes']
                            +myData['number of titles for irma in guardian'])
    myData['harvey_count'] = (myData['number of titles for harvey in reddit'] 
                            + myData['number of titles for harvey in nytimes']
                            +myData['number of titles for harvey in guardian'])
    myData['maria_count'] = (myData['number of titles for maria in reddit'] 
                            + myData['number of titles for maria in nytimes']
                            +myData['number of titles for maria in guardian'])
    myData['irene_count'] = (myData['number of titles for irene in reddit'] 
                            + myData['number of titles for irene in nytimes']
                            +myData['number of titles for irene in guardian'])
    myData['total_mentions'] = (myData['irma_count'] + myData['harvey_count'] 
                               + myData['irene_count'] + myData['maria_count'])
    myData['total_amount'] = (myData['amount for irma'] + myData['amount for harvey']
                            + myData['amount for maria'] + myData['amount for irene'])
    newData = myData[['date','irma_count','harvey_count','maria_count','irene_count',
                     'total_mentions','total_amount']]
    return newData
    
def labels(myData):
    range_irma = myData['irma_count'].max() - myData['irma_count'].min()
    range_harvey = myData['harvey_count'].max() - myData['harvey_count'].min()
    range_maria = myData['maria_count'].max() - myData['maria_count'].min()
    range_irene = myData['irene_count'].max() - myData['irene_count'].min()
    range_mentions = myData['total_mentions'].max() - myData['total_mentions'].min()
    myData['irma_range'] = 0
    myData['harvey_range'] = 0
    myData['irene_range'] = 0
    myData['maria_range'] = 0
    myData['mentions_range'] = 0
    for i in range(0, len(myData)):
        #changing the integer values to indicative ranges
        myData['irma_range'] = myData['irma_count'].apply(lambda x: 'low' 
              if x < range_irma/3 else ('medium') if x<2*range_irma/3 else 'high')
        myData['harvey_range'] = myData['harvey_count'].apply(lambda x: 'low' 
              if x < range_harvey/3 else ('medium') if x<2*range_harvey/3 else 'high')
        myData['maria_range'] = myData['maria_count'].apply(lambda x: 'low' 
              if x < range_maria/3 else ('medium') if x<2*range_maria/3 else 'high')
        myData['irene_range'] = myData['irene_count'].apply(lambda x: 'low' 
              if x < range_irene/3 else ('medium') if x<2*range_irene/3 else 'high')
        myData['mentions_range'] = myData['total_mentions'].apply(lambda x: 'low' 
              if x < range_mentions/2 else 'high')
    newData = myData[['irma_range','harvey_range','irene_range','maria_range'
                          ,'mentions_range','total_amount']]
    return newData
    



if __name__ == "__main__":
    myData = pd.read_csv('./combined_data.csv')
    newData = new_columns(myData)
    newData = labels(newData)
    newData.to_csv('count_ranges.csv')
    
    