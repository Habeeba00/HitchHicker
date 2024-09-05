from rest_framework import status
from Shipments.models import Shipments
from Shipments.serializers import ShipmentsSerializer
from rest_framework.response import Response
from CustomUser.models import CustomUser
from rest_framework import serializers

from Trips.models import tripsModel
class tripSerializers(serializers.ModelSerializer):
    shipments = ShipmentsSerializer(many=True, read_only=True)  # Add shipments to trip serializer

    class Meta:
        model=tripsModel
        fields = ['id','From', 'username','To', 'depart_Date', 'depart_Time', 'TotalWeightTrip', 'ComsumedWeight', 'FreeWeight', 'shipments']
   
        def create(self, validated_data):
            trip = tripsModel.objects.create(
            From=validated_data['From'],
            To=validated_data['To'],
            depart_Date=validated_data['depart_Date'],
            depart_Time=validated_data['depart_Time'],
            FreeWeight=validated_data['FreeWeight'],
            ComsumedWeight=validated_data.get('ComsumedWeight', 0.0), 
            TotalWeightTrip=validated_data.get('TotalWeightTrip', 0.0)
        )
            return trip
    

