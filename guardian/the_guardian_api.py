import requests
import json


def get_parameters(api_key):
    parameters = {"api-key": api_key,
                  "format": "json",
                  "lang": "en",
                  "from-date": "2017-5-1",
                  "to-date": "2017-12-31",
                  "show-fields": ["all"]}
    return parameters


def retrieve(base_url, api_key):
    response = requests.get(base_url, get_parameters(api_key))
    if response.status_code is 200:
        with open("the_guardian_response.json", 'w') as file:
            file.writelines(json.dumps(response.json(), indent=4))
    else:
        with open("the_guardian_response_{}.json".format(response.status_code), 'w') as file:
            file.writelines(json.dumps(response.json(), indent=4))


if __name__ == "__main__":
    api_key = "ede93040-cd7a-4350-a2f7-6b0426126659"
    base_url = "https://content.guardianapis.com/search"
    retrieve(base_url, api_key)
    input("Press anything to exit. ")
