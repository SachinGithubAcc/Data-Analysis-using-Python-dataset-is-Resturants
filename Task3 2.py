# -*- coding: utf-8 -*-
"""
Created on Sun May 25 19:21:15 2025

@author: sachi
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv("resturants.csv")  # Replace with actual file name

# Check if necessary columns exist
if "Votes" in df.columns and "Aggregate rating" in df.columns:
    # Identify restaurants with highest and lowest votes
    highest_voted_restaurant = df.loc[df["Votes"].idxmax(), ["Restaurant Name", "Votes"]]
    lowest_voted_restaurant = df.loc[df["Votes"].idxmin(), ["Restaurant Name", "Votes"]]

    print(f"\nHighest Voted Restaurant: {highest_voted_restaurant['Restaurant Name']} ({highest_voted_restaurant['Votes']} votes)")
    print(f"Lowest Voted Restaurant: {lowest_voted_restaurant['Restaurant Name']} ({lowest_voted_restaurant['Votes']} votes)")

    # Analyze correlation between votes and rating
    correlation = df["Votes"].corr(df["Aggregate rating"])
    print(f"Correlation between Votes and Rating: {correlation:.2f}")

    # Visualize the relationship
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x=df["Aggregate rating"], y=df["Votes"])
    plt.xlabel("Aggregate Rating")
    plt.ylabel("Number of Votes")
    plt.title("Votes vs. Rating Relationship")
    plt.show()
else:
    print("Error: Required columns ('Votes' or 'Aggregate rating') are missing in the CSV file.")
