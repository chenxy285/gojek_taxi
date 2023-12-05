# This script is to obtain the distance between start location and end location using OneMap routing API (https://www.onemap.gov.sg/apidocs/)

from pyonemap import OneMap
import pandas as pd

df = pd.read_csv(r'results/trip_data_sample.csv')

# Obtain access token using email and password.
response = OneMap.getToken('xychen@smu.edu.sg', 'CXy82377882@97') # go to OneMap API and register
access_token = response['access_token']

# Instantiate OneMap object for API query.
onemap = OneMap(access_token)


def get_dist(row):
    # Search for a address using postal code.
    start_lat = row['booking_pickup_latitude']
    start_lon = row['booking_pickup_longitude']
    end_lat = row['booking_destination_latitude']
    end_lon = row['booking_destination_longitude']
    # start = ["1.2513", "103.81782"]
    # end = ["1.331852", "103.9463505"]
    route = onemap.routing.route(start_lat,start_lon,end_lat,end_lon, "drive")
    return route['route_summary']['total_distance']

li_dist = []
for index, row in df.iterrows():
    print(f'progress: {index+1}|{len(df)}')
    li_dist.append(get_dist(row))
df['trip_dist'] = li_dist
# print(df.head(10))
df.to_csv(r'results/trip_data_status_distance.py',index=False)
