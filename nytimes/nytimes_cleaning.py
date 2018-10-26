import os
import re
import csv
import json


# count occurrence of a word using regular expression
def count(text, regular_expression) -> int:
    try:
        _all = regular_expression.findall(text)
        return len(_all)
    except TypeError as err:
        print("TypeError: {}".format(err))
        return 0


# extract year-month-date from the date in the json files
def process_date(iso_date):
    full_date = iso_date.split('T', 1)[0]
    return full_date.strip()


# extract counts from the json_file using regular expressions
def extract_from(json_file, r_hurricane, r_irma, r_harvey, r_maria):
    lst = []
    # get all docs from the json file
    docs = json_file["response"]["docs"]
    # for each doc, make a list of date, n_hurricane, n_irma, n_harvey, n_maria
    for dc in docs:
        date = dc["pub_date"]
        headline = dc["headline"]["main"]
        snippet = dc["snippet"]
        # count occurrence of each word in headline and snippet
        n_hurricane = count(headline, r_hurricane) + count(snippet, r_hurricane)
        n_irma = count(headline, r_irma) + count(snippet, r_irma)
        n_harvey = count(headline, r_harvey) + count(snippet, r_harvey)
        n_maria = count(headline, r_maria) + count(snippet, r_maria)
        lst.append([process_date(date), n_hurricane, n_irma, n_harvey, n_maria])
    return lst


# the main method
if __name__ == "__main__":
    # compile regular expression for words: hurricane, irma, harvey, maria
    # they will be later used for counting the number of occurrence of each word in each article
    r_hurricane = re.compile('hurricane', re.IGNORECASE)
    r_irma = re.compile('irma', re.IGNORECASE)
    r_harvey = re.compile('harvey', re.IGNORECASE)
    r_maria = re.compile('maria', re.IGNORECASE)

    # create a list of id, date, n_hurricane, n_irma, n_harvey, n_maria for each news from nytimes
    ll = [["news date", "occurrence of hurricane", "occurrence of irma", "occurrence of harvey", "occurrence of maria"]]

    # list all files in the directory
    path = "./response_archive/"
    json_files = os.listdir(path)
    for jf in json_files:
        # if it is a json file, extract number of occurrence of words and append them to the list
        if jf.endswith(".json"):
            # print("\nCleaning {}".format(jf))
            with open(path + jf, 'r') as file:
                json_file = json.loads(file.read())
                ll.extend(extract_from(json_file, r_hurricane, r_irma, r_harvey, r_maria))

    # save the list to a csv file
    print("\nSaving as csv. ")
    with open("nytimes_cleaned.csv", 'w') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(ll)
    # input("press any key to exit")
