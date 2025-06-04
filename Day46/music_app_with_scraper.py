import requests
from bs4 import BeautifulSoup

BASIC_URL = "https://www.billboard.com/charts/hot-100/"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 OPR/119.0.0.0"
}

# user_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
hard_coded = "1994-03-05"
url = BASIC_URL + hard_coded

response = requests.get(url=url, headers=header)
response_text = response.text
soup = BeautifulSoup(response_text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
for song in song_names:
    print(song)