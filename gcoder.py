import pandas as pd
import googlemaps

## feed a list of places to geocode, covert to a list

mar17 = pd.read_excel('17mar20.xlsx')

cities = mar17['City'].to_list()

## geocode function to output a list of places with lat, lon combos into cities.xlsx

def geocode_address(cities):
    gmaps = googlemaps.Client(key='AIzaSyA8rdGWADDPbQt1hxpSwjxILcCdEOikwxs')
    virus = pd.DataFrame(columns=['City', 'Lat', 'Lon'])
    for city in cities:    
        geocode_result = gmaps.geocode(city, region='nl')
        lat = geocode_result[0]["geometry"]["location"]["lat"]
        lon = geocode_result[0]["geometry"]["location"]["lng"]
        #add to dataframe
        virus = virus.append({'City': city, 'Lat': lat, 'Lon': lon}, ignore_index=True)
        virus.to_excel('cities.xlsx')
        #print results
        print (city, lat, lon)
        

## trigger the geocode_address function, using the list of places as an argument, and outputs the cities.xls file

geocode_address(cities)
