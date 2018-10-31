import csv

from Main.extract_reddit import leanify_reddit as process_reddit
from Main.combine_lean_data import combine_lean_data

from reddit import reddit_api, clean_reddit_data
from reddit.process_reddit_data import process_reddit_data

from nytimes.search_api import search_articles

from guardian.guardian_api import retrieve_articles

from fpds.process_fpds import process_fpds

def reddit_data():
    # reddit_api.extractdata()
    # clean_reddit_data.nullratio()
    # clean_reddit_data.invalidratio()
    # clean_reddit_data.cleandata()
    # process_reddit_data()
    return


def nytimes_data():
    # search_articles()
    return


def guardian_data():
    # retrieve_articles()
    return


def fpds_data():
    process_fpds()
    return


def combine():

    return


if __name__ == "__main__":
    reddit_data()
    nytimes_data()
    guardian_data()
    fpds_data()

    combine()

    # # process reddit data
    # reddit_clean = "../reddit/reddit_cleaned_data.csv"
    # process_reddit(reddit_clean, "../reddit/reddit_lean.csv")
    #
    # # combine all data together, and aggregate data for each day
    # reddit_lean = "../reddit/reddit_lean.csv"
    # nytimes_lean = "../news_further_cleaning/nytimes_lean.csv"
    # guardian_lean = "../news_further_cleaning/the_guardian_lean.csv"
    # with open(reddit_lean, 'r') as reddit:
    #     with open(nytimes_lean, 'r') as nytimes:
    #         with open(guardian_lean, 'r') as guardian:
    #             combined = combine_lean_data(reddit, nytimes, guardian)
    #
    # # save combined data into csv
    # with open("./counts_combined.csv", 'w') as combined_save:
    #     writer = csv.writer(combined_save, delimiter=',')
    #     writer.writerows(combined)



