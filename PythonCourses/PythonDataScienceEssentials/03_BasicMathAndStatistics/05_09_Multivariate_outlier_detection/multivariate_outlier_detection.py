import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb

rcParams['figure.figsize'] = [5, 4]
sb.set_style('whitegrid')

# MULTIVARIATE OUTLIER DETECTION:
# Use multivariate methods to find the outliers that only show up within combinations of observations from
# TWO OR MORE different variables.

address = "../../Data/iris.data.csv"

# Visually inspecting boxplots
df = pd.read_csv(filepath_or_buffer=address, header=None, sep=',')
df.columns = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species"]

# Get data from the first column to the fourth column. And only get values
data = df.iloc[:, 0:4].values
# Get values of the last column
target = df.iloc[:, 4].values

print("\nFirst 5 records:\n" + str(df[:5]))

# Let's generate a boxplot in order to see outliers
sb.boxplot(x='Species', y='Sepal Length', data=df, palette='hls')
plt.show()

# Looking at the scatterplot matrix
sb.pairplot(df, hue='Species', palette='hls')
plt.show()

# if we look at the scatterplot matrix, we can see that there are some outliers. After detecting these,
# we can take necessary steps to remove them.



