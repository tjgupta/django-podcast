from django.shortcuts import get_object_or_404, render
from .models import Episode


def episode_list(request):
    latest_episodes_list = Episode.objects.order_by('-pub_date')
    context = {'episode_list': latest_episodes_list, }
    return render(request, 'episode_list.html', context)


def episode_detail(request, episode_id):
    episode = get_object_or_404(Episode, pk=episode_id)
    return render(request, 'episode_detail.html', {'episode': episode})
