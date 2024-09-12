from django.db import models
from CustomUser.models import CustomUser
from Trips.models import Trips
from locations.models import locationModel


class Shipments(models.Model):
    From= models.ForeignKey(locationModel, on_delete=models.CASCADE, related_name="Ship_from_location")  
    To= models.ForeignKey(locationModel, on_delete=models.CASCADE, related_name="Ship_to_location") 
    Date_Befor=models.DateField()
    Shipment_Name=models.CharField(max_length=20)
    Quantity=models.IntegerField()
    Weight=models.FloatField()
    Price=models.FloatField()
    Reward=models.FloatField(null=True,blank=True)
    Total_Weight=models.FloatField(null=True,blank=True)
    image=models.ImageField(upload_to='images/')
    added_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    trips=models.ForeignKey(Trips,on_delete=models.CASCADE,null=True,blank=True,related_name='ship')
    class Meta:
        ordering = ['Date_Befor']
    
    
    
    def save(self, *args, **kwargs):
        self.Reward = self.Price * self.Quantity
        self.Total_Weight = self.Weight * self.Quantity
        super(Shipments, self).save(*args, **kwargs)
        
    
