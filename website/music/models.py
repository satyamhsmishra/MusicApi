from django.db import models
from django.urls import reverse
class Album(models.Model):
    artist=models.CharField(max_length=250)
    album_title=models.CharField(max_length=500)
    genre=models.CharField(max_length=100)
    album_logo=models.FileField()

    def get_absolute_url(self):
        return reverse('music:details',kwargs={'pk':self.pk})


class Song(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=10)
    song_title=models.CharField(max_length=250)
    is_favorite=models.BooleanField(default=False)


