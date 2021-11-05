import os
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproj.settings')

import django
django.setup()

from my_app.models import Category, Album, Song

def get_category():
    categories = ["jazz", "classic", "rap", "Arabic"]
    category = Category.objects.get_or_create(name= random.choice(categories))[0]
    category.save()
    return category

from faker import Faker
fake = Faker()

def populate_albums(nb_of_albums=10):
    for i in range(nb_of_albums):
        fake_name = fake.name()
        album = Album.objects.get_or_create(name= fake_name)[0]
        album.save()

def populate_song(number_songs=10):
    albums = list(Album.objects.all())
    song  =[]
    for i in range(number_songs):
        fake_name = fake.name()
        song = Song.objects.get_or_create(
            name= fake_name,
            album= random.choice(albums),
            category= get_category)[0]
        song.save()
def delete_songs():
    Song.objects.all().delete()
if __name__ == "__main__":
    populate_albums(10)
    populate_song(1500)

