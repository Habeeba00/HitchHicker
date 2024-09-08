from django.db import models
from CustomUser.models import CustomUser
from Trips.models import tripsModel
from rest_framework.response import Response
from rest_framework import status


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
    Trips=models.ForeignKey(tripsModel,on_delete=models.CASCADE,null=True,blank=True)
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

    def add_to_trip(self, trip_id):
        try:
            trip = tripsModel.objects.get(id=trip_id)

            if self.Total_Weight > trip.FreeWeight:
                raise ValueError(f"Not enough free weight on the trip. Available: {trip.FreeWeight} kg")

            self.Trips = trip

            trip.ComsumedWeight += self.Total_Weight
            trip.TotalWeightTrip += self.Total_Weight  

            self.save()
            trip.save()

            return True  

        except tripsModel.DoesNotExist:
            raise ValueError(f"Trip with id {trip_id} not found")