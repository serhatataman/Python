import matplotlib_inline.config
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sb
from pylab import rcParams

import scipy
from scipy.stats.stats import pearsonr, spearmanr
from scipy.stats import chi2_contingency

# THE SPEARMAN RANK CORRELATION AND CHI-SQUARE TEST FOR INDEPENDENCE


rcParams['figure.figsize'] = [8, 4]
plt.style.use('seaborn-whitegrid')

address = "../../Data/mtcars.csv"

cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

print("\nCars dataset: \n" + str(cars.head()))

# sb.pairplot(cars)  # This prints out all the tables
# plt.show(block=True)

X = cars[['cyl', 'vs', 'am', 'gear']]
sb.pairplot(X)
plt.show(block=True)

# isolate variables
cyl = cars['cyl']
vs = cars['vs']
am = cars['am']
gear = cars['gear']

# The Spearman Rank Correlation

spearmanr_coefficient, p_value = spearmanr(cyl, vs)
print("\nSpearman Rank Correlation Coefficient for vs %0.3f" % spearmanr_coefficient)

spearmanr_coefficient, p_value = spearmanr(cyl, am)
print("\nSpearman Rank Correlation Coefficient for am %0.3f" % spearmanr_coefficient)

spearmanr_coefficient, p_value = spearmanr(cyl, gear)
print("\nSpearman Rank Correlation Coefficient for gear %0.3f" % spearmanr_coefficient)


# Chi-square test for independence
# We need a value that is greater than 0.05 in order to conclude that values are independent of one another
# Since none of the p values below are greater than 0.05, we decide that all values ARE CORRELATED and NOT INDEPENDENT

# create a crosstab
table = pd.crosstab(cyl, am)
chi2, p, dof, expected = chi2_contingency(table.values)
print("\nFor cyl-am Chi-square statistic %0.3f p_value %0.3f" % (chi2, p))

table = pd.crosstab(cyl, vs)
chi2, p, dof, expected = chi2_contingency(table.values)
print("\nFor cyl-vs Chi-square statistic %0.3f p_value %0.3f" % (chi2, p))

table = pd.crosstab(cyl, gear)
chi2, p, dof, expected = chi2_contingency(table.values)
print("\nFor cyl-gear Chi-square statistic %0.3f p_value %0.3f" % (chi2, p))




