import csv
import re


def count_topics(directory: str, topics: list, time_splitter: str):
    # process the topic list, compile each word for each topic into regex
    re_topics = []
    for t in topics:
        re_t = [re.compile(w, re.IGNORECASE) for w in t]
        re_topics.append(re_t)
    # read in nytimes
    with open(directory, 'r') as read_file:
        articles = list(csv.reader(read_file, delimiter=','))[1:]
    # iterate through all articles, determine if it is of each topic
    # [[date, is topic 1, is 2, 3 ,4, 5, ...]]
    topics_of_article = []
    for line in articles:
        # line 1: date, 2 title, 3 summary
        date = line[1].split(time_splitter)[0]
        # iterate through all words for that topic, determine if this articles is of each
        is_topcics = []
        for re_t in re_topics:
            n_words = 0.0  # number of words defining that topic appeared in articles and summary
            for re_w in re_t:
                if re_w.search(line[2]) is not None:
                    n_words += 1
                elif re_w.search(line[3]) is not None:
                    n_words += 1
            # if most of the words defining a topic appear in title and summary, this articles if of this topic
            if n_words/len(re_t) > 0.51:  # --- threshold --- #
                is_topcics.append(1)
            else:
                is_topcics.append(0)
        is_topcics.insert(0, date)
        topics_of_article.append(is_topcics)
    # aggregate for each day
    topics_on_day = {}
    for line in topics_of_article:
        if line[0] in topics_on_day:
            counts = topics_on_day[line[0]]
            for i, c in enumerate(counts[1:], start=1):
                counts[i] = c + line[i]
            # topics_on_day[line[0]] = counts
        else:
            topics_on_day[line[0]] = line
    topics_on_day = list(topics_on_day.values())
    # sort on date
    topics_on_day = sorted(topics_on_day, key=lambda line: line[0])
    return topics_on_day


def main():
    directory_reddit_data = "../basic_analysis/reddit_data.csv"
    # list of topics for reddit with words
    reddit_topics = [["climate", "change"],  # climate change
                     ["hurricanes", "people", "die"],  # impact
                     ["send", "help", "suppl", "food", "water"],  # send help
                     ["thread", "twitter", "reddit"],  # social media
                     ["trump", "president", "mexico"],  # politics
                     ["Puerto Rico", "Hurricane", "Maria", "government"]]  # maria
    # count topics for each and save
    topics_on_day = count_topics(directory_reddit_data, reddit_topics, ' ')
    topics_on_day.insert(0, ["date", "Climate Change", "Impact", "Send Help", "Social Media", "Politics", "Maria"])
    with open("../topic_modeling/is_topic_reddit.csv", 'w') as save_file:
        write = csv.writer(save_file, delimiter=',')
        write.writerows(topics_on_day)


    directory_nytimes_data = "../basic_analysis/nytimes_data.csv"
    # list of topics for nytimes with words
    nytimes_topics = [["climate", "change"],  # climate change
                      ["hurricane", "storm", "rain", "flood", "damage"],  # impact
                      ["profit", "business", "quarter"],  # business
                      ["hurricane", "warming", "nature", "scientists", "extreme"],  # global warming
                      ["shows", "awards", "dance", "article", "mtv"]]  # entertainment
    # count topics for each and save
    topics_on_day = count_topics(directory_nytimes_data, nytimes_topics, 'T')
    topics_on_day.insert(0, ["date", "Climate Change", "Impact", "Business", "Global Warming", "Entertainment"])
    with open("../topic_modeling/is_topic_nytimes.csv", 'w') as save_file:
        write = csv.writer(save_file, delimiter=',')
        write.writerows(topics_on_day)


    directory_guardian_data = "../basic_analysis/guardian_data.csv"
    # list of topics for guardian
    guardian_topics = [["climate", "change"],  # climate change
                       ["hurricane", "storm", "people", "child", "famil"],  # impact
                       ["Puerto Rico", "Hurricane", "Maria", "government"],  # maria
                       ["Hurricane", "Florence", "North Carolina", "Florida"],  # florence
                       ["film", "story", "book"],  # entertainment
                       ["brexit", "minister", "secretary", "labour", "government"],  # politics
                       ["Elizabeth", "Queen", "Edward"]]  # the Royal
    # count topics for each and save
    topics_on_day = count_topics(directory_guardian_data, guardian_topics, 'T')
    topics_on_day.insert(0, ["date", "Climate Change", "Impact", "Maria", "Florence", "Entertainment", "Politics", "The Royal"])
    with open("../topic_modeling/is_topic_guardian.csv", 'w') as save_file:
        write = csv.writer(save_file, delimiter=',')
        write.writerows(topics_on_day)
    return


if __name__ == "__main__":
    main()
