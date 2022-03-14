import matplotlib_inline.config
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sb
from pylab import rcParams

import scipy
from scipy.stats.stats import pearsonr

# Pearson correlation: To uncover LINEAR relationships between variables.
# Checks if there are any correlations between them

rcParams['figure.figsize'] = [8, 4]
plt.style.use('seaborn-whitegrid')

# The Pearson correlation

address = "../../Data/mtcars.csv"

cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

# sb.pairplot(cars)  # This prints out all the tables
# plt.show(block=True)

# Create a subset of some of the values
X = cars[['mpg', 'hp', 'qsec', 'wt']]
sb.pairplot(X)
plt.show(block=True)

# Using scipy to calculate the Pearson correlation coefficient
mpg = cars['mpg']
hp = cars['hp']
qsec = cars['qsec']
wt = cars['wt']

# We are looking for a correlation between mpg variable and hp variable
pearsonr_coefficient, p_value = pearsonr(mpg, hp)
print("\nUsing scipy - PearsonR Correlation Coefficient for mpg and hp %0.3f" % pearsonr_coefficient)

pearsonr_coefficient, p_value = pearsonr(mpg, qsec)
print("\nUsing scipy - PearsonR Correlation Coefficient for mpg and qsec %0.3f" % pearsonr_coefficient)

pearsonr_coefficient, p_value = pearsonr(mpg, wt)
print("\nUsing scipy - PearsonR Correlation Coefficient for mpg and wt %0.3f" % pearsonr_coefficient)


# Using pandas to calculate the Pearson correlation coefficient
corr = X.corr()
# All of
print("\nUsing pandas - PearsonR Correlation Coefficient for each pair:")
print(corr)


# Using Seaborn to calculate the Pearson correlation coefficient
sb.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values)
plt.show(block=True)
