import datetime

from django.db import models
from django.utils import timezone
from django.utils import formats


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

    def get_pub_date(self):
        return formats.date_format(self.pub_date, "D, d M Y H:i:s O")


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

    def get_pub_date(self):
        return formats.date_format(self.pub_date, "D, d M Y H:i:s O")


class Media(models.Model):

    AUDIO = 1
    VIDEO = 2
    FORMAT_TYPES = (
        (AUDIO, 'Audio'),
        (VIDEO, 'Video'),
    )

    MIME_TYPES = (
        (AUDIO, 'audio/mpeg'),
        (VIDEO, 'video/mp4'),
    )
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    format = models.IntegerField(
        choices=FORMAT_TYPES,
        default=AUDIO
    )

    duration = models.IntegerField()  # seconds
    filename = models.CharField(max_length=255)
    mime = models.IntegerField(
        choices=MIME_TYPES,
        default=AUDIO
    )

    def __str__(self):
        return self.filename
