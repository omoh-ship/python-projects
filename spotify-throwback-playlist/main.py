import pprint

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100"
SPOTIFY_CLIENT_ID = "f80793a6271143edb48a6e87bfb76f75"
SPOTIFY_CLIENT_SECRET = "3edbce5e45e0453abc780a13cae3d2e2"
SPOTIPY_REDIRECT_URI = "http://localhost/"
SCOPE="playlist-modify-private"

date = input("What year do you want to travel to? Type the data in this format YYYY-MM-DD: ")

# go to website
response = requests.get(url=f"{BILLBOARD_URL}/{date}")
website_html = response.text

# webscrape
soup = BeautifulSoup(website_html, "html.parser")
singles = soup.find_all(name="span", class_="chart-element__information__song")
list_of_singles = [single.getText() for single in singles]



# Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=SCOPE,
                                               show_dialog=True,
                                               cache_path="token.txt"
                                               )
                     )

user_id = sp.current_user()['id']
song_uris = []
for song in list_of_singles:
    results = sp.search(f"track: {song} year: {date.split('-')[0]}", type="track")
    try:
        song_uri = results["tracks"]["items"][0]["uri"]
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
        continue
    song_uris.append(song_uri)

# CREATE PLAYLIST
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

# ADD TO PLAYLIST
sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)


# pprint.pprint(song_uris)

