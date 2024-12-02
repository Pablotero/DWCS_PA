from django.db import models

class Profile(models.Model):
    recommendationId = models.CharField(max_length=12, blank=True)
    profileName = models.CharField(max_length=30, help_text='Introduce your profileName')
    profilePhoto = models.ImageField(upload_to='appProfile/images/')
    urlSpotify = models.URLField(help_text='Introduce your spotify profile URL')
    artistCheck = models.BooleanField(default=False)
