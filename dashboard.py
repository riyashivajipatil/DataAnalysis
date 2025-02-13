#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
apps_df=pd.read_csv(r'C:\Users\Riya Shivaji Patil\Downloads\Play Store Data.csv')
reviews_df=pd.read_csv(r'C:\Users\Riya Shivaji Patil\Downloads\User Reviews.csv')


# In[4]:


#PLOTLY  1


# In[2]:


import plotly.express as px
fig=px.bar(x=["A","B","C"],y=[1,2,3],title="Sample bar chart")
fig.show()


# In[ ]:





# In[ ]:





# In[17]:


import os
import plotly.io as pio
import plotly.express as px


# In[34]:


html_files_path="./"
if not os.path.exists(html_files_path):
    os.makedirs(html_files_path)


# In[35]:


plot_containers=""


# In[36]:


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


# In[37]:


plot_width = 400
plot_height = 300
plot_bg_color = 'black'
text_color = 'white'
title_font = {'size': 16}
axis_font = {'size': 12}


# In[38]:


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


# In[39]:


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


# In[40]:


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


# In[41]:


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


# In[42]:


import pandas as pd
import plotly.express as px



# In[43]:


import pandas as pd
import plotly.express as px

# Load data
file_path = r'C:\Users\Riya Shivaji Patil\Downloads\Play Store Data.csv'
apps_df = pd.read_csv(file_path)

# Convert 'Reviews' column to integer
apps_df['Reviews'] = apps_df['Reviews'].astype(str).str.replace(',', '', regex=True)
apps_df['Reviews'] = pd.to_numeric(apps_df['Reviews'], errors='coerce').fillna(0).astype(int)

# Convert 'Installs' column to integer
apps_df['Installs'] = apps_df['Installs'].astype(str).str.replace(r'[+,]', '', regex=True)
apps_df['Installs'] = pd.to_numeric(apps_df['Installs'], errors='coerce').fillna(0).astype(int)

# Group installs by Reviews
installs_by_category = apps_df.groupby('Reviews')['Installs'].sum().nlargest(10)

# Create Bar Chart
fig5 = px.bar(
    x=installs_by_category.index,
    y=installs_by_category.values,
    orientation='h',
    labels={'x': 'Reviews', 'y': 'Installs'},
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

# Function to save plot as HTML
def save_plot_as_html(fig, filename):
    fig.write_html(filename)
    return f'<iframe src="{filename}" width="100%" height="400px"></iframe>'
# Save the plot
save_plot_as_html(fig5, "Installs_Graph_5.html", "The categories with the most installs are social and communication apps, reflecting their broad appeal.")


# In[44]:


import pandas as pd
import plotly.express as px

# Ensure 'Last Updated' is in datetime format
apps_df['Last Updated'] = pd.to_datetime(apps_df['Last Updated'], errors='coerce')

# Extract year and count occurrences
updates_per_year = apps_df['Last Updated'].dt.year.value_counts().sort_index()

# Define missing variables
plot_width = 800  # Adjust as needed
plot_height = 500  # Adjust as needed
plot_bg_color = "white"
text_color = "black"
title_font = {"size": 20, "color": "black"}
axis_font = {"size": 15, "color": "black"}

# Create the line plot
fig6 = px.line(
    x=updates_per_year.index,
    y=updates_per_year.values,
    labels={'x': 'Year', 'y': 'Number of Updates'},
    title='Number of Updates Over the Years',
    color_discrete_sequence=['#AB63FA'],
    width=plot_width,
    height=plot_height
)

# Customize layout
fig6.update_layout(
    plot_bgcolor=plot_bg_color,
    paper_bgcolor=plot_bg_color,
    font_color=text_color,
    title_font=title_font,
    xaxis=dict(title_font=axis_font),
    yaxis=dict(title_font=axis_font),
    margin=dict(l=10, r=10, t=30, b=10)
)

# Define save_plot_as_html function (if not already defined)
def save_plot_as_html(fig, filename):
    fig.write_html(filename)
    return f'<iframe src="{filename}" width="100%" height="400px"></iframe>'
    
# Save plot
save_plot_as_html(fig6, "updates_per_year.html", "Updates have been increasing over the years, showing that developers are actively maintaining and improving applications.")


# In[ ]:





# In[45]:


#Figure 5
installs_by_category = apps_df.groupby('Category')['Installs'].sum().nlargest(10)

fig5 = px.bar(
    x=installs_by_category.index,
    y=installs_by_category.values,
    orientation="h",
    labels={'x': "Installs", 'y': "Category"},
    title="Installs by Category",
    color=installs_by_category.index,
    color_discrete_sequence=px.colors.sequential.Blues,
    width=400,
    height=300
)

fig5.update_layout(
    plot_bgcolor="black",
    paper_bgcolor='black',
    font_color='white',
    title_font={'size':16},
    xaxis_title_font={'size':12},

    yaxis_title_font={'size':12},
    margin=dict(l=10, r=10, t=30, b=10)
)

fig5.update_traces(marker=dict(pattern=dict(line=dict(color="white", width=1))))

save_plot_as_html(fig5, "Installs Graph 5.html", "The categories with the most installs are social and communication")


# In[46]:


import pandas as pd
import plotly.express as px

# Ensure 'Price' is numeric (convert from string if necessary)
apps_df['Price'] = pd.to_numeric(apps_df['Price'], errors='coerce')

# Group by 'Category' and sum up 'Price', then get top 10 categories
revenue_by_category = apps_df.groupby('Category')['Price'].sum().nlargest(10)

# Create the bar chart
fig7 = px.bar(
    x=revenue_by_category.index,
    y=revenue_by_category.values,
    labels={'x': 'Category', 'y': 'Total Revenue'},
    title='Revenue by Category',
    color=revenue_by_category.index,
    color_discrete_sequence=px.colors.sequential.Greens,
    width=400,
    height=300
)

# Customize layout
fig7.update_layout(
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
save_plot_as_html(fig7, "Revenue_Graph_7.html", "Categories such as Business and Productivity lead in revenue generation, indicating their monetization potential.")


# In[47]:


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


# In[48]:


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


# In[49]:


# Figure 10
fig10 = px.box(
    apps_df,
    y='Rating',
    color='Type',
    title='Rating for Paid vs Free Apps',
    color_discrete_sequence=px.colors.qualitative.Pastel,
    width=400,
    height=300
)

fig10.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='white',
    title_font_size=16,
    xaxis_title_font_size=12,
    yaxis_title_font_size=12,
    margin=dict(l=10, r=10, t=30, b=10)
)

# fig10.update_traces(marker=dict(pattern=dict(line_color='white', width=1)))

save_plot_as_html(fig10, "Paid Free Graph 10.html", "Paid apps generally have higher ratings compared to free apps, suggesting that users expect higher quality from paid apps")


# In[50]:


plot_containers_split=plot_containers.split('</div>')


# In[51]:


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


# In[52]:


final_html = dashboard_html.format(plots=plot_containers, plot_width=plot_width, plot_height=plot_height)


# In[53]:


final_html = dashboard_html.replace("{plots}", plot_containers).replace("{plot_width}", str(plot_width)).replace("{plot_height}", str(plot_height))



# In[54]:


dashboard_path = os.path.join(html_files_path, "web_page.html")


# In[55]:


with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(final_html)


# In[56]:


import webbrowser
import os


# In[57]:


webbrowser.open('file://'+os.path.realpath(dashboard_path))


# In[ ]:





# In[ ]:




