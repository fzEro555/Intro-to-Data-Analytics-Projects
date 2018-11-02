import csv

from reddit import reddit_api, clean_reddit_data
from reddit.process_reddit_data import process_reddit_data
from nytimes.search_api import search_articles as nytimes_data
from guardian.guardian_api import retrieve_articles as guardian_data
from fpds.process_fpds import process_fpds as fpds_data

from Main.count import count

from Main.combine_lean_data import combine

from hypothesis_testing.decision_tree import main as decision_tree__and_random_forest
from hypothesis_testing.knn import main as knn


def get_and_process_data():
    # reddit data
    print("Getting and processing reddit data. ")
    reddit_api.extractdata()
    clean_reddit_data.nullratio()
    clean_reddit_data.invalidratio()
    clean_reddit_data.cleandata()
    process_reddit_data()
    # nytimes data
    print("Getting and processing nytimes data. ")
    nytimes_data()
    # guardian data
    print("Getting and processing guardian data. ")
    guardian_data()
    # FPDS data
    print("Processing FPDS data. ")
    fpds_data()
    return


def hypothesis_testing():
    # hyp1 predict level of hurricane, decision tree, random forest
    decision_tree__and_random_forest()
    # hyp2 storm hits, anova, knn, svm
    knn()
    # hyp3 government spending, naive bayes, linear regression

    return


if __name__ == "__main__":
    # getting and process data
    get_and_process_data()

    count()
    combine()

    # statistical analysis

    # identify outliers (LOF) and remove them

    # binning

    # histogram and correlations

    # clustering analysis

    # association rules

    # predictive analysis

    # hypothesis testing
    hypothesis_testing()

    # input("any")
