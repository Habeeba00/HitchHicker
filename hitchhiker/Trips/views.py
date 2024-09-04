from django.shortcuts import render
from Trips.models import tripsModel
from Trips.serializers import tripSerializers
from rest_framework import viewsets

class tripViewset(viewsets.ModelViewSet):
    queryset = tripsModel.objects.all()
    serializer_class = tripSerializers