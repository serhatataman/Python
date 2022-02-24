
# Multiplying matrices and basic linear algebra

import numpy as np
from numpy.random import randn

# Don't print out more than 2 decimal places
np.set_printoptions(precision=2)

# create 3x3 matrix
aa = np.array([[2., 4., 6.], [1., 3., 5], [10., 20., 30]])

print("Matrix aa: " + str(aa))

bb = np.array([[0., 1., 2.], [3., 4., 5], [6., 7., 8]])
print("Matrix bb: " + str(bb))

print("Multiplication of aa and bb arrays: " + str(aa*bb))

# THIS IS THE REAL MATRIX MULTIPLICATION METHOD
print("Dot function: " + str(np.dot(aa, bb)))


