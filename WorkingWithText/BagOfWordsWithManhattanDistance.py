# Your task is to write a program that calculates the distances (or differences) between every pair of lines in the
# This Little Piggy rhyme and finds the most similar pair.
# Use the Manhattan distance (also called Taxicab distance) as your distance metric.
#
# You can start by building a numpy array to store all the distances.
# Notice that the diagonal elements in the array (elements at positions [i, j] with i=j) will be equal to zero.
# This happens because the program will compare every row also with itself. To avoid selecting those elements,
# you can assign the value np.inf (the maximum possible floating point value).
# To do this, it's necessary to make sure the type of the array is float.
#
# A quick way to get the index of the element with the
# lowest value in a 2D array (or in fact, any dimension) is by the function
#
# np.unravel_index(np.argmin(dist), dist.shape))
#
# where dist is the 2D array. This will return the index as a list of length two.
# If you're curious,
# here's an intuitive explanation (https://stackoverflow.com/questions/48135736/what-is-an-intuitive-explanation-of-np-unravel-index)
# of the function, and here's its documentation (https://numpy.org/doc/stable/reference/generated/numpy.unravel_index.html).

import numpy as np

data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]


def find_nearest_pair(data):
    N = len(data)
    dist = np.empty((N, N), dtype=float)
    new_data = all_pairs(data)
    for i in range(len(new_data)):
        for j in range(len(new_data[i])):
            if i == j:
                new_data[i][j] = np.Inf

    a = np.unravel_index(np.argmin(new_data), dist.shape)

    print(a)


def distance(row1, row2):
    result = 0
    for i in range(len(row1)):
        result = result + abs(row1[i]-row2[i])
    return result


def all_pairs(data):
    return [[distance(sent1, sent2) for sent1 in data] for sent2 in data]


find_nearest_pair(data)
