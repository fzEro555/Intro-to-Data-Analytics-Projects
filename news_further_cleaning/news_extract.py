import csv


def not_all_zeros(ll):
    for e in ll:
        if e is not "0":
            return True
    return False


def extract(read_file, start, end, name):
    reader = csv.reader(read_file, delimiter=',')
    lst = list(reader)
    lst_lean = [line for line in lst if not_all_zeros(line[start:end])]
    with open(name, 'w') as write_file:
        writer = csv.writer(write_file, delimiter=',')
        writer.writerows(lst_lean)


if __name__ == "__main__":
    with open("../nytimes/nytimes_cleaned.csv", 'r') as file:
        extract(file, 2, 6, "nytimes_lean.csv")
    with open("../guardian/the_guardian_cleaned.csv") as file:
        extract(file, 1, 5, "the_guardian_lean.csv")
    # input("press any key to exit")
