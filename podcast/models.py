import datetime

from django.db import models
from django.utils import timezone
from django.utils import formats
from django.conf import settings


class Podcast(models.Model):

    EXPLICIT = (
        ('yes', 'yes'),
        ('no', 'no'),
        ('clean', 'clean'))

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
    explicit = models.CharField(max_length=5, choices=EXPLICIT)

    def __str__(self):
        return self.title

    @property
    def formatted_pub_date(self):
        return formats.date_format(self.pub_date, "D, d M Y H:i:s O")

    @property
    def full_image_url(self):
        return settings.PODCAST_APP['base_url'] + "/static/media/{}".format(self.image_url)

    @property
    def full_link_url(self):
        return settings.PODCAST_APP['base_url'] + "/" + self.link


class Keyword(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Episode(models.Model):
    EXPLICIT = (
        ('yes', 'yes'),
        ('no', 'no'),
        ('clean', 'clean'))

    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    keywords = models.ManyToManyField(Keyword)
    image_url = models.CharField(max_length=255)  # TODO: switch to using ImageField and handle upload stuff
    description = models.CharField(max_length=255)
    explicit = models.CharField(max_length=5, choices=EXPLICIT)
    pub_date = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    @property
    def get_pub_date(self):
        return formats.date_format(self.pub_date, "D, d M Y H:i:s O")

    @property
    def full_image_url(self):
        return settings.PODCAST_APP['base_url'] + "/static/media/{}".format(self.image_url)


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

    @property
    def full_media_url(self):
        return settings.PODCAST_APP['base_url'] + "/static/media/{}".format(self.filename)

    @property
    def convert_mime_to_string(self):
        for mime in self.MIME_TYPES:
            if mime[0] == self.mime:
                return mime[1]

    @staticmethod
    def convert_format_query(format_type):

        if type(format_type) is not str:
            return None

        for format_type_row in Media.FORMAT_TYPES:
            if format_type_row[1].lower() == format_type.lower():
                return format_type_row[0]

        return None

