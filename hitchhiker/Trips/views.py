from Trips.models import Trips
from Trips.serializers import TripSerializers
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from CustomUser.models import CustomUser

class TripsViewset(viewsets.ModelViewSet):
    queryset = Trips.objects.all()
    serializer_class = TripSerializers


