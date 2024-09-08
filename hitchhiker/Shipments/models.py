from django.db import models
from CustomUser.models import CustomUser
from Trips.models import Trips
from location.models import locationModel
from rest_framework.response import Response
from rest_framework import status


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

    # def update(self, trip_id):
    #     try:
    #         trip = Trips.objects.get(id=trip_id)

    #         free_weight = trip.FreeWeight - trip.ComsumedWeight

    #         if self.Total_Weight > free_weight:
    #             raise ValueError(f"Not enough free weight on the trip. Available: {free_weight} kg")

    #         trip.ComsumedWeight += self.Total_Weight
    #         trip.TotalWeightTrip += self.Total_Weight

    #         self.trips = trip
    #         self.save()

    #         trip.save()

    #         return True

    #     except Trips.DoesNotExist:
    #         raise ValueError(f"Trip with id {trip_id} not found")

    #     except Exception as e:
    #         raise ValueError(f"An error occurred while updating the shipment: {str(e)}")