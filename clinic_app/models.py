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
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)
    email = models.EmailField(max_length=100)
    specialization = models.CharField(max_length=100)
    profile_information = models.TextField()

class Administrator(models.Model):
    pass

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name ="appointments")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="appointments")
    admin = models.ForeignKey(Administrator, on_delete=models.CASCADE, related_name="appointments")
    date = models.DateField()
    time = models.TimeField()
    status = models.IntegerField(choices=STATUS, default=0)

class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reminders")
    message = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)



class Therapy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="therapies")
