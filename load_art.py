import os
# Configure settings for project
# need to run this before calling models from application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mywebsite.settings')

from django.core.files import File

import django
# import settings
django.setup()

from gallery.models import Art


def create_stuff():
    atitle = Art(title="Redd's new title")
    atitle.save()

    ao_title = Art(original_title="New Starry Night")
    ao_title.save()

    adescription = Art(description="This is a test description of the painting")
    adescription.save()


def populate(N=5):

    for entry in range(N):
        artwork = Art(title="Redd's new title", original_title="Its a night",
                      description="This the new descrip")
        artwork.picture.save('star_painting.jpg', File(open('starry_night.jpg', 'rb')))


if __name__ == '__main__':
    print("Populating the database... Please wait")
    populate(20)
    print('Populating complete')