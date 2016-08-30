from django.contrib import admin

from .models import Episode, Podcast, ItunesMetaData, Video, Audio, Keyword

# Register your models here.
# admin.site.register(PodcastInline)
# admin.site.register(ItunesMetaData)
# admin.site.register(Keyword)
# admin.site.register(Episode)
# admin.site.register(Video)
# admin.site.register(Audio)
#


class PodcastInline(admin.TabularInline):
    model = Podcast
    fk_name = 'podcast'


class ItunesMetaDataAdmin(admin.ModelAdmin):
    inlines = [
        PodcastInline,
    ]


admin.site.register(PodcastInline)
