#!/usr/bin/env python
# coding: utf-8

# ![alt text](https://upload.wikimedia.org/wikipedia/commons/2/26/Spotify_logo_with_text.svg) 

# # Analysis of top 2000 Songs (2000-2019) via Spotify dataset
# - Data Distribution 
# - Top charts/artists comparison
# - Dynamic/Interactive Visualization
# - Data Correlation
# 

# ### Questions I wanted to answer: 
# - Top 25 tracks based on given features? (popularity and danceability were the ones I was most intrigued by)
# - Top artists based on popularity? 
# - Correlation between: 
#     - Danceability score and Popularity score?
#     - Energy score and Danceability score?
#     - Energy score and Loudness score?
# - Most popular Genres? 

# ### Visualizations used:
# - correlation matrix
# - feature distribution
# - trend-line 
# - Treemap
# - Boxplot 
# - Scatter plot
# - Barchart

# ## Download relevant libraries

# In[134]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.offline import init_notebook_mode
import seaborn as sns
import datetime as dt
import warnings
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns',None)
init_notebook_mode(connected=True) #enable Plotly charts to be displayed in Jupyter notebook


# ## Dataframe

# In[45]:


df = pd.read_csv("/Users/Mirzafamily/Downloads/k_spotify.csv")
df.head()


# In[9]:


df.info()


# In[4]:


df.drop_duplicates(inplace=True) #drop duplicates 


# In[5]:


#general
df.describe()


# ## Correlation Matrix Plot

# In[146]:


fig = px.imshow(df.corr(),text_auto=True,height=800,width=800,color_continuous_scale=px.colors.sequential.Blues,aspect='auto',title='<b>paiwise correlation of columns')
fig.update_layout(title_x=0.5)
fig.show()


# ## Column Distributions

# In[6]:


fig=make_subplots(rows=3,cols=3,subplot_titles=('<i>popularity', '<i>danceability', '<i>energy', '<i>loudness', '<i>speechiness', '<i>acousticness', '<i>liveness', '<i>valence', '<i>tempo'))
fig.add_trace(go.Histogram(x=df['popularity'],name='popularity'),row=1,col=1)
fig.add_trace(go.Histogram(x=df['danceability'],name='danceability'),row=1,col=2)
fig.add_trace(go.Histogram(x=df['energy'],name='energy'),row=1,col=3)
fig.add_trace(go.Histogram(x=df['loudness'],name='loudness'),row=2,col=1)
fig.add_trace(go.Histogram(x=df['speechiness'],name='speechiness'),row=2,col=2)
fig.add_trace(go.Histogram(x=df['acousticness'],name='acousticness'),row=2,col=3)
fig.add_trace(go.Histogram(x=df['liveness'],name='liveness'),row=3,col=1)
fig.add_trace(go.Histogram(x=df['valence'],name='valence'),row=3,col=2)
fig.add_trace(go.Histogram(x=df['tempo'],name='tempo'),row=3,col=3)
fig.update_layout(height=900,width=900,title_text='<b>Feature Distribution')
fig.update_layout(template='plotly_dark',title_x=0.5)


# ## Number of Songs Per Year (trend-line: somewhat evenly distributed)

# In[7]:


fig=px.area(df.groupby('year',as_index=False).count().sort_values(by='song',ascending=False).sort_values(by='year'),x='year',y='song',markers=True,labels={'song':'Total songs'},color_discrete_sequence=['green'],title='<b>Year by Year Songs collection')
fig.update_layout(hovermode='x',title_x=0.5)


# ## TOP 25 Fun 

# In[9]:


fig=px.line(df.sort_values(by='popularity',ascending=False).head(25),x='song',y='popularity',hover_data=['artist'],color_discrete_sequence=['green'],markers=True,title='<b> Top 25 songs in Spotify')
fig.show()


# In[10]:


fig=px.line(df.sort_values(by='danceability',ascending=False).head(25),x='song',y='danceability',hover_data=['artist'],color_discrete_sequence=['orange'],markers=True,title='<b> Top 25 danceability in Spotify')
fig.show()


# ## Top Singers based on Popularity ( treemap: click artist to see their most popular tracks)

# In[11]:


fig = px.treemap(df,path=[px.Constant('Singer'),'artist','genre','song'],values='popularity',title='<b>TreeMap of Singers Playlist')
fig.update_traces(root_color ='white')
fig.update_layout(title_x = 0.5)


# ## Popularity based on if the track included 'explicit language' (boxplot: true/false) 

# In[123]:


px.box(df,x='explicit',y='popularity',color='explicit',template='plotly_dark',color_discrete_sequence=['cyan','magenta'],title='<b>popularity based on explicit content')
#does explicit language fluctuate the popularity of a track? 


# ## Any correlation between Danceability score and Popularity score?  (scatter) 

# In[13]:


px.scatter(df,x='danceability',y='popularity',color='danceability',color_continuous_scale = px.colors.sequential.Plasma,template ='plotly_dark',title='<b>Danceability Versus Popularity')


# ## How about Energy score and Danceability score? 

# In[14]:


px.scatter(df,x='energy',y='danceability',color='danceability',color_continuous_scale=px.colors.sequential.Plotly3,template='plotly_dark',title='<b>Energy Versus Danceability')


# ## Energy score and Loudness score? 

# In[15]:


px.scatter(df,x='energy',y='loudness',color_discrete_sequence=['lightgreen'],template='plotly_dark',title='<b>Energy versus Loudness correlation')


# ## Popularity Over Time  

# In[30]:


# Set up the search query for your genre of interest
genre = "hip hop"

# Filter the dataframe to include only the rows with the desired genre
df_genre = df[df["genre"] == genre]

# Group the dataframe by year and calculate the average popularity for each year
df_popularity = df_genre.groupby("year")["popularity"].mean().reset_index()

# Create a line graph of popularity over time
plt.plot(df_popularity["year"], df_popularity["popularity"])
plt.title(f"Popularity of {genre.capitalize()} Music Over Time")
plt.xlabel("Year")
plt.ylabel("Popularity (Average)")
plt.show()


# ## Popularity Over Time (Better trendline)

# In[40]:


genre = "hip hop" #change to the genre you want 

# Filter the dataframe to include only the rows with the desired genre
df_genre = df[df["genre"] == genre]

# Group the dataframe by year and calculate the average popularity for each year
df_popularity = df_genre.groupby("year")["popularity"].mean().reset_index()

# Create a line graph of popularity over time using plotly.express
fig = px.line(df_popularity, x="year", y="popularity", color_discrete_sequence = ["orange"], markers = True, title=f"<b>Popularity of {genre.capitalize()} Music Over Time")
fig.update_xaxes(title_text="Year")
fig.update_yaxes(title_text="Popularity (Average)")
fig.show()


# ## Genre Popularity (Barchart) 

# In[118]:


genre_popularity = df.groupby('genre')['popularity'].mean().reset_index().sort_values(by='popularity', ascending=False).head(25)


# In[144]:


sns.set_style('darkgrid')
plt.figure(figsize=(15, 5))
my_palette = sns.color_palette('Greens', n_colors=25)
sns.barplot(x='genre', y='popularity', data = genre_popularity, palette = my_palette)
sns.despine()
plt.title('Genre Popularity on Spotify')
plt.xlabel('Genre', size = 15)
plt.ylabel('Popularity Score (0-100)', size = 15)
plt.xticks(rotation=90, size = 12.5)
plt.show()

