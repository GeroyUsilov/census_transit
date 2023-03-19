import geopandas
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
from shapely import wkt
from tqdm import tqdm

def walkshed_poly(point, cook_crs, distance=1/2 *1609.34):
    lat, lon = point.y, point.x
    gs = geopandas.GeoSeries(wkt.loads(f'POINT ({lon} {lat})'))
    gdf = geopandas.GeoDataFrame(geometry=gs)
    gdf.crs=cook_crs
    gdf = gdf.to_crs('EPSG:32616')
    res = gdf.buffer(
        distance=distance,
        cap_style="round", #3 for square
    )
    return res.to_crs(cook_crs).iloc[0]

def tract_cont_walkshed(tract_poly, walkshed_poly,tract_density,cook_crs):
    sqm2sqmi = 3.86102E-7
    intersect = tract_poly.intersection(walkshed_poly)
    gdf = geopandas.GeoDataFrame(geometry=[intersect])
    gdf.crs=cook_crs
    intersect_area = gdf.to_crs(epsg=32616).area.iat[0]*sqm2sqmi
    return intersect_area*tract_density