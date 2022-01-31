import pandas as pd
from pandas import Series, DataFrame
import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt
from matplotlib import rcParams


# Create line chart

x = range(1, 10)
y = [1, 2, 3, 4, 0, 4, 3, 2, 1]

# demonstrate our first line chart
# plt.plot(x, y)
# plt.show(block=True) is displaying the chart and stopping the continuation of debugging
# plt.show(block=True)


address = "../../Data/mtcars.csv"
cars = pd.read_csv(address)

# create a list of column names (which are already in the csv file)
cars.columns = ["car_names", "mpg", "cyl", "disp", "hp", "drat", "wt", "qsec", "vs", "am", "gear", "carb"]

print("\nCars original:")
print(cars.head())

# plotting mpg
mpg = cars["mpg"]
mpg.plot()
# plt.show(block=True)

# generate linechart which plotting 3 values
# select values we want to plot out
df = cars[["cyl", "wt", "mpg"]]
df.plot()
plt.show(block=True)


# create a bar-chart 
plt.bar(x, y)
plt.show(block=True)


# plotting mpg as bar chart
# NOTE: if you want to print the bar chart horizontally, you need to set kind="barh"
mpg.plot(kind="bar")
plt.show(block=True)


# create pie chart
x = [1, 2, 3, 4, 0.5]
plt.pie(x)
plt.show(block=True)

# saving a plot
plt.pie(x)
plt.savefig("pie_chart.png")
plt.show(block=True)







