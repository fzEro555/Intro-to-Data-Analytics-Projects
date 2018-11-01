from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
import pandas as pd


def run_svm(X, Y):
    # split train and test
    test_size = 0.20
    seed = 7
    X_train, X_validate, Y_train, Y_validate = train_test_split(X, Y, test_size=test_size, random_state=seed)

    # set up svm
    svm_model = svm.SVC(kernel='linear', C=1)

    # cross validation
    num_folds = 10
    num_instances = len(X_train)
    scoring = 'accuracy'

    kfold = KFold(n_splits=num_folds, random_state=seed, shuffle=False)

    cv_results = cross_val_score(svm_model, X_train, Y_train, cv=kfold, scoring=scoring)

    # print results
    print("SVM cv score: {} ({})".format(cv_results.mean(), cv_results.std()))
    return


def load_data():
    # load data into data frame
    data_frame = pd.read_csv("./reddit.csv", sep=',')
    print(data_frame.head())
    # take out x and y
    value = data_frame.values
    X = value[:, 2:11]
    Y = [val is 0 for val in value[:, 11]]
    return X, Y


if __name__ == "__main__":
    x, y = load_data()
    run_svm(x ,y)
    # input("\nany")
