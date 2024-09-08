from rest_framework import serializers
from .models import Shipments
from rest_framework.response import Response
from rest_framework import status

from Trips.models import Trips
from django.shortcuts import get_object_or_404

class ShipmentsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model=Shipments
        fields = ['id','From', 'To', 'Date_Befor', 'trips','Shipment_Name', 'Quantity', 'Price','Total_Price' ,'Weight','Total_Weight','image' ,'added_by']
    def update(self, instance, validated_data):
        # Update instance fields with validated data
        instance.From = validated_data.get('From', instance.From)
        instance.To = validated_data.get('To', instance.To)
        instance.Date_Befor = validated_data.get('Date_Befor', instance.Date_Befor)
        instance.Quantity = validated_data.get('Quantity', instance.Quantity)
        instance.Price = validated_data.get('Price', instance.Price)
        instance.Total_Price = instance.Price * instance.Quantity
        instance.Weight = validated_data.get('Weight', instance.Weight)
        instance.Total_Weight = instance.Quantity * instance.Weight
        instance.image = validated_data.get('image', instance.image)
        
        trip_obj = validated_data.get('trips', instance.trips)

        if trip_obj is not None:
            free_weight = trip_obj.FreeWeight - trip_obj.ComsumedWeight
            if instance.Total_Weight > free_weight:
                raise serializers.ValidationError(f"Not enough free weight on the trip. Available: {trip_obj.FreeWeight} kg")

            trip_obj.ComsumedWeight += instance.Total_Weight
            trip_obj.TotalWeightTrip += instance.Total_Weight

            instance.trips = trip_obj
            trip_obj.save()

        instance.save()
        return instance
  
    