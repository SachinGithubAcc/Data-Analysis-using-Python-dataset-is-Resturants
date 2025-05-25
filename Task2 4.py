import pandas as pd

# Load dataset
file_path = "resturants.csv"  # Update this with the actual CSV file path
df = pd.read_csv(file_path)

# Identify restaurant chains (restaurants appearing more than once)
chain_counts = df['Restaurant Name'].value_counts()
chains = chain_counts[chain_counts > 1].index.tolist()

# Filter dataset for restaurant chains
chain_df = df[df['Restaurant Name'].isin(chains)]

# Analyze ratings and popularity
chain_analysis = chain_df.groupby("Restaurant Name").agg({
    "Aggregate rating": "mean",
    "Votes": "sum"
}).reset_index()

# Sort results by popularity (Votes)
chain_analysis = chain_analysis.sort_values(by="Votes", ascending=False)

# Display the results
print("Identified restaurant chains and their ratings/popularity:")
print(chain_analysis)


import matplotlib.pyplot as plt

# Select top 10 restaurant chains
top_chains = chain_analysis.head(10)

# Plot bar chart
plt.figure(figsize=(10, 6))
plt.barh(top_chains["Restaurant Name"], top_chains["Votes"], color="skyblue")
plt.xlabel("Total Votes")
plt.ylabel("Restaurant Chain")
plt.title("Top 10 Popular Restaurant Chains Based on Votes")
plt.gca().invert_yaxis()  # Invert to show the highest on top
plt.show()