from . import views
from django.urls import path

# URL patterns list for the 'main' app
urlpatterns = [
    # Define a URL pattern for the HomePageView view
    path('', views.HomePageView.as_view(), name='home'),    
]