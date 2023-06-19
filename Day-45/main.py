import requests
from bs4 import BeautifulSoup

res = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(res.text, "html.parser")
content = soup.find_all("h3", class_="title")
content = content[::-1]

    
with open("movies.txt","a") as file:
    for i in content:
        file.write(i.getText()+"\n")