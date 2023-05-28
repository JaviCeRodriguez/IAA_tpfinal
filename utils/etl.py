from tqdm import tqdm
from spotipy import Spotify
from pandas import DataFrame

def get_playlist_info(playlist: dict, genre: str):
    return {
        "id": playlist["id"],
        "name": playlist["name"],
        "tracks_href": playlist["tracks"]["href"],
        "main_image": playlist["images"][0]["url"] if len(playlist["images"]) else None,
        "genre": genre
    }


def get_track_info(track):
    return {
        "id": track["id"],
        "name": track["name"],
        "track_href": track["href"],
        "album_name": track["album"]["name"],
        "album_id": track["album"]["id"]
    }


def get_tracks_from_playlists(playlists: DataFrame, sp: Spotify):
    tracks_playlists = []
    errors = []

    for idx, playlist_id in enumerate(tqdm(playlists["id"])):
        try:
            # TODO: get all tracks from playlist
            playlist_tracks = sp.playlist_tracks(playlist_id=playlist_id)
            tracks_playlist = [get_track_info(item["track"]) for item in playlist_tracks["items"]]
            tracks_playlists += tracks_playlist
        except TypeError as err:
            # print(f"Error en fila {idx}", err)
            errors.append(f"Error en fila {idx}, {err}")
            continue
    
    print('Errors: ', errors)

    return tracks_playlists