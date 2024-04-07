from . import views
from django.urls import path


app_name = 'about'
# URL patterns list for the 'about' app
urlpatterns = [
    # Define a URL pattern for the AboutUs view
    path('', views.AboutUs.as_view(), name='about'),    
]