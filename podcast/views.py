from django.shortcuts import get_object_or_404, render
from django.utils import formats
import datetime
from .models import Episode, Podcast


def episode_list(request):
    latest_episodes_list = Episode.objects.order_by('-pub_date')
    context = {'episode_list': latest_episodes_list, }
    return render(request, 'episode_list.html', context)


def episode_detail(request, episode_id):
    episode = get_object_or_404(Episode, pk=episode_id)
    return render(request, 'episode_detail.html', {'episode': episode})


def podcast_feed(request, podcast_id):
    podcast = get_object_or_404(Podcast, pk=podcast_id)
    # episodes = Episode.objects.filter(podcast_id=podcast_id).select_related()
    # episodes = Episode.objects.with_media(podcast_id=podcast_id)
    episodes = podcast.episode_set.all().filter(media__format=1)
    print(episodes)

    last_build_date = formats.date_format(datetime.datetime.now(), "D, d M Y H:i:s O")

    return render(request, 'feed.xml', {
        'podcast': podcast,
        'episodes': episodes,
        'last_build_date': last_build_date
    })
