"""
Looking at classifying category of hurricane for hurricanes Irene, Harvey, and Maria
"""

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


def date_ranges(date: str) -> str:
	# first two dates from Irene --> category 1
	# second two Harvey --> category 4
	# final two Maria --> category 5
	# all else, no hurricane /
	date_list = ['2011-08-16', '2011-09-02',
				 '2017-08-12', '2017-09-08',
				 '2017-09-11', '2017-10-07']

	category = ""
	if date < date_list[0]:
		category = "none"
	if date_list[0] <= date <= date_list[1]:
		category = "category 1"
	if date_list[1] < date < date_list[2]:
		category = "none"
	if date_list[2] <= date <= date_list[3]:
		category = "category 4"
	if date_list[3] < date < date_list[4]:
		category = "none"
	if date_list[4] <= date <= date_list[5]:
		category = "category 5"
	if date > date_list[5]:
		category = "none"
	return category


def category_level(data_frame: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
	# classify storm hit on date based on date ranges
	for index, row in data_frame.iterrows():
		data_frame['storm_category'] = data_frame.apply(lambda row: date_ranges(row['date']), axis=1)


def upload_data(csv_file: str) -> pd.core.frame.DataFrame:
	# grab data from csv file provided
	data_frame = pd.read_csv(csv_file, sep=',')

	# df_shape = data_frame.shape
	# print(df_shape, df_shape[0], df_shape[1])

	# add categories to data (class will be predicting)

	category_level(data_frame)
	data_frame['storm_category'].fillna("none", inplace=True)

	print(data_frame.head())
	# scatter plot of vars
	# scatter_matrix(data_frame)
	# plt.show()
	return data_frame


# separate test/train data
def separate_data(data_frame: pd.core.frame.DataFrame) -> tuple:
	val_array = data_frame.values
	# 234 - reddit titles
	# 678 - reddit summaries
	# 10, 11, 12 nytimes titles
	# nytimes summaries
	# guardian titles
	# guardian summaries
	# contracts
	# amount
	# all
	# X = val_array[:, (2, 3, 4, 6, 7, 8, 10, 11, 12, 14, 15, 16, 18, 19, 20, 22, 23, 24, 26, 27, 28, 30, 31, 32)]

	X = val_array[:, (2, 3, 4, 10, 11, 12, 18, 19, 20, 26, 27, 28)]
	Y = val_array[:, 35]
	print(type(data_frame['storm_category'].unique().tolist()))
	classes = data_frame['storm_category'].unique().tolist()
	print("classes: {}".format(data_frame['storm_category'].unique().tolist()))
	print("class counts: {}".format(data_frame['storm_category'].value_counts()))
	print("x shape: {}".format(X.shape))
	print("y shape: {}".format(Y.shape))

	test_size = 0.20
	seed = 7
	X_train, X_validate, Y_train, Y_validate = train_test_split(X, Y, test_size=test_size, random_state=seed)

	return X_train, X_validate, Y_train, Y_validate


def run_decision_tree(split_data: tuple):
	# Setup 10-fold cross validation to estimate the accuracy of different models
	# Split data into 10 parts
	# Test options and evaluation metric
	print("CART decision tree...")
	X_train, X_validate, Y_train, Y_validate = split_data

	num_folds = 10
	seed = 7
	scoring = 'accuracy'

	decision_tree_model = DecisionTreeClassifier()
	decision_tree_model.fit(X_train, Y_train)
	kfold = KFold(n_splits=num_folds, random_state=seed, shuffle=False)
	cv_results = cross_val_score(decision_tree_model, X_train, Y_train, cv=kfold, scoring=scoring)
	msg = "CART decision tree classifier: %f (%f)" % (cv_results.mean(), cv_results.std())
	print(msg)

	predictions = decision_tree_model.predict(X_validate)

	print(accuracy_score(Y_validate, predictions))
	print(confusion_matrix(Y_validate, predictions))

	print(classification_report(Y_validate, predictions))


def run_random_forest_tree(split_data: tuple):
	print("random_forest tree...")
	X_train, X_validate, Y_train, Y_validate = split_data

	num_folds = 10
	num_instances = len(X_train)
	seed = 7
	scoring = 'accuracy'

	clf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
	clf.fit(X_train, Y_train)

	kfold = KFold(n_splits=num_folds, random_state=seed, shuffle=False)
	cv_results = cross_val_score(clf, X_train, Y_train, cv=kfold, scoring=scoring)
	msg = "Random forest tree classifier: %f (%f)" % (cv_results.mean(), cv_results.std())
	print(msg)

	predictions = clf.predict(X_validate)
	classes = data_frame['storm_category'].unique().tolist()

	print("random_forest tree...")
	print(accuracy_score(Y_validate, predictions))
	print(confusion_matrix(Y_validate, predictions))
	print(classification_report(Y_validate, predictions))


def main():
	combined_final = "combined_data.csv"

	data_frame = upload_data(combined_final)

	run_decision_tree(separate_data(data_frame))

	run_random_forest_tree(separate_data(data_frame))


if __name__ == "__main__":
	main()