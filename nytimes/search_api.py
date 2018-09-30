import requests
import json


def search(base_url, api_key, query):
    parameters = {"api-key": api_key,
                  "q": query}
    response = requests.get(base_url, parameters)
    return response


def extract_docs(response):
    resp_json = response.json()
    return resp_json["response"]["docs"]


def extract_headline_and_snippet(doc: dict):
    headline = doc["headline"]["main"]
    snippet = doc["snippet"]
    return headline, snippet


if __name__ == "__main__":
    base_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
    api_key = "e7bbf035e3694a01894a2b523c4c589e"
    # search
    queries = ["healthcare"]
    response = search(base_url, api_key, "healthcare")
    with open("response.json", 'w') as file:
        file.writelines(json.dumps(response.json(), indent=4))
    docs = extract_docs(response)
    articles = [extract_headline_and_snippet(d) for d in docs]
    with open("articles.txt", 'w') as file:
        file.writelines(["{0}\n{1}\n\n".format(atcl[0], atcl[1]) for atcl in articles])
    # get full articles based on search result

