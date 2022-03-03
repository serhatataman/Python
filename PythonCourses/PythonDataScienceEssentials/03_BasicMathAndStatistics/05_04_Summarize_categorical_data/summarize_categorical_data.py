

import numpy as np
import pandas as pd


address = "../../Data/mtcars.csv"

cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

# let's set index for our cars dataset which is going to be car names.
cars.index = cars.car_names
print("\nCars dataset: \n" + str(cars.head()))

# Count all unique values for carburetors. This gives a result like: 10 cars have 4 carbs, 7 cars have 1 carbs etc.
carb = cars.carb
print("\nCarb values: \n" + str(carb.value_counts()))

# GroupBy -> To group a dataframe by its values in a particular column
# create a small subset
cars_cat = cars[['cyl', 'vs', 'am', 'gear', 'carb']]
print("\nSmall subset of cars: \n" + str(cars_cat.head()))
# GroupBy gears
gears_group = cars_cat.groupby('gear')
print("\nStatistical description of the grouping: \n" + str(gears_group.describe()))


# Transforming variables to categorical data type
# create a new column
cars['group'] = pd.Series(cars.gear, dtype="category")
print("\nNew group created and added to cars dataFrame:\n" + str(cars['group'].dtypes))


# CREATING CROSSTAB
# Describing categorical data with crosstabs
# Crosstab is a cross-tabulation of two or more features.
# By default, a crosstab table shows frequency counts for features
# In this example, we demonstrate how gears are broken up with respect to automatic and manual transmission.
# (am - manual transmission)
pd.crosstab(cars['am'], cars['gear'])
print("\nCrosstab for am and gears: \n" + str(pd.crosstab(cars['am'], cars['gear'])))

