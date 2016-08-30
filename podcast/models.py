import datetime

from django.db import models
from django.utils import timezone


class Podcast(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    language = models.CharField(max_length=10)
    copyright = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    webmaster = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)  # TODO: switch to using ImageField and handle upload stuff
    owner = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.title


class Keyword(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Episode(models.Model):
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    keywords = models.ManyToManyField(Keyword)
    image_url = models.CharField(max_length=255) # TODO: switch to using ImageField and handle upload stuff
    description = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Video(models.Model):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    duration = models.IntegerField()  # seconds
    filename = models.CharField(max_length=255)
    mime = models.CharField(max_length=40)  # derived from the file

    def __str__(self):
        return self.filename


class Audio(models.Model):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    duration = models.IntegerField()  # seconds
    filename = models.CharField(max_length=255)
    mime = models.CharField(max_length=40)  # derived from the file

    def __str__(self):
        return self.filename
