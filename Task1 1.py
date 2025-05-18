import pandas as pd

#read csv file in Resturants
data = pd.read_csv('resturants.csv')  

# Count of each cuisine
cuisine_counts = data['Cuisines'].value_counts()

# top three most common cuisines
top_cuisines = cuisine_counts.head(3)

# total number of restaurants
total_restaurants = len(data)

#percentage of restaurants 
top_cuisine_percentages = (top_cuisines / total_restaurants) * 100

# Create DataFrame to display the results
results = pd.DataFrame({
    'Cuisines': top_cuisines.index,
    'Count': top_cuisines.values,
    'Percentage': top_cuisine_percentages.values
})

# Reset index for better readability
results.reset_index(drop=True, inplace=True)

print("\n\n ********* TOP CUISINES ********** \n")
#Display results
print(results)
