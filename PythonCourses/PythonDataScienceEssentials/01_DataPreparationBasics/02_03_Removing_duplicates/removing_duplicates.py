import numpy as np
import pandas as pd
from pandas import Series, DataFrame


df_obj = DataFrame({"column 1": [1, 1, 2, 2, 3, 3, 3],
                    "column 2": ["a", "a", "b", "b", "c", "c", "c"],
                    "column 3": ["A", "A", "B", "B", "C", "C", "C"]})
print("\nDataFrame original:")
print(df_obj)

# Find duplicate rows
# If a row is the first occurrence of a particular combination of values in a DataFrame, it is called a unique row.
# therefore, it is not a duplicate, and it returns FALSE
print("\nDuplicate rows:")
print(df_obj.duplicated())

# Drop duplicate rows
print("\nDataFrame without duplicate rows:")
print(df_obj.drop_duplicates())


df_obj = DataFrame({"column 1": [1, 1, 2, 2, 3, 3, 3],
                    "column 2": ["a", "a", "b", "b", "c", "c", "c"],
                    "column 3": ["A", "A", "B", "B", "C", "D", "C"]})

# Drop duplicates from only a specific column
print("\nDataFrame without duplicate rows from a specific column:")
print(df_obj.drop_duplicates(["column 3"]))

