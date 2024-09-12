from rest_framework import serializers
from locations.models import locationModel
from CustomUser.serializers import SignUpSerializer
from Trips.models import Trips
from Shipments.serializers import ShipmentsSerializer

class tripSerializers(serializers.ModelSerializer):
    username = SignUpSerializer(read_only=True)

    From = serializers.PrimaryKeyRelatedField( queryset=locationModel.objects.all())
    To = serializers.PrimaryKeyRelatedField( queryset=locationModel.objects.all())
    ship = ShipmentsSerializer(many=True, required=False)  

    class Meta:
        model = Trips
        fields = ['id', 'From', 'To', 'depart_Date', 'depart_Time','FreeWeight', 'ComsumedWeight', 'TotalWeightTrip', 'username', 'ship']
        read_only_fields = ['TotalWeightTrip', 'shipments']
        
        
        def create(self, validated_data):
            from_location = validated_data.pop('From')
            to_location = validated_data.pop('To')

            user = self.context['request'].user

            trip = Trips.objects.create(
                From=from_location,
                To=to_location,
                username=user,
                **validated_data
            )

            return trip
    
           
           
           
        def update(self, instance, validated_data):
            instance.From = validated_data.get('From', instance.From)
            instance.To = validated_data.get('To', instance.To)
            instance.depart_Date = validated_data.get('depart_Date', instance.depart_Date)
            instance.depart_Time = validated_data.get('depart_Time', instance.depart_Time)
            instance.FreeWeight = validated_data.get('FreeWeight', instance.FreeWeight)
            instance.ComsumedWeight = validated_data.get('ComsumedWeight', instance.ComsumedWeight)
            instance.TotalWeightTrip = instance.FreeWeight + instance.ComsumedWeight
            
            instance.save()
            return instance
