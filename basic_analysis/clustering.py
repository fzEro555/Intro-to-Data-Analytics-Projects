import pandas as pd
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as shc
import sys
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
import numpy as np
from pprint import pprint
from sklearn.metrics import calinski_harabaz_score
from sklearn import preprocessing
from sklearn import decomposition


def add_data(csv_file: str) -> pd.core.frame.DataFrame:
    # grab data from csv file, return cleaned data frame
    data_frame = pd.read_csv(csv_file, sep=',', encoding='latin1')
    return data_frame


def hierarchical_clustering(data_frame: pd.core.frame.DataFrame, n_clusters):
    print("HIERARCHICAL CLUSTERING")
    x = data_frame.values
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    normalized_data_frame = pd.DataFrame(x_scaled)

    agglomerative_clustering = AgglomerativeClustering(n_clusters, affinity='euclidean', linkage='ward')

    cluster_labels = agglomerative_clustering.fit_predict(normalized_data_frame)

    calinski_harabaz_avg = calinski_harabaz_score(normalized_data_frame, cluster_labels)
    print("The average calinski_harabaz_score is :", calinski_harabaz_avg)

    pca2D = decomposition.PCA(2)
    # Turn the data into two columns with PCA
    plot_columns = pca2D.fit_transform(normalized_data_frame)
    # Plot using a scatter plot and shade by cluster label
    plt.scatter(x=plot_columns[:, 0], y=plot_columns[:, 1], c=cluster_labels)
    plt.show()


def kmeans_clustering(data_frame: pd.core.frame.DataFrame, n_clusters):
    print("KMEANS CLUSTERING")
    x = data_frame.values
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    normalized_data_frame = pd.DataFrame(x_scaled)
    kmeans = KMeans(n_clusters)

    cluster_labels = kmeans.fit_predict(normalized_data_frame)

    calinski_harabaz_avg = calinski_harabaz_score(normalized_data_frame, cluster_labels)
    print("The average calinski_harabaz_score is :", calinski_harabaz_avg)
    centroids = kmeans.cluster_centers_
    pprint(cluster_labels)
    pprint(centroids)

    pca2D = decomposition.PCA(2)
    # Turn the data into two columns with PCA
    plot_columns = pca2D.fit_transform(normalized_data_frame)
    # Plot using a scatter plot and shade by cluster label
    plt.scatter(x=plot_columns[:, 0], y=plot_columns[:, 1], c=cluster_labels)
    plt.show()


def dbscan_clustering(data_frame: pd.core.frame.DataFrame):
    print("DBSCAN clustering")
    x = data_frame.values
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    normalized_data_frame = pd.DataFrame(x_scaled)

    DBSCAN_clustering = DBSCAN()

    cluster_labels = DBSCAN_clustering.fit_predict(normalized_data_frame)
    calinski_harabaz_avg = calinski_harabaz_score(normalized_data_frame, cluster_labels)
    print("The average calinski_harabaz_score is :", calinski_harabaz_avg)

    pca2D = decomposition.PCA(2)
    # Turn the data into two columns with PCA
    plot_columns = pca2D.fit_transform(normalized_data_frame)
    # Plot using a scatter plot and shade by cluster label
    plt.scatter(x=plot_columns[:, 0], y=plot_columns[:, 1], c=cluster_labels)
    plt.show()


def main():
    # reddit_clean = "../reddit/reddit_cleaned_data.csv"
    # nytimes_clean = "../nytimes/nytimes_cleaned.csv"

    data = pd.read_csv("FPDS.csv")
    data = data.drop(['date'], axis=1)

    kmeans_clustering(data, 4)
    hierarchical_clustering(data, 4)
    dbscan_clustering(data)


if __name__ == "__main__":
    main()

