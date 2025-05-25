import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("resturants.csv")

# Scatter plot of restaurant locations
plt.figure(figsize=(10, 6))
plt.scatter(df["Longitude"], df["Latitude"], c=df["Aggregate rating"], cmap="coolwarm", alpha=0.7)

# Add labels
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Restaurant Locations and Ratings")

# Color bar to represent ratings
plt.colorbar(label="Aggregate Rating")

# Show plot
plt.show()




