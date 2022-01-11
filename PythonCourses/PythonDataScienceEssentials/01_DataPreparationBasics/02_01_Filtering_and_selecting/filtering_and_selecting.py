import numpy as np
from pandas import Series, DataFrame

# We want 8 a range of values from 0 to 7, then give info about their index and columns
series_obj = Series(np.arange(8), index=["row 1", "row 2", "row 3", "row 4", "row 5", "row 6", "row 7", "row 8"])
print(series_obj)

print("Row 7 includes: " + str(series_obj["row 7"]))

# Be careful when printing a series object, we create TWO square brackets [[ like so
print("Row 1 and row 8 includes: \n" + str(series_obj[[0, 7]]))

# a series of 36 random generated numbers. If you want to create the same randomly generated numbers,
# you can use the np.random.seed() function to set the seed.
np.random.seed(25)

# reshape(6, 6) creates a 6x6 matrix
df_obj = DataFrame(np.random.rand(36).reshape(6, 6),
                   index=["row 1", "row 2", "row 3", "row 4", "row 5", "row 6"],
                   columns=["column 1", "column 2", "column 3", "column 4", "column 5", "column 6"])

print("\nDataFrame Object: \n" + str(df_obj))

# We can use the .loc[] method to select rows and columns
print(df_obj.loc[["row 2", "row 5"], ["column 5", "column 2"]])

# DATA SLICING

# select every row between row 3 and row 7
print("\n Rows between row 3 and row 7")
print(series_obj["row 3": "row 7"])

# Get all the values that are smaller than 0.2
print("\n Values smaller than 0.2")
print(df_obj < .2)


# Filtering with scalar values
print("\n Values greater than 6: ")
print(series_obj[series_obj > 6])


# Setting values with scalars. Meaning that we will get all rows and set each one 8
print("\n Setting values with scalars")
series_obj["row 1", "row 5", "row 8"] = 8
print(series_obj)





