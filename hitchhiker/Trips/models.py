from django.db import models
from CustomUser.models import CustomUser
from Locations.models import locationModel
from Shipments.models import Shipments


class Trips(models.Model):
    From= models.ForeignKey(locationModel, on_delete=models.CASCADE, related_name="trips_from_location") 
    To= models.ForeignKey(locationModel, on_delete=models.CASCADE, related_name="trips_to_location")
    depart_Date=models.DateField()
    depart_Time=models.TimeField()
    FreeWeight=models.FloatField()
    ComsumedWeight=models.FloatField()
    Total_Shipment_Weight=models.ForeignKey(Shipments,on_delete=models.CASCADE,null=True,blank=True)
    added_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
