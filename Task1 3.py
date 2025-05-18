#TASK 1 - 3

import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("resturants.csv") 

#  dataset has a 'price_range' column
if 'Price range' not in df.columns:
    raise ValueError("The dataset must contain a 'Price range column.")

# Count restaurants in each price range
price_counts = df['Price range'].value_counts()

# Calculate percentage
total_restaurants = len(df)
price_percentages = (price_counts / total_restaurants) * 100

# Plot bar chart
plt.figure(figsize=(8, 5))
price_percentages.plot(kind='bar', color=['blue', 'green', 'red', 'Orange']) #plots colors

plt.xlabel("Price Range")
plt.ylabel("Percentage of Restaurants")
plt.title("Price Range Distribution Among Restaurants")

plt.xticks(rotation=0)  # Keep labels horizontal
plt.show()

