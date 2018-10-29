import csv


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
        ll.extend([0, 0, 0, 0])
    # turn data from string to integer and add to list
    original_data = [int(s) for s in original[1:5]]
    ll.extend(original_data)
    # pad copies of 4 zeros after the data
    for i in range(0, after):
        ll.extend([0, 0, 0, 0])
    return ll


# combine data from reddit and news
def combine_lean_data(reddit_file, nytimes_file, guardian_file):
    # turn files into lists
    reddit = list(csv.reader(reddit_file))[1:]
    nytimes = list(csv.reader(nytimes_file))[1:]
    guardian = list(csv.reader(guardian_file))[1:]

    header = ["date",
              "reddit count hurricane", "reddit count irma", "reddit count harvey", "reddit count maria",
              "nytimes count hurricane", "nytimes count irma", "nytimes count harvey", "nytimes count maria",
              "guardian count hurricane", "guardian count irma", "guardian count harvey", "guardian count maria"]

    # insert zeros to match the header of the combined data, also turn string into integer
    reddit = [pad_zeros(line, 0, 2) for line in reddit]
    nytimes = [pad_zeros(line, 1, 1) for line in nytimes]
    guardian = [pad_zeros(line, 2, 0) for line in guardian]

    # aggregate data from all three sources
    combined = {}
    aggregate(combined, reddit)
    aggregate(combined, nytimes)
    aggregate(combined, guardian)

    # turn into list and return
    combined_list = []
    # combined_list = [[key,].extend(value) for key, value in combined.items()]
    for key, value in combined.items():
        tmp = [key,]
        tmp.extend(value)
        combined_list.append(tmp)
    return combined_list
