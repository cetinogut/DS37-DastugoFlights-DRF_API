from django.urls import path
from .views import home, FlightDescriptionList, FlightDescriptionOperations, PassengerList, PassengerOperations, ReservationList, ReservationOperations

urlpatterns = [
    path('', home, name='home'),
    path('flight/', FlightDescriptionList.as_view()),
    path('flight/<int:pk>/', FlightDescriptionOperations.as_view(), name="flight-detail"),
    path('passanger/', PassengerList.as_view()),
    path('passanger/<int:pk>/', PassengerOperations.as_view(), name="passanger-detail"),
    path('reservation/', ReservationList.as_view()),
    path('reservation/<int:pk>/', ReservationOperations.as_view(), name="reservation-detail"),
]