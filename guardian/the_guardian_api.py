import os
import shutil
import requests
import json


def get_parameters(api_key, from_date, to_date, page):
    parameters = {"api-key": api_key,
                  "format": "json",
                  "lang": "en",
                  "from-date": from_date,
                  "to-date": to_date,
                  "page": page,
                  "page-size": "50",
                  "show-fields": ["all"]}
    return parameters


def write_response(response, page: str, hurricane_name: str):
    print("status code: {}".format(response.status_code))
    if response.status_code is 200:
        with open("./response_archive/the_guardian_response_{}_{}.json".format(hurricane_name, page), 'w') as file:
            file.writelines(json.dumps(response.json(), indent=4))
    else:
        with open("./response_archive/the_guardian_response_{}_{}_{}.json".format(
                hurricane_name, page, response.status_code), 'w') as file:
            file.writelines(json.dumps(response.text))


def retrieve(base_url, api_key, hurricane_name, from_date, to_date):
    print("\ninitial request")
    response = requests.get(base_url, get_parameters(api_key, from_date, to_date, "1"))
    write_response(response, "1", hurricane_name)
    n_pages = response.json()["response"]["pages"]
    for n in range(2, n_pages+1):
        print("\nrequesting page {}/{}".format(n, int(n_pages)))
        response = requests.get(base_url, get_parameters(api_key, from_date, to_date, str(n)))
        write_response(response, str(n), hurricane_name)


if __name__ == "__main__":

    path = "./response_archive"
    if os.path.exists(path):
        shutil.rmtree(path)
    else:
        os.mkdir(path)

    all_from = "2017-6-1"
    all_to = "2017-12-31"
    
    api_key = "ede93040-cd7a-4350-a2f7-6b0426126659"
    base_url = "https://content.guardianapis.com/search"

    retrieve(base_url, api_key, "all", all_from, all_to)
    
    # input("Press key to exit. ")
