from django.shortcuts import render
from django.views import generic
from .models import ContactUs 

# Create your views here.

class ContactUs(generic.ListView):
    model = ContactUs
    template_name = "contact/contact.html"