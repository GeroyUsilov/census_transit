import geopandas
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
from shapely import wkt
from functions import *
import sys

station_number = int(sys.argv[1])
print(station_number)
cook = geopandas.read_file("processed_data/cook/cook.shp")
cta = geopandas.read_file("processed_data/cta/cta.shp")
station_name = cta.at[station_number,"LONGNAME"]
station_id = cta.at[station_number,"STATION_ID"]
station_walkshed = cta.at[station_number,"geometry"]
cook_crs = cook.crs
total_walkshed = 0
for i in range(len(cook)):
    tract_poly = cook.at[i,'geometry']
    tract_density = cook.at[i,'density']
    total_walkshed = total_walkshed + tract_cont_walkshed(tract_poly, station_walkshed,tract_density,cook_crs)

pd.DataFrame(np.array([station_name, 
                       station_id, 
                       total_walkshed])).to_csv("output/" +station_name +  ".csv", 
                                                                          header=None, 
                                                                          index=None)