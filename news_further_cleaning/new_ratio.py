import csv
import numpy as np


def count_non_zeros(lst, c_from, c_to):
    lst = [line[c_from:c_to] for line in lst]
    nparray = np.array(lst, dtype='int32')
    count = np.count_nonzero(nparray, axis=0)
    return count


def write_up(n_clean, n_lean, n_hurricane, n_irma, n_harvey, n_maria) -> list:
    to_write = []
    # numbers
    to_write.append("\nnumber of instances in cleaned file: {}".format(n_clean))
    to_write.append("\nnumber of not-all-zero instances: {}".format(n_lean))
    to_write.append("\nnumber of appearance of hurricane: {}".format(n_hurricane))
    to_write.append("\nnumber of appearance of irma: {}".format(n_irma))
    to_write.append("\nnumber of appearance of harvey: {}".format(n_harvey))
    to_write.append("\nnumber of appearance of maria: {}".format(n_maria))
    # ratios
    to_write.append("\nratio of not-all-zero to all: {}".format(n_lean / n_clean))
    to_write.append("\nratio of hurricane to not-all-zero: {}".format(n_hurricane / n_clean))
    to_write.append("\nratio of irma to not-all-zero: {}".format(n_irma / n_clean))
    to_write.append("\nratio of harvey to not-all-zero: {}".format(n_harvey / n_clean))
    to_write.append("\nratio of maria to not-all-zero: {}".format(n_maria / n_clean))
    return to_write


if __name__ == "__main__":
    # nytimes
    with open("../nytimes/nytimes_cleaned.csv", 'r') as file:
        n_nytimes = len(file.readlines())
    with open("nytimes_lean.csv", 'r') as lean_file:
        reader = csv.reader(lean_file, delimiter=',')
        lst = list(reader)
        n_nytimes_lean = len(lst)
        count = count_non_zeros(lst, 2, 6)
    with open("nytimes_count.txt", 'w') as write_files:
        to_write = write_up(n_nytimes, n_nytimes_lean, count[0], count[1], count[2], count[3])
        write_files.writelines(to_write)
    # the guardian
    with open("../guardian/the_guardian_cleaned.csv", 'r') as file:
        n_guardian = len(file.readlines())
    with open("the_guardian_lean.csv", 'r') as lean_file:
        reader = csv.reader(lean_file, delimiter=',')
        lst = list(reader)
        n_guardian_lean = len(lst)
        count = count_non_zeros(lst, 1, 5)
    with open("the_guardian_count.txt", 'w') as write_files:
        to_write = write_up(n_guardian, n_guardian_lean, count[0], count[1], count[2], count[3])
        write_files.writelines(to_write)
    input("any key")
