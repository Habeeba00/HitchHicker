from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Shipments

@receiver(post_save, sender=Shipments)
@receiver(post_delete, sender=Shipments)
def update_shipment_totals(sender, instance, **kwargs):
    
    total_price = instance.Quantity * instance.Price* instance.Weight
    total_weight = instance.Quantity * instance.Weight
    
    instance.Total_Price = total_price
    instance.Total_Weight = total_weight
    instance.save(update_fields=['Total_Price', 'Total_Weight'])