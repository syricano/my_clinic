from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class HomePage(models.Model):
    """
    Model class for storing information about the home page.

    Inherits from Django's models.Model class.
    """

    # Define fields for the model
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Method to represent the object as a string
    def __str__(self):
        return self.title