from django.shortcuts import HttpResponse
from .models import FlightDescription, Passenger, Reservation
from .serializers import FlightDescriptionSerializer, PassengerSerializer, ReservationSerializer
from rest_framework import generics



# Create your views here.

def home(request):
    return HttpResponse('<h1>API Page</h1>')

class FlightDescriptionList(generics.ListCreateAPIView):
    serializer_class = FlightDescriptionSerializer
    queryset = FlightDescription.objects.all()

class FlightDescriptionOperations(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FlightDescriptionSerializer
    queryset = FlightDescription.objects.all()

## Passenger
class PassengerList(generics.ListCreateAPIView):
    serializer_class = PassengerSerializer
    queryset = Passenger.objects.all()

class PassengerOperations(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PassengerSerializer
    queryset = Passenger.objects.all()
    
## Reservation
class ReservationList(generics.ListCreateAPIView):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()

class PassengerOperations(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()