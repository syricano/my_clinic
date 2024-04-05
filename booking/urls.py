from . import views
from django.urls import path

urlpatterns = [    
    path('', views.makeAppointment.as_view(), name='appointments'),
]