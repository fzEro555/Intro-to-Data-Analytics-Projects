import requests
import csv
import time


def search(base_url, api_key, query, year, month_ranges):
    ll = []
    # search articles within a time range to avoid getting too many results at a time
    for begin_date, end_date in month_ranges:
        # set initial parameters and get initial response
        parameters = {"api-key": api_key,
                      "q": query,
                      "begin_date": year+begin_date,
                      "end_date": year+end_date,
                      "page": 0}
        response = requests.get(base_url, parameters)
        time.sleep(2)
        # get number of pages
        resp_json = response.json()
        hits = int(resp_json["response"]["meta"]["hits"])
        if hits > 1000:
            raise Exception("Over 1000 pages returned, adjust date range.\n"
                            "Query: {} Date range: {}{} - {}{}".format(query, year, begin_date, year, end_date))
        n_pages = round(hits/10) + 1
        # process response
        ll.extend(process_response(query, resp_json))
        for i_page in range(1, n_pages + 1):
            # get next page and process
            parameters["page"] = i_page
            response = requests.get(base_url, parameters)
            time.sleep(2)
            ll.extend(process_response(query, response.json()))
    return ll


# extract article date, titles, summary
# returns a list ["search query", "article date", "article title", "article summary"]
def process_response(query, resp_json):
    ll = []
    docs = resp_json["response"]["docs"]
    for d in docs:
        date = d["pub_date"]
        title = d["headline"]["main"]
        summary = d["snippet"]
        ll.append([query, date, title, summary])
    return ll


def search_articles():
    base_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
    api_key = "e7bbf035e3694a01894a2b523c4c589e"
    # hurricanes to search
    queries = ["hurricane irma", "hurricane harvey", "hurricane maria", "hurricane irene"]
    # date ranges by months
    month_ranges = [("0601", "0630"), ("0701", "0731"), ("0801", "0831"), ("0901", "0930"),
                    ("1001", "1031"), ("1101", "1130"), ("1201", "1231")]
    # the header
    all_articles = [["search query", "article date", "article title", "article summary"]]
    # search for hurricanes irma
    all_articles.extend(search(base_url, api_key, queries[0], "2018", month_ranges))
    # search for hurricanes harvey
    all_articles.extend(search(base_url, api_key, queries[1], "2018", month_ranges))
    # search for hurricanes maria
    all_articles.extend(search(base_url, api_key, queries[2], "2018", month_ranges))
    # search for hurricanes irene
    all_articles.extend(search(base_url, api_key, queries[3], "2011", month_ranges))
    # save to csv
    with open("./nytimes_data.csv", 'w') as file_save:
        writer = csv.writer(file_save, delimiter=',')
        writer.writerows(all_articles)


if __name__ == "__main__":
    search_articles()
    # base_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
    # api_key = "e7bbf035e3694a01894a2b523c4c589e"
    # # search
    # queries = ["healthcare"]
    # response = search(base_url, api_key, "healthcare")
    # with open("response.json", 'w') as file:
    #     file.writelines(json.dumps(response.json(), indent=4))
    # docs = extract_docs(response)
    # articles = [extract_headline_and_snippet(d) for d in docs]
    # with open("articles.txt", 'w') as file:
    #     file.writelines(["{0}\n{1}\n\n".format(atcl[0], atcl[1]) for atcl in articles])
    # # get full articles based on search result

