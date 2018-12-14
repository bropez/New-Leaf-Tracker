import csv
import requests

with open('output_file.csv', newline='') as f:
    reader = csv.reader(f)
    for line in reader:
        fake_n = line[0] + ' fake.jpg'
        real_n = line[0] + ' real.jpg'
        if line[1] != 'N/A':
            fake_url = line[1]
            response = requests.get(fake_url)
            with open('images/' + fake_n, 'wb') as f2:
                f2.write(response.content)
        real_url = line[2]
        response = requests.get(real_url)
        with open('images/' + real_n, 'wb') as f3:
            f3.write(response.content)