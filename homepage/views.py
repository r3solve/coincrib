from django.shortcuts import render
from django.http import HttpResponseRedirect as redirect
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
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        password = request.POST["passwd"]
        check_box = request.POST["check"]
        print(fname, lname, email, password, check_box)

        if User.objects.filter(email=email).exists():
            messages.info(request,"Email Address Already Exists")
            return redirect('signup-page')
        elif check_box != 'on':
            messages.info(request, "You need to accept the terms and conditions")
        else:
            user = User.objects.create_user(username=fname+lname, password=password, email=email, first_name=fname, last_name=lname)
            user.save()
            messages.info(request, 'User Created')
            return redirect('login-page')
    return render(request, 'registration/signup.html')

def logout(request):
    pass


