from django.shortcuts import render
import time
from django.http import HttpResponseRedirect
from django.contrib import auth 
# from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



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
            return render(request, 'homepage/html/user_model.html')
        else:
            messages.error(request, 'Invalid Username or Password')
            return HttpResponseRedirect('login')
        
    return render(request, 'registration/login.html')

def signup(request):
    if request.method == "POST" :
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        password = request.POST["passwd"]

        if User.objects.filter(email=email).exists():
            messages.error(request,"Email Address Already Exists")
            return HttpResponseRedirect('signup')
        elif "check" not in request.POST:
            messages.error(request, "You need to accept terms and conditions")
            return render(request, 'registration/signup.html')
            
        else:
            user = User.objects.create_user(username=email, password=password, email=email, first_name=fname, last_name=lname)
            user.save()
            messages.info(request, 'User Created')
            return HttpResponseRedirect('login')
    return render(request, 'registration/signup.html')

def log_out(request):
    auth.logout(request)
    return HttpResponseRedirect('')

def dash_board(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('dashboard')
    else:
        return HttpResponseRedirect('login')

