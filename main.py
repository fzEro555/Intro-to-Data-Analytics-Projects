from topic_modeling.topic_modeling import main as generate_topics
from topic_modeling.count_topics import main as count_topics
from topic_modeling.plot_topics_distribution import main as plot_topics_distribution

from Visualization.irene_LG import main as irene_longitude
from Visualization.irma_LG import main as irma_longitude
from Visualization.harvey_LG import main as harvey_longitude
from Visualization.maria_LG import main as maria_longitude
from Visualization.reddit_mentions import main as reddit_mentions

from Visualization.hypo2_plot import plot_hypo2


def main():
    # topic modeling and visualizations
    generate_topics()
    count_topics()
    plot_topics_distribution()

    # sentiment analysis and visualization

    # other visualizations
    # longitude graphs displaying the number of mentions for each hurricane
    irene_longitude()
    irma_longitude()
    harvey_longitude()
    maria_longitude()
    # longitude graph of number of mentions in Reddit for the three hurricanes
    reddit_mentions()
    # Hypothesis 2
    plot_hypo2()op
    return


if __name__ == "__main__":
    main()
