from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"hello/index.html")

def adnan(request):
    return HttpResponse("Hello, Adnan")

def greet(request, name):
    return HttpResponse(f"Hello, {name}")