from django.urls import path
from . import views

urlpatterns  = [
    path('', views.home, name='home-page'),
    path('login', views.login, name='login-page'),
    path('signup', views.signup, name='signup-page'),
    path('signout', views.log_out, name='signout-page'),
    path('dashboard', views.dash_board, name='dash_board',)
    
        ]
