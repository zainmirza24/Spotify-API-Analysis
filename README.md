<div align="center">
<img src= https://upload.wikimedia.org/wikipedia/commons/2/26/Spotify_logo_with_text.svg>
</div>

# Spotify API + Analysis Project
Spotify is the most popular global audio streaming service with 365m users, including 165m subscribers across 178 markets. They are the largest driver of revenue to the music business today.

## Objective 
This project contains 2 main objectives: 
1) Extract Spotify API from webscraping Billboard's 'Hot 100' list. (*API*)  
2) Analyze Spotify music data to gain insights into user preferences, popular genres, and the popularity of different artists. (*Analysis*)
Specific Questions I wanted to answer include: 
    - Top 25 tracks based on given features? (popularity and danceability were the ones I was most intrigued by)
    - Top artists based on popularity?
    - Correlation between:
        - Danceability score and Popularity score?
        - Energy score and Danceability score?
        - Energy score and Loudness score?
        - Most popular Genres?

## Data 
The data for this project is split into 2 sections, stemming from the 2 objectives:
1) *API*: To gain a better understanding of Spotify's **audio features**, lets pull all relevant data from Spotify's API, connecting to the 'Hot 100' list. With this we can derive all **audio features** from the top 100 songs in the US, constantly updating as Billboard continues to update the charts. Understanding how to pull Spotify's API allowed for a more clear understanding with the data analysis portion of this project   

2) *Analysis*: After completion of webscraping the 'Hot 100' list and connecting to Spotify's API, I grabbed a dataset from Kaggle containing **audio feature** statistics of the top 2000 tracks on Spotify from 2000-2019. This data contains 18 columns each describing the same qualities derived from the *API*. 

- **See "Data Description" file for column details** 
        





