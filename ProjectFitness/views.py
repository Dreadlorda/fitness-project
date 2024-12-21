from django.shortcuts import render
from django.urls import path
def home(request):
    return render(request, 'home.html')
def index(request):
    return render(request, 'index.html')  # Ensure you have an 'index.html' template

