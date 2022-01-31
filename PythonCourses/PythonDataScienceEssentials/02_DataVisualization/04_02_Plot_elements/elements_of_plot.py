# Plot elements add context to your plots, so the plot is more readable.

import os
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt
from matplotlib import rcParams

# assign figure size dimensions
rcParams["figure.figsize"] = 5, 4

# Define axes, ticks and grids
x = range(1, 10)
y = [1, 2, 3, 4, 0, 4, 3, 2, 1]

# generate a figure
fig = plt.figure()
# add axes
ax = fig.add_axes([.1, .1, 1, 1])

# ax.plot(x, y)
# plt.show(block=True)


# generate a figure
fig = plt.figure()
# add axes
ax = fig.add_axes([.1, .1, 1, 1])
# define limits
ax.set_xlim([1,9])
ax.set_ylim([0,5])

ax.set_xticks([0,1,2,4,5,6,8,9,10])
ax.set_yticks([0,1,2,3,4,5])

# add grid
ax.grid()

ax.plot(x, y)
plt.show(block=True)

# Generate multiple plots in one figure with subplots
fig = plt.figure()
fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.plot(x)
ax2.plot(x, y)
plt.show(block=True)


















