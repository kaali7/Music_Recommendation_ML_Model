from flask import Flask, render_template, jsonify, request
import json
import random  # For demo purposes, replace with actual recommendation logic later

app = Flask(__name__)

# Sample music database (replace with actual database later)
SAMPLE_SONGS = [
    {"id": 1, "name": "Bohemian Rhapsody", "artist": "Queen", "genre": "Rock", "image": "/static/images/placeholder.jpg"},
    {"id": 2, "name": "Billie Jean", "artist": "Michael Jackson", "genre": "Pop", "image": "/static/images/placeholder.jpg"},
    {"id": 3, "name": "Sweet Child O' Mine", "artist": "Guns N' Roses", "genre": "Rock", "image": "/static/images/placeholder.jpg"},
    {"id": 4, "name": "Shape of You", "artist": "Ed Sheeran", "genre": "Pop", "image": "/static/images/placeholder.jpg"},
    {"id": 5, "name": "Stairway to Heaven", "artist": "Led Zeppelin", "genre": "Rock", "image": "/static/images/placeholder.jpg"},
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    song_name = data.get('song', '').lower()
    artist_name = data.get('artist', '').lower()
    genre = data.get('genre', '').lower()
    
    # Simple search logic (replace with more sophisticated search later)
    results = []
    for song in SAMPLE_SONGS:
        if (song_name in song['name'].lower() or 
            artist_name in song['artist'].lower() or 
            genre in song['genre'].lower()):
            results.append(song)
    
    # Get recommendations (currently random, replace with actual recommendation logic)
    recommendations = random.sample(
        [s for s in SAMPLE_SONGS if s not in results],
        min(6, len(SAMPLE_SONGS) - len(results))
    )
    
    return jsonify({
        'matches': results,
        'recommendations': recommendations
    })

if __name__ == '__main__':
    app.run(debug=True)