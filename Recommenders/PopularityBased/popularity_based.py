import pandas as pd
import numpy as np

# Users' place ratings
frame = pd.read_csv('../rating_final.csv')
# The type of cuisine that is served in each restaurant
cuisine = pd.read_csv('../chefmozcuisine.csv')

# display data
print('\n---------------------Ratings data-----------------------------------------------')
print(frame.head())
print('\n---------------------Cuisine data-----------------------------------------------')
print(cuisine.head())

# Count the number of ratings that each place has gotten and convert it to a dataframe
rating_count = pd.DataFrame(frame.groupby('placeID')['rating'].count())

# Sort places in descending order according to their review numbers
rating_count.sort_values('rating', ascending=False).head()

# Take top five most often rated places and see if they have any similarities between their cuisine served
most_rated_places = pd.DataFrame([135085, 132825, 135032, 135052, 132834], index=np.arange(5), columns=['placeID'])

summary = pd.merge(most_rated_places, cuisine, on='placeID')

print('\n--------------------Most rated (popular) places---------------------------------')
print(summary)
print('\n-- Note: The places that serve most popular types of cuisine '
      'are more likely to be appreciated by the average restaurant goers. '
      'So, most rated places will be recommended--')
print('\n--------------------------------------------------------------------')
print(cuisine['Rcuisine'].describe())
