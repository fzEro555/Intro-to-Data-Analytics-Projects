import pandas
import numpy
import plotly
import plotly.plotly as py
from plotly.graph_objs import *


def get_sublist(period: tuple, data: pandas.DataFrame) -> tuple:
    topic_names = list(data)[1:]
    date_values = data['date'].values
    # find start and end index
    start_index = 0
    end_index = 0
    index = 0
    while index < len(date_values) and date_values[index] < period[0]:
        index += 1
    start_index = index
    while index < len(date_values) and date_values[index] <= period[1]:
        index += 1
    end_index = index
    # return sublist within range [start_index, end_index]
    sublist = data.values[start_index:end_index]
    return topic_names, sublist[:, 0], sublist[:, 1:]


# plot distribution of topics each day in a source during a hurricanes period
def plot_topic_distribution(period, data, source):
    # get sublist from data within period
    topic_names, date, value = get_sublist(period, data)
    # add 1 to each cell
    # value += 1
    # normalize each column
    # row_sums = value.sum(axis=1)
    # for i, (row, r_sum) in enumerate(zip(value, row_sums)):
    #     if r_sum == 0:
    #         # if a row is all 0, keep it at zero
    #         value[i, :] = row / 1
    #     else:
    #         # if a row is not all 0, all a small value to every element to avoid the situation where 1 topic is 100%
    #         value += 0.1
    #         value[i, :] = row / r_sum
    for i, row in enumerate(value):
        r_sum = row.sum()
        if r_sum == 0:
            # if a row is all 0, keep it at zero
            value[i, :] = row / 1
        else:
            # if a row is not all 0, all a small value to every element to avoid the situation where 1 topic is 100%
            new_row = row + 0.01
            r_sum = new_row.sum()
            value[i, :] = new_row / r_sum
    # plot
    traces = []
    n_topics = len(value[0])
    for i in range(n_topics):
        trace = {
            "x": date,
            "y": value[:, i],
            "name": "topic: {}".format(topic_names[i]),
            "type": "bar"
        }
        traces.append(trace)
    layout = {
        "title": "Topic distribution during time period \n{} -- {} from {}".format(period[0], period[1], source),
        "barmode": "stack",
        "dragmode": "zoom",
        "hovermode": "x"
    }
    fig = Figure(data=traces, layout=layout)
    py.plot(fig)
    return


def main():
    # read in data with pandas
    reddit = pandas.read_csv('../topic_modeling/is_topic_reddit.csv')
    nytimes = pandas.read_csv('../topic_modeling/is_topic_nytimes.csv')
    guardian = pandas.read_csv('../topic_modeling/is_topic_guardian.csv')

    # remove lines with only 0s
    # reddit = reddit.replace(0, numpy.nan).dropna(how='all', axis=0).replace(numpy.nan, 0)
    # nytimes = nytimes.replace(0, numpy.nan).dropna(how='all', axis=0).replace(numpy.nan, 0)
    # guardian = guardian.replace(0, numpy.nan).dropna(how='all', axis=0).replace(numpy.nan, 0)

    # set up plotly credentials
    plotly.tools.set_credentials_file(username='peuleupeu', api_key='ZWZ27kkaZcUtiHOpEZ3I')

    # plot 3 graphs for each period, one from each source
    # period_maria = ("2017-09-01", "2017-10-17")
    # plot_topic_distribution(period_maria, reddit, "reddit")
    # plot_topic_distribution(period_maria, nytimes, "nytimes")
    # plot_topic_distribution(period_maria, guardian, "guardian")
    #
    # period_harvey = ("2017-08-02", "2017-09-19")
    # plot_topic_distribution(period_harvey, reddit, "reddit")
    # plot_topic_distribution(period_harvey, nytimes, "nytimes")
    # plot_topic_distribution(period_harvey, guardian, "guardian")
    #
    # period_irma = ("2017-08-15", "2017-09-29")
    # plot_topic_distribution(period_irma, reddit, "reddit")
    # plot_topic_distribution(period_irma, nytimes, "nytimes")
    # plot_topic_distribution(period_irma, guardian, "guardian")
    #
    # period_irene = ("2011-08-06", "2011-09-12")
    # plot_topic_distribution(period_irene, reddit, "reddit")
    # plot_topic_distribution(period_irene, nytimes, "nytimes")
    # plot_topic_distribution(period_irene, guardian, "guardian")

    period_harvey = ("2017-08-02", "2017-10-09")
    plot_topic_distribution(period_harvey, reddit, "reddit")
    plot_topic_distribution(period_harvey, nytimes, "nytimes")
    plot_topic_distribution(period_harvey, guardian, "guardian")
    return


if __name__ == "__main__":
    main()
