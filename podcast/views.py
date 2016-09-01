from django.shortcuts import get_object_or_404, render
from django.utils import formats
from django.http import HttpResponseBadRequest
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

    format_type = request.GET.get('format', Media.AUDIO)

    if type(format_type) is str:
        format_type = Media.convert_format_query(format_type)

    if format_type is None:
        return HttpResponseBadRequest()

    podcast = get_object_or_404(Podcast, pk=podcast_id)
    items = Media.objects.filter(format=format_type).select_related('episode').filter(episode__podcast=podcast_id)
    last_build_date = formats.date_format(datetime.datetime.now(), "D, d M Y H:i:s O")

    return render(request, 'feed.xml', {
        'podcast': podcast,
        'items': items,
        'last_build_date': last_build_date
    }, content_type='application/xhtml+xml')
