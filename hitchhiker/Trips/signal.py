from django.db.models.signals import post_save
from django.dispatch import receiver
from Trips.models import Trips


# @receiver(post_save, sender=Trips)
# def calculate_totalWeight(sender, instance,created, **kwargs):
#     if created:
#       instance.TotalWeightTrip= instance.FreeWeight + instance.ComsumedWeight  

@receiver(post_save, sender=Trips)
def calculate_totalWeight(sender, instance, created, **kwargs):
    if created:
        # Ensure both values are floats before adding them
        free_weight = float(instance.FreeWeight)
        consumed_weight = float(instance.ComsumedWeight)
        instance.TotalWeightTrip = free_weight + consumed_weight
        instance.save() 
