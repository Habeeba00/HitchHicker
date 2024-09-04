from django.db import models
from CustomUser.models import CustomUser
from Locations.models import locationModel


class tripsModel(models.Model):
    From_Field = models.ForeignKey(locationModel, on_delete=models.CASCADE, related_name="trips_from_location") 
    To_Field = models.ForeignKey(locationModel, on_delete=models.CASCADE, related_name="trips_to_location")
    depart_Date=models.DateField()
    depart_Time=models.TimeField()
    FreeWeight=models.FloatField()
    ComsumedWeight=models.FloatField()
    TotolWeight=models.FloatField()
    username=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
   

