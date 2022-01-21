import pandas as pd

csv_file = pd.read_csv("../Data/mtcars.csv")

grouped = csv_file.groupby("am")
grouped_by_mean = grouped.mean()

print("\nGrouped by am:")
print(grouped_by_mean["mpg"])


# Create subset
subset = csv_file[["mpg", "disp", "hp", "wt"]]
print("\nSubset of csv file:")
print(subset)





