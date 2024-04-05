from django.shortcuts import render
from django.views import generic
from .models import HomePage 

# Create your views here.

class HomePageView(generic.ListView):
    model = HomePage
    template_name = "main/index.html"