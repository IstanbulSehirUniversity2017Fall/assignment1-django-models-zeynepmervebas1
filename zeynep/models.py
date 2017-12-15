# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=25)
    album_title = models.CharField(max_length=25)
    genre = models.CharField(max_length=10)
    album_logo = models.CharField(max_length=1000)
    def __str__(self):
        return self.album_title + " - " + self.artist

class Song (models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=25)
# Create your models here.
