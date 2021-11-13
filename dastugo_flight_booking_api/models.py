from django.db import models

#import signals
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# Create your models here.

class FlightDescription(models.Model):
    flightNumber = models.CharField(max_length=10)
    operatingAirlines = models.CharField(max_length=50)
    departureCity = models.CharField(max_length=30)
    arrivalCity = models.CharField(max_length=30)
    dateofDeparture = models.DateField()
    estimatedTimeofDeparture = models.TimeField()
    
    def __str__(self):
        return f"{self.operatingAirlines} {self.flightNumber}"

class Passenger(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.CharField(max_length=20, blank=True, null=True)
    phoneNumber = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.last_name} {self.first_name}"

class Reservation(models.Model):
    flight = models.ForeignKey(FlightDescription,on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.flight} {self.passenger}"
    
# @receiver(post_save,sender=settings.AUTH_USER_MODEL)
# def createAuthToken(sender,instance,created,**kwargs):
# 	if created:
# 		Token.objects.create(user=instance)