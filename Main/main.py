import pandas as pd
import sys


def add_data(csv_file: str) -> pd.core.frame.DataFrame:
	# grab data from csv file, return cleaned data frame
	data_frame = pd.read_csv(csv_file, sep=',', encoding='latin1')
	return data_frame


def get_date(data_frame: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
	data_frame['comment_date'], data_frame['comment_time'] = zip(*data_frame['Comment_Time'].apply(lambda x: x.split(' ')))
	
	return data_frame

if __name__ == "__main__":
	fpds_clean = "FPDS_final.csv"
	reddit_clean = "../reddit/reddit_cleaned_data.csv"
	nytimes_clean = "nytimes_cleaned.csv"
	guardian_clean = "the_guardian_cleaned.csv"

	reddit_data_frame = get_date(add_data(reddit_clean))





