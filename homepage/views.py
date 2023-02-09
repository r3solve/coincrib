from django.shortcuts import render
from django.http import HttpResponseRedirect 
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    return render(request, 'homepage/html/index.html')

def login(request):
    return render(request, 'registration/login.html')

def signup(request):
    if request.method == "POST":
        fname,lname, email,password,confirm_password
        fname = request.POST["fname"]
        lanme = request.POST["lname"]
        email = request.POST["email"]
        password = request.POST["passwd"]
        check_box = request.POST["check"]

        if User.objects.filter(email=email).exists():
            messages.info(request,"Email Address Already Exists")
            return redirect('signup-page')
        elif check_box not in request.POST:
            messages.info(request, "You need to acceptes the terms and conditions")
        else:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save()
            return redirect('login-page')
    return render(request, 'registration/signup.html')

def logout(request):
    pass


