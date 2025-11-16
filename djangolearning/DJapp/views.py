from django.shortcuts import render
from .models import Varity
# Create your views here.
def all_dj(request):
    animes = Varity.objects.all()
    return render(request, 'DJapp/all_dj.html', {'animes': animes})



