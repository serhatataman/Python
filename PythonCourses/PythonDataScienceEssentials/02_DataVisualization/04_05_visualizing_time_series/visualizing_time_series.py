
import os
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams["figure.figsize"] = 5, 4

# The simplest time series plot
address = "../../Data/Superstore-Sales.csv"

df = pd.read_csv(address, index_col="Order Date", encoding="cp1252", parse_dates=True)
print(df.head())


df["Order Quantity"].plot()
plt.show(block=True)

# sample -> get random samples from the data
df2 = df.sample(n=100, random_state=25, axis=0)

plt.xlabel("Order Date")
plt.ylabel("Order quantity")
# add title to the plot
plt.title("Superstore Sales")

df2["Order Quantity"].plot()
plt.show(block=True)




