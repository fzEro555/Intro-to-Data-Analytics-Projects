import csv
import matplotlib.pyplot as plt
import pandas as pd


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


if __name__ == "__main__":
    # with open("./counts_combined.csv", 'r') as combined_file:
    #     reader = csv.reader(combined_file, delimiter=',')
    #     combined = list(reader)
    #
    # plot_histograms(combined[1:])

    data = pd.read_csv("./counts_combined.csv")

    # input("any key")
