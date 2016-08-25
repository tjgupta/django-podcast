from django.shortcuts import render

def episode_list(request):
    return render(request, 'episode_list.html')

def episode_detail(request, episode_id):
    return render(request, 'episode_detail.html')
