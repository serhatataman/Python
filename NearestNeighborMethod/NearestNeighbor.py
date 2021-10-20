# The program below uses the library sklearn to generate a random dataset.
# Each sample in the dataset has two input features X and one binary output class y.
# We can think of a sample as a cabin, with its size and price as its input features,
# and whether we like it (1) or not (0) as its output class.

# The program's goal is to classify the cabins based on their nearest neighbor's class.
# That is, predict whether we would like a cabin based on
# our opinion of another cabin with the most similar input features.

# The program first generates the random dataset and splits it into training and test sets.
# Then, for each cabin in the test set,
# it identifies its nearest neighbor from the cabins in the train set using the distance function.
# However, the program has very high standards and dislikes all the cabins y_predict[i] = 0.

# Your goal is to make the program smarter
# by predicting the output class (y_predict) for each cabin in the test set
# based on the output class (y_train) of its nearest neighbor.


import numpy as np
from sklearn.datasets import make_blobs
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# create random data with two classes
X, y = make_blobs(n_samples=16, n_features=2, centers=2, center_box=(-2, 2))

# scale the data so that all values are between 0.0 and 1.0
X = MinMaxScaler().fit_transform(X)

# split two data points from the data as test data and
# use the remaining n-2 points as the training data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=2)

# place-holder for the predicted classes
y_predict = np.empty(len(y_test), dtype=np.int64)

# produce line segments that connect the test data points
# to the nearest neighbors for drawing the chart
lines = []


# distance function
def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi) ** 2
    return np.sqrt(sum)


def main(X_train, X_test, y_train, y_test):
    global y_predict
    global lines

    # process each of the test data points
    for i, test_item in enumerate(X_test):
        # calculate the distances to all training points
        distances = [dist(train_item, test_item) for train_item in X_train]

        # find the index of the nearest neighbor
        nearest = np.argmin(distances)

        # create a line connecting the points for the chart
        lines.append(np.stack((test_item, X_train[nearest])))

        # add your code here:
        y_predict[i] = y_train[nearest]

    print(y_predict)


main(X_train, X_test, y_train, y_test)
