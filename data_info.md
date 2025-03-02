# Million Song Dataset Web Project

## About Dataset

This project is based on a rebuilt version and subset of The Million Song Dataset. The dataset integrates multiple sources, including lastfm-spotify-tags-sim-userdata, The Echo Nest Taste Profile Subset, lastfm-dataset-2020, tagtraum genre annotations, and Spotify API.

### Dataset Features:

- **Music Info**: 50,683 songs (tracks)
- **User Listening History**: 9,711,301 records
- **MP3 Examples**: 100 songs per genre, 15 genres, totaling 1,500 songs

### Key Columns:

1. **track\_id** – Unique identifier for each track.
2. **name** – Title of the track.
3. **artist** – Name of the performer/band.
4. **spotify\_preview\_url** – Link to a short Spotify preview.
5. **spotify\_id** – Track's unique Spotify identifier.
6. **tags** – Descriptive labels (e.g., moods, themes).
7. **genre** – Music classification (e.g., pop, rock, jazz).
8. **year** – Release year of the track.
9. **duration\_ms** – Track length in milliseconds.
10. **danceability** – Score (0-1) indicating dance suitability.
11. **energy** – Score (0-1) representing track intensity.
12. **key** – Musical key (e.g., 1,2,3).
13. **loudness** – Track volume in decibels (dB).
14. **mode** – Major (1) or minor (0) key.
15. **speechiness** – Score (0-1) for spoken words.
16. **acousticness** – Score (0-1) indicating acoustic nature.
17. **instrumentalness** – Score (0-1) for absence of vocals.
18. **liveness** – Score (0-1) for live performance likelihood.
19. **valence** – Score (0-1) indicating happiness of the track.
20. **tempo** – Speed of track (BPM).
21. **time\_signature** – Number of beats per measure.

---

## Project Overview

This is my first web project, and I hope you like it! The project was completed in **5 days**, and I focused on learning web development from scratch. The model-making process was relatively easier for me, but frontend development was quite challenging since this is my first frontend project.

### Technologies Used:

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Machine Learning**:
  - Pandas for data handling
  - Scikit-learn for implementing Nearest Neighbors algorithm
  - LabelEncoder for preprocessing categorical data

### Modules Used:

```python
from flask import Flask, render_template, request
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import LabelEncoder
```

### Song Recommendation Function:

```python
def Reccomedation(self):
    """Get song recommendations."""
    
    song_index = self.songs_data.index[self.songs_data['name'] == self.song].tolist()[0]
    
    # Find nearest neighbors for the given song
    distances, indices = self.knn.kneighbors([self.feature_data.loc[song_index]])
    
    # Get actual song names (not numbers)
    recommended_songs = self.feature_data.iloc[indices[0][1:]].index.tolist()
    
    recommended_songs.insert(0, song_index)  # Insert original song at the start
    
    # Get song names from the index
    recommended_songs = [self.songs_data.loc[song_id, 'name'] for song_id in recommended_songs]
    
    # Get the song name, artist name, and genre
    recommended_songs = [self.songs_data.loc[self.songs_data['name'] == song] for song in recommended_songs]
    
    df = pd.concat(recommended_songs).to_dict(orient='records')
    
    return df
```

### Dataset Reference:

[Kaggle Dataset Link](https://www.kaggle.com/datasets/undefinenull/million-song-dataset-spotify-lastfm)

---

## Acknowledgments

I don't lie; I used ChatGPT, Canvas, and other online tools, especially for front-end development. Learning frontend was tough, but I am improving step by step. Thank you for supporting me!

### Feedback & Repository

You can check out my project and leave feedback on GitHub:
**GitHub Repository**: [Link]

Thank you for checking out my project! 🚀

