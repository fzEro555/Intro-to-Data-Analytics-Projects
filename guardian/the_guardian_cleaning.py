import os
import glob
import re
import csv
import json


def count(text, regular_expression) -> int:
    try:
        _all = regular_expression.findall(text)
        return len(_all)
    except TypeError as err:
        print("TypeError: {}".format(err))
        return 0


def extract_from(json_file, r_hurricane, r_irma, r_harvey, r_maria):
    lst = []
    # get all docs from the json file
    results = json_file["response"]["results"]
    # for each doc, make a list of id, date, n_hurricane, n_irma, n_harvey, n_maria
    for res in results:
        fields = res["fields"]
        date = None
        try:
            date = fields["firstPublicationDate"]
        except KeyError:
            date = fields["newspaperEditionDate"]
        headline = fields["headline"]
        bodytext = fields["bodyText"]
        # count
        n_hurricane = count(headline, r_hurricane) + count(bodytext, r_hurricane)
        n_irma = count(headline, r_irma) + count(bodytext, r_irma)
        n_harvey = count(headline, r_harvey) + count(bodytext, r_harvey)
        n_maria = count(headline, r_maria) + count(bodytext, r_maria)
        lst.append([date, n_hurricane, n_irma, n_harvey, n_maria])
    return lst


if __name__ == "__main__":
    r_hurricane = re.compile('hurricane', re.IGNORECASE)
    r_irma = re.compile('irma', re.IGNORECASE)
    r_harvey = re.compile('harvey', re.IGNORECASE)
    r_maria = re.compile('maria', re.IGNORECASE)
    # a list of id, date, n_hurricane, n_irma, n_harvey, n_maria for each news from nytimes
    ll = []
    # list all json files in the directory
    path = "./response_archive/"
    json_files = os.listdir(path)
    for jf in json_files:
        # print("\nCleaning {}".format(jf))
        with open(path + jf, 'r') as file:
            json_file = json.loads(file.read())
            ll.extend(extract_from(json_file, r_hurricane, r_irma, r_harvey, r_maria))
    print("\nSaving as csv. ")
    with open("the_guardian_cleaned.csv", 'w') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(ll)
    # input("press any key to exit")
