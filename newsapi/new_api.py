import requests
import json


def get_sources():
    sources = ["the-new-york-times",
               "cnn",
               "buzzfeed",
               "abc-news-au",
               "the-guardian-au",
               "bbc-news",
               "the-guardian-uk"]
    return ",".join(sources)


def get_parameters(api_key, beginning, end):
    parameters = {"sources": get_sources(),
                  "from": beginning,
                  "to": end,
                  "language": "en",
                  "apiKey": api_key}
    return parameters


def get_new_within_time_period(base_url, api_key, beginning, end):
    print("\nrequesting for all from {} to {}".format(beginning, end))
    response = requests.get(base_url, get_parameters(api_key, beginning, end))
    print("status code: {}".format(response.status_code))
    if response.status_code is 200:
        with open("{}_to_{}.json".format(beginning, end), 'w') as file:
            file.writelines(json.dumps(response.json(), indent=4))
    else:
        with open("{}_to_{}_{}.txt".format(beginning, end, response.status_code), 'w') as file:
            file.writelines(response.text)


if __name__ == "__main__":
    base_url = "https://newsapi.org/v2/everything"
    api_key = "6199a399509048dea9db4df39ca1da68"

    # irma
    beginning = "2017-8-30"
    end = "2017-9-13"
    get_new_within_time_period(base_url, api_key, beginning, end)

    # input("Press anything to exit. ")
