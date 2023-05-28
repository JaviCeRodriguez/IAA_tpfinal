from spotipy import Spotify
from pandas import DataFrame

def get_playlist_info(playlist):
    return {
        "id": playlist["id"],
        "name": playlist["name"],
        "tracks_href": playlist["tracks"]["href"],
        "main_image": playlist["images"][0]["url"] if len(playlist["images"]) else None
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

    for idx, track_id in enumerate(playlists["id"]):
        try:
            # response = requests.get(track_href, headers=headers)
            # TODO: get all tracks from playlist
            playlist_tracks = sp.playlist_tracks(track_id)

            # TODO: Search for a better way to handle this with spotipy library
            # if response.status_code != 200:
            #     print(f'Algo pasó :( leí solamente {idx + 1} playlists')
            #     return tracks_playlists

            tracks_playlist = [get_track_info(item["track"]) for item in playlist_tracks["items"]]
            tracks_playlists += tracks_playlist
        except TypeError as err:
            print(f"Error en fila {idx}", err)
            continue
    
    return tracks_playlists