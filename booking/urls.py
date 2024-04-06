from . import views
from django.urls import path

# URL patterns list for the 'booking' app
urlpatterns = [    
    # Define a URL pattern for the makeAppointment view
    path('', views.makeAppointment.as_view(), name='appointments'),
]