import os
from dotenv import load_dotenv
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def get_playlist_info(playlist):
    return {
        "id": playlist["id"],
        "name": playlist["name"],
        "tracks_href": playlist["tracks"]["href"],
        "main_image": playlist["images"][0]["url"] if len(playlist["images"]) else None
    }

genres_seeds = [
    "acoustic", "afrobeat", "alt-rock", "alternative", "ambient", "anime", "black-metal", 
    "bluegrass", "blues", "bossanova", "brazil", "breakbeat", "british", "cantopop", 
    "chicago-house", "children", "chill", "classical", "club", "comedy", "country", "dance", 
    "dancehall", "death-metal", "deep-house", "detroit-techno", "disco", "disney", 
    "drum-and-bass", "dub", "dubstep", "edm", "electro", "electronic", "emo", "folk", "forro", 
    "french", "funk", "garage", "german", "gospel", "goth", "grindcore", "groove", "grunge", 
    "guitar", "happy", "hard-rock", "hardcore", "hardstyle", "heavy-metal", "hip-hop", "holidays", 
    "honky-tonk", "house", "idm", "indian", "indie", "indie-pop", "industrial", "iranian", 
    "j-dance", "j-idol", "j-pop", "j-rock", "jazz", "k-pop", "kids", "latin", "latino", "malay", 
    "mandopop", "metal", "metal-misc", "metalcore", "minimal-techno", "movies", "mpb", "new-age", 
    "new-release", "opera", "pagode", "party", "philippines-opm", "piano", "pop", "pop-film", 
    "post-dubstep", "power-pop", "progressive-house", "psych-rock", "punk", "punk-rock", "r-n-b", 
    "rainy-day", "reggae", "reggaeton", "road-trip", "rock", "rock-n-roll", "rockabilly", "romance", 
    "sad", "salsa", "samba", "sertanejo", "show-tunes", "singer-songwriter", "ska", "sleep", 
    "songwriter", "soul", "soundtracks", "spanish", "study", "summer", "swedish", "synth-pop", 
    "tango", "techno", "trance", "trip-hop", "turkish", "work-out", "world-music"
]


if __name__ == "__main__":
    # Spotify API credentials
    load_dotenv()
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')

    # Spotify API authentication
    client_credentials_manager = SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret
    )
    sp = spotipy.Spotify(
        client_credentials_manager=client_credentials_manager
    )

    # Search playlists by genre
    playlists_data = sp.search(q='alt-rock', type='playlist', limit=50, offset=0)
    playlists = []

    # print(playlists_data['playlists']['items'][:2])

    # for playlist in playlists_data['playlists']['items']:
    #     playlists.append(get_playlist_info(playlist))

    # print(len(playlists))