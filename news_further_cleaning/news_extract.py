import csv


# check if a line is not all zeros
def not_all_zeros(ll):
    for e in ll:
        if e is not "0":
            return True
    return False


# clean the file by extracting those articles that have counts that are not all zeros
# meaning that only keep the articles that mentioned ay of the four words: hurricane, irma, harvey, maria
def extract(read_file, start, end, name):
    # read csv file
    reader = csv.reader(read_file, delimiter=',')
    lst = list(reader)
    # keep only lines have counts that are not all zeros
    lst_lean = [line for line in lst if not_all_zeros(line[start:end])]
    # save extracted lines to a csv file
    with open(name, 'w') as write_file:
        writer = csv.writer(write_file, delimiter=',')
        writer.writerows(lst_lean)


# the main method
if __name__ == "__main__":
    with open("../nytimes/nytimes_cleaned.csv", 'r') as file:
        extract(file, 1, 5, "nytimes_lean.csv")
    with open("../guardian/the_guardian_cleaned.csv", 'r') as file:
        extract(file, 1, 5, "the_guardian_lean.csv")
    # input("press any key to exit")
