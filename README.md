# COVID19-in-NL
Assorted data files and Python scripts to track and map COVID19 in the Netherlands:

- 'infections.xlxs' -- contains the # of infections for a range of dates, per Dutch municipality (gemeente). Data is sourced from the daily reports at rivm.nl website and manually appended (periodically).

- 'cities.xlsx' -- contains a list of all municipalities (gemeente) in the Netherlands and the geocoded lat / lon position of the municipality, as geocoded using the Google Maps V3 python library. Use this if you do not want to geocode yourself or don't have access to an (unlimited....) geocoding service like Google.

- 'Gemeentegrenzen_2019.json" -- geojson file with all the borders of all municipalities in the Netherlands. Use this for choropleth style maps. Data is sourced from ArcGis website.

- 'gcoder.py' -- python function to geocode a list of municipalities, returns a file with the 'lat' 'lon' of each municipality.

- 'dataplotlyii.py'-- python script to create a choropleth map of the Netherlands using plotly express; sources its data from the 'infections.xlsx' file (single date only, multiple dates and animation is work in progress).

- 'datafolium.py' -- python script to make heatmap of infections on date of choice sourced from 'infections.xlsx' for every Dutch municipality, using the lat / lons from cities.xlsx.




