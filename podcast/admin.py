from django.contrib import admin

from .models import Episode, Podcast, ItunesMetaData, Video, Audio

# Register your models here.
admin.site.register(Episode)
admin.site.register(Podcast)
admin.site.register(ItunesMetaData)
admin.site.register(Video)
admin.site.register(Audio)