from django.shortcuts import render

# Create your views here.
def all_dj(request):
    return render(request, 'DJapp/all_dj')