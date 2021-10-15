import numpy as np

a=[14, 3, 0.8]
b=[2, 6, 0.8]


def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2

    distance = np.sqrt(sum)
    print(distance)
    return distance


dist(a, b)