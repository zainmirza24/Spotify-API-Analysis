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
    - Data Description: 
        - artist: Name of the Artist
        - song: Name of the Track
        - duration_ms: Duration of the track in milliseconds.
        -  explicit: The lyrics or content of a song or a music video contain one or more of the criteria which could be considered offensive or unsuitable for children
        -   year: Release Year of the track.
        -   *popularity*: The higher the value the more popular the song is.
        -   *danceability*: Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.
* energy: Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity.
* key: The key the track is in. Integers map to pitches using standard Pitch Class notation. E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is -1.
* loudness: The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typically range between -60 and 0 db.
* mode: Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0.
* speechiness: Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks.
* acousticness: A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic.
* instrumentalness: Predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly "vocal". The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.
* liveness: Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live.
* valence: A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).
* tempo: The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.
* genre: Genre of the track.





