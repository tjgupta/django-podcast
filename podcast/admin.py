from django.contrib import admin

from .models import Episode, Podcast, Video, Audio, Keyword

admin.site.register(Podcast)
admin.site.register(Keyword)
admin.site.register(Episode)
admin.site.register(Video)
admin.site.register(Audio)
