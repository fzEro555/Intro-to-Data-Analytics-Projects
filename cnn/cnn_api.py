import requests
import json


if __name__ == "__main__":
    base_url = "http://www.cnn.com/newsgraph/search"
    api_key = ""
    parameters_url = "/firstPublishDate:{}T00:00:00Z~{}1T23:59:59Z/".format("2017-05-01", "2017-12-31")
    print("\nrequesting")
    response = requests.get(base_url+parameters_url)
    print("status code: {}".format(response.status_code))
    if response.status_code is 200:
        with open("cnn_response.json", 'w') as file:
            file.writelines(json.dumps(response.json(), indent=4))
    else:
        with open("cnn_response_{}.json".format(response.status_code), 'w') as file:
            file.writelines(response.text)
    # input("Press key to exit. ")
