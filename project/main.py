from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://projects.fivethirtyeight.com/2022-nfl-predictions/games/'
page = urlopen(url)
# html = page.read().decode('utf-8')
soup = BeautifulSoup(page, "html.parser")

print(soup.get_text())