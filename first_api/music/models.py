from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_year = models.IntegerField()

    def __str__(self):
        return self.title


class Song(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)  # Artist or band name
    album = models.ForeignKey(Album, on_delete=models.CASCADE)  # Album the song belongs to
    duration = models.IntegerField()  # Duration of the song in seconds