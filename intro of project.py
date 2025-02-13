#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hi")


# In[1]:


import pandas as pd


# In[2]:


data=pd.read_csv(r'C:\Users\Riya Shivaji Patil\Downloads\Heart.csv')


# In[3]:


data


# In[4]:


print(data)


# In[5]:


print(data.head)


# In[6]:


data.head()


# In[7]:


data.tail()


# In[11]:


data.describe()


# In[12]:


data.info()


# In[13]:


data.isnull()


# In[14]:


print(data.isnull().sum())


# In[17]:


import numpy as np


# In[18]:


data['Chol']=data['Chol'].replace(np.nan,data['Chol'].mean())


# In[20]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[19]:


Xpoints=np.array([0,6])
Ypoints=np.array([0,250])


# In[22]:


plt.plot(Xpoints,Ypoints,'o')
plt.show()


# In[28]:


y=np.array([25,25,15,35])
plt.pie(y)
plt.show()


# In[32]:


x=np.random.normal(170,10,250)
print(x)


# In[33]:


plt.hist(x)


# In[34]:


sns.distplot([0,1,2,3,4,5])
plt .show()


# In[8]:


pip install scikit-learn


# In[9]:


from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metric import mean_squared_error,r2_score


# In[3]:


import pandas as pd


# In[4]:


apps_df=pd.read_csv(r'C:\Users\Riya Shivaji Patil\Downloads\Play Store Data.csv')
reviews_df=pd.read_csv(r'C:\Users\Riya Shivaji Patil\Downloads\User Reviews.csv')


# In[5]:


apps_df.head()


# In[6]:


reviews_df.head()


# In[7]:


#pd.read_csv() :csv files
#pd.read_excel():excel files
#pd.read_sql():SQL database
#pd.read_json():JSON files


# In[8]:


#df.isnull():missing values
#df.dropna():removes rows and columns that contain the missing values
#df.fillna():fills missing values


# In[9]:


#df.duplicated():identifies duplicates
#df.drop_duplicates():removes duplicate rows


# In[5]:


#step 2:cleaning data
apps_df=apps_df.dropna(subset=['Rating'])
for column in apps_df.columns:
    apps_df[column].fillna(apps_df[column].mode()[0],inplace=True)
apps_df.drop_duplicates(inplace=True)
apps_df=apps_df=apps_df[apps_df['Rating']<=5]
reviews_df.dropna(subset=['Translated_Review'],inplace=True)


# In[13]:


apps_df.dtypes


# In[14]:


#Coverting installs column to numeric by removing commas and +
apps_df['Installs']=apps_df['Installs'].str.replace(',','').str.replace('+','').astype(int)

#convert price column to numeric after removing $
apps_df['Price']=apps_df['Price'].str.replace('$','').astype(float)


# In[15]:


apps_df.dtypes


# In[16]:


#merging apps and reviews data
merged_df=pd.merge(apps_df,reviews_df,on='App',how='inner')


# In[17]:


merged_df.head()


# In[28]:


#DATA TRANSFORMATION    
def convert_size(size):
   if 'M' in size:
     return float(size.replace('M',''))
   elif 'k' in size:
     return float(size.replace('k',''))/1024
   else:
     return np.nan
apps_df['Size']=apps_df['Size'].apply(convert_size)
     


# In[29]:


apps_df


# In[10]:


import numpy as np


# In[12]:


apps_df=pd.read_csv(r'C:\Users\Riya Shivaji Patil\Downloads\Play Store Data.csv')


# In[13]:


#Logarithmic
#apps_df['Log_Installs']=np.log(apps_df['Installs'])
apps_df['Log_Reviews']=np.log(apps_df['Reviews'])


# In[ ]:


apps_df['Reviews']=apps_df['Reviews'].astype(int)  


# In[14]:


apps_df['Log_Reviews'] = np.log(apps_df['Reviews'])


# In[43]:


apps_df.dtypes


# In[56]:


apps_df['Installs']=apps_df['Installs'].str.replace(',','').str.replace('+','').astype(int)


# In[57]:


apps_df.dtypes


# In[53]:


apps_df['Log_Installs']=np.log(apps_df['Installs'])


# In[58]:


apps_df['Reviews']=apps_df['Reviews'].astype(int)


# In[59]:


apps_df['Log_Reviews']=np.log(apps_df['Reviews'])


# In[60]:


apps_df.dtypes


# In[61]:


def rating_group(rating):
    if rating>=4:
        return 'Top rated app'
    elif rating>=3:
        return 'Above average'
    elif rating>=2:
        return 'Average'
    else:
        return 'Below average'
apps_df['Rating_Group']=apps_df['Rating'].apply(rating_group)


# In[ ]:


#revenue column
apps_df['Revenue']=apps_df['Price']*apps_df['Installs']


# In[63]:


apps_df


# In[37]:


from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import webbrowser
import os


# In[3]:


nltk.download('vader_lexicon')


# In[4]:


sia =SentimentIntensityAnalyzer()


# In[5]:


#polarity scores in SIA
#positive,negative,neural and compound:-1:very -ve
                                  #     +1:very +ve


# In[8]:


review="This app is amazing! I love the new features."
sentiment_score=sia.polarity_scores(review)
print(sentiment_score)


# In[9]:


review="This app is bad! I hate the new features."
sentiment_score=sia.polarity_scores(review)
print(sentiment_score)


# In[10]:


review="This app is very  bad! I hate the new features."
sentiment_score=sia.polarity_scores(review)
print(sentiment_score)


# In[11]:


review="This app is worst! I hate the new features."
sentiment_score=sia.polarity_scores(review)
print(sentiment_score)


# In[12]:


review="This app is okay."
sentiment_score=sia.polarity_scores(review)
print(sentiment_score)


# In[17]:


import pandas as pd


# In[18]:


reviews_df=pd.read_csv(r'C:\Users\Riya Shivaji Patil\Downloads\User Reviews.csv')


# In[19]:


reviews_df['Sentiment_Score']=reviews_df['Translated_Review'].apply(lambda x: sia.polarity_scores(str(x))['compound'])


# In[20]:


reviews_df.head()


# In[15]:


import pandas as pd


# In[16]:


apps_df=pd.read_csv(r'C:\Users\Riya Shivaji Patil\Downloads\Play Store Data.csv')


# In[19]:


apps_df['last Updated']= pd.to_datetime(apps_df['Last Updated'],errors='coerce')


# In[20]:


apps_df['Year'] = apps_df['Last Updated'].dt.year


# In[29]:


apps_df.head()


# In[42]:


apps_df['Year']=apps_df['Last Updated'].dt.year


# In[47]:


apps_df.head()


# In[46]:


print(apps_df)


# In[43]:


print(apps_df['Last Updated'].dtype)


# In[48]:


print(apps_df[apps_df['Last Updated'].isna()])


# In[52]:


apps_df['Year'] = apps_df['Last Updated'].dt.year   


# In[1]:


#PLOTLY  1


# In[3]:


import plotly.express as px
fig=px.bar(x=["A","B","C"],y=[1,2,3],title="Sample bar chart")
fig.show()


# In[4]:


fig.write_html("interactive_plot.html")


# In[5]:


#static visualizations:fixed imgs or plots,non interactive
#Interactive Visualizations:


# In[14]:


import os
import plotly.io as pio
import plotly.express as px


# In[15]:


html_files_path="./"
if not os.path.exists(html_files_path):
    os.makedirs(html_files_path)


# In[16]:


plot_containers=""


# In[17]:


def save_plot_as_html(fig, filename, insight):
    global plot_containers
    filepath = os.path.join(html_files_path, filename)
    html_content = pio.to_html(fig, full_html=False,  include_plotlyjs='inline')
    
    # Append the plot and its insight to plot_containers
    plot_containers += f"""
    <div class="plot-container" id="{filename}" onclick="openPlot('{filename}')">
        <div class="plot">{html_content}</div>
        <div class="insights">{insight}</div>
    </div>
    """
    fig.write_html(filepath, full_html=False,include_plotlyjs='inline')


# In[18]:


plot_width = 400
plot_height = 300
plot_bg_color = 'black'
text_color = 'white'
title_font = {'size': 16}
axis_font = {'size': 12}


# In[29]:


import plotly.express as px
import plotly.io as pio


# In[30]:


# Figure 1
category_counts = apps_df['Category'].value_counts().nlargest(10)
fig1 = px.bar(
    x=category_counts.index,
    y=category_counts.values,
    labels={'x': 'Category', 'y': 'Count'},
    title='Top Categories on Play Store',
    color=category_counts.index,
    color_discrete_sequence=px.colors.sequential.Plasma,
    width=400,
    height=300
)

fig1.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='white',
    title_font={'size': 16},
    xaxis=dict(title_font={'size': 12}),
    yaxis=dict(title_font={'size': 12}),
    margin=dict(l=10, r=10, t=30, b=10)
)

# fig1.update_traces(marker=dict(pattern=dict(line=dict(color='white', width=1))))
save_plot_as_html(
    fig1, 
    "Category Graph 1.html", 
    "The top categories on the Play Store are dominated by tools, entertainment, and productivity apps"
)


# In[31]:


import pandas as pd


# In[32]:


apps_df=pd.read_csv(r'C:\Users\Riya Shivaji Patil\Downloads\Play Store Data.csv')


# In[33]:


# Figure 2
type_counts = apps_df['Type'].value_counts()
fig2 = px.pie(
    values=type_counts.values,
    names=type_counts.index,
    title='App Type Distribution',
    color_discrete_sequence=px.colors.sequential.RdBu,
    width=400,
    height=300
)

fig2.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='white',
    title_font={'size': 16},
    margin=dict(l=10, r=10, t=30, b=10)
)

# fig2.update_traces(marker=dict(pattern=dict(line=dict(color='white', width=1))))
save_plot_as_html(fig2,"Type Graph 2.html", "Most apps on the Playstore are free, indicating a strategy to attract users first and monetize through ads")


# In[27]:


# Figure 3
fig3 = px.histogram(
    apps_df,
    x='Rating',
    nbins=20,
    title='Rating Distribution',
    color_discrete_sequence=['#636EFA'],
    width=400,
    height=300
)

fig3.update_layout(
    plot_bgcolor="black",
    paper_bgcolor="black",
    font_color='white',
    title_font_size=16,
    xaxis_title_font_size=12,
    yaxis_title_font_size=12,
    margin=dict(l=10, r=10, t=30, b=10)
)

# fig3.update_traces(marker=dict(pattern=dict(line_color='white', width=1)))

save_plot_as_html(fig3, "Rating Graph 3.html", "Ratings are skewed towards higher values, suggesting that most apps are rated favorably by users")


# In[26]:


reviews_df=pd.read_csv(r'C:\Users\Riya Shivaji Patil\Downloads\User Reviews.csv')


# In[28]:


# Figure 4
sentiment_counts = reviews_df['Sentiment_Polarity'].value_counts()

fig4 = px.bar(
    x=sentiment_counts.index,
    y=sentiment_counts.values,
    labels={'x': 'Sentiment_Polarity', 'y': 'Count'},
    title='Sentiment Distribution',
    color=sentiment_counts.index,
    color_discrete_sequence=px.colors.sequential.RdPu,
    width=400,
    height=300
)

fig4.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='white',
    title_font_size=16,
    xaxis_title_font_size=12,
    yaxis_title_font_size=12,
    margin=dict(l=10, r=10, t=30, b=10)
)

# fig4.update_traces(marker=dict(pattern=dict(line_color='white', width=1)))

save_plot_as_html(fig4, "Sentiment Graph 4.html", "Sentiments in reviews show a mix of positive and negative feedback, with a slight lean towards positive")


# In[39]:


reviews_df.dtypes


# In[18]:


# Figure 5
installs_by_category = apps_df.groupby('Reviews')['Installs'].sum().nlargest(10)

fig5 = px.bar(
    x=installs_by_category.index,
    y=installs_by_category.values,
    orientation='h',
    labels={'x': 'Reviews', 'y': 'Category'},
    title='Installs by Category',
    color=installs_by_category.index,
    color_discrete_sequence=px.colors.sequential.Blues,
    width=400,
    height=300
)

fig5.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='white',
    title_font_size=16,
    xaxis_title_font_size=12,
    yaxis_title_font_size=12,
    margin=dict(l=10, r=10, t=30, b=10)
)

# fig5.update_traces(marker=dict(pattern=dict(line_color='white', width=1)))

save_plot_as_html(fig5, "Installs Graph 5.html", "The categories with the most installs are social and communication apps, reflecting their broad appeal")


# In[19]:


apps_df.dtypes


# In[20]:


apps_df.dtypes


# In[34]:


# Updates Per Year Plot
updates_per_year = apps_df['Last Updated'].dt.year.value_counts().sort_index()

fig6 = px.line(
    x=updates_per_year.index,
    y=updates_per_year.values,
    labels={'x': 'Year', 'y': 'Number of Updates'},
    title='Number of Updates Over the Years',
    color_discrete_sequence=['#636EFA'],
    width=plot_width,
    height=plot_height
)

fig6.update_layout(
    plot_bgcolor=plot_bg_color,
    paper_bgcolor=plot_bg_color,
    font_color=text_color,
    title_font=title_font,
    xaxis=dict(title_font=axis_font),
    yaxis=dict(title_font=axis_font),
    margin=dict(l=10, r=10, t=30, b=10)
)

plot_containers = save_plot_as_html(fig5, "Installs_Graph_5.html", "Updates have been increasing over the years, showing that developers are actively maintaining and improving their apps")


# In[50]:


# Figure 7
revenue_by_category = apps_df.groupby('Category')['Price'].sum().nlargest(10)

fig7 = px.bar(
    x=revenue_by_category.index,
    y=revenue_by_category.values,
    labels={'x': 'Category', 'y': 'Price'},
    title='Revenue by Category',
    color=revenue_by_category.index,
    color_discrete_sequence=px.colors.sequential.Greens,
    width=400,
    height=300
)

fig7.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='white',
    title_font_size=16,
    xaxis_title_font_size=12,
    yaxis_title_font_size=12,
    margin=dict(l=10, r=10, t=30, b=10)
)

# fig7.update_traces(marker=dict(pattern=dict(line_color='white', width=1)))

save_plot_as_html(fig7, "Revenue Graph 7.html", "Categories such as Business and Productivity lead in revenue generation, indicating their monetization potential")


# In[35]:


# Figure 8
genre_counts = apps_df['Genres'].str.split(';', expand=True).stack().value_counts().nlargest(10)

fig8 = px.bar(
    x=genre_counts.index,
    y=genre_counts.values,
    labels={'x': 'Genre', 'y': 'Count'},
    title='Top Genres',
   color=genre_counts.index, # This line might need correction
    color_discrete_sequence=px.colors.sequential.OrRd,
    width=400,
    height=300
)

fig8.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='white',
    title_font_size=16,
    xaxis_title_font_size=12,
    yaxis_title_font_size=12,
    margin=dict(l=10, r=10, t=30, b=10)
)

# fig8.update_traces(marker=dict(pattern=dict(line_color='white', width=1)))

save_plot_as_html(fig8, "Genre Graph 8.html", "Action and Casual genres are the most common, reflecting users' preference for engaging and easy-to-play games")


# In[12]:


# Figure 9
fig9 = px.scatter(
    apps_df,
    x='Last Updated',
    y='Rating',
    color="Type",
    title='Impact of Last Update on Rating',
    color_discrete_sequence=px.colors.qualitative.Vivid,
    width=400,
    height=300
)

fig9.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='white',
    title_font_size=16,
    xaxis_title_font_size=12,
    yaxis_title_font_size=12,
    margin=dict(l=10, r=10, t=30, b=10)
)

# fig9.update_traces(marker=dict(pattern=dict(line_color='white', width=1)))

save_plot_as_html(fig9, "Update Graph 9.html", "The Scatter Plot shows a weak correlation between the last update and ratings, suggesting that more frequent updates do not necessarily lead to higher ratings")


# In[5]:


import pandas as pd
import plotly.express as px

# Create a box plot comparing Ratings of Paid vs Free Apps
fig10 = px.box(
    apps_df,
    y='Rating',
    color='Type',
    title='Rating for Paid vs Free Apps',
    color_discrete_sequence=px.colors.qualitative.Pastel,
    width=400,
    height=300
)

# Customize layout
fig10.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='white',
    title_font_size=16,
    xaxis_title_font_size=12,
    yaxis_title_font_size=12,
    margin=dict(l=10, r=10, t=30, b=10)
)

# Define save_plot_as_html function (if not already defined)
def save_plot_as_html(fig, filename, description):
    fig.write_html(filename)
    print(f"Plot saved as {filename}. {description}")

# Save the plot
save_plot_as_html(fig10, "Paid_Free_Graph_10.html", "Paid apps generally have higher ratings compared to free apps, suggesting that users expect higher quality from paid apps.")


# In[30]:


plot_containers_split=plot_containers.split('</div>')


# In[31]:


if len(plot_containers_split)>1:
    final_plot=plot_containers_split[-2]+'</div>'
else:
    final_plot=plot_containers


# In[1]:


dashboard_html="""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Google Play Store Review Analytics</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #333;
      color: #fff;
      margin: 0;
      padding: 0;
    }

    .header {
      display: flex;
      align-items: center;
      justify-content: center;
     padding: 20px;
      background-color: #444
    }

    .header img {
      margin:0 10px;
      height: 50px;
    }

    .container {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      padding: 20px;
    }



    .plot_containers{
  border: 2px solid #555;
  margin: 10px;
  padding: 10px;
  width: {plot_width}px;
  height: {plot_height}px;
  overflow: hidden;
  position: relative;
  cursor: pointer;
}

.insights {
  display: none;
  position: absolute;
  right: 10px;
  top: 10px;
  background-color: rgba(0, 0, 0, 0.7);
  padding: 5px;
  border-radius: 5px;
  color: #fff;
}


 .plot-containers:hover .insights {
      display: block;
    }
  </style>
  <script>
    function openPlot(filename) {
      window.open(filename, '_blank');
    }
  </script>
</head>
<body>

  <div class="header">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Logo_2013_Google.png/800px-Logo_2013_Google.png" alt="Google Logo">
    <h1>Google Play Store Reviews Analytics</h1>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Google_Play_Store_badge_EN.svg/1024px-Google_Play_Store_badge_EN.svg.png" alt="Google Play Store Badge">
  </div>

  <div class="container">
  {plots}
    </div>

</body>
</html>

"""


# In[2]:


import os
import webbrowser


# In[3]:


final_html = dashboard_html.format(plots=plot_containers, plot_width=plot_width, plot_height=plot_height)


# In[4]:


dashboard_path = os.path.join(html_files_path, "web_page.html")


# In[8]:


with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(final_html)


# In[9]:


webbrowser.open('file://'+os.path.realpath(dashboard_path))


# In[37]:


dashboard_html = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Google Play Store Review Analytics</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #333;
            color: #fff;
            margin: 0;
            padding: 0;
        }}

        .header {{
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
            background-color: #444;
        }}

        .header img {{
            margin: 0 10px;
            height: 50px;
        }}

        .container {{
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            padding: 20px;
        }}

        .plot-container {{
    border: 2px solid #555;
    margin: 10px;
    padding: 10px;
    width: {plot_width}px;
    height: {plot_height}px;
    overflow: hidden;
    position: relative;
    cursor: pointer;
}}

.insights {{
    display: none;
    position: absolute;
    right: 10px;
    top: 10px;
    background-color: rgba(0, 0, 0, 0.7);
    padding: 5px;
    border-radius: 5px;
    color: #fff;
}}


.plot-container:hover .insights {{
    display: block;
}}
</style>
<script>
    function openPlot(filename) {{
        window.open(filename, '_blank');
    }}
</script>
</head>
<body>
    <div class="header">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Logo_2013_Google.png/800px-Logo_2013_Google.png" 
             alt="Google Logo">
        <h1>Google Play Store Reviews Analytics</h1>
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Google_Play_Store_badge_EN.svg/1024px-Google_Play_Store_badge_EN.svg.png" 
             alt="Play Store Logo">
    </div>
    <div class="container">
        {plots}
    </div>
</body>
</html>

"""


# In[38]:


final_html = dashboard_html.format(plots=plot_containers, plot_width=plot_width, plot_height=plot_height)


# In[ ]:





# In[ ]:





# In[ ]:




