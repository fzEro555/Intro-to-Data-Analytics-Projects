import csv
import matplotlib.pyplot as plt
import pandas as pd


def plot_variables(data):
    # Basic plotting - boxplot of entire dataframe
    plt.style.use = 'default'
    data.boxplot()
    plt.title("Box plots of all variables in data set")
    plt.show()
    # plt.savefig('boxPlot.png')
    # Basic plotting - histogram of entire dataframe

    data.hist()
    plt.title("Distribution of different variables")
    plt.show()
    return


def plot_correlarion(data):
    # data = pd.read_csv("counts_combined.csv")
    # The following will create a collection of subplots
    # that are histograms for each variable by nytimes count hurricane
    VariableList = ["nytimes count irma", "nytimes count harvey", "nytimes count maria"]
    # print(VariableList)
    for var in VariableList:
        name = "nytimes_Graph_for_" + var

        data[var].hist(by=data['nytimes count hurricane'])
        pl.suptitle("Histograms by nytimes count hurricane for " + var)
        plt.savefig(name)
        plt.clf()
        plt.show()
        plt.close()
    return

'''
# plot histograms
def plot_histograms(data):
    plt.figure(0)
    plt.hist([line[1] for line in data])
    # add subplot for hurricane in nytimes
    plt.figure(1)
    plt.hist([line[5] for line in data])
    # add subplot for hurricane in guardian
    plt.figure(2)
    plt.hist([line[9] for line in data])
    # show
    plt.show()
    return


# plot histograms
def plot_histogram(data):
    # create a figure
    fig = plt.figure()
    # add subplot for hurricane in reddit
    fig.add_subplot(131)
    plt.hist([line[1] for line in data])
    # add subplot for hurricane in nytimes
    fig.add_subplot(132)
    plt.hist([line[5] for line in data])
    # add subplot for hurricane in guardian
    fig.add_subplot(133)
    plt.hist([line[9] for line in data])
    # show
    plt.show()
    return
'''

def main():
    # with open("./counts_combined.csv", 'r') as combined_file:
    #     reader = csv.reader(combined_file, delimiter=',')
    #     combined = list(reader)
    #
    # plot_histograms(combined[1:])

    data = pd.read_csv("counts_combined.csv")

    plot_variables(data)
    plot_correlarion(data)
    # input("any key")


if __name__ == "__main__":
    main()
