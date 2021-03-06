
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

# The functional method
plt.pie(z)
plt.legend(veh_type, loc="best")
plt.show(block=True)



# The object-oriented method

fig = plt.figure()
ax = fig.add_axes([.1, .1, 1, 1])
mpg.plot()

ax.set_xticks(range(32))

ax.set_xticklabels(cars.car_names, rotation=60, fontsize="medium")

ax.set_title("Miles per gallon of Cars in mtcars Dataset")

ax.set_xlabel("car names")
ax.set_ylabel("miles/gal")

ax.legend(loc="best")
plt.show(block=True)

# Annotating your plot (labeling the point on chart)

print("MPG max: " + str(mpg.max()))

fig = plt.figure()
ax = fig.add_axes([.1, .1, 1, 1])
mpg.plot()

ax.set_xticks(range(32))

ax.set_xticklabels(cars.car_names, rotation=60, fontsize="medium")

ax.set_title("Miles per gallon of Cars in mtcars Dataset")

ax.set_xlabel("car names")
ax.set_ylabel("miles/gal")

ax.legend(loc="best")
# set limit for y axis
ax.set_ylim([0, 45])

# add tag name, provide the point and text pixels and choose the arrow color and size
ax.annotate("Toyota Corolla", xy=(19, 33.9), xytext=(21, 35),
            arrowprops=dict(facecolor="black", shrink=0.05))
plt.show(block=True)






