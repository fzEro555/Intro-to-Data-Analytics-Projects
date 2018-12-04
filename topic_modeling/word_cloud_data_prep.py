import pandas


def count_total_for_each_topic(dataFrame: pandas.DataFrame) -> dict:
    # initialize dictionary
    article_count = {}
    # iterate through each column in data frame,
    # get column name and sum of counts
    column_names = list(dataFrame)
    for c_name in column_names[1:]:
        total = dataFrame[c_name].sum()
        article_count[c_name] = total
    return article_count


def main():
    with open("./topic_counts_for_reddit.json", 'w') as write_file:
        df = pandas.read_csv("./is_topic_reddit.csv")
        article_count = count_total_for_each_topic(df)
        write_file.write(str(article_count))

    with open("./topic_counts_for_nytimes.json", 'w') as write_file:
        df = pandas.read_csv("./is_topic_nytimes.csv")
        article_count = count_total_for_each_topic(df)
        write_file.write(str(article_count))

    with open("./topic_counts_for_guardian.json", 'w') as write_file:
        df = pandas.read_csv("./is_topic_guardian.csv")
        article_count = count_total_for_each_topic(df)
        write_file.write(str(article_count))

    return


if __name__ == "__main__":
    main()
