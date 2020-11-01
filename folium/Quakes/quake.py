import os
import json

import pandas as pd

import folium
from folium import plugins

quakes = pd.read_csv('/data/2.5_month.csv')

m = folium.Map()

for i,row in quakes.iterrows():
    folium.CircleMarker((row.latitude,row.longitude), radius=4, weight=1, color='red', fill_color='red', fill_opacity=.3).add_to(m)

m

