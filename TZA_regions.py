import pandas as pd  
import geopandas as gpd
import fiona
import shapely
import pyogrio
import matplotlib.pyplot as plt

# Define the regions you want to highlight
highlight_regions = ["Mara", "Morogoro", "Lindi", "Mtwara"]





# Load districts map dataset
regions = gpd.read_file("Maps/TZAmap_regions.shp")

# Filter the selected regions
regions_highlight = regions[regions["shapeName"].isin(highlight_regions)]




# Create a figure and axis for a single plot
fig, ax = plt.subplots(figsize=(10, 6))



# Plot the region map
regions.plot(ax = ax,  edgecolor="#747474", linewidth=0.8,facecolor = "none")

# Plot only selected regions with color
regions_highlight.plot(ax=ax, edgecolor="#747474", linewidth=0.8, color="lightblue", alpha=0.4)


# removing the axis 
plt.axis("off")


# Show the plot
plt.title("Regions of Tanzania")
plt.xlabel("Longitude")
plt.ylabel("Latitude")


plt.savefig("Tanzania_map.png", dpi=300, bbox_inches="tight")

plt.show()