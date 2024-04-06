from . import views
from django.urls import path

# URL patterns list for the 'contact' app
urlpatterns = [
    # Define a URL pattern for the ContactUs view
    path('', views.ContactUs.as_view(), name='contact'),    
]