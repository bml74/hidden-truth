from django.contrib import admin
from .models import Podcast, Episode, Host, Photo


admin.site.register(Podcast)
admin.site.register(Episode)
admin.site.register(Host)
admin.site.register(Photo)