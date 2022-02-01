
import os
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Labeling plot features

# the functional method:

x = range(1, 10)
y = [1, 2, 3, 4, .5, 4, 3, 2, 1]
plt.bar(x, y)
# create label
plt.xlabel("your x-axis label")
plt.ylabel("your y-axis label")
plt.show(block=True)

# let's do this in pie chart
z = [1, 2, 3, 4, .5]
veh_type = ["bicycle", "motorbike", "car", "van", "stroller"]
plt.pie(z, labels=veh_type)
plt.show(block=True)


# the object-oriented method:

address = "../../Data/mtcars.csv"
cars = pd.read_csv(address)

# create a list of column names (which are already in the csv file)
cars.columns = ["car_names", "mpg", "cyl", "disp", "hp", "drat", "wt", "qsec", "vs", "am", "gear", "carb"]
mpg = cars.mpg

# create figure
fig = plt.figure()
ax = fig.add_axes([.1, .1, 1, 1])
mpg.plot()

ax.set_xticks(range(32))

ax.set_xticklabels(cars.car_names, rotation=60, fontsize="medium")

ax.set_title("Miles per gallon of Cars in mtcars Dataset")

ax.set_xlabel("car names")
ax.set_ylabel("miles/gal")
plt.show(block=True)


# Adding a legend




