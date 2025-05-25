import pandas as pd

# Load the CSV file
df = pd.read_csv("resturants.csv")

# Disp"lay the first few row"s
print(df.head())

# Find the most common rating range max
most_common_range = df["Aggregate rating"].value_counts().idxmax()
print(f"Most Common Max Rating: {most_common_range}")

# Find the most common rating range min
most_common_range = df["Aggregate rating"].value_counts().idxmin()
print(f"Most Common Min Rating: {most_common_range}")

# Calculate the average number of votes
average_votes = df["Votes"].mean()

# Display the result
print(f" \n Average Number of Votes Received by Restaurants: {average_votes:.2f}")

#Find Basic Statistics of Ratings
print("\nRating\n",df["Aggregate rating"].describe())

#Graph Create 
top_restaurants = df[df["Aggregate rating"] >= 4.5]
print("\nTop Resturants 4.5 Ratings\n",top_restaurants)

#Count Number of Ratings per Restaurant
rating_counts = df["Restaurant Name"].value_counts()
print("\n Rating Count for Resturant Name\n",rating_counts)


#Visualize Ratings Distribution
import matplotlib.pyplot as plt

df["Aggregate rating"].hist(bins=10)
plt.xlabel("Aggregate rating")
plt.ylabel("Number of Restaurants")
plt.title("Distribution of Restaurant Ratings")
plt.show()





