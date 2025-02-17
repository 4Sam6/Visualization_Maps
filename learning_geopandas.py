import pandas as pd  
import geopandas as gpd
import fiona
import shapely
import pyogrio
import matplotlib.pyplot as plt

# Define the regions you want to highlight
highlight_regions = ["Mara", "Morogoro", "Lindi", "Mtwara"]


# Load districts map dataset
gdf1 = gpd.read_file("Maps/TZAmap_districts.shp")


# Load districts map dataset
gdf2 = gpd.read_file("Maps/TZAmap_regions.shp")

# Filter the selected regions
gdf_highlight = gdf2[gdf2["shapeName"].isin(highlight_regions)]


# Display the first few rows of the dataset
print(gdf1.head())

# Create a figure and axis for a single plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the districts map
gdf1.plot(ax = ax,  edgecolor="#ababab", linewidth=0.3, color="white")

# Plot the region map
gdf2.plot(ax = ax,  edgecolor="#747474", linewidth=0.8,facecolor = "none")

# Plot only selected regions with color
gdf_highlight.plot(ax=ax, edgecolor="#747474", linewidth=0.8, color="lightblue", alpha=0.4)




# removing the axis 
plt.axis("off")


# Show the plot
plt.title("Tanzania")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()

plt.savefig("Tanzania_map.png", dpi=300, bbox_inches="tight")