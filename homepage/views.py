from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
from django.contrib import auth 
# from django.http import redirect
from django.urls import reverse
from django.contrib import messages



# Create your views here.
def home(request):
    return render(request, 'homepage/html/index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        person = auth.authenticate(username=username, password=password)
        if person is not None:
            auth.login(request, person)
            return HttpResponse('You logged in ')
        else:
            print(person)
            messages.info(request, 'Invalid Username or Password')
            return redirect('login-page')
        
    return render(request, 'registration/login.html')

def signup(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        password = request.POST["passwd"]
        check_box = request.POST["check"]

        if User.objects.filter(email=email).exists():
            messages.info(request,"Email Address Already Exists")
            return redirect(reverse('signup-page'))
        elif check_box != 'on':
            messages.info(request, "You need to accept the terms and conditions")
            
        else:
            user = User.objects.create_user(username=email, password=password, email=email, first_name=fname, last_name=lname)
            user.save()
            messages.info(request, 'User Created')
            return redirect('login-page')
    return render(request, 'registration/signup.html')

def logout(request):
    logout(request)
    return redirect('home-page')


