from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd


app = Flask(__name__)

class music_Data:
    def __init__(self, songs):


        # Recommendation Model
        self.model = pickle.load(open('static/data/save_data_model_pkl_file/music_model.pkl', 'rb'))
          
        # Music Data     
        self.songs = songs
    
    def INdata(self):
        df = pd.read_csv('static/data/Music Info.csv')
        song_data = df['name'].unique().tolist()
        if self.songs in self.song_data:
            return True
        else:
            return False
        
    
@app.route('/', methods=['POST', 'GET'])
def index():

    df = pd.read_csv('static/data/Music Info.csv')
    select_song = df['name'].unique().tolist()

    # working search engine
    if request.method == 'POST':
        song = request.form['song']
        music = music_Data(song)

        if music.INdata():
            return render_template('index.html', message="Song found in dataset!")
        else:
            return render_template('index.html', message="Song not found!")

    else:
        return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html') 

if __name__ == '__main__':
    app.run(debug=True)