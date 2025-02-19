import pandas as pd  
import geopandas as gpd
import fiona
import shapely
import pyogrio
import matplotlib.pyplot as plt

# Define the districts you want to highlight
highlight_districts = ["Tarime", "Bunda"]

#If any of the districts dont show up run this code so you can find the one you are looking for
#print(districts["district_name"].unique())

# Load districts map dataset
districts = gpd.read_file("Maps/TZAmap_districts.shp")  

# List of districts to keep
selected_districts = ["Bunda", "Butiam", "Musoma", "Nyakonga", "Rorya", "Serengeti", "Tarime", "Musoma Urban"]

# Filter the GeoDataFrame to keep only the selected districts
filtered_districts = districts[districts["shapeName"].isin(selected_districts)]


# Filter the selected regions
districts_highlight = districts[districts["shapeName"].isin(highlight_districts)] 

# Create a figure and axis for a single plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the filtered districts
filtered_districts.plot(ax=ax, edgecolor="grey", linewidth=0.8, color="white")

# Plot only selected districts with color
districts_highlight.plot(ax=ax, edgecolor="#747474", linewidth=0.3, color="lightblue", alpha=0.4)

# Remove the axis
plt.axis("off")

# Label graph
plt.title("Districts in Mara")

# Label each district by plotting the district name at the centroid
for idx, row in filtered_districts.iterrows():  # Iterate through the rows of the GeoDataFrame
    # Get the centroid of each district
    centroid = row.geometry.centroid
    # Add the district name at the centroid's coordinates
    ax.text(centroid.x, centroid.y, row["shapeName"], fontsize=8, ha="center", color="black")  # Add the label


plt.savefig("Visuals/region_districts.png", dpi=300, bbox_inches="tight")

# Show the plot
plt.show()
