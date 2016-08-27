from django.contrib import admin

from .models import Episode, Podcast, ItunesMetaData

# Register your models here.
admin.site.register(Episode)
admin.site.register(Podcast)
admin.site.register(ItunesMetaData)