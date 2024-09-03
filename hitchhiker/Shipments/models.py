from django.db import models
from CustomUser.models import CustomUser
# from Trips.models import Trips


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
    image=models.ImageField(null=True,blank=True)
    added_by=models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True,blank=True,default=1)
    # Trips=models.ForeignKey(Trips,on_delete=models.CASCADE,null=True,blank=True)
