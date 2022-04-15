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

# 3. Simple Bar chart

# with the "trace" variable we specify what kind of chart we want to create
data = [go.Bar(x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], y=[1, 2, 3, 4, 0.5, 4, 3, 2, 1])]
print("Data for bar chart: ", data)

layout = dict(title='Bar Chart from Pandas Dataframe', xaxis=dict(title='x-axis'), yaxis=dict(title='y-axis'))

py.iplot(data, filename='basic-bar-chart', layout=layout, auto_open=True)


# 4. Simple Pie chart

fig = {'data': [{'labels': ['bicycle', 'motorcycle', 'car', 'van', 'stroller'],
                 'values': [1, 2, 3, 4, 0.5],
                 'type': 'pie'}],
       'layout': {'title': 'Simple Pie Chart'}}

py.iplot(fig, auto_open=True)


