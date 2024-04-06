from django.shortcuts import render
from django.views import generic
from .models import AboutUs 

# Create your views here.

class AboutUs(generic.ListView):
    # Specify the model to be used for the view
    model = AboutUs
    # Specify the template to render
    template_name = "about.html"