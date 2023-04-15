import pandas as pd
import numpy as np
import argparse
import fuzzywuzzy
import Levenshtein
from fuzzywuzzy import process
from shapely.geometry import Point
import geopandas as gpd

def parse_arguments():
    parser = argparse.ArgumentParser(description='Generar un dataframe completo o indicar un lugar de interés')
    parser.add_argument('--all', action='store_true', help='Create a Table with all places/distances')
    parser.add_argument('--place', type=str, help='Indicate a Place Of Interest')
    return parser.parse_args()

def combine_df(df1, df2):
    df_combined = df2.merge(df1, how='cross')
    return df_combined

def to_mercator(lat, long):
    c = gpd.GeoSeries([Point(lat, long)], crs=4326)
    c = c.to_crs(3857)
    return c

def distance_meters(lat_start, long_start, lat_finish, long_finish):
    start = to_mercator(lat_start, long_start)
    finish = to_mercator(lat_finish, long_finish)
    return start.distance(finish)

def distance_df(combined_df):
    lat_x = np.array(combined_df['Latitude_x'])
    lon_x = np.array(combined_df['Longitude_x'])
    lat_y = np.array(combined_df['Latitude_y'])
    lon_y = np.array(combined_df['Longitude_y'])
    dist = np.vectorize(distance_meters)(lat_x, lon_x, lat_y, lon_y)
    combined_df['Distance'] = dist
    return combined_df

def final_df(df_distance):
    final_df = df_distance.loc[df_distance.groupby("Place of Interest")["Distance"].idxmin()]
    final_df = final_df.drop(['Latitude_x','Longitude_x','Latitude_y','Longitude_y'], axis=1)
    final_df = final_df.reset_index(drop=True)
    final_df['Distance'] = final_df['Distance'].round(0)
    return final_df

def filter_place(df, lugar):
    df_filtered = df[df['Place of Interest'] == lugar]
    return df_filtered

def create_csv(df_final):
    csv_df = df_final[['Place of Interest', 'Type of Place','Place Address','BiciMAD Station','Station Location']]
    csv_df.to_csv('Bicimad_Distances.csv', index=False)
    return csv_df