
from reddit import reddit_api, clean_reddit_data
from reddit.process_reddit_data import process_reddit_data
from nytimes.search_api import search_articles as nytimes_data
from guardian.guardian_api import retrieve_articles as guardian_data
from fpds.process_fpds import process_fpds as fpds_data

from Main.count import count
from Main.combine_lean_data import combine

from Main.attribute_stats import main as statistical_analysis
from Main.LOF import main as lof
from Main.binning import main as binning
from Main.histograms import main as histogram_and_correlations
from Main.association_rules import main as association_rules

from hypothesis_testing.decision_tree import main as decision_tree__and_random_forest
from hypothesis_testing.anova import main as anova
from hypothesis_testing.knn import main as knn
from hypothesis_testing.svm import main as svm
from hypothesis_testing.naive_bayes import main as naive_bayes


# get and process data from all four sources, reddit, nytimes, guardian, fpds
def get_and_process_data():
    # reddit data
    reddit_api.extractdata()
    clean_reddit_data.nullratio()
    clean_reddit_data.invalidratio()
    clean_reddit_data.cleandata()
    process_reddit_data()
    # nytimes data
    nytimes_data()
    # guardian data
    guardian_data()
    # FPDS data
    fpds_data()
    return


def further_processing():
    count()
    combine()
    return


# include all the hypothesis testing part
def hypothesis_testing():
    # hypothesis 1: predict level of hurricane
    # methods used: decision tree, random forest
    decision_tree__and_random_forest()
    # hypothesis 2: storm hits
    # methods used: anova, knn, svm
    anova()
    knn()
    svm()
    # hypothesis 3: government spending
    # methods used: naive bayes, linear regression
    naive_bayes()
    return


if __name__ == "__main__":
    # getting and process data
    get_and_process_data()

    # extract counts and other information useful for tasks for project 2
    # including counting, combining and reshaping the data, etc
    further_processing()

    # statistical analysis
    statistical_analysis()

    # identify outliers (LOF) and remove them
    lof()

    # binning
    binning()

    # histogram and correlations
    histogram_and_correlations()

    # clustering analysis

    # association rules
    association_rules()

    # predictive analysis, hypothesis testing
    hypothesis_testing()

    # input("any")
