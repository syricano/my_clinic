from django.shortcuts import render
from django.views import generic
from .models import ContactUs 

# Create your views here.

class ContactUs(generic.ListView):
    # Specify the model to be used for the view
    model = ContactUs
    # Specify the template to render
    template_name = "contact.html"