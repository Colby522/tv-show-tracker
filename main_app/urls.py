from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('tvShows/', views.tv_shows, name='tvshow-index'),
    path('tvShows/<int:tvshow_id>/', views.tvshow_detail, name='tvshow-detail')
]