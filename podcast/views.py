from django.shortcuts import render
from .models import Episode


def episode_list(request):
    latest_episodes_list = Episode.objects.order_by('-pub_date')
    context = {'episode_list': latest_episodes_list, }
    return render(request, 'episode_list.html', context)


def episode_detail(request, episode_id):
    return render(request, 'episode_detail.html')
