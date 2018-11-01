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
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification


def upload_data(csv_file: str) -> pd.core.frame.DataFrame:
	# grab data from csv file provided
	# ************ final data wrong?
	data_frame = pd.read_csv(csv_file, sep=',', skiprows=363)

	# print(data_frame.head(364))

	# cleaning

	# data_frame['year'], data_frame['month'], data_frame['day'] = zip(
	# 	*data_frame['date'].apply(lambda x: x.split('-')))
	#
	# del data_frame['date']

	print(data_frame.head())

	# # normalize data
	# normalized = Normalizer().fit_transform(data_frame['day'])
	#
	# print(normalized, type(normalized))
	# print(data_frame.head())

	# print(norm_data)

	# scatter plot of vars
	scatter_matrix(data_frame)
	plt.show()

	# return normalized df
	return data_frame


# separate test/train data
def separate_data(data_frame: pd.core.frame.DataFrame) -> tuple:
	val_array = data_frame.values
	X = val_array[:, 1:5]
	Y = val_array[:, 5]

	print(X)
	print(Y)
	test_size = 0.20
	seed = 7
	X_train, X_validate, Y_train, Y_validate = train_test_split(X, Y, test_size=test_size, random_state=seed)

	return X_train, X_validate, Y_train, Y_validate


def run_decision_tree(split_data: tuple):
	# Setup 10-fold cross validation to estimate the accuracy of different models
	# Split data into 10 parts
	# Test options and evaluation metric

	X_train, X_validate, Y_train, Y_validate = split_data
	print(X_train)
	print(X_validate)
	print(Y_train)
	print(Y_validate)

	num_folds = 10
	num_instances = len(X_train)
	seed = 7
	scoring = 'accuracy'

	decision_tree_model = DecisionTreeClassifier()

	kfold = KFold(n_splits=num_folds, random_state=seed, shuffle=False)
	# cv_results = cross_val_score(decision_tree_model, X_train, Y_train, cv=kfold, scoring=scoring)
	# msg = "CART decision tree classifier: %f (%f)" % (cv_results.mean(), cv_results.std())
	# print(msg)


def run_random_forest_tree(split_data: tuple):
	X_train, X_validate, Y_train, Y_validate = split_data

	clf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
	clf.fit(X_train, Y_train)
	print(clf.predict(X_validate))



if __name__ == "__main__":
	combined_final = "combined_data.csv"

	data_frame = upload_data(combined_final)

	# run_decision_tree(separate_data(data_frame))

	run_random_forest_tree(separate_data(data_frame))
