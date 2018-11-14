import re
import csv
import pandas as pd
from hypothesis_testing.anova import calhits
from hypothesis_testing.anova import hurricaneName


def tally(ll, title, summary, r_irma, r_harvey, r_maria, r_irene, r_hurricane):
    # check title if it mentions each hurricane
    if r_irma.search(title):
        ll[1] += 1
    if r_harvey.search(title):
        ll[2] += 1
    if r_maria.search(title):
        ll[3] += 1
    if r_irene.search(title):
        ll[4] += 1
    # check summary if it mentions each hurricane
    if r_irma.search(summary):
        ll[5] += 1
    if r_harvey.search(summary):
        ll[6] += 1
    if r_maria.search(summary):
        ll[7] += 1
    if r_irene.search(summary):
        ll[8] += 1
    # count the number occurrence of hurricane the word both in the title and the summary
    if r_hurricane is not None:
        ll[9] += len(r_hurricane.findall(title) + r_hurricane.findall(summary))
    return


# count the number of title and summary that mentions each hurricane
# all_articles: all the articles/comments from the news resources and reddit
# splitter: the splitter used to split the time string, either a "T" or a space " "
# with_occurrence_of_hurricane: a boolean indicating to include the count of the word hurricane or not
def count_title_and_summary(all_articles, splitter, with_occurrence_of_hurricane):
    # compile regular expression for hurricane and the names
    r_irene = re.compile('irene', re.IGNORECASE)
    r_irma = re.compile('irma', re.IGNORECASE)
    r_harvey = re.compile('harvey', re.IGNORECASE)
    r_maria = re.compile('maria', re.IGNORECASE)
    r_hurricane = re.compile('hurricane', re.IGNORECASE)
    # count title and summary
    all_counts = {}
    if with_occurrence_of_hurricane:
        for line in all_articles:
            # process the date
            date = line[1].split(splitter)[0]
            # accumulate number of title and summary that mentions the hurricanes for each day
            # pass in the regular expression for hurricane to include the count for the word hurricane
            if date in all_counts:
                tally(all_counts[date], line[2], line[3], r_irma, r_harvey, r_maria, r_irene, r_hurricane)
            else:
                all_counts[date] = [date, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                tally(all_counts[date], line[2], line[3], r_irma, r_harvey, r_maria, r_irene, r_hurricane)
        # turn into list
        all_counts = list(all_counts.values())
        header = ["date",
                  "number of titles for irma", "number of titles for harvey",
                  "number of titles for maria", "number of titles for irene",
                  "number of summaries for irma", "number of summaries for harvey",
                  "number of summaries for maria", "number of summaries for irene",
                  "number of occurrence of hurricane"]
        all_counts.insert(0, header)
    else:
        for line in all_articles:
            # process the date
            date = line[1].split(splitter)[0]
            # accumulate number of title and summary that mentions the hurricanes for each day
            if date in all_counts:
                tally(all_counts[date], line[2], line[3], r_irma, r_harvey, r_maria, r_irene, None)
            else:
                all_counts[date] = [date, 0, 0, 0, 0, 0, 0, 0, 0]
                tally(all_counts[date], line[2], line[3], r_irma, r_harvey, r_maria, r_irene, None)
        # turn into list
        all_counts = list(all_counts.values())
        header = ["date",
                  "number of titles for irma", "number of titles for harvey",
                  "number of titles for maria", "number of titles for irene",
                  "number of summaries for irma", "number of summaries for harvey",
                  "number of summaries for maria", "number of summaries for irene"]
        all_counts.insert(0, header)
    return all_counts


def count():
    # count nytimes data
    with open("./nytimes_data.csv", 'r') as file:
        reader = csv.reader(file, delimiter=',')
        counts = count_title_and_summary(list(reader)[1:], "T", False)
        with open("./nytimes.csv", 'w') as save:
            # save to csv file
            writer = csv.writer(save, delimiter=',')
            writer.writerows(counts)

    # count guardian data
    with open("./guardian_data.csv", 'r') as file:
        reader = csv.reader(file, delimiter=',')
        counts = count_title_and_summary(list(reader)[1:], "T", False)
        # save to csv file
        with open("./guardian.csv", 'w') as save:
            writer = csv.writer(save, delimiter=',')
            writer.writerows(counts)

    # count reddit data
    with open("./reddit_data.csv", 'r') as file:
        reader = csv.reader(file, delimiter=',')
        counts = count_title_and_summary(list(reader)[1:], " ", True)
        with open("./reddit.csv", 'w') as save:
            # save to csv file
            writer = csv.writer(save, delimiter=',')
            writer.writerows(counts)

    # add number of occurrence of hurricanes into reddit, and the names of hurricanes
    data = pd.read_csv("reddit.csv")
    calhits(data)
    hurricaneName(data)
    data.to_csv("reddit_anova.csv")


if __name__ is "__main__":
    count()
