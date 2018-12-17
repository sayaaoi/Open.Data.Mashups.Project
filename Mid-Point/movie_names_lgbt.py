# web scrape from Wikipedia

# import packages needed
import requests as req
from bs4 import BeautifulSoup

origin_page = req.get("https://en.wikipedia.org/wiki/List_of_LGBT-related_films")

soup = BeautifulSoup(origin_page.text, "html.parser")
# print(soup.prettify())

movie_name = ''
for element in soup.find_all('a'):
    if element.get('title') is not None:
        movie_name += (str(element.string) + "***")

# Get movie names part only
chunks = movie_name.split('edit***')
for chunk in chunks:
    if chunk.startswith('Z'):
        z_index = chunks.index(chunk)
    if chunk.startswith('$'):
        a_index = chunks.index(chunk)

movie_list = chunks[a_index : z_index+1]

# convert each movie into an element of a list
movie_names = []
for movie_chunk in movie_list:
    movie_temp = movie_chunk.split('***')
    movie = movie_temp[:-1]
    movie_names.extend(movie)
    
# a list of all lgbt movie names from Wiki page
print(movie_names)
