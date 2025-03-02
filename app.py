from flask import Flask, render_template, request
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

class music_Data:
    def __init__(self, song):
        # Load feature data
        self.feature_data = pd.read_csv('static/data/feature_data.csv')

        # Load songs data
        self.songs_data = pd.read_csv('static/data/songs_artist.csv')

        # Ensure 'name' column exists and set it as index
        if 'name' in self.feature_data.columns:
            self.feature_data.set_index('name', inplace=True)

        # Encode only the features (not the index)
        self.feature_data = self.feature_data.apply(LabelEncoder().fit_transform)

        # Train KNN model using numerical data
        self.knn = NearestNeighbors(n_neighbors=7, metric='euclidean')
        self.knn.fit(self.feature_data)

        # Store the song name
        self.song = song

    def INdata(self):
        """Check if the song exists in the dataset."""
        return self.song in self.songs_data['name'].values

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

        #get the song name , artist name, genre 
        recommended_songs = [self.songs_data.loc[self.songs_data['name'] == song] for song in recommended_songs]

        df = pd.concat(recommended_songs).to_dict(orient='records')

        return df

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        song = request.form['song']
        print(f"User searched for: {song}")

        music = music_Data(song)

        if music.INdata():
            print("Song found in dataset!")
            recommended_songs = music.Reccomedation()
            print("Recommended songs:", recommended_songs)
            return render_template('index.html', message="Song found!", recommendations=recommended_songs, pos=1)
        else:
            print("Song not found!")
            other_random_list = music.songs_data.sample(6).to_dict(orient='records')
            return render_template('index.html', message="Song not found!" , pos=2)
        
    random_songs_list = pd.read_csv('static/data/songs_artist.csv').sample(12).to_dict(orient='records')
    return render_template('index.html', songs=random_songs_list, pos=0)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
