import math

a=[14, 3, 0.8]
b=[2, 6, 0.8]


def euclidean_distance():
    distance = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)
    print(distance)

euclidean_distance()