from django.shortcuts import render
from django.http import HttpRequest
from .models import Profile
from userRecommendation.models import Recommendation  

def home(request):
    profiles = Profile.objects.all()
    recommendations = Recommendation.objects.all()
    return render(request, 'appProfile/home.html', {'profiles' : profiles, 'recommendations':recommendations})

def all_artsits(request):
    artists = Profile.objects.filter(artistCheck = True)
    return render(request, 'appProfile/all_artists.html', {'artists': artists})

def all_recommendations(request):
    recomendations = Recommendation.objects.all()
    return render(request, 'appRecommendations/all_recommendations.html', {'recommendations': recomendations})