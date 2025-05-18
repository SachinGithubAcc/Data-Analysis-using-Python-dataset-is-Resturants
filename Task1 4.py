import pandas as pd

# Load the dataset
df = pd.read_csv("resturants.csv")

# Check the first few rows to understand the structure
print(df.head())

# Assuming the column 'online_delivery' exists and contains "Yes" or "No"
# Calculate percentage of restaurants offering online delivery
total_restaurants = len(df)
delivery_restaurants = len(df[df["Has Online delivery"] == "Yes"])
percentage_online_delivery = (delivery_restaurants / total_restaurants) * 100

# Compare average ratings
avg_rating_with_delivery = df[df["Has Online delivery"] == "Yes"]["Aggregate rating"].mean()
avg_rating_without_delivery = df[df["Has Online delivery"] == "No"]["Aggregate rating"].mean()

# Print results
print(f"\nPercentage of restaurants offering online delivery: {percentage_online_delivery:.2f}%")
print(f"\nAverage rating of restaurants with online delivery: {avg_rating_with_delivery:.2f}")
print(f"\nAverage rating of restaurants without online delivery: {avg_rating_without_delivery:.2f}")
