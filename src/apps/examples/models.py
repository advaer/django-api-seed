from django.db import models

from src.apps.core.models import BaseModel

from .managers import ArtistManager, AlbumManager


class Artist(BaseModel):
    artist_name = models.CharField(max_length=128)
    country_code = models.CharField(max_length=2)

    objects = ArtistManager()

    def __str__(self):
        return f"{self.pk} - {self.artist_name}"


class Album(BaseModel):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_title = models.CharField(max_length=128)
    year = models.PositiveSmallIntegerField()

    objects = AlbumManager()

    def __str__(self):
        return f"{self.pk} - {self.album_title}"
