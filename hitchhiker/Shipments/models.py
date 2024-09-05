from django.db import models
from CustomUser.models import CustomUser
# from Trips.models import tripsModel


class Shipments(models.Model):
    From=models.CharField(max_length=15)
    To=models.CharField(max_length=15)
    Date_Befor=models.DateField()
    Shipment_Name=models.CharField(max_length=20)
    Quantity=models.IntegerField()
    Weight=models.FloatField()
    Price=models.FloatField()
    Total_Price=models.FloatField(null=True,blank=True)
    Total_Weight=models.FloatField(null=True,blank=True)
    image=models.ImageField(upload_to='images/')
    added_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    # Trips=models.ForeignKey(tripsModel,on_delete=models.CASCADE,null=True,blank=True)
    class Meta:
        ordering = ['Date_Befor']

