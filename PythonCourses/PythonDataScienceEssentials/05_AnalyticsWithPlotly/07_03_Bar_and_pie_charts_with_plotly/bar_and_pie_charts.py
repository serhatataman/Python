import numpy as np
import pandas as pd
import cufflinks as cf
import chart_studio
import chart_studio.plotly as py
import chart_studio.tools as tls
import plotly.graph_objects as go
import matplotlib.pyplot as plt

U = "serhat"
AK = "ZZirFKYhBM3wYcJ8rkhL"
tls.set_credentials_file(username=U, api_key=AK)


# CREATING LINE CHARTS
# 1. Basic Line chart

a = np.linspace(start=0, stop=36, num=36)

# set random seed generator
np.random.seed(25)

# set random uniform values
b = np.random.uniform(low=0.0, high=1.0, size=36)

# create trace object
trace = go.Scatter(x=a, y=b)

data = [trace]

py.iplot(data, filename='basic-line-chart', auto_open=True)


# 2. Line chart from pandas dataframe
address = "../../Data/mtcars.csv"

cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

df = cars[['cyl', 'wt', 'mpg']]

layout = dict(title='Chart from Pandas Dataframe', xaxis=dict(title='x-axis'), yaxis=dict(title='y-axis'))

df.iplot(filename='cf-simple-line-chart', layout=layout)


# 3. Bar chart from pandas dataframe

# with the "trace" variable we specify what kind of chart we want to create
data = [go.Bar(x=[range(1, 10)], y=[1, 2, 3, 3, 0.5, 4, 3, 2, 1])]
print("Data for bar chart: ", data)







