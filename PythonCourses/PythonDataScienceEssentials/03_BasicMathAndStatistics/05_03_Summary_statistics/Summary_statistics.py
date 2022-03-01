import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import scipy
from scipy import stats

# Generating summary statistics using pandas and scipy

address = "../../Data/mtcars.csv"

cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

print(cars.head())

# Looking at summary statistics that describe a variable's numeric values
# sum up all the values in columns
print("Cars sum columns: " + str(cars.sum()))

# sum up all the values in rows
# print("Cars sum rows: " + str(cars.sum(axis=1))) # deprecated function
print("\nCars sum rows: " + str(cars.sum(axis=1, numeric_only=True))) # sum up only numeric values

# Median (the middle value)
print("\nCars median: " + str(cars.median(numeric_only=True)))


# Mean = average value for each value in cars dataframe
print("\nCars mean value: " + str(cars.mean(numeric_only=True)))


# Max = greatest value in each of the variables
print("\nCars max value: " + str(cars.max()))


# index value of the row that includes the maximum value
mpg = cars.mpg
print("\nThe index number of the row which holds the maximum value in the mpg variable: " + str(mpg.idxmax()))


# Looking at summary statistics that describe variable distribution

# Standard deviation = The most fundamental summary statistic that describes distribution
print("\nStandard deviation for each column: " + str(cars.std(numeric_only=True)))


# Calculate variants
print("\nVariants for each column: " + str(cars.var(numeric_only=True)))

# Count unique values in a series -> it shows how many unique values are present in a dataset
gear = cars.gear
print("\nUnique values for each column: \n" + str(gear.value_counts()))







