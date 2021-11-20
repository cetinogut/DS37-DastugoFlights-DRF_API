from rest_framework import serializers
from .models import FlightDescription, Passenger, Reservation

class FlightDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightDescription
        # fields = ["id", "first_name", "last_name", "number"]
        fields = '__all__'

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'
        
class ReservationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reservation
        fields = '__all__'