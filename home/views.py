from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render (request, 'home/index.html')

def about(request):
    return render (request, 'home/about.html')

def service(request):
    return render (request, 'home/service.html')

def contactus(request):
    return render (request, 'home/contactus.html')