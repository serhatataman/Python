import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from pylab import rcParams

rcParams['figure.figsize'] = [8, 4]
plt.style.use('seaborn-whitegrid')

# EXTREME VALUE ANALYSIS FOR OUTLIERS



address = "../../Data/mtcars.csv"

cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

print("\nCars dataset: \n" + str(cars.head()))

# sb.pairplot(cars)  # This prints out all the tables
# plt.show(block=True)