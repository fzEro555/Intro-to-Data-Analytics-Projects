import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.classify import SklearnClassifier
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.sentiment.vader import SentiText


def upload_data(csv_file: str) -> pd.core.frame.DataFrame:
	# grab data from csv file provided
	data_frame = pd.read_csv(csv_file, sep=',')
	print(data_frame.head(5))
	return data_frame


def get_sent_score(data_frame: pd.core.frame.DataFrame, col_list: list) -> dict:
	sent_analyzer = SentimentIntensityAnalyzer()
	score_list = []
	neg_total = 0
	pos_total = 0
	neutral_total = 0
	total = 0
	for index, row in data_frame.iterrows():
		for col in col_list:
			score = sent_analyzer.polarity_scores(row[col])
			score_list.append((row[col], score))
			neg_total += score['neg']
			pos_total += score['pos']
			neutral_total += score['neu']

			total += 1

	score_dict = {}
	score_dict["neg"] = neg_total/total
	score_dict["pos"] = pos_total/total
	score_dict["neutral"] = neutral_total/total

	print(score_dict)

	return score_dict


def main():
	# upload reddit data
	reddit_csv = "../reddit/reddit.csv"
	data_frame = upload_data(reddit_csv)
	get_sent_score(data_frame, ["comment"])


if __name__ == "__main__":
	main()


