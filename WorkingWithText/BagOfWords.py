# Your task is to write a function that calculates the distances
# (or differences) between a pair of lines in the This Little Piggy rhyme.
#
# Every row in the list data represents one line in the rhyme.
#
# When you run the code, you see that the output of the whole program is a list of lists.
# When your function works correctly, each list will contain
# the distances between a single row and all the other rows in data.
#
# Note that the program will compare every row also with itself.
# In this case – when the compared rows are the same – their distance will be zero.
#
# You can use the function abs(x-y) to calculate the distance between numbers x and y,
# where x comes from list row1 and y comes from row2.
#
# Your program must work with any text, not only with the rhyme This Little Piggy.

# this data here is the bag of words representation of This Little Piggy
data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]


def distance(row1, row2):
    # fix this function so that it returns
    # the sum of differences between the occurrences
    # of each word in row1 and row2.
    # you can assume that row1 and row2 are lists with equal length, containing numeric values.
    result = 0
    for i in range(len(row1)):
        result = result + abs(row1[i]-row2[i])

    return result


def all_pairs(data):
    # this calls the distance function for all the two-row combinations in the data
    # you do not need to change this
    dist = [[distance(sent1, sent2) for sent1 in data] for sent2 in data]
    print(dist)


all_pairs(data)
