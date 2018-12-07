from topic_modeling.topic_modeling import main as generate_topics
from topic_modeling.count_topics import main as count_topics
from topic_modeling.plot_topics_distribution import main as plot_topics_distribution

def main():
    # topic modeling and visualizations
    generate_topics()
    count_topics()
    plot_topics_distribution()

    # sentiment analysis and visualization

    return


if __name__ == "__main__":
    main()
