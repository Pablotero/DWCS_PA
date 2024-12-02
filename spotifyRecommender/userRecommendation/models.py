from django.db import models


class Recommendation(models.Model):
    idRecommendation = models.CharField(max_length=12, blank=True)
    projectName = models.CharField(max_length=50)
    spotifyUrl = models.URLField()
    projectImage = models.ImageField(upload_to='spotifyRecommender/images/')
    artistName = models.CharField(max_length=30) 