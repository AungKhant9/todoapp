from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
        path('authenticate/user', views.user, name='user'),
        path('authenticate/SignUp', views.SignUp, name='SignUp'),
        path('authenticate/Login', views.Login, name='Login'),
    ]