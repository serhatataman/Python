import numpy as np
from io import StringIO

train_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

test_string = '''
36 3 15 1 850 196000
75 5 18 2 540 290000
'''


def main():
    np.set_printoptions(precision=1)  # this just changes the output settings for easier reading

    # Please write your code inside this function
    # read in the training data and separate it to x_train and y_train

    x_training = []
    y_training = []
    training_dataset = [y for y in train_string.split("\n")]
    for training_data in training_dataset:
        if training_data != '':
            x_training.append([int(a) for a in training_data.split(" ")[0:5]])
            y_training.append([int(a) for a in training_data.split(" ")[5:6]].pop())

    # fit a linear regression model to the data and get the coefficients
    c = np.linalg.lstsq(x_training, y_training, rcond=None)[0]

    # read in the test data and separate x_test from it
    x_test = []
    y_test = []
    test_dataset = [y for y in test_string.split("\n")]
    for test_data in test_dataset:
        if test_data != '':
            x_test.append([int(a) for a in test_data.split(" ")[0:5]])
            y_test.append([int(a) for a in test_data.split(" ")[5:6]].pop())


    # print out the linear regression coefficients
    print(c)

    # this will print out the predicted prices for the two new cabins in the test data set
    print(x_test @ c)


main()
