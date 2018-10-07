# AMQS
Intro to Data Analytics Project 1


Reddit (./reddit)
 - reddit_api.py
        - gets data from reddit
 - reddit_api_data.csv
        - raw data collected
 - clean_reddit_data.py
        - cleans raw data
 - reddit_Datacleanliness.txt
        - cleaning info, missing value fraction and invalid value fractions
 - reddit_cleaned_data.csv
        - cleaned data

FPDS - NG Data(./FPDS-NG)
 - The data is downloadable from https://www.fpds.gov/fpdsng_cms/index.php/en/
       -  The data needs to be copied into the ./FPDS-NG folder
 - The data we downloaded has been added and named:
       - Hurricane_Harvey_Report.xlsx
       - Hurricane_Irma_Report.xlsx
       - Hurricane_Maria_Report.xlsx
 - main.py
       - runs entire program
 - OneDataFrame.py
        - combines data from three separate files into one dataframe
 - Cleaning.py
        - removes irrelevant columns and removes columns which are needed to preserve privacy and rows with
 - FPDS_final.csv
        - final, cleaned data

News: 

NYTimes: (./nytimes)
 - archive_api.py
        - retrieves all news within a certain time period, the data is stored as json files
 - nytimes_cleaning.py
        - cleans the data, including extracting the news id, time stamp, count the number of appearance of words in headlines and snippets, cleaned data is stored as a csv file
 - nytimes_cleaned.csv
        - cleaned data generated by nytimes_cleaning.py
 - search_api.py
        - the api that retrieves news using queries (not used in the project)


The Guardian: (./guardian)
 - the_guardian_api.py
        - retrieves all news with a certain time period, the data is stored as json files
 - the_guardian_cleaning.py
        - cleans the data, including extracting time stamp, count the number of appearance of words in headlines and body text
 - the_guardian_cleaning.csv
        - cleaned data generated by the_guardian_cleaning.py

Further cleaning: (./news_further_cleaning)
 - news_extract.py
        - extract from the cleaned files those whose word counts are not all zeros, results are stored in csv files (nytimes_lean.csv and the_guardian_lean.csv)
 - news_ratio.py
        - count the number of instances in the cleaned data files and the lean data files, number of news that mention each of the selected words
 - nytimes_lean.csv
        - nytimes news with word counts that are not all zeros
 - the_guardian_lean.csv
        - the guardian news with word counts that are not all zeros
 - nytimes_count.txt
        - count and ratio information of nytimes news generated by news_ratio.py
 - the_guardian_count.txt
        - count and ratio information of the guardian news generated by news_ratio.py

