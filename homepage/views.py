from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import auth 
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Coins



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
            return render(request, 'registration/login.html')
        
    return render(request, 'registration/login.html')

def signup(request):
    if request.method == "POST" :
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        password = request.POST["passwd"]
        
        if User.objects.filter(email=email).exists():
            messages.error(request,"Email Address Already Exists")
            
        elif "check" not in request.POST:
            messages.error(request, "You need to accept terms and conditions")
            return render(request, 'registration/signup.html')
            
        else:
            user = User.objects.create_user(username=email, password=password, email=email, first_name=fname, last_name=lname)
            user.save()
            messages.info(request, 'User Created')
            return redirect('login')
    return render(request, 'registration/signup.html')


def log_out(request):
    if request.user.is_authenticated():
        auth.logout(request)
        return redirect(reverse('login-page'))
    return redirect('login')
@login_required(login_url='login-page')
def dash_board(request):
    context = {'post':Coins.objects.all()}
    if request.user.is_authenticated:
        return render(request, context)
    else:
        return redirect('login')

@login_required(login_url='login/')
def settings(request):
    return render('homepage/html/settings.html')
