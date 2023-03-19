library(tidyverse)
library(tidycensus)
library(sf)
census_api_key("7dab025a469c2b39ac9450467f12b7df67e3e21a")
options(tigris_use_cache = TRUE)
v20 <- load_variables(2020, "pl")
cook <- get_decennial(state = "IL",
                      county = "Cook",
                      geography = "block", 
                       variables = "P013001", 
                       year = 2010)
cook <- get_decennial(
  state = "IL",
  county = "Cook",
  geography = "tract",
  variables = "P1_001N",
  geometry = TRUE,
  year = 2020
)
v20 <- load_variables(2020, "pl", cache = TRUE)
view(v20)
st_write(cook, "cook.shp")
