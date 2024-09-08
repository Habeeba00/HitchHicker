from rest_framework import serializers
from .models import Shipments
from CustomUser.serializers import SignUpSerializer
from Locations.serializers import locationSerializer
from Locations.models import locationModel



class ShipmentsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    added_by = SignUpSerializer(read_only=True)
    From = serializers.PrimaryKeyRelatedField(queryset=locationModel.objects.all())
    To = serializers.PrimaryKeyRelatedField(queryset=locationModel.objects.all())

    class Meta:
        model = Shipments
        fields = ['id', 'From', 'To', 'Date_Befor', 'Shipment_Name', 'Quantity', 'Weight', 'Price', 'Total_Price', 'Total_Weight', 'image', 'added_by', 'Trips']

    def create(self, validated_data):
        # Check if 'From' exists in the validated data
        from_location = validated_data.get('From')
        if from_location is None:
            raise serializers.ValidationError("The 'From' field is required.")
        shipment = Shipments.objects.create(**validated_data)

        # Create the shipment
        return shipment 