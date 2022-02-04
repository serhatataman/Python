import os
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sb


rcParams["figure.figsize"] = 5, 4

sb.set_style("whitegrid")

address = "../../Data/mtcars.csv"
cars = pd.read_csv(address)

# create a list of column names (which are already in the csv file)
cars.columns = ["car_names", "mpg", "cyl", "disp", "hp", "drat", "wt", "qsec", "vs", "am", "gear", "carb"]

# set index to cars
cars.index = cars.car_names
mpg = cars["mpg"]
# plot out as histogram
mpg.plot(kind="hist")

# Another way to create histogram is to call hist function
plt.hist(mpg)

# use seaborn to create a histogram
sb.displot(mpg)

# Let's create some Scatterplots
cars.plot(kind="scatter", x="hp", y="mpg", c=["darkgray"], s=150)

# create scatterplot with Seaborn
sb.regplot(x="hp", y="mpg", data=cars, scatter=True)

# Generate scatterplot matrix with using seaborn
# NOTE: The following code will create a big plot with so many charts
# sb.pairplot(cars)
# plt.show(block=True)

# Let's create a subset of sb.pairplot(cars)
cars_subset = cars[["mpg", "disp", "hp", "wt"]]
sb.pairplot(cars_subset)


# Creating Boxplots (boxplots are useful when it comes to outlier detection)
cars.boxplot(column="mpg", by="am")
cars.boxplot(column="wt", by="am")

# Let's do boxplots in Seaborn
sb.boxplot(x = "am", y="mpg", data=cars, palette="hls")

plt.show(block=True)







