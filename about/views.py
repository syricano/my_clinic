from django.shortcuts import render
from django.views import generic
from .models import AboutUs 

# Create your views here.

class AboutUs(generic.ListView):
    model = AboutUs
    template_name = "about/about.html"