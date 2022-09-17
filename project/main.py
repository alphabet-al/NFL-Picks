from bs4 import BeautifulSoup
from urllib.request import urlopen
import xml

url = 'https://projects.fivethirtyeight.com/2022-nfl-predictions/games/'
page = urlopen(url)
soup = BeautifulSoup(page, "lxml")

current_week = soup.select('section.week')[0]
matchups = current_week.find_all(class_ = 'game-body')

winner = []

for i in matchups:
    versus = i.find_all('td', class_='td text team')
    probability = i.find_all('td', class_ = 'td number chance')
    
    versus = [v.text for v in versus]
    probability = [p.text for p in probability]

    if probability[0] > probability[1]:
        winner.append(versus[0])
    elif probability[1] > probability[0]:
        winner.append(versus[1])
    else:
        winner.append('Even match between {} and {}'.format(versus[0], versus[1]))

print(winner)