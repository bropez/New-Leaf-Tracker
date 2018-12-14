import os
# Configure settings for project
# need to run this before calling models from application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mywebsite.settings')

from django.core.files import File

import django
# import settings
django.setup()

import csv
from gallery.models import Art


def create_stuff():
    with open('output_file.csv', newline='') as f:
        reader = csv.reader(f)
        for line in reader:
            title = line[0]
            # real_img = line[2]
            description = line[3]
            artwork = Art(title=title, description=description)
            artwork.real_img.save(title + '.jpg', File(open('images/' + title + ' real.jpg', 'rb')))


if __name__ == '__main__':
    print("Populating the database... Please wait")
    create_stuff()
    print('Populating complete')
