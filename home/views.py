from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render (request, 'home/index.html')

def about(request):
    return render (request, 'home/about.html')

def service_3pl(request):
    return render (request, 'home/service_3pl.html')

def service_it(request):
    return render (request, 'home/service_it.html')   

def contactus(request):
    return render (request, 'home/contactus.html')