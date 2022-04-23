import numpy as np
import pandas as pd
import cufflinks as cf
import chart_studio
import chart_studio.plotly as py
import chart_studio.tools as tls
import plotly.graph_objects as go

from sklearn.preprocessing import StandardScaler

U = "serhat"
AK = "ZZirFKYhBM3wYcJ8rkhL"
tls.set_credentials_file(username=U, api_key=AK)

# CREATING HISTOGRAMS
# Make a histogram from a pandas Series object


address = "../../Data/mtcars.csv"
cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

mpg = cars.mpg

# 1- create a simple histogram
mpg.iplot(kind="histogram", filename="simple-histogram-chart")

# 2- create multiple histogram chart
cars_subset = cars[['mpg', 'disp', 'hp']]

# scale variables
cars_data_std = StandardScaler().fit_transform(cars_subset)

# In order to make plotting easy, we need to transform our cars dataset into dataframe
cars_select = pd.DataFrame(cars_data_std)

# name the columns of this dataframe
cars_select.columns = ['mpg', 'disp', 'hp']

# plot it out
cars_select.iplot(kind='histogram', filename='multiple-histogram-charts')


# 3- Create subplot histogram
cars_select.iplot(kind='histogram', subplots=True, filename='subplot-histograms')

# in order to change the layout, we can pass in shape parameter
cars_select.iplot(kind='histogram', subplots=True, shape=(3, 1), filename='subplot-histograms')


# CREATING BOX PLOTS
cars_select.iplot(kind='box', filename='box-plots')


# CREATE A SCATTER PLOT
fig = {'data': [{'x': cars_select.mpg, 'y': cars_select.disp, 'mode': 'markers', 'name': 'mpg'},
                {'x': cars_select.hp, 'y': cars_select.disp, 'mode': 'markers', 'name': 'hp'}],
       'layout': {'xaxis': {'title': 'xaxis-title'}, 'yaxis': {'title': 'Standardized Displacement'}}}

py.iplot(fig, filename='Grouped-scatter-plot')


















