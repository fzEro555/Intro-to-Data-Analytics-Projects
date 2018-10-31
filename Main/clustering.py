import pandas as pd
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as shc
import sys
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
import numpy as np


def add_data(csv_file: str) -> pd.core.frame.DataFrame:
	# grab data from csv file, return cleaned data frame
	data_frame = pd.read_csv(csv_file, sep=',', encoding='latin1')

	# data_frame['comment_date'], data_frame['comment_time'] = zip(
	# 	*data_frame['Comment_Time'].apply(lambda x: x.split(' ')))
	#
	# data_frame['year'], data_frame['month'], data_frame['day'] = zip(
	# 	*data_frame['comment_date'].apply(lambda x: x.split('-')))
	return data_frame


def plot_data(data: pd.core.frame.DataFrame):
	######################################################
	# Plot the data
	######################################################

	# Histogram
	data.hist()
	plt.show()

	# Scatterplots to look at 2 variables at once
	# scatter plot matrix
	scatter_matrix(data)
	plt.show()


def hierarchical_clustering(data_frame: pd.core.frame.DataFrame, attr_list, n_clusters):
	print(data_frame.head())
	cluster = AgglomerativeClustering(n_clusters, affinity='euclidean', linkage='ward')

	cluster.fit_predict(data_frame)
	print(cluster.labels_)
	print(cluster)

	plt.scatter(data_frame['occurrence of hurricane'], data_frame['occurrence of maria'], c=cluster.labels_, cmap='rainbow')


def kmeans_clustering(data_frame: pd.core.frame.DataFrame, attr_list, n_clusters):
	print("KMEANS CLUSTERING")
	kmeans = KMeans(n_clusters=2, random_state=0).fit(data_frame)
	clusters = kmeans.predict(data_frame)

	centroids = kmeans.cluster_centers_

	plt.scatter(data_frame['occurrence of hurricane'], data_frame['occurrence of maria'], c=kmeans.labels_, cmap='rainbow')


def dbscan_clustering(data_frame: pd.core.frame.DataFrame, attr_list, n_clusters):
	print("DBSCAN clustering")
	clustering = DBSCAN(eps=3, min_samples=2).fit(data_frame)
	labels = clustering.labels_
	plt.scatter(data_frame['occurrence of hurricane'], data_frame['occurrence of maria'], c=labels,
				cmap='rainbow')

def get_attr(data_frame: pd.core.frame.DataFrame, attr_list):
	# del data_frame['comment_time']
	# del data_frame['Submission_Time']
	# del data_frame['Submission_Content']
	# del data_frame['Hurricane_Name']
	# del data_frame['comment_date']
	# del data_frame['Comment_Content']
	# del data_frame['Comment_Time']
	# del data_frame['Submission_Title']
	# del data_frame['Unnamed: 0']
	#
	# del data_frame['Total_Comment_Number']
	# del data_frame['day']

	del data_frame['news date']
	del data_frame['occurrence of irma']
	del data_frame['occurrence of harvey']

	return data_frame

if __name__ == "__main__":
	reddit_clean = "../reddit/reddit_cleaned_data.csv"
	nytimes_clean = "../nytimes/nytimes_cleaned.csv"

	sample_df = add_data(nytimes_clean)
	sample_df = get_attr(sample_df, [])
	plot_data(sample_df)

	# hierarchical_clustering(sample_df, [], 5)
	# kmeans_clustering(sample_df, [], 5)
	dbscan_clustering(sample_df, [], 5)