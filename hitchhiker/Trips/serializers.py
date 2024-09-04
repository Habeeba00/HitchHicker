from rest_framework import serializers
from Trips.models import tripsModel
from Shipments.serializers import ShipmentsSerializer
class tripSerializers(serializers.Serializer):
    
    class Meta:
        model=tripsModel
        fields="__all__"
        read_only_fields = ['TotolWeight','ComsumedWeight']
        
    def create (self, validated_data):
        validated_data['TotolWeight'] = validated_data['FreeWeight'] + validated_data['ComsumedWeight']
        return super().create(validated_data)
# 