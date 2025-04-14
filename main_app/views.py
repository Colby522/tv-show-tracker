from django.shortcuts import render
from django.http import HttpResponse
from .models import Tv_Show

def home(request):
    return HttpResponse('<h1>Hello</h1>')

def about(request):
    return render(request, 'about.html')

def tv_shows(request):
    tvshows = Tv_Show.objects.all()
    return render(request, 'tvShows/index.html', {'tvshows': tvshows})

def tvshow_detail(request, tvshow_id):
    tvshow = Tv_Show.objects.get(id=tvshow_id)
    return render(request, 'tvShows/detail.html', {'tvshow': tvshow})
