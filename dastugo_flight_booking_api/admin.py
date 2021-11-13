from django.contrib import admin
from .models import FlightDescription, Passenger, Reservation

# Register your models here.
admin.site.register(FlightDescription)
admin.site.register(Passenger)
admin.site.register(Reservation)
