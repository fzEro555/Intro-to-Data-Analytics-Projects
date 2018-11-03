

import pandas as pd
import numpy as np

class attribute_stats:
    #att_string is the variable that contains the attribute name
    #functions that make the statistics
    def mean(myDataframe, att_string):
        m = myDataframe[att_string].mean()
        with open('Stats.txt', 'a') as text_file:
            text_file.write("Mean for attribute: %s = %f \n" % (att_string,m))
    
    def median(myDataframe, att_string):
        m = myDataframe[att_string].median()
        with open('Stats.txt', 'a') as text_file:
            text_file.write("Median for attribute: %s = %f \n"% (att_string,m))
    
    def mode(myDataframe, att_string):
        m = myDataframe[att_string].mode()
        with open('Stats.txt', 'a') as text_file:
            text_file.write("Mode for attribute: %s = %s \n"% (att_string,m))
    
    def std(myDataframe, att_string):
        m = myDataframe[att_string].std()
        with open('Stats.txt', 'a') as text_file:
            text_file.write("Standard Deviation for attribute: %s = %f \n"% (att_string,m))
    
    
    def getResults(df1, df2):
        #for the news data
        att_string = ['number of titles for irma in reddit','number of titles for harvey in reddit','number of titles for maria in reddit',
                          'number of titles for irene in reddit','number of titles for irma in nytimes','number of titles for harvey in nytimes',
                          'number of titles for maria in nytimes','number of titles for irene in nytimes','number of contract for irma']
        with open('Stats.txt','w') as text_file:
            text_file.write("For the combined_data data: \n")
        for i in range(len(att_string)):
            attribute_stats.mean(df1,att_string[i])
            attribute_stats.median(df1,att_string[i])
            attribute_stats.std(df1,att_string[i])
        
        with open('Stats.txt','a') as text_file:
            text_file.write("For the FPDS data: \n")
        attribute_stats.mode(df2,att_string = 'Contracting Agency Name')
        
        
def main():
    news_data = pd.read_csv("./combined_data.csv")
    FPDS_data = pd.read_csv("./FPDS_final.csv")
    attribute_stats.getResults(news_data,FPDS_data)
    

if __name__ == "__main__":
    main()
