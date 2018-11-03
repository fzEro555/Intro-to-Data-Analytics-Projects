import requests
import csv


# extract article date, titles, summary
# returns a list ["search query", "article date", "article title", "article summary"]
def process_response(query, resp_json):
    ll = []
    results = resp_json["response"]["results"]
    for res in results:
        fields = res["fields"]
        date = None
        try:
            date = fields["firstPublicationDate"]
        except KeyError:
            try:
                date = fields["newspaperEditionDate"]
            except KeyError:
                date = res["webPublicationDate"]
        title = fields["headline"]
        summary = fields["bodyText"]
        ll.append([query, date, title, summary])
    return ll


def retrieve(base_url, api_key, query, year, month_ranges):
    ll = []
    # process query, because the default for q is or
    q = query.split(" ")
    q = "{}%20AND%20{}".format(q[0], q[1])
    # retrieve articles within certain time
    for begin_date, end_date in month_ranges:
        # set initial parameter and get initial response
        parameters = {"api-key": api_key,
                      "format": "json",
                      "lang": "en",
                      "q": q,
                      "from-date": "{}-{}".format(year, begin_date),
                      "to-date": "{}-{}".format(year, end_date),
                      "page": 1,
                      "page-size": "50",
                      "show-fields": ["all"]}
        response = requests.get(base_url, parameters)
        resp_json = response.json()
        pages = int(resp_json["response"]["pages"])
        if pages > 500:
            raise Exception("Too many pages, adjust date range. ")
        # process response
        ll.extend(process_response(query, resp_json))
        for i_page in range(2, pages + 1):
            # get next page and process
            parameters["page"] = i_page
            response = requests.get(base_url, parameters)
            ll.extend(process_response(query, resp_json))
    return ll


def retrieve_articles():
    base_url = "https://content.guardianapis.com/search"
    api_key = "ede93040-cd7a-4350-a2f7-6b0426126659"

    # hurricanes to search for
    queries = ["hurricane irma", "hurricane harvey", "hurricane maria", "hurricane irene"]
    # date ranges by months
    month_ranges = [("06-01", "06-30"), ("07-01", "07-31"), ("08-01", "08-31"), ("09-01", "09-30"),
                    ("10-01", "10-31"), ("11-01", "11-30"), ("12-01", "12-31")]

    # the header
    all_articles = [["search query", "article date", "article title", "article summary"]]
    # search for hurricanes irma
    all_articles.extend(retrieve(base_url, api_key, queries[0], "2018", month_ranges))
    # search for hurricanes harvey
    all_articles.extend(retrieve(base_url, api_key, queries[1], "2018", month_ranges))
    # search for hurricanes maria
    all_articles.extend(retrieve(base_url, api_key, queries[2], "2018", month_ranges))
    # search for hurricanes irene
    all_articles.extend(retrieve(base_url, api_key, queries[3], "2011", month_ranges))
    # save to csv
    with open("./guardian_data.csv", 'w') as file_save:
        writer = csv.writer(file_save, delimiter=',')
        writer.writerows(all_articles)
    return


if __name__ is "__main__":
    retrieve_articles()
