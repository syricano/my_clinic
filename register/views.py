from django.views import generic
from .models import RegisterUser 

# Create your views here.

class RegisterUser(generic.ListView):
    # Specify the model to be used for the view
    model = RegisterUser
    # Specify the template to render
    template_name = "register.html"