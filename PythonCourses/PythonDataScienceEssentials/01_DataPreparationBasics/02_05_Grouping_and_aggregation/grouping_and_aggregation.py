# PythonCourses/PythonDataScienceEssentials/05_AnalyticsWithPlotly/Data/mtcars.csv
import pandas as pd

address = "../../Data/mtcars.csv"
cars = pd.read_csv(address)

# create a list of column names (which are already in the csv file)
cars.columns = ["car_names", "mpg", "cyl", "disp", "hp", "drat", "wt", "qsec", "vs", "am", "gear", "carb"]

print("\nCars original:")
print(cars.head())

print("\nGroup by cylinders 'cyl' and get their mean value of each column:")
# first group by cylinders
cars_groups = cars.groupby(cars["cyl"])
# then get the mean of each group (get average value of each column that falls into cylinder category)
print(cars_groups.mean())


