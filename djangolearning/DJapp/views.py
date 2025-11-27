from django.shortcuts import render
from .models import Varity, Store
from django.shortcuts import get_object_or_404
from .forms import VarityForm

# Create your views here.
def all_dj(request):
    animes = Varity.objects.all()
    return render(request, 'DJapp/all_dj.html', {'animes': animes})

def anime_detail(request, anime_id):
    anime = get_object_or_404(Varity, pk= anime_id)
    return render(request, 'DJapp/anime_detail.html', {'anime': anime})

def stores_view(request):
    stores = None
    
    if request.method == 'POST': 
        form = VarityForm(request.POST)
        if form.is_valid():
            anime_varity = form.cleaned_data['anime_varity']
            stores = Store.objects.filter(anime_varieties=anime_varity)
    
    else:
        form = VarityForm()
    return render(request, 'DJapp/stores_temp.html', {'stores': stores, 'form': form})