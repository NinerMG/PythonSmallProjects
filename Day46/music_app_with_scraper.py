import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify config
Client_ID = ""
Client_Secret = ""
Spotify_USERNAME = ""

def create_playlist():
    user_date = entry.get()
    BASIC_URL = "https://www.billboard.com/charts/hot-100/"
    header = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url=BASIC_URL + user_date, headers=header)
        soup = BeautifulSoup(response.text, 'html.parser')
        song_names_spans = soup.select("li ul li h3")
        song_names = [song.getText().strip() for song in song_names_spans]

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
        song_url = []
        year = user_date.split("-")[0]

        for song in song_names:
            result = sp.search(q=f"track:{song} year:{year}", type='track')
            try:
                uri = result['tracks']['items'][0]["uri"]
                song_url.append(uri)
            except IndexError:
                print(f"{song} doesn't exist in Spotify. Skipped.")

        playlist = sp.user_playlist_create(
            user=user_id,
            name=f"{user_date} Billboard 100",
            public=False,
            description="Playlist from Billboard Top 100"
        )
        sp.playlist_add_items(playlist_id=playlist["id"], items=song_url)
        messagebox.showinfo("Sukces!", "Playlistę utworzono!")

    except Exception as e:
        messagebox.showerror("Błąd", str(e))

# GUI setup
root = tk.Tk()
root.title("Spotify Billboard 100 Playlist")

label = tk.Label(root, text="Wprowadź datę (YYYY-MM-DD):")
label.pack(pady=10)

entry = tk.Entry(root, width=20)
entry.pack()

button = tk.Button(root, text="Utwórz playlistę", command=create_playlist)
button.pack(pady=10)

root.mainloop()
