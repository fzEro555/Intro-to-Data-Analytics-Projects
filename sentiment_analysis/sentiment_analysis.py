import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.classify import SklearnClassifier
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.sentiment.vader import SentiText
import json


def upload_data(csv_file: str) -> pd.core.frame.DataFrame:
	# grab data from csv file provided
	data_frame = pd.read_csv(csv_file, sep=',')
	print(data_frame.head(5))
	return data_frame


def get_sent_score(data_frame: pd.core.frame.DataFrame, col_list: list) -> dict:
	# calculates total sentiment score for every row of dataframe
	sent_analyzer = SentimentIntensityAnalyzer()
	score_list = []
	neg_total = 0
	pos_total = 0
	neutral_total = 0
	total = 0
	for index, row in data_frame.iterrows():
		for col in col_list:
			score = sent_analyzer.polarity_scores(str(row[col]))
			score_list.append((row[col], score))
			neg_total += score['neg']
			pos_total += score['pos']
			neutral_total += score['neu']

			total += 1

	# return average sentiment score of data
	score_dict = {}
	score_dict["neg"] = neg_total/total
	score_dict["pos"] = pos_total/total
	score_dict["neutral"] = neutral_total/total

	print(score_dict)

	return score_dict


def main():
	all_sent_scores = dict()
	# upload reddit data
	reddit_csv = "./reddit/reddit.csv"
	guardian_csv = "./basic_analysis/guardian_data.csv"
	nytimes_csv = "./basic_analysis/nytimes_data.csv"
	reddit_df = upload_data(reddit_csv)
	nytimes_df = upload_data(nytimes_csv)
	guardian_df = upload_data(guardian_csv)

	# evaluate sent score for each comment in reddit data
	all_sent_scores["reddit"] = get_sent_score(reddit_df, ["comment"])
	all_sent_scores["nytimes"] = get_sent_score(nytimes_df, ["article summary"])
	all_sent_scores["guardian"] = get_sent_score(guardian_df, ["article summary"])

	with open("./sentiment_analysis/all_sent.json", "w") as json_file:
		json.dump(all_sent_scores, json_file)


if __name__ == "__main__":
	main()


