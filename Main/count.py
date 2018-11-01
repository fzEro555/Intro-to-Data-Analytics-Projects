import re
import csv


def tally(ll, title, summary, r_irma, r_harvey, r_maria, r_irene, r_hurricane):
    # check title
    if r_irma.search(title):
        ll[1] += 1
    if r_harvey.search(title):
        ll[2] += 1
    if r_maria.search(title):
        ll[3] += 1
    if r_irene.search(title):
        ll[4] += 1
    # check summary
    if r_irma.search(summary):
        ll[5] += 1
    if r_harvey.search(summary):
        ll[6] += 1
    if r_maria.search(summary):
        ll[7] += 1
    if r_irene.search(summary):
        ll[8] += 1
    if r_hurricane is not None:
        ll[9] += len(r_hurricane.findall(title) + r_hurricane.findall(summary))
    return


def count_title_and_summary(ll, splitter, with_occurrence_of_hurricane):
    # compile regular expression for hurricane and the names
    r_irene = re.compile('irene', re.IGNORECASE)
    r_irma = re.compile('irma', re.IGNORECASE)
    r_harvey = re.compile('harvey', re.IGNORECASE)
    r_maria = re.compile('maria', re.IGNORECASE)
    r_hurricane = re.compile('hurricane', re.IGNORECASE)
    # count
    all_counts = {}
    if with_occurrence_of_hurricane:
        for line in ll:
            date = line[1].split(splitter)[0]
            if date in all_counts:
                tally(all_counts[date], line[2], line[3], r_irma, r_harvey, r_maria, r_irene, r_hurricane)
            else:
                all_counts[date] = [date, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                tally(all_counts[date], line[2], line[3], r_irma, r_harvey, r_maria, r_irene, r_hurricane)
        # return list
        all_counts = list(all_counts.values())
        header = ["date",
                  "number of titles for irma", "number of titles for harvey",
                  "number of titles for maria", "number of titles for irene",
                  "number of summaries for irma", "number of summaries for harvey",
                  "number of summaries for maria", "number of summaries for irene",
                  "number of occurrence of hurricane"]
        all_counts.insert(0, header)
    else:
        for line in ll:
            date = line[1].split(splitter)[0]
            if date in all_counts:
                tally(all_counts[date], line[2], line[3], r_irma, r_harvey, r_maria, r_irene, None)
            else:
                all_counts[date] = [date, 0, 0, 0, 0, 0, 0, 0, 0]
                tally(all_counts[date], line[2], line[3], r_irma, r_harvey, r_maria, r_irene, None)
        # return list
        all_counts = list(all_counts.values())
        header = ["date",
                  "number of titles for irma", "number of titles for harvey",
                  "number of titles for maria", "number of titles for irene",
                  "number of summaries for irma", "number of summaries for harvey",
                  "number of summaries for maria", "number of summaries for irene"]
        all_counts.insert(0, header)
    return all_counts


def count():
    with open("./nytimes_data.csv", 'r') as file:
        reader = csv.reader(file, delimiter=',')
        counts = count_title_and_summary(list(reader)[1:], "T", False)
        with open("./nytimes.csv", 'w') as save:
            writer = csv.writer(save, delimiter=',')
            writer.writerows(counts)

    with open("./guardian_data.csv", 'r') as file:
        reader = csv.reader(file, delimiter=',')
        counts = count_title_and_summary(list(reader)[1:], "T", False)
        with open("./guardian.csv", 'w') as save:
            writer = csv.writer(save, delimiter=',')
            writer.writerows(counts)

    with open("./reddit_data.csv", 'r') as file:
        reader = csv.reader(file, delimiter=',')
        counts = count_title_and_summary(list(reader)[1:], " ", True)
        with open("./reddit.csv", 'w') as save:
            writer = csv.writer(save, delimiter=',')
            writer.writerows(counts)


if __name__ is "__main__":
    count()
