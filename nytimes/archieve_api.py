import requests
import json
import time


def retrieve(base_url, api_key):
    for year in range(2018, 2019):
        for month in range(8, 13):
            url = "{}/{}/{}.json?api-key={}".format(base_url, year, month, api_key)
            print("\nrequesting for {}/{}".format(month, year))
            response = requests.get(url)
            print("status code: {}".format(response.status_code))
            if response.status_code is 200:
                with open("{}_{}.json".format(year, month), 'w') as file:
                    file.write(json.dumps(response.json(), indent=4))
            else:
                with open("{}_{}_{}.txt".format(year, month, response.status_code), 'w') as file:
                    file.writelines(response.text)


def test_for_error(base_url, api_key):
    year = 1851
    month = 1
    url = "{}/{}/{}.json?api-key={}".format(base_url, year, month, api_key)
    response = requests.get(url)
    if response.status_code is 200:
        print(json.dumps(response.json(), indent=4))
    else:
        print(response.text)


if __name__ == "__main__":
    base_url = "https://api.nytimes.com/svc/archive/v1"
    api_key = "e7bbf035e3694a01894a2b523c4c589e"
    retrieve(base_url, api_key)
    # test_for_error(base_url, api_key)
    # input("Press anything to exit. ")