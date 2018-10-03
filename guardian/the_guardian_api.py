import requests
import json


def get_parameters(api_key, from_date, to_date):
    parameters = {"api-key": api_key,
                  "format": "json",
                  "lang": "en",
                  "from-date": from_date,
                  "to-date": to_date,
                  "show-fields": ["all"]}
    return parameters


def retrieve(base_url, api_key, hurricane_name, from_date, to_date):
    print("\nrequesting")
    response = requests.get(base_url, get_parameters(api_key, from_date, to_date))
    json_response = response.json()
    print(len(json_response["response"]["results"]))
    print("status code: {}".format(response.status_code))
    if response.status_code is 200:
        with open("the_guardian_response_{}.json".format(hurricane_name), 'w') as file:
            file.writelines(json.dumps(response.json(), indent=4))
    else:
        with open("the_guardian_response_{}.json".format(response.status_code), 'w') as file:
            file.writelines(json.dumps(response.txt))


if __name__ == "__main__":
    
    irma_from = "2017-8-30"
    irma_to = "2017-9-13"
    
    harvey_from = "2017-8-17"
    harvey_to = "2017-9-2"
    
    maria_from = "2017-9-16" 
    maria_to = "2017-10-2"
    
    api_key = "ede93040-cd7a-4350-a2f7-6b0426126659"
    base_url = "https://content.guardianapis.com/search"
    
    retrieve(base_url, api_key, "irma", irma_from, irma_to)
    retrieve(base_url, api_key, "harvey", harvey_from, harvey_to)
    retrieve(base_url, api_key, "maria", maria_from, maria_to)
    
    # input("Press key to exit. ")
