import numpy as np
import pandas as pd
import cufflinks as cf
import chart_studio
import chart_studio.plotly as py
import plotly.graph_objects as go
import chart_studio.tools as tls
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

py.iplot(data, filename='basic-line', auto_open=True)


# 2. Line chart from pandas dataframe
address = "../../Data/mtcars.csv"

cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']










