import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation


# https://scikit-learn.org/stable/auto_examples/applications/plot_topics_extraction_with_nmf_lda.html#sphx-
# glr-auto-examples-applications-plot-topics-extraction-with-nmf-lda-py
def get_top_words(model, feature_names, n_top_words) -> list:
    messages = []
    for topic_idx, topic in enumerate(model.components_):
        message = "Topic #%d: " % topic_idx
        message += " ".join([feature_names[i]
                             for i in topic.argsort()[:-n_top_words - 1:-1]])
        message += "\n"
        messages.append(message)
    return messages


def generate_topics(corpus: list):
    # vectorize all text
    tf_vectorizer = CountVectorizer(analyzer='word', stop_words='english')
    tf = tf_vectorizer.fit_transform(corpus)
    # fit using lda
    seed = 7
    n_topics = 10
    lda = LatentDirichletAllocation(n_components=n_topics, random_state=seed)
    topic = lda.fit(tf)
    # get topics and top words for each topic
    n_top_words = 20
    tf_feature_names = tf_vectorizer.get_feature_names()
    return get_top_words(lda, tf_feature_names, n_top_words)


def load_data(directory: str) -> list:
    # open file in directory
    with open(directory, 'r') as file:
        data = list(csv.reader(file, delimiter=','))
    # concatenate column 2 and 3, title and summary
    data = ["{} {}".format(line[2], line[3]) for line in data]
    # return a list of strings that are combines of title and summary
    return data


def main():
    # get data from each source
    reddit = load_data("../basic_analysis/reddit_data.csv")
    nytimes = load_data("../basic_analysis/nytimes_data.csv")
    guardian = load_data("../basic_analysis/guardian_data.csv")

    # generate topics for reddit
    print("Generate topics for reddit")
    reddit_topics = generate_topics(reddit)
    with open("../topic_modeling/topics_reddit.txt", 'w') as write_file:
        write_file.writelines(reddit_topics)

    # generate topics for nytimes
    print("Generate topics for nytimes")
    nytimes_topics = generate_topics(nytimes)
    with open("../topic_modeling/topics_nytimes.txt", 'w') as write_file:
        write_file.writelines(nytimes_topics)

    # generate topics for guardian
    print("Generate topics for guardian")
    guardian_topics = generate_topics(guardian)
    with open("../topic_modeling/topics_guardian.txt", 'w') as write_file:
        write_file.writelines(guardian_topics)

    # all text data
    all_text = []
    all_text.extend(reddit)
    all_text.extend(nytimes)
    all_text.extend(guardian)
    all_topics = generate_topics(all_text)
    print("Generate topics for all")
    with open("../topic_modeling/topics_all.txt", 'w') as write_file:
        write_file.writelines(all_topics)

    return


if __name__ == "__main__":
    main()
