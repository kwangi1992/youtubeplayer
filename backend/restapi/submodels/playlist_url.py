from django.db import models
from django.contrib import admin

class Playlisturl(models.Model):
    playlist = models.ManyToManyField('playlist', blank=True, null=True)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    url = models.CharField(max_lengh=255)




