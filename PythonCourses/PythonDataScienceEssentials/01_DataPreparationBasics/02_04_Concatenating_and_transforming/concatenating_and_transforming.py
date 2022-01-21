# Concatenating is a way to combine two or more data sets together
# Transforming is a way to change the data in a format we want

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# np.arange(36) tells python to create an array of 36 numbers
df_obj = pd.DataFrame(np.arange(36).reshape(6, 6))
print("\nDataFrame df_obj:")
print(df_obj)


df_obj_2 = pd.DataFrame(np.arange(15).reshape(5, 3))
print("\nDataFrame df_obj_2:")
print(df_obj_2)


# Concatenate two data frames
pd.concat([df_obj, df_obj_2], axis=1)  # axis=1 means we are concatenating on the columns (meaning that the rows will be the same)
print("\nConcatenated DataFrame on the columns:")
print(pd.concat([df_obj, df_obj_2], axis=1))


pd.concat([df_obj, df_obj_2], axis=0)  # axis=0 means we are concatenating on the rows (meaning that the columns will be the same)
print("\nConcatenated DataFrame on the rows:")
print(pd.concat([df_obj, df_obj_2], axis=0))


# Drop rows
df_obj.drop([0, 2])  # drop row 0 and row 2
print("\nDropped row 0 and row 2:")
print(df_obj.drop([0, 2]))


# Drop columns
df_obj.drop([1, 3], axis=1)  # drop column 1 and column 3
print("\nDropped column 1 and column 3:")
print(df_obj.drop([1, 3], axis=1))


# Add data
# get series of values from zero to five
series_obj = Series(np.arange(6))
series_obj.name = "added_variable" # we declare the name so when we join it with DataFrame, the name appears as column name
print("\nSeries of new data with variable name:")
print(series_obj)

# Join them to our dataframe
variable_added = DataFrame.join(df_obj, series_obj)
print("\nJoined the newly created series with object:")
print(variable_added)

# Note: we can also use .append method to join 2 DataFrames/Series

# Sort data
# sort the data according to values in column 5
df_sorted = df_obj.sort_values(by=5, ascending=False)
print("\nSorted DataFrame:")
print(df_sorted)

