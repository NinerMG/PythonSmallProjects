import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
response_text = response.text
soup = BeautifulSoup(response_text, 'html.parser')

all_titles = soup.find_all('h3', class_='title')
all_titles.reverse()

with open('movies.txt', 'w') as file:
    for title in all_titles:
        file.write(str(title.getText()) + "\n")




