from django.db import models

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateField(auto_now_add= True)
    def __str__(self):
        return self.name

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name
        }

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    ctegory = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add= True, null=True)
    def __str__(self):
        return f"Song name: {self.name}, Album:{self.album.name}, Category:{self.ctegory.name}"
