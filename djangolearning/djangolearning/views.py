from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello World. Welcome to home page")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hello World. Welcome to about page")

def contact(request):
    return HttpResponse("Hello World. Welcome to contact page")

