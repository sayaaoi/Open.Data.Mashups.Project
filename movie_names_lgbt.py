# web scrape from Wikipedia

# import packages needed
import requests as req
from bs4 import BeautifulSoup

origin_page = req.get("https://en.wikipedia.org/wiki/List_of_LGBT-related_films")

soup = BeautifulSoup(origin_page.text, "html.parser")
# print(soup.prettify())
# print(soup.find_all('a'))

for link in soup.find_all('a'):
    # print(link.get('title'))
    print(link.string)
