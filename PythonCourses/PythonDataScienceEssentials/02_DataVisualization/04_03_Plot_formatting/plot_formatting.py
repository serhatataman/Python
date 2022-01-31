# Coloring, marker styles, line styles

import os
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Defining plot color
x = range(1, 10)
y = [1, 2, 3, 4, 0.5, 4, 3, 2, 1]

# create bar chart
plt.bar(x, y)
plt.show(block=True)

# bar chart with color, width and alignment
wide = [.5, .5, .5, .9, .9, .9, .5, .5, .5]
color = ["salmon"]
plt.bar(x, y, width=wide, color=color, align="center")
plt.show(block=True)

address = "../../Data/mtcars.csv"
cars = pd.read_csv(address)

# create a list of column names (which are already in the csv file)
cars.columns = ["car_names", "mpg", "cyl", "disp", "hp", "drat", "wt", "qsec", "vs", "am", "gear", "carb"]

df = cars[["cyl", "mpg", "wt"]]

# let's change the color scheme
color_theme = ["darkgray", "lightsalmon", "powderblue"]
df.plot(color=color_theme)
plt.show(block=True)

# change colors according to rgb values
color_theme = ["#A9A9A9", "#FFA07A", "#B0E0E6", "#FFE4C4", "#BDB76B"]
z = [1, 2, 3, 4, .5]
plt.pie(z, colors=color_theme)
plt.show(block=True)

# Customize line styles
x1 = range(0, 10)
y1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# ds = drawing style, lw = line width
plt.plot(x, y, ds="steps", lw=5)
# ls = line style,
plt.plot(x1, y1, ls="--", lw=10)
plt.show(block=True)

# Setting plot markers
# mew = marker width
plt.plot(x, y, marker="1", mew=10)
plt.plot(x1, y1, marker="+", mew=15)
plt.show(block=True)




