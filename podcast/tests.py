from django.test import TestCase

import factory

import datetime

from .models import Podcast, Episode, Media


class PodcastFactory(factory.Factory):
    class Meta:
        model = Podcast

    pub_date = datetime.datetime.strptime('2016-08-30 17:58:54', "%Y-%m-%d %H:%M:%S")
    title = "Being the Doctor Who Podcast"
    description = "Podcast discussing the latest Doctor Who news and rumors"
    link = "podcasts/doctorwho"
    language = "en-us"
    copyright = "Davinder Mahal"
    webmaster = "webmaster@example.com"
    author = "Davinder Mahal"
    subtitle = "Doctor Who news and rumors"
    summary = "Podcast discussing the latest Doctor Who news and rumors"
    category = "TV & Film"
    image_url = "doctorwho.jpg"
    owner = "Davinder Mahal"
    email = "webmaster@example.com"
    explicit = "no"


class EpisodeFactory(factory.Factory):
    class Meta:
        model = Episode

    podcast = PodcastFactory.build()
    title = "Episode 1: Galiffrey"
    author = "Davinder"
    subtitle = "Doctor Who news and rumors"
    summary = "First episode in this podcast"
    image_url = "doctorwho.jpg"
    description = "First episode in this new podcast discussing the latest Doctor Who news anad rumors"
    explicit = "no"
    pub_date = datetime.datetime.strptime("2016-08-30 18:17:04", "%Y-%m-%d %H:%M:%S")
    date_created = datetime.datetime.strptime("2016-08-30 18:20:56", "%Y-%m-%d %H:%M:%S")
    last_modified = datetime.datetime.strptime("2016-08-31 18:02:22", "%Y-%m-%d %H:%M:%S")


class MediaFactory(factory.Factory):
    class Meta:
        model = Media

    duration = 344
    filename = "episode1.mp3"
    mime = 1


class PodcastTests(TestCase):

    def test_formatted_pub_date(self):
        """
        :return: a formatted date string
        """
        pod = PodcastFactory.build()
        self.assertEqual(pod.formatted_pub_date, 'Tue, 30 Aug 2016 17:58:54 +0000')

    # todo Do we need this test? If so, what's the best way to test?
    def test_full_image_url(self):
        """
        :return: string url
        """
        pod = PodcastFactory.build()
        self.assertEqual(pod.full_image_url, 'http://127.0.0.1:8000/static/media/doctorwho.jpg')


class EpisodeTests(TestCase):

    def test_formatted_pub_date(self):
        """
        :return: a formatted date string
        """
        episode = EpisodeFactory.build()
        self.assertEqual(episode.formatted_pub_date, 'Tue, 30 Aug 2016 18:17:04 +0000')


class MediaTests(TestCase):

    def test_convert_format_str_to_int(self):
        """

        :return: None or int
        """
        media = MediaFactory.build()
        self.assertEqual(media.convert_format_str_to_int('audio'), 1)
        self.assertEqual(media.convert_format_str_to_int('AUDIO'), 1)
        self.assertEqual(media.convert_format_str_to_int('video'), 2)
        self.assertEqual(media.convert_format_str_to_int('vIdEo'), 2)

        self.assertIsNone(media.convert_format_str_to_int('random_format_string'), None)
        self.assertIsNone(media.convert_format_str_to_int(1), None)



