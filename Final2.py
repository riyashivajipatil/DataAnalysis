#!/usr/bin/env python
# coding: utf-8

# In[4]:


import plotly.graph_objects as go
from datetime import datetime
import pytz
import pandas as pd
import numpy as np
# Load the dataset
file_path = (r'C:\Users\Riya Shivaji Patil\Downloads\Play Store Data (1).csv')

apps_df = pd.read_csv(file_path)

# Data Cleaning and Transformation

# Convert Installs to numeric
apps_df["Installs"] = apps_df["Installs"].astype(str).str.replace("[+,]", "", regex=True)
apps_df["Installs"] = pd.to_numeric(apps_df["Installs"], errors="coerce")

# Convert Size to numeric (MB)
apps_df["Size"] = apps_df["Size"].astype(str).str.replace("M", "").replace("Varies with device", np.nan)
apps_df["Size"] = pd.to_numeric(apps_df["Size"], errors="coerce")

# Convert Price to numeric (Revenue Calculation)
apps_df["Price"] = apps_df["Price"].astype(str).str.replace("$", "", regex=True)
apps_df["Price"] = pd.to_numeric(apps_df["Price"], errors="coerce")

# Convert Last Updated to datetime
apps_df["Last Updated"] = pd.to_datetime(apps_df["Last Updated"], errors="coerce")

# Extract numeric Android Version
apps_df["Android Ver"] = apps_df["Android Ver"].astype(str).str.extract(r"(\d+\.\d+)").astype(float)

# Calculate Revenue for Paid Apps
apps_df["Revenue"] = apps_df["Installs"] * apps_df["Price"]

# Apply Filtering Conditions
filtered_apps = apps_df[
    (apps_df["Installs"] >= 10000) &
    (apps_df["Revenue"] >= 10000) &
    (apps_df["Android Ver"] > 4.0) &
    (apps_df["Size"] > 15) &
    (apps_df["Content Rating"] == "Everyone") &
    (apps_df["App"].str.len() <= 30)
]

# Identify Top 3 Categories by Count
top_categories = filtered_apps["Category"].value_counts().nlargest(3).index.tolist()

# Filter dataset for top 3 categories
filtered_apps = filtered_apps[filtered_apps["Category"].isin(top_categories)]

# Calculate Average Installs & Revenue for Free vs Paid Apps within Top 3 Categories
category_summary = filtered_apps.groupby(["Category", "Type"]).agg(
    Avg_Installs=("Installs", "mean"),
    Avg_Revenue=("Revenue", "mean")
).reset_index()

# Get current time in IST
ist = pytz.timezone("Asia/Kolkata")
current_time = datetime.now(ist).time()

# Check if current time is between 1 PM - 2 PM IST
start_time = datetime.strptime("13:00:00", "%H:%M:%S").time()
end_time = datetime.strptime("14:00:00", "%H:%M:%S").time()

if start_time <= current_time <= end_time:
    # Create dual-axis chart
    fig = go.Figure()

    # Bar chart for Avg Installs
    fig.add_trace(go.Bar(
        x=category_summary["Category"],
        y=category_summary["Avg_Installs"],
        name="Average Installs",
        marker_color="blue"
    ))

    # Line chart for Avg Revenue
    fig.add_trace(go.Scatter(
        x=category_summary["Category"],
        y=category_summary["Avg_Revenue"],
        name="Average Revenue",
        mode="lines+markers",
        yaxis="y2",
        marker=dict(color="red", size=8)
    ))

    # Layout settings for dual-axis
    fig.update_layout(
        title="Comparison of Average Installs and Revenue for Free vs. Paid Apps",
        xaxis_title="App Category",
        yaxis=dict(title="Average Installs", side="left"),
        yaxis2=dict(title="Average Revenue", overlaying="y", side="right"),
        legend=dict(x=0, y=1),
        template="plotly_white"
    )

    fig.show()
else:
    print("Graph is only available between 1 PM - 2 PM IST.")


# In[5]:


import plotly.graph_objects as go

# Create dual-axis chart (overriding time restriction for preview)
fig = go.Figure()

# Bar chart for Avg Installs
fig.add_trace(go.Bar(
    x=category_summary["Category"],
    y=category_summary["Avg_Installs"],
    name="Average Installs",
    marker_color="blue"
))

# Line chart for Avg Revenue
fig.add_trace(go.Scatter(
    x=category_summary["Category"],
    y=category_summary["Avg_Revenue"],
    name="Average Revenue",
    mode="lines+markers",
    yaxis="y2",
    marker=dict(color="red", size=8)
))

# Layout settings for dual-axis
fig.update_layout(
    title="Comparison of Average Installs and Revenue for Free vs. Paid Apps",
    xaxis_title="App Category",
    yaxis=dict(title="Average Installs", side="left"),
    yaxis2=dict(title="Average Revenue", overlaying="y", side="right"),
    legend=dict(x=0, y=1),
    template="plotly_white"
)

# Show the chart
fig.show()


# In[ ]:




