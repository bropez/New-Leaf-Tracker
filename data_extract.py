from bs4 import BeautifulSoup
import requests
import csv

url = 'https://animalcrossing.fandom.com/wiki/Forgery'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
table_painting = soup.find('table', {'class': 'wikitable'})
table_statue = soup.find_all('table', {'class': 'wikitable'})[-1]

rows = []

# this changes all of the td's img data-src's and src's to the text
# TODO: refactor this into something more pythonic
for tr in table_painting.find_all('tr')[2:]:
    for td in tr.find_all('td'):
        if td.img:
            td.string = td.img('data-src')
        elif td.a:
            td.string = td.a.text
        td.string = td.text.strip()

for tr in table_painting.find_all('tr')[:2]:
    for td in tr.find_all('td'):
        if td.img:
            td.string = td.img('src')
        elif td.a:
            td.string = td.a.text
        td.string = td.text.strip()

for tr in table_statue.find_all("tr"):
    for td in tr.find_all("td"):
        if td.img:
            td.string = td.img['data-src']
        elif td.a:
            td.string = td.a.text
        td.string = td.text.strip()

for row in table_painting.find_all('tr'):
    rows.append([val.get_text() for val in row.find_all('td')])

for row in table_statue.find_all('tr'):
    rows.append([val.get_text() for val in row.find_all('td')])

with open('output_file.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(row for row in rows if row)
