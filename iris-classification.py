from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def main():
    # Split the data into training and testing sets
    iris = datasets.load_iris()
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=0)

    # Create a random forest classifier
    clf = RandomForestClassifier(n_estimators=100, random_state=0)

    # Train the classifier
    clf.fit(x_train, y_train)

    predicted_labels = clf.predict(x_test)
    print(predited_labels)
    print(y_test)

    performance = clf.score(x_test, y_test)
    print(performance)


if __name__ == "__main__":
    main()
