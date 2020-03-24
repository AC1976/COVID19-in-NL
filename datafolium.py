import pandas as pd
import numpy as np
import folium
from folium import plugins
from folium.plugins import HeatMap

## read data: infections per date per city + lat lons for cities

infections = pd.read_excel('infections_geo.xlsx')
cities = pd.read_excel('cities.xlsx')
data = infections.merge(cities, left_on='City', right_on='City')

data['Lat'] = data['Lat'].astype(float)
data['Lon'] = data['Lon'].astype(float)

mar17 = list(data[['17_Mar','Lat', 'Lon']].set_index('17_Mar'))
mar18 = data[['18_Mar','Lat', 'Lon']].set_index('18_Mar')
mar19 = data[['19_Mar','Lat', 'Lon']].set_index('19_Mar')
mar20 = data[['20_Mar','Lat', 'Lon']].set_index('20_Mar')
mar21 = data[['21_Mar','Lat', 'Lon']].set_index('21_Mar')
mar22 = data[['22_Mar','Lat', 'Lon']].set_index('22_Mar')
mar23 = data[['23_Mar','Lat', 'Lon']].set_index('23_Mar')
mar24 = list(data[['24_Mar','Lat', 'Lon']].set_index('24_Mar'))

heat = [mar17, mar24]

print(heat)

map = folium.Map(location=[52, 5.0], zoom_start=8, tiles="CartoDB dark_matter")

hm = plugins.HeatMapWithTime(heat, auto_play=False, max_opacity=0.8)
hm.add_to(map)

map.save(outfile="test.html")









