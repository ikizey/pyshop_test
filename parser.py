"""Разработайте скрипт на Python, который будет выводить в консоль (STDOUT) информацию о предстоящих событиях анонсированных на главной странице python.org (Upcoming Events). Вывод информации оформите по своему усмотрению. Выбор библиотек на ваше усмотрение."""

import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

events_block = soup.find("div", class_="event-widget")
events = events_block.find_all("a")
for x in events:
    if x.text != "More":
        print(x.text)
