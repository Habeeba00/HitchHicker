from django.db import models
from CustomUser.models import CustomUser
from locations.models import locationModel


class Trips(models.Model):
    From= models.ForeignKey(locationModel, on_delete=models.CASCADE, related_name="trips_from_location") 
    To= models.ForeignKey(locationModel, on_delete=models.CASCADE, related_name="trips_to_location")
    depart_Date=models.DateField()
    depart_Time=models.TimeField()
    FreeWeight=models.FloatField()
    ComsumedWeight=models.FloatField(default='0.00')
    TotalWeightTrip=models.FloatField(default='0.00')
    username=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    
    
    def save (self,*args,**kwargs):
        self.FreeWeight=float(self.FreeWeight)if self.FreeWeight is not None else 0.0
        self.ComsumedWeight=float(self.ComsumedWeight)if self.ComsumedWeight is not None else 0.0
        self.TotalWeightTrip = self.FreeWeight + self.ComsumedWeight
        super().save(*args, **kwargs)
