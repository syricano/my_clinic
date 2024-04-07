from . import views
from django.urls import path

app_name = 'booking'
# URL patterns list for the 'booking' app
urlpatterns = [    
    # Define a URL pattern for the makeAppointment view
    path('', views.makeAppointment.as_view(), name='appointments'),
]