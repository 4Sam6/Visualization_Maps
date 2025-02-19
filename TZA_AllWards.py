import pandas as pd  
import geopandas as gpd
import fiona
import shapely
import pyogrio
import matplotlib.pyplot as plt


# Load wards map dataset
wards = gpd.read_file("Maps/TZAmap_wards.shp")

# Define the ward you want to keep
tarime_fill = ["Binagi", "Bomani", "Bumera", "Genyange", "Gorong'a"]

# Define the wards In Tarime
tarime = ["Binagi", "Bomani", "Bumera", "Genyange", "Gorong'a", "Gwitiryo", "Itiryo", "Kemambo", "Kibasuka", "Kiore", "Komaswa", "Kwihancha", "Manga", "Matongo", "Mbogi", "Muriba", "Mwema", "Nyakonga", "Nyamisangura", "Nyamwaga", "Nyangoto", "Nyamongo", "Nyansincha", "Nyanungu", "Nyarero", "Nyarokoba", "Nyabichune", "Mjini Kati", "Pemba", "Regicheri", "Sabasaba", "Sirari", "Susuni", "Turwa"]

# print(len(wards)) = 34

# Load wards map dataset
wards = gpd.read_file("Maps/TZAmap_wards.shp")

# Create a figure and axis for a single plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the filtered wards
wards.plot(ax=ax, edgecolor="grey", linewidth=0.8, color="white")


# Remove the axis
plt.axis("off")

# Label graph
plt.title("Wards in Tarime")



plt.savefig("Visuals/all_Wards.png", dpi=300, bbox_inches="tight")

# Show the plot
plt.show()