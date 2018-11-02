import pandas as pd
import numpy as np
from pprint import pprint


def upload_data(csv_file: str) -> pd.core.frame.DataFrame:
	# grab data from csv file provided
	data_frame = pd.read_csv(csv_file, sep=',', encoding='latin1')
	return data_frame


def binning(data_frame: pd.core.frame.DataFrame)-> None:
	min_money = data_frame["Action Obligation"].min()
	max_money = data_frame["Action Obligation"].max()

	min_money -= 1
	max_money -= 1

	# evenly spaced bins using min/max

	min_max_bins = np.arange(min_money, max_money, 5000000)

	labels = range(1, 21)
	cut_bins = pd.cut(data_frame['Action Obligation'], 20, retbins=True)
	cut_bins = np.asarray(cut_bins)

	# bin data
	mm_bins = np.digitize(data_frame['Action Obligation'], min_max_bins)


	# add to data_frame
	data_frame['mm_bins'] = pd.cut(data_frame['Action Obligation'], min_max_bins)
	data_frame['even_bins'] = pd.cut(data_frame['Action Obligation'], 20, labels=labels)

	# print(data_frame.head)

	# Print Bin Counts
	pprint(data_frame['mm_bins'].value_counts())
	pprint(data_frame['even_bins'].value_counts())

	# data_frame['mm_bins'].hist()
	data_frame['even_bins'].hist()


def main():
	fpds_clean = "../FPDS-NG/FPDS_final.csv"

	data_frame = upload_data(fpds_clean)
	binning(data_frame)


if __name__ == "__main__":
	main()
