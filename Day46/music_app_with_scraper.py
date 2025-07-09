import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup


Client_ID = "11c54aee5102472cbc5fd3bdaabb7381"
Client_Secret = "311e1d1947f041d5b123c7392d8fa61b"
Spotify_USERNAME = "ukgboez7d6gsb40fzfqpa0fhf"


### Top 100 music request

BASIC_URL = "https://www.billboard.com/charts/hot-100/"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 OPR/119.0.0.0"
}

user_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
hard_coded = "1994-03-05"
url = BASIC_URL + user_date

response = requests.get(url=url, headers=header)
response_text = response.text
soup = BeautifulSoup(response_text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
# for song in song_names:
#     print(song)


### Spotify request

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=Client_ID,
    client_secret=Client_Secret,
    redirect_uri="https://example.com",
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path="token.txt",
    username=Spotify_USERNAME,
))
user_id = sp.current_user()["id"]
print("Your Spotify user ID:", user_id)


### Searching and pasting into song list top 100 music found eariler

song_url = []
year = user_date.split("-")[0]

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type='track')
    try:
        uri = result['tracks']['items'][0]["uri"]
        song_url.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

### creating a playlist
playlist = sp.user_playlist_create(
    user=user_id,
    name = f"{user_date} Billboard 100",
    public=False,
    description="Playlist with top songs from one of my favorite days"
)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_url)