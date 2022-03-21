import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from pylab import rcParams

rcParams['figure.figsize'] = [5, 4]

# EXTREME VALUE ANALYSIS FOR OUTLIERS

# Extreme value analysis using uni-variate methods

address = "../../Data/iris.data.csv"

df = pd.read_csv(filepath_or_buffer=address, header=None, sep=',')
df.columns = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species"]

# Use data slicing and select all the rows but only get first 4 columns. Then get values only.
X = df.iloc[:, 0:4].values

# Y is going to be our target
y = df.iloc[:, 4].values

# Print first 5 records of the dataframe
print("\nFirst five records of dataframe: \n" + str(df[:5]))

# IDENTIFYING OUTLIERS FROM TUKEY BOXPLOTS. (yes, the name is Tukey)

# Create boxplot automatically and return a dictionary
df.boxplot(return_type='dict')
plt.plot()
plt.show(block=True)

# Use filtering and comparing operations to isolate outliers (that are found in Sepal_Width)
# from the rest of the dataframe
Sepal_Width = X[:, 1]  # isolate Sepal_Width column
iris_outliers = (Sepal_Width > 4)  # isolate these records where Sepal_Width is greater than 4 so we can understand what's really happening


