"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

# URL patterns list for routing URLs to views
urlpatterns = [
    # Admin site URLs
    path('admin/', admin.site.urls, name = "admin"),

    # Include URLs from the 'main' app
    path('', include("main.urls"), name = "main"),

    # Include URLs from the 'register' app
    path('register/', include("register.urls"), name = "register"),

    # Include URLs from the 'booking' app
    path('booking/', include("booking.urls"), name = "booking"),
    
    # Include URLs from the 'contact' app
    path('contact/', include("contact.urls"), name = "contact"),
    
    # Include URLs from the 'about' app
    path('about/', include("about.urls"), name = "about"),    
]
