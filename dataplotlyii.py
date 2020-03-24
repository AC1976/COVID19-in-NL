## feed a list of data with headers "City" and "Status" columns (XX_Stat: "Geen infecties", "Meer infecties", "Minder infecties", "Geen nieuwe infecties")

import pandas as pd
import numpy as np

infections = pd.read_excel('infections.xlsx')

## pull just the bare minimum data from 'infections' for plotting

data = infections[['City', '20_Stat']]

## set index to "City" just to be sure... 

data.set_index('City')

## plot: (i) load the geojson file that contains the cities and the borders 

import json

with open('Gemeentegrenzen_2019.json', 'r') as f:
    geojson = json.load(f)

import plotly.express as px

fig = px.choropleth(data, geojson=geojson, locations='City', color='20_Stat',
                           color_continuous_scale=px.colors.sequential.YlOrRd,
                           featureidkey="properties.Gemeentena",
                           projection='mercator', hover_data=["20_Stat"],
                           color_discrete_map={"Geen infecties": "grey", "Meer infecties": "red", "Minder infecties":"green", "Geen nieuwe infecties": "yellow"}, 
                          )
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(title="COVID in NL: 20 maart")
fig.show()
