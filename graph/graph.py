import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as date
#import seaborn as sns
#import shapefile as shp
import plotly.graph_objects as go

#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_us_cities.csv')
df = pd.read_csv('losangeles.csv')
print(df)
df['text'] = df['name'] + '<br>CO ' + (df['pop']).astype(str)+'ppm'
# limits = [(0,2),(3,10),(11,20),(21,50),(50,3000)]
limits = [(0,1),(1,3),(3,7),(7,10),(10,15)]
colors = ["crimson","orange","yellow","lightseagreen","lightgrey"]
cities = []
scale = 0.001

fig = go.Figure()

for i in range(len(limits)):
    lim = limits[i]
    df_sub = df[lim[0]:lim[1]]
    fig.add_trace(go.Scattergeo(
        locationmode = 'USA-states',
        lon = df_sub['lon'],
        lat = df_sub['lat'],
        text = df_sub['text'],
        marker = dict(
            size = df_sub['pop']/scale,
            color = colors[i],
            line_color='rgb(40,40,40)',
            line_width=0.5,
            sizemode = 'area'
        ),
        name = '{0} - {1}'.format(lim[0],lim[1])))

fig.update_layout(
        title_text = '2016-2019 LA Poluiton Nasa Data<br>(Click legend to toggle traces)',
        showlegend = True,
        geo = dict(
            scope = 'usa',
            landcolor = 'rgb(217, 217, 217)',
        )
    )

fig.show()