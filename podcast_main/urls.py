from django.urls import path
from .views import *
from . import views


urlpatterns = [

    path('', views.home, name='home'),
    path('about/', views.about, name='about'), 
    path('episodes/', views.episodes, name='episodes'),
    path('trailer/', views.trailer, name='trailer'),
    path('e1/', views.e1, name='e1'),
    path('e2/', views.e2, name='e2'),
    path('e3/', views.e3, name='e3'),
    path('e4/', views.e4, name='e4'),
    path('map/', views.map, name='map'), 
    path('photos/', views.photos, name='photos'), 
    path('documents/', views.documents, name='documents'), 
    path('contact/', views.contact, name='contact'), 
    path('hosts/', views.hosts, name='hosts'), 
    path('episode/<int:pk>/', views.EpisodeDetailView.as_view(), name='episode-detail'), 
    path('new/', views.EpisodeCreateView.as_view(), name='episode-create'),
    path('update/<int:pk>/', views.EpisodeUpdateView.as_view(), name='episode-update'), 
    path('host/update/<int:pk>/', views.HostUpdateView.as_view(), name='host-update'),
    path('photo/new/', views.PhotoCreateView.as_view(), name='photo-create'),
    path('photo/update/<int:pk>/', views.PhotoUpdateView.as_view(), name='photo-update'), 

]