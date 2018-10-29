import csv
import re


# check if a line is not all zeros
def not_all_zeros(ll):
    for e in ll:
        if e is not "0":
            return True
    return False


# count occurrence of a word using regular expression
def count(text, regular_expression) -> int:
    try:
        _all = regular_expression.findall(text)
        return len(_all)
    except TypeError as err:
        print("TypeError: {}".format(err))
        return 0


# gets the counts of hurricane, irma, harvey, maria in each comment
def count_reddit(date_text):
    # compile regular expression for words: hurricane, irma, harvey, maria
    # they will be later used for counting the number of occurrence of each word in each article
    r_hurricane = re.compile('hurricane', re.IGNORECASE)
    r_irma = re.compile('irma', re.IGNORECASE)
    r_harvey = re.compile('harvey', re.IGNORECASE)
    r_maria = re.compile('maria', re.IGNORECASE)

    # initialize the list of count
    counts = []
    for dt in date_text:
        date = dt[0]
        text = dt[1]
        # count occurrence of the four words
        n_hurricane = count(text, r_hurricane)
        n_irma = count(text, r_irma)
        n_harvey = count(text, r_harvey)
        n_maria = count(text, r_maria)
        # append to list of counts
        counts.append([date, n_hurricane, n_irma, n_harvey, n_maria])
    # counts = [line for line in counts if not_all_zeros(line[1:])]
    return counts


# take out the date, title and comment from a line of data
def extract_date_text(reddit_data_line):
    date = reddit_data_line[7].split(' ', 1)[0]
    title = reddit_data_line[2]
    comment = reddit_data_line[6]
    return date, "{} {}".format(title, comment)


# count number of occurrence of hurricane, irma, harvey, maria in each comment
def leanify_reddit(reddit_cleaned_directory, reddit_save_directory):
    # read in cleaned reddit file
    with open(reddit_cleaned_directory, 'r') as reddit_cleaned_file:
        reader = csv.reader(reddit_cleaned_file, delimiter=',')
        reddit_data = list(reader)
        # extract date, title and comment from the reddit file
        date_text = [extract_date_text(line) for line in reddit_data[1:]]
        # get counts from each comment
        counts = count_reddit(date_text)
        # save the counts to csv file
        with open(reddit_save_directory, 'w') as reddit_save_file:
            ll = [['date', 'occurrence of hurricane', 'occurrence of hurricane', 'occurrence of hurricane']]
            ll.extend(counts)
            writer = csv.writer(reddit_save_file, delimiter=',')
            writer.writerows(ll)

