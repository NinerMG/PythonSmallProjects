from bs4 import BeautifulSoup
import lxml

# simple web scraper

with open('website.html') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'lxml')
# print(soup.title.name)
all_anchor_tags = soup.find_all(name='a')
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())