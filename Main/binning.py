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

	labels_20 = range(1, 21)
	labels_10= range(1, 11)
	labels_100 = range(1, 101)
	labels_3 = range(1, 4)

	cut_bins = pd.cut(data_frame['Action Obligation'], 20, retbins=True)
	print(cut_bins)

	# bin data
	mm_bins = np.digitize(data_frame['Action Obligation'], min_max_bins)

	# add to data_frame
	data_frame['mm_bins'] = pd.cut(data_frame['Action Obligation'], min_max_bins, labels=False)
	data_frame['even_bins_20'] = pd.cut(data_frame['Action Obligation'], 20, labels=labels_20)
	# data_frame['even_bins_10'] = pd.cut(data_frame['Action Obligation'], 10, labels=labels_10)
	# data_frame['even_bins_3'] = pd.cut(data_frame['Action Obligation'], 3, labels=labels_3)
	# data_frame['even_bins_100'] = pd.cut(data_frame['Action Obligation'], 100, labels=labels_100)

	# Print Bin Counts
	pprint(data_frame['mm_bins'].value_counts())
	pprint(data_frame['even_bins_20'].value_counts())
	# pprint(data_frame['even_bins_10'].value_counts())
	# pprint(data_frame['even_bins_3'].value_counts())
	# pprint(data_frame['even_bins_100'].value_counts())

	data_frame['mm_bins'].hist()
	data_frame['even_bins_20'].hist()
	# data_frame['even_bins_10'].hist()
	# data_frame['even_bins_3'].hist()
	# data_frame['even_bins_100'].hist()


def main():
	fpds_clean = "FPDS_final.csv"

	data_frame = upload_data(fpds_clean)
	binning(data_frame)


if __name__ == "__main__":
	main()
