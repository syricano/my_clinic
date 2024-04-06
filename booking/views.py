from django.shortcuts import render
from django.views import generic 
from .models import Appointment
# Create your views here.

class makeAppointment(generic.ListView):
    """
    View class for displaying a list of appointments.

    Inherits from Django's generic ListView class.
    """
    # Specify the model to be used for the view
    model = Appointment

    # Specify the template to render
    template_name = "booking.html"
 