#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import nltk
from nltk.corpus import stopwords
import re


# In[2]:


# Download stopwords if not already available
nltk.download('stopwords')
custom_stopwords = set(stopwords.words('english'))  # Load default stopwords


# In[3]:


# Load the dataset
file_path =r"C:\Users\Riya Shivaji Patil\Downloads\User Reviews (1).csv"  # Update the path if needed
df = pd.read_csv(file_path)


# In[12]:


# Ensure the dataset contains relevant columns
if 'Sentiment' in df.columns and 'Translated_Review' in df.columns and 'App' in df.columns:
    # Filter only 5-star reviews (assuming 5-star reviews are labeled as "Positive")
    df_5star = df[df['Sentiment'] == 'Positive'].copy()

    # Get the list of unique app names (to remove from the text)
    app_names = set(df['App'].dropna().unique())

     # Function to clean text
    def clean_text(text):
        text = str(text).lower()  # Convert to lowercase
        text = re.sub(r'\W+', ' ', text)  # Remove special characters
        words = text.split()  # Tokenize
        words = [word for word in words if word not in custom_stopwords and word not in app_names]  # Remove stopwords & app names
        return " ".join(words)

    # Apply text cleaning
    df_5star['Cleaned_Review'] = df_5star['Translated_Review'].astype(str).apply(clean_text)

    # Combine all reviews into one large text
    text = " ".join(df_5star['Cleaned_Review'])

    # Generate word cloud
    wordcloud = WordCloud(width=800, height=400, background_color="white", stopwords=STOPWORDS).generate(text)

    # Display the word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Word Cloud of Most Frequent Keywords in 5-Star Reviews")
    plt.show()

else:
    print("Required columns ('Sentiment', 'Review', 'App') not found in the dataset.")


# In[ ]:





# In[16]:


import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import nltk
from nltk.corpus import stopwords
import re

# Download stopwords if not already available
nltk.download('stopwords')
custom_stopwords = set(stopwords.words('english'))  # Load default stopwords

# Load the datasets
reviews_file = r"C:\Users\Riya Shivaji Patil\Downloads\User Reviews (1).csv"
apps_file = r"C:\Users\Riya Shivaji Patil\Downloads\Play Store Data (1).csv"

# Read the datasets
df_reviews = pd.read_csv(reviews_file)
df_apps = pd.read_csv(apps_file)

# Ensure the datasets contain relevant columns
if 'App' in df_reviews.columns and 'Sentiment' in df_reviews.columns and 'Translated_Review' in df_reviews.columns:
    if 'App' in df_apps.columns and 'Category' in df_apps.columns:
        # Filter apps in "Health & Fitness" category
        health_apps = set(df_apps[df_apps['Category'] == 'HEALTH_AND_FITNESS']['App'].dropna().unique())

        # Filter only 5-star reviews and those belonging to health apps
        df_5star = df_reviews[(df_reviews['Sentiment'] == 'Positive') & (df_reviews['App'].isin(health_apps))].copy()

        # Get the list of unique app names (to remove from text)
        app_names = set(df_reviews['App'].dropna().unique())

        # Function to clean text
        def clean_text(text):
            text = str(text).lower()  # Convert to lowercase
            text = re.sub(r'\W+', ' ', text)  # Remove special characters
            words = text.split()  # Tokenize
            words = [word for word in words if word not in custom_stopwords and word not in app_names]  # Remove stopwords & app names
            return " ".join(words)

        # Apply text cleaning
        df_5star['Cleaned_Review'] = df_5star['Translated_Review'].astype(str).apply(clean_text)

        # Combine all reviews into one large text
        text = " ".join(df_5star['Cleaned_Review'])

         # Generate word cloud
        wordcloud = WordCloud(width=800, height=400, background_color="white", stopwords=STOPWORDS).generate(text)

        # Display the word cloud
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.title("Word Cloud of Most Frequent Keywords in 5-Star Health & Fitness App Reviews")
        plt.show()
    else:
        print("Required columns ('App', 'Category') not found in Play Store dataset.")
else:
    print("Required columns ('App', 'Sentiment', 'Review') not found in User Reviews dataset.")


# In[ ]:





# In[17]:


import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import nltk
from nltk.corpus import stopwords
import re

# Download stopwords if not already available
nltk.download('stopwords')
custom_stopwords = set(stopwords.words('english'))  # Load default stopwords

# Load the datasets
reviews_file = r"C:\Users\Riya Shivaji Patil\Downloads\User Reviews (1).csv"
apps_file = r"C:\Users\Riya Shivaji Patil\Downloads\Play Store Data (1).csv"

# Read the datasets
df_reviews = pd.read_csv(reviews_file)
df_apps = pd.read_csv(apps_file)

# Ensure necessary columns exist in both datasets
if 'App' in df_reviews.columns and 'Translated_Review' in df_reviews.columns and 'App' in df_apps.columns and 'Category' in df_apps.columns:
    
    # Filter apps in "Health & Fitness" category
    health_apps = set(df_apps[df_apps['Category'] == 'HEALTH_AND_FITNESS']['App'].dropna().unique())

    # Filter reviews for only health & fitness apps
    df_health_reviews = df_reviews[df_reviews['App'].isin(health_apps)].copy()

    # Get the list of unique app names to remove from text
    app_names = set(df_health_reviews['App'].dropna().unique())

    # Function to clean text
    def clean_text(text):
        text = str(text).lower()  # Convert to lowercase
        text = re.sub(r'\W+', ' ', text)  # Remove special characters
        words = text.split()  # Tokenize
        words = [word for word in words if word not in custom_stopwords and word not in app_names]  # Remove stopwords & app names
        return " ".join(words)

    # Apply text cleaning
    df_health_reviews['Cleaned_Review'] = df_health_reviews['Translated_Review'].astype(str).apply(clean_text)

    # Combine all reviews into one large text
    text = " ".join(df_health_reviews['Cleaned_Review'])

    # Generate word cloud
    wordcloud = WordCloud(width=800, height=400, background_color="white", stopwords=STOPWORDS).generate(text)

    # Display the word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Word Cloud of Most Frequent Keywords in Health & Fitness App Reviews")
    plt.show()

else:
    print("Required columns ('App', 'Review', 'Category') not found in the datasets.")


# In[ ]:




