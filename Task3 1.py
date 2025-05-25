import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv("resturants.csv")  # Replace with the correct file name

# Ensure the relevant columns exist
if "Rating text" in df.columns and "Aggregate rating" in df.columns:
    # Calculate review length from 'Rating text'
    df["review_length"] = df["Rating text"].astype(str).apply(len)

    # Calculate the average review length
    average_length = df["review_length"].mean()
    print(f"Average Review Length: {average_length:.2f} characters")

    # Explore correlation between review length and rating
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x=df["Aggregate rating"], y=df["review_length"])
    plt.xlabel("Aggregate Rating")
    plt.ylabel("Review Length")
    plt.title("Relationship Between Review Length and Rating")
    plt.show()

    # Calculate correlation coefficient
    correlation = df["Aggregate rating"].corr(df["review_length"])
    print(f"Correlation between Review Length and Rating: {correlation:.2f}")
else:
    print("Error: Required columns ('Rating text' or 'Aggregate rating') are missing in the CSV file.")

