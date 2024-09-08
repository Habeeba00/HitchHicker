from django.db import models
from CustomUser.models import CustomUser
from Trips.models import Trips
from Locations.models import locationModel


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
    trips=models.ForeignKey(Trips,on_delete=models.CASCADE,null=True,blank=True)
    class Meta:
        ordering = ['Date_Befor']


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        shipment = serializer.save()

        trip_id = request.data.get('trip_id')  
        try:
            shipment.add_to_trip(trip_id)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

   
