import pandas as pd
import duckdb
import requests

def acquisition(database1, database2):
    db_connect = duckdb.connect(database1)
    bicimad_df1 = duckdb.query('SELECT name AS "BiciMAD Station", address AS "Station Location", \
        "geometry.coordinates" AS "Coordinates" FROM main.bicimad_stations', connection=db_connect).df()
    
    response = requests.get(database2)
    json_data = response.json()
    places_df1 = pd.json_normalize(json_data['@graph'])
    
    return bicimad_df1, places_df1