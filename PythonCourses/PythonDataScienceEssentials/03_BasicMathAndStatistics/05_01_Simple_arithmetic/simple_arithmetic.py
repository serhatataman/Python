import numpy as np
from numpy.random import randn

# just get 2 digits after the decimal point
np.set_printoptions(precision=2)

# Create arrays
a = np.array([1, 2, 3, 4, 5, 6])
print("Array a: " + str(a))

b = np.array([[10, 20, 30], [40, 50, 60]])
print("Array b: " + str(b))

# Creating arrays via assignment
# create six random signed numbers
np.random.seed(25)
# we want 6 values
c = 36 * np.random.randn(6)
print("Array c: " + str(c))

# get numbers between 1 and 36 as an array
d = np.arange(1, 36)
print("Array d: " + str(d))





