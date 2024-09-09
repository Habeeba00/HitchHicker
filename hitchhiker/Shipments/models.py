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
    Total_Price=models.FloatField(null=True,blank=True)
    Total_Weight=models.FloatField(null=True,blank=True)
    image=models.ImageField(upload_to='images/')
    added_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    # trips=models.ForeignKey(Trips,on_delete=models.CASCADE,null=True,blank=True)
    class Meta:
        ordering = ['Date_Befor']

   
