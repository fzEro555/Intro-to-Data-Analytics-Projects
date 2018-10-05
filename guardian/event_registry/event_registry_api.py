import requests
import json


def get_parameters(api_key, from_date, to_date, page_num):
	parameters = {"api-key": api_key,
				  "resultType": "articles",
				  "articlesPage": page_num,
				  "articlesCount": 100,
				  "articlesSortBy": "date",
				  "dataType": "news",
				  "sourceUri": "washingtonpost.com",
				  "locationUri": "http://en.wikipedia.org/wiki/United_States",
				  "lang": "en",
				  "dateStart": from_date,
				  "dateEnd": to_date
				  }
	return parameters


def retrieve(base_url, api_key, hurricane_name, from_date, to_date, page_num):
	print("\nrequesting")
	response = requests.get(base_url, get_parameters(api_key, from_date, to_date, page_num))
	print(response)
	# json_response = response.json()
	# print(len(json_response["response"]["results"]))
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

	from_date = "2017-06-01"
	to_date = "2017-12-31"

	api_key = "d844e3cf-3e4c-4a84-b3b6-a6faf62cfd72"
	base_url = "http://eventregistry.org"

	for i in range(200):
		retrieve(base_url, api_key, str(i), from_date, to_date, i)


	# retrieve(base_url, api_key, "irma", irma_from, irma_to)
	# retrieve(base_url, api_key, "harvey", harvey_from, harvey_to)
	# retrieve(base_url, api_key, "maria", maria_from, maria_to)

# input("Press key to exit. ")




