from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Podcast(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    

class Episode(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField(blank=True, null=True)
    podcast_fk = models.ForeignKey(Podcast, on_delete=models.CASCADE)
    listens = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('home')


class Host(models.Model):
    description = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='hidden-truth', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('home')
    

class Photo(models.Model):
    image = models.FileField(upload_to='hidden-truth/photos', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('photos')