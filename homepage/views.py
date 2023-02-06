from django.shortcuts import render
from django.http import HttpResponseRedirect 
from django.urls import reverse
import requests, json

data = json.loads(requests.get(f"https://api.coincap.io/v2/assets/bitcoin").content.decode())

# Create your views here.
def home(request):
    return render(request, 'homepage/index.html', { 'data' : data})

def login(request):
    pass
