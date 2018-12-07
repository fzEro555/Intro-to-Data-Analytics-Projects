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
        "hovermode": "x",
        "xaxis": dict(title='Time'),
        "yaxis": dict(title='Distribution of topics')
    }
    fig = Figure(data=traces, layout=layout)
    plotly.offline.plot(fig,
                        filename=
                        "Topic distribution during time period <br> {} -- {} from {}".format(period[0], period[1], source),
                        auto_open=True)
    return


def main():
    # read in data with pandas
    reddit = pandas.read_csv('../topic_modeling/is_topic_reddit.csv')
    nytimes = pandas.read_csv('../topic_modeling/is_topic_nytimes.csv')
    guardian = pandas.read_csv('../topic_modeling/is_topic_guardian.csv')

    # set up plotly credentials
    plotly.tools.set_credentials_file(username='peuleupeu', api_key='ZWZ27kkaZcUtiHOpEZ3I')

    # plot topic distribution
    period_harvey = ("2017-08-02", "2017-10-09")
    plot_topic_distribution(period_harvey, reddit, "Reddit")
    plot_topic_distribution(period_harvey, nytimes, "New York Times")
    plot_topic_distribution(period_harvey, guardian, "The Guardian")
    return


if __name__ == "__main__":
    main()
