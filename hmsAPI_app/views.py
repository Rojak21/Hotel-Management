# hotel_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

def index(request):
     return render(request, 'templates_user_api/index.html', {'title':'index'})
 
