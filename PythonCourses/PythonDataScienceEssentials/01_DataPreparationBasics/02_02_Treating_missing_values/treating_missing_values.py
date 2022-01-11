import numpy as np
from pandas import Series, DataFrame

# Figure out what is missing in the data
missing = np.nan

series_obj = Series(["row 1", "row 2", missing, "row 4", "row 5", "row 6", missing, "row 8"])
print(series_obj)

# Check for missing values
print("\nCheck for missing values:")
print(series_obj.isnull())

# Fill missing values
np.random.seed(25)
# Create a random 6x6 array of numbers
dataFrame_obj = DataFrame(np.random.rand(36).reshape(6, 6))
print("\nOriginal dataframe:")
print(dataFrame_obj)

# From 3rd row to 5th row, for column zero, replace all values with missing
dataFrame_obj.loc[3:5, 0] = missing
# From 1st row to 4th row, for column 5, replace all values with missing
dataFrame_obj.loc[1:4, 5] = missing
print("\nDataframe with missing values:")
print(dataFrame_obj)

# Fill all the missing values with zero
filled_dataFrame_obj = dataFrame_obj.fillna(0)
print("\nDataFrame with zero values filled:")
print(filled_dataFrame_obj)

# Change zero values in column index 0 to 0.1 and in column index 5 to 1.25
# We achieve this by introducing a dictionary
filled_dataFrame_obj = dataFrame_obj.fillna({0: 0.1, 5: 1.25})
print("\nDataFrame fill values according to a dictionary to a specific column:")
print(filled_dataFrame_obj)


# ffill: forward fill. Fill missing values with the next available value
# bfill: backward fill. Fill missing values with the previous available value

filled_dataFrame_obj = dataFrame_obj.fillna(method="ffill")
print("\nDataFrame fill values according to ffill:")
print(filled_dataFrame_obj)


# Count missing values
# regenerate the dataframe with missing values
np.random.seed(25)
dataFrame_obj = DataFrame(np.random.rand(36).reshape(6, 6))
dataFrame_obj.loc[3:5, 0] = missing
dataFrame_obj.loc[1:4, 5] = missing

# Attention: The sum of the missing values returns an array with column indexes and missing value counts!
print("\nCount missing values per column:")
print(dataFrame_obj.isnull().sum())


# Filter out missing values
# Drop rows with missing values

df_with_no_missing_values = dataFrame_obj.dropna()
print("\nDataFrame with no missing value rows:")
print(df_with_no_missing_values)

# Drop the columns where at least one value is missing
df_with_no_missing_values = dataFrame_obj.dropna(axis="columns")
print("\nDataFrame with no missing value columns:")
print(df_with_no_missing_values)






