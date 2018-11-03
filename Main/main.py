
from reddit import reddit_api, clean_reddit_data
from reddit.process_reddit_data import process_reddit_data
from nytimes.search_api import search_articles as nytimes_data
from guardian.guardian_api import retrieve_articles as guardian_data
from fpds.process_fpds import process_fpds as fpds_data

from Main.count import count as count_mentions_in_news_and_reddit_data
from Main.combine_lean_data import combine as combine_counts_from_news_and_reddit_data

from Main.attribute_stats import main as statistical_analysis
from Main.LOF import main as lof
from Main.binning import main as binning
from Main.histograms import main as histogram_and_correlations
from Main.clustering import main as clustering
from Main.association_rules import main as association_rules

from hypothesis_testing.decision_tree import main as decision_tree_and_random_forest
from hypothesis_testing.anova import main as anova
from hypothesis_testing.knn import main as knn
from hypothesis_testing.svm import main as svm
from hypothesis_testing.freq_spend import main as prepare_data_for_naive_bayes_and_linear_regression
from hypothesis_testing.naive_bayes import main as naive_bayes
from hypothesis_testing.linear_regression import main as linear_regression


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
    count_mentions_in_news_and_reddit_data()
    combine_counts_from_news_and_reddit_data()
    return


# include all the hypothesis testing part
def hypothesis_testing():
    print("\n\n===================={}================================\n".format("H1: Decision Tree, Random Forest"))
    # hypothesis 1: predict level of hurricane
    # methods used: decision tree, random forest
    decision_tree_and_random_forest()

    print("\n\n===================={}================================\n".format("H2: ANOVA, KNN, SVM"))
    # hypothesis 2: storm hits
    # methods used: anova, knn, svm
    anova()
    knn()
    svm()

    print("\n\n===================={}================================\n".format("H3: Naive Bayes, Linear Regression"))
    # hypothesis 3: government spending
    # methods used: naive bayes, linear regression
    prepare_data_for_naive_bayes_and_linear_regression()
    naive_bayes()
    linear_regression()
    return


if __name__ == "__main__":
    # # getting and process data
    # get_and_process_data()

    # # extract counts and other information useful for tasks for project 2
    # # including counting, combining and reshaping the data, etc
    # further_processing()

    # statistical analysis
    print("\n\n===================={}================================\n".format("Statistical Analysis"))
    statistical_analysis()

    # identify outliers (LOF) and remove them
    print("\n\n===================={}================================\n".format("LOF"))
    lof()

    # binning
    print("\n\n===================={}================================\n".format("Binning"))
    binning()

    # histogram and correlations
    print("\n\n===================={}================================\n".format("Histogram and Correlations"))
    histogram_and_correlations()

    # clustering analysis
    print("\n\n===================={}================================\n".format("Clustering Analysis"))
    clustering()

    # association rules
    print("\n\n===================={}================================\n".format("Association Rules"))
    association_rules()

    # predictive analysis, hypothesis testing
    hypothesis_testing()

    # input("any")
