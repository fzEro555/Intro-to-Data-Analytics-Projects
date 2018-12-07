from topic_modeling.topic_modeling import main as generate_topics
from topic_modeling.count_topics import main as count_topics
from topic_modeling.plot_topics_distribution import main as plot_topics_distribution
from sentiment_analysis.sentiment_analysis import main as sentiment_analysis
from sentiment_analysis.sentiment_analysis_date import main as sentiment_analysis_by_date
from sentiment_analysis.sent_overlaybar import main as sent_overlaybar
from sentiment_analysis.sent_piechart import main as sent_piechart
from Visualization.irene_LG import main as irene_longitude
from Visualization.irma_LG import main as irma_longitude
from Visualization.harvey_LG import main as harvey_longitude
from Visualization.maria_LG import main as maria_longitude
from Visualization.reddit_mentions import main as reddit_mentions
from Visualization.barchart_spending import barchart_amount as barchart_spending
from Visualization.bubbles_each_hurricane import bubblechart as bubblechart_for_each_hurricane
from Visualization.hypo2_plot import plot_hypo2


def main():
    # topic modeling and visualizations
    # generate_topics()
    count_topics()
    plot_topics_distribution()

    # sentiment analysis and visualization
    sentiment_analysis()
    sentiment_analysis_by_date()
    sent_overlaybar()
    sent_piechart()

    # other visualizations
    # longitude graphs displaying the number of mentions for each hurricane
    irene_longitude()
    irma_longitude()
    harvey_longitude()
    maria_longitude()
    # longitude graph of number of mentions in Reddit for the three hurricanes
    reddit_mentions()
    # bar char for spending
    barchart_spending()
    # bubble chart for each hurricane
    bubblechart_for_each_hurricane()
    # Hypothesis 2
    plot_hypo2()

    return


if __name__ == "__main__":
    main()
