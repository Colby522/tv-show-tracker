from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tvShows/', views.tv_shows, name='tvshow-index'),
    path('tvShows/<int:tvshow_id>/', views.tvshow_detail, name='tvshow-detail'),
    path('tvShows/create/', views.TvShowCreate.as_view(), name='tvshow-create'),
    path('tvShows/<int:pk>/update/', views.TvShowUpdate.as_view(), name='tvshow-update'),
    path('tvShows/<int:pk>/delete/', views.TvShowDelete.as_view(), name='tvshow-delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', views.Login.as_view(), name='login'),
    path('tvShows/recommendations/', views.recommended_list, name='recommendations')
]