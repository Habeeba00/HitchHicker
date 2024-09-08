from django.db import models
from CustomUser.models import CustomUser
from Locations.models import locationModel


class Trips(models.Model):
    From= models.ForeignKey(locationModel, on_delete=models.CASCADE, related_name="trips_from_location") 
    To= models.ForeignKey(locationModel, on_delete=models.CASCADE, related_name="trips_to_location")
    depart_Date=models.DateField()
    depart_Time=models.TimeField()
    FreeWeight=models.FloatField()
    ComsumedWeight=models.FloatField(default='0.00')
    TotalWeightTrip=models.FloatField(default='0.00')
    username=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
