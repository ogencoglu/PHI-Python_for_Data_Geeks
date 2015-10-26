import numpy as np
from sklearn import datasets
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split

if __name__ == '__main__':

    iris = datasets.load_iris()
    iris_feats = iris.data
    iris_tar = iris.target
    
    # Split into test and training
    X_train, X_test, y_train, y_test = train_test_split(iris_feats, iris_tar, test_size=.2)
    
    # Classify
    classifier = SVC(C = 0.5)
    classifier.fit(X_train, y_train)
    print(100 * sum(classifier.predict(X_test) == y_test) / float(y_test.shape[0]))