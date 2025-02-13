#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
import pytz


# In[2]:


# Load the datasets
playstore_file_path = r"C:\Users\Riya Shivaji Patil\Desktop\Play Store Data.csv"
reviews_file_path = r"C:\Users\Riya Shivaji Patil\Desktop\User Reviews.csv"
apps_df = pd.read_csv(playstore_file_path)
reviews_df = pd.read_csv(reviews_file_path)

# Data Cleaning & Transformation

# Convert 'Installs' to numeric
apps_df["Installs"] = apps_df["Installs"].astype(str).str.replace("[+,]", "", regex=True)
apps_df["Installs"] = pd.to_numeric(apps_df["Installs"], errors="coerce")

# Convert 'Size' to numeric (MB)
apps_df["Size"] = apps_df["Size"].astype(str).str.replace("M", "").replace("Varies with device", np.nan)
apps_df["Size"] = pd.to_numeric(apps_df["Size"], errors="coerce")

# Convert 'Reviews' to numeric
apps_df["Reviews"] = pd.to_numeric(apps_df["Reviews"], errors="coerce")

# Convert 'Rating' to numeric
apps_df["Rating"] = pd.to_numeric(apps_df["Rating"], errors="coerce")

# Convert 'Last Updated' to datetime
apps_df["Last Updated"] = pd.to_datetime(apps_df["Last Updated"], errors="coerce")

# Extract numeric Android Version
apps_df["Android Ver"] = apps_df["Android Ver"].astype(str).str.extract(r"(\d+\.\d+)").astype(float)

# Merge User Reviews with Play Store Data on "App"
merged_df = pd.merge(apps_df, reviews_df, on="App", how="inner")

# Convert 'Reviews' in User Reviews dataset to numeric
merged_df["Reviews"] = pd.to_numeric(merged_df["Reviews"], errors="coerce")

# Apply Filtering Conditions
filtered_apps = merged_df[
    (merged_df["Category"].map(merged_df["Category"].value_counts()) > 50) &  # Categories with > 50 apps
    (merged_df["App"].str.contains("C", case=False, na=False)) &  # App name must contain 'C'
    (merged_df["Reviews"] >= 10) &  # Apps with at least 10 reviews
    (merged_df["Rating"] < 4.0)  # Rating must be < 4.0
]

# Get current time in IST
ist = pytz.timezone("Asia/Kolkata")
current_time = datetime.now(ist).time()

# Check if current time is between 4 PM - 6 PM IST
start_time = datetime.strptime("16:00:00", "%H:%M:%S").time()
end_time = datetime.strptime("18:00:00", "%H:%M:%S").time()

if start_time <= current_time <= end_time:
    # Create Violin Plot
    plt.figure(figsize=(12, 6))
    sns.violinplot(x="Category", y="Rating", data=filtered_apps, palette="muted")

    # Customize the plot
    plt.title("Distribution of Ratings for Each App Category (Filtered)")
    plt.xticks(rotation=45, ha="right")
    plt.xlabel("App Category")
    plt.ylabel("Rating")
    plt.grid(True)

    # Show the plot
    plt.show()
else:
    print("Graph is only available between 4 PM - 6 PM IST.")


# In[ ]:




