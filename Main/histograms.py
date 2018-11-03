﻿import csv
import matplotlib.pyplot as plt
import pandas as pd


def plot_variables(data):
    # Basic plotting - boxplot of entire dataframe
    plt.style.use = 'default'
    data = data[['number of titles for irma in reddit', 'number of summaries for irma in reddit',
                 'number of titles for harvey in reddit', 'number of summaries for harvey in reddit']]
    data.boxplot()
    plt.title("Box plots of 4 variables in data set")
    plt.show()
    # plt.savefig('boxPlot.png')
    # Basic plotting - histogram of entire dataframe

    data.hist()
    plt.title("Distribution of different variables")
    plt.show()
    return


def plot_correlation(data):
    data = data[data['hurricane name'].str.contains('Irma|Harvey', na=False)]

    data = data[['number of titles for irma in reddit', 'number of summaries for irma in reddit',
                 'number of titles for harvey in reddit', 'number of summaries for harvey in reddit']]

    # The following will create a collection of subplots
    # that are histograms for each variable by age group

    VariableList = ["number of titles for irma in reddit"]
    # print(VariableList)
    for var in VariableList:
        name = "reddit_irma_summaries_Graph_for_" + var

        data[var].hist(by=data['number of summaries for irma in reddit'])
        pl.suptitle("Histograms by number of summaries for irma in reddit for " + var)
        plt.savefig(name)
        plt.clf()
        plt.show()
        plt.close()
        return


# scatter plot
def scatter_plot(data):
    data = data[data['hurricane name'].str.contains('Irma|Harvey', na=False)]

    data = data[['number of titles for irma in reddit', 'number of summaries for irma in reddit',
                 'number of titles for harvey in reddit', 'number of summaries for harvey in reddit']]

    plt.scatter(data['number of titles for irma in reddit'], data['number of summaries for irma in reddit'])
    plt.scatter(data['number of titles for harvey in reddit'], data['number of summaries for harvey in reddit'])
    # plt.scatter(data['nytimes count maria'], data['nytimes count harvey'])
    return


if __name__ == "__main__":
    # with open("./counts_combined.csv", 'r') as combined_file:
    #     reader = csv.reader(combined_file, delimiter=',')
    #     combined = list(reader)
    #
    # plot_histograms(combined[1:])

    data = pd.read_csv("combined_data.csv")

    plot_variables(data)
    scatter_plot(data)
    plot_correlation(data)
    # input("any key")
