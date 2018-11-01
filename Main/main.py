import csv

from reddit import reddit_api, clean_reddit_data
from reddit.process_reddit_data import process_reddit_data
from nytimes.search_api import search_articles as nytimes_data
from guardian.guardian_api import retrieve_articles as guardian_data
from fpds.process_fpds import process_fpds as fpds_data

from Main.combine_lean_data import combine


def reddit_data():
    reddit_api.extractdata()
    clean_reddit_data.nullratio()
    clean_reddit_data.invalidratio()
    clean_reddit_data.cleandata()
    process_reddit_data()
    return


if __name__ == "__main__":
    # reddit_data()
    # nytimes_data()
    # guardian_data()
    # fpds_data()

    combine()

    # input("any")
