from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from Trips.models import Trips
from Shipments.models import Shipments
from rest_framework import status
from rest_framework.response import Response

@receiver(post_save, sender=Trips)
def calculate_totalWeight(sender, instance,created, **kwargs):
    if created:
      instance.TotalWeightTrip=  instance.FreeWeight + instance.ComsumedWeight  
