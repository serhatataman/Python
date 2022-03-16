import pandas as pd
import numpy as np
import scipy

import matplotlib.pyplot as plt
from pylab import rcParams
# import matplotlib_inline.config
import seaborn as sb

import sklearn
from sklearn import preprocessing
from sklearn.preprocessing import scale

rcParams['figure.figsize'] = [8, 4]
plt.style.use('seaborn-whitegrid')

# Scale and transform variables. You scale the variable so scales and magnitudes don't produce erroneous results.

# For example, if you have a sales data from 1989 and 2016 and you want to compare them,
# you can't just compare the values.
# There have been few changes since then, for example inflation and trust of the product... We need to scale the data
# so that the values are comparable.

# We can use scikit-learn to Scale, Center, Normalize, Bin, and Impute the data.

# Normalizing and transforming features with MinMaxScalar() and fit_transform()

address = "../../Data/mtcars.csv"

cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

print("\nCars dataset: \n" + str(cars.head()))

# sb.pairplot(cars)  # This prints out all the tables
# plt.show(block=True)

mpg = cars.mpg
plt.plot(mpg)
plt.show(block=True)

print("\nSummary statistics of mpg: \n" + str(mpg.describe()))

# get the mpg variable and reshape it as one column matrix
mpg_matrix = mpg.values.reshape(-1, 1)

# MinMaxScalar() is the function we use to transform our variable by scaling it to a defined range.
# Default range is (0, 1)

scaled = preprocessing.MinMaxScaler()

scaled_mpg = scaled.fit_transform(mpg_matrix)
plt.plot(scaled_mpg)
plt.show(block=True)








