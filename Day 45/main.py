from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
html = response.text
soup = BeautifulSoup(html, "html.parser")
movies = soup.findAll(name="h3", class_="title")
movie_list = [i.getText() for i in movies]

with open("movies.txt", "a", encoding="utf-8") as mov:
    output =[mov.write(f"\n{i}") for i in reversed(movie_list)]



