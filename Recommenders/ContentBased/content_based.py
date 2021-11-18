# Content-based recommender
# Recommends an an item based on its features and how similar they are to features of other items in data set.
# The best scenario will be to use Nearest neighbors algorithm.

# Nearest Neighbors Algorithm
# 1. Find the k nearest neighbors of the target item
# 2. Calculate the weighted average of the features of the neighbors
# 3. Return the item with the highest weighted average

import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors

# We are going to use mtcars dataset

print('\n---------------------Existing cars\' features-----------------------------------------------')
cars = pd.read_csv('mtcars.csv')
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
print(cars.head())


# What a random customer wants
test = [15, 300, 160, 3.2]

# Let's see how the nearest neighbors algorithm can be used to recommend a cor for this customer based on his requirements
# Inside parenthesis are the variable names
X = cars.loc[:, ('mpg', 'disp', 'hp', 'wt')].values
print(X[0:5])

# Search the item dataset to find a single point (this could be more by changing n_neighbors value) that is nearest to the test point
nbrs = NearestNeighbors(n_neighbors=1).fit(X)

print('\n---------------------The most similar in dataset X-----------------------------------------------')

# To find the nearest neighbors of the test point, we need to pass the test point to the kneighbors method
nearest_neighbor = nbrs.kneighbors([test])
idx_nearest_neighbor = nearest_neighbor[1][0][0]
print(cars.iloc[idx_nearest_neighbor])












