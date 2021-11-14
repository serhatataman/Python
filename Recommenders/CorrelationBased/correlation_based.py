import numpy as np
import pandas as pd

frame = pd.read_csv('../rating_final.csv')
cuisine = pd.read_csv('../chefmozcuisine.csv')
geo_data = pd.read_csv('../geoplaces2.csv', encoding='latin-1')


# display data
print('\n---------------------Ratings data-----------------------------------------------')
print(frame.head())

print('\n---------------------Cuisine data-----------------------------------------------')
print(cuisine.head())

print('\n---------------------Entire geo data-----------------------------------------------')
print(geo_data.head())

# Subset the geo data to only id and name
places = geo_data[['placeID', 'name']]

print('\n---------------------2 column geo data-----------------------------------------------')
print(places.head())

# Calculating mean value (average) rating of each place
rating = pd.DataFrame(frame.groupby('placeID')['rating'].mean())
print('\n---------------------Properties of each place-----------------------------------------------')

# Let's see how popular each of these places are
rating['rating_count'] = pd.DataFrame(frame.groupby('placeID')['rating'].count())
print(rating.head())

print('\n---------------------Statistical description of properties above-----------------------------')
# count: number of unique places that have been reviewed in the rating data frame
# max: max property. max.rating_count is the place which has received max ratings
print(rating.describe())

print('\n---------------------Places sorted according to their rating counts-----------------------------')
sorted_rating_values = rating.sort_values('rating_count', ascending=False).head()
print(sorted_rating_values)

print('\n---------------------The most rated place-----------------------------')
the_most_rated_placeId = sorted_rating_values.index[0]
# Filter the places where it is the most rated placeId
print(places[places['placeID'] == the_most_rated_placeId])

print('\n---------------------Type of cuisine they serve-----------------------------')
print(cuisine[cuisine['placeID'] == the_most_rated_placeId])

print('\n---------------------Crosstab places-----------------------------')
# Ratings that each user has given to each place
places_crosstab = pd.pivot_table(data=frame, values='rating', index='userID', columns='placeID')
print(places_crosstab.head())

print('\n---------------------The most popular place\'s rating that has been given by users-----------------------------')
tortas_ratings = places_crosstab[the_most_rated_placeId]
# filter out the null values
print(tortas_ratings[tortas_ratings >= 0])

# Now, we will find the correlation between the most rated place and the other places.
# This correlation is based on similarities of user reviews that is given to each place.

print('\n---------------------PearsonR correlation-----------------------------')
similar_to_tortas = places_crosstab.corrwith(tortas_ratings)
corr_tortas = pd.DataFrame(similar_to_tortas, columns=['PearsonR'])
# filter out null values
corr_tortas.dropna(inplace=True)
print(corr_tortas.head())

# If we've found some places that were really well correlated with Tortas but that had only, say, two ratings total,
# then those places probably wouldn't really be all that similar to Tortas. I mean maybe those places got similar ratings as Tortas,
# but they wouldn't be very popular. Therefore, that correlation really wouldn't be significant.
# We also need to take stock of how popular each of these places is, in addition to how well the review scores correlate
# with the ratings that were given to other places in the dataset. So to do that, let's join our corr Tortas data frame with a rating state of frame.
# So we're going to say corr_Tortas.join and we want to join it to the rating data frame, but we're only interested in rating count here.
print('\n---------------------Places where they have at least 10 user ratings-----------------------------')

tortas_corr_summary = corr_tortas.join(rating['rating_count'])
# Get the places where it has at least 10 ratings
at_least_10_reviews = tortas_corr_summary[tortas_corr_summary['rating_count'] >= 10].sort_values('PearsonR', ascending=False).head(10)
print(at_least_10_reviews)

print('\n---------------------Correlated places with type of food they serve-----------------------------')
placeIds_of_values = at_least_10_reviews.index.values
places_corr_tortas = pd.DataFrame(placeIds_of_values[:9], index=np.arange(9), columns=['placeID'])
summary = pd.merge(places_corr_tortas, cuisine, on='placeID')
print(summary)


print('\n---------------------Most relevant place-----------------------------')
print([places[places['placeID'] == 135046]])
print('\nDescription: ')
print(cuisine['Rcuisine'].describe())










