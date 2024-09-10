from rest_framework import status
from Shipments.models import Shipments
from Shipments.serializers import ShipmentsSerializer
from rest_framework.response import Response
from CustomUser.models import CustomUser
from rest_framework import serializers
from locations.models import locationModel
from CustomUser.serializers import SignUpSerializer
from Trips.models import Trips


class tripSerializers(serializers.ModelSerializer):
    username = SignUpSerializer(read_only=True)

    From = serializers.SlugRelatedField(slug_field='country', queryset=locationModel.objects.all())
    To = serializers.SlugRelatedField(slug_field='country', queryset=locationModel.objects.all())

    shipments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  # assuming reverse relation

    class Meta:
<<<<<<< HEAD
        model=Trips
        fields = '__all__'
=======
        model = Trips
        fields = ['id', 'From', 'To', 'depart_Date', 'depart_Time', 'FreeWeight', 'ComsumedWeight', 'TotalWeightTrip', 'username', 'shipments']
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
>>>>>>> 75b81d8a95a7366119c581ae0d5fcedf521acc2d
