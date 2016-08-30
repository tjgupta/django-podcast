from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.episode_list, name="episode_list"),
    url(r'^podcast/(?P<podcast_id>\d+)/feed.xml$', views.podcast_feed, name="podcast_feed"),
    url(r'^episode/(?P<episode_id>\d+)/$', views.episode_detail, name="episode_detail"),
]
