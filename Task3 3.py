# -*- coding: utf-8 -*-
"""
Created on Sun May 25 19:26:03 2025

@author: sachi
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv("resturants.csv")  # Replace with your actual file name

# Ensure necessary columns exist
required_columns = {"Price range", "Has Online delivery", "Has Table booking"}
if required_columns.issubset(df.columns):
    # Convert categorical columns to numerical format (Yes: 1, No: 0)
    df["Has Online delivery"] = df["Has Online delivery"].map({"Yes": 1, "No": 0})
    df["Has Table booking"] = df["Has Table booking"].map({"Yes": 1, "No": 0})

    # Group by price range and calculate the percentage of restaurants offering services
    price_delivery = df.groupby("Price range")["Has Online delivery"].mean()
    price_booking = df.groupby("Price range")["Has Table booking"].mean()

    # Visualizing the relationship
    plt.figure(figsize=(12, 5))

    # Online Delivery vs Price Range
    plt.subplot(1, 2, 1)
    sns.barplot(x=price_delivery.index, y=price_delivery.values, palette="Blues")
    plt.xlabel("Price Range")
    plt.ylabel("Proportion Offering Online Delivery")
    plt.title("Online Delivery vs Price Range")

    # Table Booking vs Price Range
    plt.subplot(1, 2, 2)
    sns.barplot(x=price_booking.index, y=price_booking.values, palette="Greens")
    plt.xlabel("Price Range")
    plt.ylabel("Proportion Offering Table Booking")
    plt.title("Table Booking vs Price Range")

    plt.tight_layout()
    plt.show()

    # Correlation Analysis
    correlation_delivery = df["Price range"].corr(df["Has Online delivery"])
    correlation_booking = df["Price range"].corr(df["Has Table booking"])

    print(f"Correlation between Price Range and Online Delivery: {correlation_delivery:.2f}")
    print(f"Correlation between Price Range and Table Booking: {correlation_booking:.2f}")

else:
    print("Error: Required columns ('Price range', 'Has Online delivery', 'Has Table booking') are missing in the CSV file.")


