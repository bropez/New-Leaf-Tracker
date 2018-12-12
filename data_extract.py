from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

html = urlopen('https://animalcrossing.fandom.com/wiki/Forgery')
soup = BeautifulSoup(html, "html.parser")
table_painting = soup.find_all("table", {"class": "wikitable"})[0]
table_statue = soup.find_all("table", {"class": "wikitable"})[1]

rows = []

# this changes all of the td's img data-src's and src's to the text
# TODO: refactor this into something more pythonic
for tr in table_painting.find_all('tr')[2:]:
    for td in tr.find_all('td'):
        if td.img:
            td.string = td.img('data-src')
        elif td.a:
            td.string = td.a.text

for tr in table_painting.find_all('tr')[:2]:
    for td in tr.find_all('td'):
        if td.img:
            td.string = td.img('src')
        elif td.a:
            td.string = td.a.text

for tr in table_statue.find_all("tr"):
    for td in tr.find_all("td"):
        if td.img:
            td.string = td.img['data-src']
        elif td.a:
            td.string = td.a.text

    # rows.append(tr)

# TODO: Need to find out how to transfer these two tables above into one and into a formatted csv

# with open('output_file.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerows(rows)
