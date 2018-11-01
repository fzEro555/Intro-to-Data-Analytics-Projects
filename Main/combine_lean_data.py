import csv


# decorate line with date
def decorate(line):
    date = line[0].split('-')
    return int(date[0]), int(date[1]), int(date[2]), line


# sort the data on date, the first column
def sort_on_date(combined):
    # decorate
    decorated = [decorate(line) for line in combined]
    # sort on day, month, year
    decorated = sorted(decorated, key=lambda line: line[2])
    decorated = sorted(decorated, key=lambda line: line[1])
    decorated = sorted(decorated, key=lambda line: line[0])
    # undecorate
    combined = [line[3] for line in decorated]
    return combined


def aggregate(combined, source):
    for s in source:
        if s[0] in combined:
            # if this date exists, sum all counts
            combined[s[0]] = list(map(lambda x,y:x+y, combined[s[0]], s[1:]))
        else:
            combined[s[0]] = s[1:]
    return combined


# pad copies of 4 zeros before and after the data
def pad_zeros(original, before: int, after: int):
    ll = [original[0]]
    # pad copies of 4 zeros before the data
    for i in range(0, before):
        ll.extend([0, 0, 0, 0, 0, 0, 0, 0])
    # turn data from string to integer and add to list
    original_data = [float(s) for s in original[1:]]
    ll.extend(original_data)
    # pad copies of 4 zeros after the data
    for i in range(0, after):
        ll.extend([0, 0, 0, 0, 0, 0, 0, 0])
    return ll


# combine data from reddit and news
def combine_lean_data(reddit_file, nytimes_file, guardian_file, fpds_file):
    # turn files into lists
    reddit = list(csv.reader(reddit_file))[1:9]
    nytimes = list(csv.reader(nytimes_file))[1:]
    guardian = list(csv.reader(guardian_file))[1:]
    fpds = list(csv.reader(fpds_file))[1:]

    header = ["date",
              "number of titles for irma in reddit", "number of titles for harvey in reddit",
              "number of titles for maria in reddit", "number of titles for irene in reddit",
              "number of summaries for irma in reddit", "number of summaries for harvey in reddit",
              "number of summaries for maria in reddit", "number of summaries for irene in reddit",

              "number of titles for irma in nytimes", "number of titles for harvey in nytimes",
              "number of titles for maria in nytimes", "number of titles for irene in nytimes",
              "number of summaries for irma in nytimes", "number of summaries for harvey in nytimes",
              "number of summaries for maria in nytimes", "number of summaries for irene in nytimes",

              "number of titles for irma in guardian", "number of titles for harvey in guardian",
              "number of titles for maria in guardian", "number of titles for irene in guardian",
              "number of summaries for irma in guardian", "number of summaries for harvey in guardian",
              "number of summaries for maria in guardian", "number of summaries for irene in guardian",

              "number of contract for irma", "number of contract for harvey",
              "number of contract for maria", "number of contract for irene",
              "amount for irma", "amount for harvey", "amount for maria", "amount for irene"]

    # insert zeros to match the header of the combined data, also turn string into integer
    reddit = [pad_zeros(line, 0, 3) for line in reddit]
    nytimes = [pad_zeros(line, 1, 2) for line in nytimes]
    guardian = [pad_zeros(line, 2, 1) for line in guardian]
    fpds = [pad_zeros(line, 3, 0) for line in fpds]

    # aggregate data from all three sources
    combined = {}
    aggregate(combined, reddit)
    aggregate(combined, nytimes)
    aggregate(combined, guardian)
    aggregate(combined, fpds)

    # turn into list and return
    combined_list = []
    for key, value in combined.items():
        tmp = [key,]
        tmp.extend(value)
        combined_list.append(tmp)

    # sort the combined data on date
    combined_list = sort_on_date(combined_list)

    # insert header
    combined_list.insert(0, header)
    return combined_list


def combine():
    with open("./reddit.csv", 'r') as reddit_file:
        with open("./nytimes.csv", 'r') as nytimes_file:
            with open("./guardian.csv", 'r') as guardian_file:
                with open("./FPDS.csv", 'r') as fpds_file:
                    ll = combine_lean_data(reddit_file, nytimes_file, guardian_file, fpds_file)
                    with open("./combined_data.csv", 'w') as save_file:
                        writer = csv.writer(save_file, delimiter=',')
                        writer.writerows(ll)
    return


if __name__ == "__main__":
    combine()
