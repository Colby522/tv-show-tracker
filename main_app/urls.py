from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('tvShows/', views.tv_shows, name='tvshow-index'),
    path('tvShows/<int:tvshow_id>/', views.tvshow_detail, name='tvshow-detail'),
    path('tvShows/create/', views.TvShowCreate.as_view(), name='tvshow-create'),
    path('tvShows/<int:pk>/update/', views.TvShowUpdate.as_view(), name='tvshow-update'),
    path('tvShows/<int:pk>/delete/', views.TvShowDelete.as_view(), name='tvshow-delete'),
    path('accounts/sighup/', views.signup, name='signup')
]