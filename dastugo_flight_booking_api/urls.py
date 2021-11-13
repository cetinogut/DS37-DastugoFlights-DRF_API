from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
    #path('student/', StudentList.as_view()),
    #path('student/<int:pk>/', StudentOperations.as_view(), name="detail"),
]