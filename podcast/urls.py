from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<episode_id>\d+)/$', views.episode_detail),
    url(r'^$', views.episode_list)
]
