from django.contrib import admin
from .models import Appointment, Reminder, Doctor, Therapy

# Register your models here.

admin.site.register(Appointment)
admin.site.register(Reminder)
admin.site.register(Doctor)
admin.site.register(Therapy)