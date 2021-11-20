from django.db import models

#import signals
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class FlightDescription(models.Model):
    flightNumber = models.CharField(max_length=10)
    operatingAirlines = models.CharField(max_length=50)
    departureCity = models.CharField(max_length=30)
    arrivalCity = models.CharField(max_length=30)
    dateofDeparture = models.DateField()
    estimatedTimeofDeparture = models.TimeField()
    
    class Meta:
        ordering = ['flightNumber']
       
    # from django.db.models import F   #You can also use query expressions. To order by author ascending and make null values sort last, use this:
    #     ordering = [F('author').asc(nulls_last=True)]
    
    def __str__(self):
        return f"{self.operatingAirlines} {self.flightNumber} {self.departureCity[0:3].upper()}-{self.arrivalCity[0:3].upper()}"

class Passenger(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20, blank=True, null=True)
    phoneNumber = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['first_name']
    
    def __str__(self):
        return f"{self.last_name} {self.first_name}"

class Reservation(models.Model):
    flight = models.ForeignKey(FlightDescription,on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger,on_delete=models.CASCADE)
    created_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return f"{self.flight} {self.passenger} - {self.created_user}"
    