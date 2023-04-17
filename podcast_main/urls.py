from django.urls import path
from .views import *
from . import views


urlpatterns = [

    path('', views.home, name='home'), 
    path('episode/<int:pk>/', views.EpisodeDetailView.as_view(), name='episode-detail'), 
    path('new/', views.EpisodeCreateView.as_view(), name='episode-create'),
    path('update/<int:pk>/', views.EpisodeUpdateView.as_view(), name='episode-update'), 

]