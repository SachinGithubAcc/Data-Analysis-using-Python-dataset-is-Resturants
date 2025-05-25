import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("resturants.csv")

# Identify the most common cuisine combinations
cuisine_counts = df["Cuisines"].value_counts()
most_common_cuisines = cuisine_counts.head(10)

# Analyze cuisine combinations with higher ratings
cuisine_ratings = df.groupby("Cuisines")["Aggregate rating"].mean()
top_rated_cuisines = cuisine_ratings.sort_values(ascending=False).head(10)

# Print results
print("Most Common Cuisine Combinations:\n")
print(most_common_cuisines)
print("\nCuisine Combinations with Highest Ratings:\n")
print(top_rated_cuisines)

# Visualize top-rated cuisine combinations
plt.figure(figsize=(10, 5))
top_rated_cuisines.plot(kind="bar", color="skyblue")
plt.xlabel("Cuisine Combination")
plt.ylabel("Average Rating")
plt.title("Top 10 Cuisine Combinations by Rating")
plt.xticks(rotation=45)
plt.show()
