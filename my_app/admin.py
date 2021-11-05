from django.contrib import admin
from my_app.models import Category, Album, Song


# Register your models here.

admin.site.register(Category)
admin.site.register(Album)
admin.site.register(Song)