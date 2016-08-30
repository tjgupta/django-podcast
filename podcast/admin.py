from django.contrib import admin

from .models import Episode, Podcast, Keyword, Media

admin.site.register(Podcast)
admin.site.register(Keyword)
admin.site.register(Episode)
admin.site.register(Media)

