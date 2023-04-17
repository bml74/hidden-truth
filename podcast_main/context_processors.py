from .models import Podcast, Episode
from django.shortcuts import get_object_or_404


def getEpisodes(request):
    podcast = get_object_or_404(Podcast, title="Hidden Truth")
    episodes = Episode.objects.filter(podcast_fk=podcast).all()
    return {
        'episodes': episodes
    }