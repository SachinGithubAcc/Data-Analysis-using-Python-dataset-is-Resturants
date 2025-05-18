import pandas as pd

# Load the dataset
data = pd.read_csv('resturants.csv')  # Replace with your actual file path

# Count the number of restaurants in each city
city_counts = data['City'].value_counts()

# Identify the city with the highest number of restaurants
city_with_most_restaurants = city_counts.idxmax()
most_restaurants_count = city_counts.max()

# Calculate the average rating for restaurants in each city
average_ratings = data.groupby('City')['Aggregate rating'].mean()

# Identify the city with the highest average rating
city_with_highest_rating = average_ratings.idxmax()
highest_average_rating = average_ratings.max()

print("\n\n  ************ CITY ANALYSIS ************* \n\n")

# Display the results
print(f"City with the highest number of restaurants: {city_with_most_restaurants} ({most_restaurants_count} restaurants)\n")
print(f"City with the highest average rating: {city_with_highest_rating} (Aggregate rating: {highest_average_rating:.2f})")
