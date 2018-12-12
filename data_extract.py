from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

html = urlopen('https://animalcrossing.fandom.com/wiki/Forgery')
soup = BeautifulSoup(html, "html.parser")
table_painting = soup.find_all("table", {"class": "wikitable"})[0]
table_statue = soup.find_all("table", {"class": "wikitable"})

rows = []

# this is to set all of the img tag's sources into it's td instead
# it also adds all of the information to the rows list
for tr in table_painting.find_all("tr"):
    for td in tr.find_all("td"):
        if td.img:
            td.string = td.img['src']

for tr in table_statue.find_all("tr"):
    for td in tr.find_all("td"):
        if td.img:
            td.string = td.img['src']

    # rows.append(tr)

# TODO: Need to find out how to transfer these two tables above into one and into a formatted csv

# with open('output_file.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerows(rows)
