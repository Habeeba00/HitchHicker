from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import Shipments 
from Trips.models import Trips
from django.db import transaction

from django.core.exceptions import ValidationError


@receiver(post_save, sender=Shipments)
def calculate_totals(sender, instance, **kwargs):
    instance.Total_Price = instance.Quantity * instance.Price
    instance.Total_Weight = instance.Quantity * instance.Weight
    
