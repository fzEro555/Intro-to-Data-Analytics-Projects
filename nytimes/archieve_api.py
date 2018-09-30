import requests
import json
import time


if __name__ == "__main__":
    base_url = "https://api.nytimes.com/svc/archive/v1"
    api_key = "e7bbf035e3694a01894a2b523c4c589e"
    for year in range(1920, 2018):
        for month in range(1, 13):
            url = "{}/{}/{}.json?api-key={}".format(base_url, year, month, api_key)
            time.sleep(60)
            response = requests.get(url)
            with open("{}_{}.txt".format(year, month), 'w') as file:
                file.write(json.dumps(response.json()))

    input("Press anything to exit. ")
