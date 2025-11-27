from django.shortcuts import render
from .models import Varity
from django.shortcuts import get_object_or_404

# Create your views here.
def all_dj(request):
    animes = Varity.objects.all()
    return render(request, 'DJapp/all_dj.html', {'animes': animes})

def anime_detail(request, anime_id):
    anime = get_object_or_404(Varity, pk= anime_id)
    return render(request, 'DJapp/anime_detail.html', {'anime': anime})

def stores_view(request):
    return render(request, 'DJapp/stores_temp.html')
