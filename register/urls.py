from . import views
from django.urls import path

# URL patterns list for the 'register' app
urlpatterns = [
    # Define a URL pattern for the RegisterUser view
    path('', views.RegisterUser.as_view(), name='register'),    
]