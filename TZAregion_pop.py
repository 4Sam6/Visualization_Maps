import pandas as pd

import pandas as pd   
import geopandas as gpd
import fiona
import shapely
import pyogrio
import matplotlib.pyplot as plt



# Loading the data needed
# Load population data (ensure it has columns: 'shapeName' and 'population')
population = pd.read_csv("Maps/TZAmap_population.csv")
# Load districts map dataset
regions = gpd.read_file("Maps/TZAmap_regions.shp")
population.rename(columns={"area_name": "shapeName"}, inplace=True)


# Merge population data with the region shapefile
reg_pop = regions.merge(population, on="shapeName", how="left")


# generating the chart
# Create a figure and axis for a single plot
fig, ax = plt.subplots(figsize=(10, 6))
# Plot the region map
reg_pop.plot(ax = ax,  edgecolor="#747474", linewidth=0.8,color = "white")

# Plot the regions with population-based color
reg_pop.plot(ax=ax, edgecolor="#747474", linewidth=0.8, column="Population Size-Total", 
          cmap="viridis", legend=True, alpha=0.8,  legend_kwds={
                 "shrink": 0.6,  # Shrink the legend size
                 "label": "Population",  # Legend title
                 "orientation": "vertical",  # Can also be 'horizontal'
                 
             })

# label graph
plt.title("Tanzania")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
# removing the axis 
plt.axis("off")


plt.savefig("Visuals/Tanzania_population.png", dpi=300, bbox_inches="tight")

plt.show()