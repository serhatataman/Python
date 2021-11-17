# Classification based collaborative filtering system
# This is an example of Logistic Regression as a Classifier to make recommendation.
# This is a user based collaborative filtering, because recommendations will be made based on similarities between users.

import numpy as np
import pandas as pd

from pandas import Series, DataFrame
from sklearn.linear_model import LogisticRegression

print('\n---------------------Banking data-----------------------------------------------')
bank_full = pd.read_csv('../bank_full_w_dummy_vars.csv')
print(bank_full.head())

print('\n---------------------Info-----------------------------------------------')
bank_full.info()

# Get user attributes. All from 18th column until 37th column.
X = bank_full.iloc[:, 18:37].values

# Whether user subscribed to marketing offers
y = bank_full.iloc[:, 17].values

# Create the model
LogReg = LogisticRegression()
# Fit the model
LogReg.fit(X, y)

# These values are Binary variables that describes Sam (user). Variables are in binary form and
# represent stuff like "has housing loan? -yes -no", "Is single? -yes -no", "Is unemployed? -yes -no"
new_user = np.array([0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]).reshape(1, -1)

print('\n---------------------Predict if Sam will accept the offer-------------------------------------')

# We want to predict whether or not Sam will accept the offer he's marketed to
y_pred = LogReg.predict(new_user)
print(y_pred)

# If the model returns zero, then it predicts that Sam is NOT likely to accept the offer









