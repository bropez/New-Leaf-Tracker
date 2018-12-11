from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

html = urlopen('https://www.thonky.com/animal-crossing-new-leaf/paintings-works-of-art')
soup = BeautifulSoup(html, "html.parser")
table = soup.find("table", {"class": "table table-bordered"})

starter_link = "https://www.thonky.com/animal-crossing-new-leaf/"
rows = []

# this is to set all of the img tag's sources into it's td instead
# it also adds all of the information to the rows list
for tr in table.find_all("tr"):
    for td in tr.find_all("td"):
        if td.img:
            td.string = starter_link + td.img['src']

    rows.append(tr)

with open('output_file.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
