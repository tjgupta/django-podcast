import datetime

from django.db import models
from django.utils import timezone


class Episode(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    duration = models.IntegerField()
    keywords = models.CharField(max_length=255)  # TODO: maybe store this as one to many in a separate table
    image_url = models.CharField(max_length=255) # TODO: switch to using ImageField and handle upload stuff
    description = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
