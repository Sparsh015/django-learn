from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World. Welcome to home page")

def about(request):
    return HttpResponse("Hello World. Welcome to about page")

def contact(request):
    return HttpResponse("Hello World. Welcome to contact page")

