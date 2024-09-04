from rest_framework import serializers
from .models import Shipments
from CustomUser.models import CustomUser



class ShipmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shipments
        fields = ['From', 'To', 'Date_Befor', 'Shipment_Name', 'Quantity', 'Weight', 'Price','Total_Price','Total_Weight','image' ,'added_by']
