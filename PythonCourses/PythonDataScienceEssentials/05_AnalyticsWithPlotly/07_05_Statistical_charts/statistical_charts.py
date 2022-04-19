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

address = "../../Data/mtcars.csv"
cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

mpg = cars.mpg


