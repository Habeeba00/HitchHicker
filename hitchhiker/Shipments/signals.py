from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Shipments

@receiver(pre_save, sender=Shipments)
def calculate_totals(sender, instance, **kwargs):
    instance.Total_Price = instance.Quantity * instance.Price
    instance.Total_Weight = instance.Quantity * instance.Weight