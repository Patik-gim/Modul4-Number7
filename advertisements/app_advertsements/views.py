from django.shortcuts import render
from django.http import HttpResponse
from requests import request

# Create your views here.
def index(request):
    return render(request, 'index.html')

def top_sellers(request):
    return render(request, 'top-sellers.html')