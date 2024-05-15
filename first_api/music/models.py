from django.db import models

<<<<<<< Updated upstream

=======
# Create your models here.

# music/models.py
>>>>>>> Stashed changes
class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
<<<<<<< Updated upstream


=======
    
# music/models.py
>>>>>>> Stashed changes
class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_year = models.IntegerField()

    def __str__(self):
        return self.title

<<<<<<< Updated upstream

=======
# music/models.py
>>>>>>> Stashed changes
class Song(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)  # Artist or band name
    album = models.ForeignKey(Album, on_delete=models.CASCADE)  # Album the song belongs to
<<<<<<< Updated upstream
    duration = models.IntegerField()  # Duration of the song in seconds

    def __str__(self):
        return f'{self.title} - {self.artist} - {self.album}'
=======
    duration = models.IntegerField()  # Duration of the song in seconds
>>>>>>> Stashed changes
