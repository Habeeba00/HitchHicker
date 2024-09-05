from rest_framework import serializers
from Trips.models import Trips


class TripSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model=Trips
        fields="__all__"
        read_only_fields = ['id','Total_Shipment_Weight','ComsumedWeight']
        
    # def create (self, validated_data):
    #     validated_data['TotolWeight'] = validated_data['FreeWeight'] + validated_data['ComsumedWeight']
    #     return super().create(validated_data)