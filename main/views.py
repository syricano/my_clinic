from django.shortcuts import render
from django.views import generic
from .models import HomePage 

# Create your views here.

class HomePageView(generic.ListView):
    """
    View class for displaying the home page.

    Inherits from Django's generic ListView class.
    """

    # Specify the model to be used for the view
    model = HomePage

    # Specify the template to render
    template_name = "main/base.html"