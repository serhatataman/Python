# Model-Based Collaborative Filtering Systems
# SVD (Singular Value Decomposition) Matrix Factorization

# This is for using model-based collaborative filtering system using matrix factorization with singular value decomposition

# We are going to build a model-based movie recommender.

# INFO: SVD is a linear algebra method that can decompose a utility matrix into three compressed matrices.
# Model-based recommender use these compressed matrices to make recommendations without having to refer back to the complete dataset.

import pandas as pd
import numpy as np
import sklearn
from sklearn.decomposition import TruncatedSVD


print('\n---------------------Ratings given by each user to each movie-----------------------------------------------')
columns = ['user_id', 'item_id', 'rating', 'timestamp']
# Pass in columns we would like to retrieve
frame = pd.read_csv('ml-100k/u.data', sep='\t', names=columns)
print(frame.head())


print('\n---------------------Info about each movie-----------------------------------------------')
# import info about each movie
columns = ['item_id', 'movie title', 'release date', 'video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
           'Animation', 'Childrens', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir',
           'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

movies = pd.read_csv('ml-100k/u.item', sep='|', names=columns, encoding='latin-1')
print(movies.head())

print('\n---------------------Combined dataset-----------------------------------------------')
# combine movie and frame data frames into one
combined_movies_data = pd.merge(frame, movies, on='item_id')
print(combined_movies_data.head())

print('\n---------------------Number of ratings each movie has-----------------------------------------------')
# See what movies have the most number of reviews (this is like we did in popularity based recommender)
# Count ratings that are given to each movie then sort in descending order
number_of_ratings = combined_movies_data.groupby('item_id')['rating'].count().sort_values(ascending=False)
print(number_of_ratings.head())

print('\n---------------------The most rated movie-----------------------------------------------')
# Get the most rated place
Filter = combined_movies_data['item_id'] == number_of_ratings.index[0]
name_of_the_most_rated_movie = combined_movies_data[Filter]['movie title'].unique()
print(name_of_the_most_rated_movie[0])

print('\n---------------------Utility matrix-----------------------------------------------')
# Utility matrix is going to contain a value for each user and each movie. It is the ratings each user gave to each movie
# Utility matrices are Sparse (meaning that it might include null values) since not all users give ratings to all movies
# Because of this, we are going to fill null values with zero
ratings_crosstab = combined_movies_data.pivot_table(values='rating', index='user_id', columns='movie title', fill_value=0)
print(ratings_crosstab.head())

# We are going to transpose (switch rows with columns) this utility matrix,
# and then we're going to use SVD to decompose it down to synthetic representations of the user reviews

print(ratings_crosstab.shape)

# INFO: SciKit-Learn's truncated SVD method returns a single compressed version of the matrix upon which it is called.
# Compression happens along the dataset columns. Since we want to recommend movies, we want to reserve the movie names
# as uncompressed rows. We want to use the similarities between users to decide which movies to recommend, so we
# can use truncated SVD to compress all of the user ratings down to just 12 latent variables. These variables are going to
# capture most of the information that was stored in the 943 user columns previously. They represent a generalized view of
# users' tastes and preferences.

print('\n---------------------Transposed (rows and columns are swapped) matrix-----------------------------------------------')
# Transpose the matrix
X = ratings_crosstab.values.T
print(X.shape)

print('\n---------------------Decomposed matrix-----------------------------------------------')
# A utility matrix has successfully been transposed.
# Decompose it
# 12 - because we want our resultant matrix to have 12 dimensions
SVD = TruncatedSVD(n_components=12, random_state=17)
resultant_matrix = SVD.fit_transform(X)
print(resultant_matrix.shape)


print('\n---------------------Generate a correlation matrix-----------------------------------------------')
# Correlation is based on user similarities
corr_mat = np.corrcoef(resultant_matrix)
print(corr_mat.shape)


print('\n---------------------Isolating the most rated movie from correlation matrix--------------------------')
movies_names = ratings_crosstab.columns
movies_list = list(movies_names)

index_of_the_most_rated_movie = movies_list.index(name_of_the_most_rated_movie)
print(index_of_the_most_rated_movie)

# Now, for correlation matrix, isolate the array that represents
# the most rated movie at numerical index value 'index_of_the_most_rated_movie'
corr_most_rated_movie = corr_mat[index_of_the_most_rated_movie]
print(corr_most_rated_movie.shape)

print('\n---------------------Recommend a Highly Correlated Movies-----------------------------------------------')
# Generate a list of movie names that exhibit a high degree of correlation with the most rated movie
# To do that, we'll call the list function, and then pass in the expression to retrieve
# ONLY the movies that have a Pearson r coefficient close to one.

# List of movie names that have high correlation with the most rated movie
correlated_movie_list = list(movies_names[(corr_most_rated_movie < 1.0) & (corr_most_rated_movie > 0.9)])
print(correlated_movie_list)


print('\n---------------------Recommend a Highly Correlated Movie-----------------------------------------------')
highly_correlated_movie_list = list(movies_names[(corr_most_rated_movie < 1.0) & (corr_most_rated_movie > 0.95)])
print(highly_correlated_movie_list)

