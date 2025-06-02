from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')

article_tag = soup.select_one('.titleline a')
article_text = []
article_links = []


article_text = article_tag.getText()
article_link = article_tag.get('href')
article_upvote = soup.find(name='span', class_="score").getText()
