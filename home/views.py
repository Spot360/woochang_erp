from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render (request, 'home/index.html')

def about(request):
    return render (request, 'home/about.html')

def service_3PL(request):
    return render (request, 'home/service_3PL.html')

def service_IT(request):
    return render (request, 'home/service_IT.html')   

def contactus(request):
    return render (request, 'home/contactus.html')