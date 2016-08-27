from django.contrib import admin

from .models import Episode, Podcast, ItunesMetaData, Video, Audio, Keyword

# Register your models here.
admin.site.register(Podcast)
admin.site.register(ItunesMetaData)
admin.site.register(Keyword)
admin.site.register(Episode)
admin.site.register(Video)
admin.site.register(Audio)
