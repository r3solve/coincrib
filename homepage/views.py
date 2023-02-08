from django.shortcuts import render
from django.http import HttpResponseRedirect 
from django.urls import reverse
import requests, json


# Create your views here.
def home(request):
    return render(request, 'homepage/html/index.html')

def login(request):
    return render(request, 'registration/login.html')

def signup(request):
    return render(request, 'registration/signup.html')

def logout(request):
    pass


