from django.db import models
from django.contrib.auth.models import User

# Define contand for appointment status

STATUS = (
    (0, "Pending"),
    (1, "Booked"),
    (2, "Canceled"),
)
# Create your models here.

class Doctor(models.Model):
    """
    Model class for storing information about doctors.

    Inherits from Django's models.Model class.
    """

    # Define fields for the model
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)
    email = models.EmailField(max_length=100)
    specialization = models.CharField(max_length=100)
    profile_information = models.TextField()

    # Method to represent the object as a string
    def __str__(self):
        return f"Dr {self.firstName} { self.lastName}"

class Administrator(models.Model):
    """
    Model class for storing information about administrators.

    Inherits from Django's models.Model class.
    """
    # Define fields for the model
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

class Therapy(models.Model):
    """
    Model class for storing information about therapies.

    Inherits from Django's models.Model class.
    """
    # Define fields for the model
    name = models.CharField(max_length=100)
    description = models.TextField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="therapies")

    # Method to represent the object as a string
    def __str__(self):
        return self.name

class Appointment(models.Model):
    """
    Model class for storing information about appointments.

    Inherits from Django's models.Model class.
    """
    # Define fields for the model
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name ="appointments")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="appointments")
    admin = models.ForeignKey(Administrator, on_delete=models.SET_NULL, null=True, blank=True)
    therapies = models.ManyToManyField(Therapy, related_name="appointments", blank=True)  # ManyToManyField for therapies
    date = models.DateField()
    time = models.TimeField()
    status = models.IntegerField(choices=STATUS, default=0)
    
    # Method to represent the object as a string
    def __str__(self):
        return f"{self.user}'s Appointment"

class Reminder(models.Model):
    """
    Model class for storing reminders.

    Inherits from Django's models.Model class.
    """
    # Define fields for the model
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reminders")
    message = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

