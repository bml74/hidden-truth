from django.db import models


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
