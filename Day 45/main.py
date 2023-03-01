from bs4 import BeautifulSoup
import requests

# response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
#
# html = response.text
#
# soup = BeautifulSoup(html, "html.parser")
#
# movies = soup.findAll(name="h3", class_="title")
#
# movie_list = [i.getText() for i in movies]
#
#
#
# with open("movies.txt", "a", encoding="utf-8") as mov:
#     output =[mov.write(f"\n{i}") for i in reversed(movie_list)]


response = requests.get("https://news.ycombinator.com")
html = response.text
soup = BeautifulSoup(html, "html.parser")

article_tag = soup.find_all(name="a", class_="storylink")
# print(article_tag)
#
# for i in article_tag:
#     text = i.find(name='a').getText()
#     link = i.find(name='a').get('href')
#     print(text)
#     print(link)
#
# upvote = soup.find_all(name="span", class_="score")
print(article_tag)
# article = [i.find(name='a').getText() for i in article_tag]
# link = [i.find(name='a').get('href') for i in article_tag]
# upvote = soup.find_all(name="span", class_="score")
#
# nl = [int(i.getText().split()[0]) for i in upvote]
# print(article[nl.index(max(nl))])
# print(link[nl.index(max(nl))])


