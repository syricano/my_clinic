from django.shortcuts import render
from django.views import generic 
from .models import Appointment
# Create your views here.

class makeAppointment(generic.ListView):
    model = Appointment
    template_name = "booking/booking.html"
 