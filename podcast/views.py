from django.shortcuts import get_object_or_404, render
from django.utils import formats
import datetime
from .models import Episode, Podcast, Media


def episode_list(request):
    latest_episodes_list = Episode.objects.order_by('-pub_date')
    context = {'episode_list': latest_episodes_list, }
    return render(request, 'episode_list.html', context)


def episode_detail(request, episode_id):
    episode = get_object_or_404(Episode, pk=episode_id)
    return render(request, 'episode_detail.html', {'episode': episode})


def podcast_feed(request, podcast_id):
    podcast = get_object_or_404(Podcast, pk=podcast_id)
    items = Media.objects.filter(episode=1, format=Media.AUDIO).select_related('episode').filter(episode__podcast=podcast_id)
    last_build_date = formats.date_format(datetime.datetime.now(), "D, d M Y H:i:s O")

    return render(request, 'feed.xml', {
        'podcast': podcast,
        'items': items,
        'last_build_date': last_build_date
    }, content_type='application/xhtml+xml')
