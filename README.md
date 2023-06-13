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

## Visualizations 

### Correlation Matrix: 




<img width="900" alt="Screen Shot 2023-05-11 at 3 46 43 PM" src="https://github.com/zainmirza24/Spotify-API-Analysis/assets/94576481/3ad2732d-c321-4b17-b662-f719eafdd85d">

### Feature Distribution: 

![newplot](https://github.com/zainmirza24/Spotify-API-Analysis/assets/94576481/3d79deed-1c0e-4106-af92-8b6be8333799)

### TOP 25: 

#### - Songs in Spotify based on 'Popularity'

![newplot (1)](https://github.com/zainmirza24/Spotify-API-Analysis/assets/94576481/68425d9d-4f7b-422c-b78e-c0594fe520d3)

#### - Songs in Spotify based on 'Danceability'

![newplot (2)](https://github.com/zainmirza24/Spotify-API-Analysis/assets/94576481/050f9dd3-a0bb-4e8f-9478-c7d106a1f3d3)

#### - Top Singers based on Popularity (Treemap)

![newplot (3)](https://github.com/zainmirza24/Spotify-API-Analysis/assets/94576481/a2ba2805-a2bb-411c-a043-57a251fe4bcb)

##### - Detailed Look at Treemap (Songs organized by each artist and displayed by 'Popularity' score) 

![newplot (4)](https://github.com/zainmirza24/Spotify-API-Analysis/assets/94576481/6e65fa0b-19ce-4f07-ba36-0d85d9130494)









        






