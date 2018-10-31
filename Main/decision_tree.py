import pandas as pd
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn import preprocessing
import numpy as np
from sklearn.preprocessing import Normalizer


def upload_data(csv_file: str) -> pd.core.frame.DataFrame:
	# grab data from csv file provided
	data_frame = pd.read_csv(csv_file, sep=',', encoding='latin1')

	print(data_frame.head())

	# cleaning

	data_frame['year'], data_frame['month'], data_frame['day'] = zip(
		*data_frame['news date'].apply(lambda x: x.split('-')))

	del data_frame['news date']

	print(data_frame.head())

	col_name = list(data_frame.head(0))

	# normalize data
	norm_price = Normalizer().fit_transform(data_frame[])

	norm_df = pd.core.frame.DataFrame(norm_data)
	norm_df.columns = col_name

	print(norm_df.head())

	# print(norm_data)

	# scatter plot of vars
	scatter_matrix(norm_df)
	plt.show()

	# return normalized df
	return norm_df


# separate test/train data
def separate_data(data_frame: pd.core.frame.DataFrame) -> tuple:
	val_array = data_frame.values
	X = val_array[:, 0:4]
	Y = val_array[:, 4]
	test_size = 0.20
	seed = 7
	return train_test_split(X, Y, test_size=test_size, random_state=seed)


def run_decision_tree(split_data: tuple):
	# Setup 10-fold cross validation to estimate the accuracy of different models
	# Split data into 10 parts
	# Test options and evaluation metric

	X_train, X_validate, Y_train, Y_validate = split_data
	num_folds = 10
	num_instances = len(X_train)
	seed = 7
	scoring = 'accuracy'

	decision_tree_model = DecisionTreeClassifier()

	results = []
	names = []

	kfold = KFold(n_splits=num_folds, random_state=seed, shuffle=False)
	cv_results = cross_val_score(decision_tree_model, X_train, Y_train, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)


if __name__ == "__main__":
	nytimes_clean = "../nytimes/nytimes_cleaned.csv"

	data_frame = upload_data(nytimes_clean)

	run_decision_tree(separate_data(data_frame))
