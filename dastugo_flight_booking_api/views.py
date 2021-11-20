from django.shortcuts import HttpResponse
from rest_framework.decorators import api_view
from .models import FlightDescription, Passenger, Reservation
from .serializers import FlightDescriptionSerializer, PassengerSerializer, ReservationSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadOnly, IsAddedByUserOrReadOnly, IsAddedByUser
from rest_framework import serializers

# Create your views here.

def home(request):
    return HttpResponse('<h1>API Page</h1>')

@api_view(['POST'])
def find_flights(request):
    flights = FlightDescription.objects.filter(departure_city=request.data['departure_city'], arrival_city=request.data['arrival_city'], date_of_departure=request.data['date_of_departure'])
    serializer = FlightDescriptionSerializer(flights, many=True)

@api_view(['POST'])
def save_reservation(request):
    flight = FlightDescription.objects.get(id=request.data['flight_number'])

    passenger = Passenger()
    passenger.firstname = request.data['firstname']
    passenger.lastname = request.data['lastname']
    passenger.middlename = request.data['middlename']
    passenger.email = request.data['email']
    passenger.phone = request.data['phone']

    reservation = Reservation()
    reservation.flight = flight
    reservation.passenger = passenger

    Reservation.save(reservation)

    return Response(status=status.HTTP_201_CREATED)

    return Response(serializer.data)

class FlightDescriptionList(generics.ListCreateAPIView):
    queryset = FlightDescription.objects.all()
    serializer_class = FlightDescriptionSerializer
    permission_classes = [IsAdminOrReadOnly] ##only admins can add new flights, this is a read-only mode for others
    
class FlightDescriptionOperations(generics.RetrieveUpdateDestroyAPIView):
    queryset = FlightDescription.objects.all()
    serializer_class = FlightDescriptionSerializer
    permission_classes = [IsAdminOrReadOnly]
    
## Passenger
class PassengerList(generics.ListCreateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

class PassengerOperations(generics.RetrieveUpdateDestroyAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
   
## Reservation
class ReservationList(generics.ListCreateAPIView):
    #user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault()).pk_field
    #queryset = Reservation.objects.filter(created_user=user)
    #queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    #permission_classes = [IsAuthenticated] 
    permission_classes = [IsAddedByUserOrReadOnly] 
    #permission_classes = [IsAddedByUser] 
    
    def perform_create(self, serializer):
        serializer.save(created_user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(created_user=self.request.user)
    
    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        if user.is_staff:
            return Reservation.objects.all()
        else:
            return Reservation.objects.filter(created_user=user)
    
    # def get(self, request, format=None):
    #     print(request)
    #     content = {
    #         'status': ' reservations list request was permitted',
    #     }
    #     return Response(content)

class ReservationOperations(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAddedByUser] # only if the user has added the reservation can see and update the reservation record
    
    def perform_update(self, serializer):
        serializer.save(created_user=self.request.user)
    
    def get_queryset(self):
        
        user = self.request.user
        if user.is_staff:
            return Reservation.objects.all()
        else:
            return Reservation.objects.filter(created_user=user)