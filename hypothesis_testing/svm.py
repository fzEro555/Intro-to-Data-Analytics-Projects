from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import pandas as pd


def run_svm(X, Y):
    # split train and test
    test_size = 0.20
    seed = 7
    X_train, X_validate, Y_train, Y_validate = train_test_split(X, Y, test_size=test_size, random_state=seed)

    # set up svm
    svm_model = svm.LinearSVC()
    svm_model.fit(X_train, Y_train)

    # cross validation
    num_folds = 10
    scoring = 'accuracy'

    kfold = KFold(n_splits=num_folds, random_state=seed, shuffle=False)

    cv_results = cross_val_score(svm_model, X_train, Y_train, cv=kfold, scoring=scoring)

    # print cross-validation score
    print("\nSVM cross-validation score: {} ({})".format(cv_results.mean(), cv_results.std()))

    # use trained model to predict
    predictions = svm_model.predict(X_validate)

    print(accuracy_score(Y_validate, predictions))
    print()
    print(confusion_matrix(Y_validate, predictions))
    print()
    print(classification_report(Y_validate, predictions))

    return


# count and print the distribution of label in the data set
def label_distribution(Y):
    n_true = sum(Y)
    n_false = len(Y) - n_true
    print("\nNumber of days have hurricanes occurrence {}, number of days that don't {}".format(n_true, n_false))
    return


def load_data():
    # load data into data frame
    data_frame = pd.read_csv("../basic_analysis/reddit_anova.csv", sep=',')
    print(data_frame.head())
    # take out x and y
    value = data_frame.values
    X = value[:, 2:11]
    Y = [v is 0 for v in value[:, 11]]
    return X, Y


def main():
    x, y = load_data()
    label_distribution(y)
    run_svm(x, y)


if __name__ == "__main__":
    main()
