from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Administrator(models.Model):
    """
    Model class for storing information about administrators.

    Inherits from Django's models.Model class.
    """
    # Define fields for the model
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

class Message(models.Model):
    """
    Model class for storing contact information.

    Inherits from Django's models.Model class.
    """
    
    # Define fields for the model
    name = models.CharField(max_length=40)
    phone = models.CharField(null=True, default=0)
    email = models.EmailField(max_length=50)
    subject = models.TextField()
    # Method to represent the object as a string
    def __str__(self):
        return self.name



class UserMessage(models.Model):
    """
    Model class for storing messages sent by users to admin.

    Inherits from Django's models.Model class.
    """
    # Define fields for the model
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    recipient = models.ForeignKey(Administrator, on_delete=models.CASCADE, related_name="received_messages")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)