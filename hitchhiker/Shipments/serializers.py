from rest_framework import serializers
from .models import Shipments



class ShipmentsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model=Shipments
        fields = ['id','From', 'To', 'Date_Befor', 'Shipment_Name', 'Quantity', 'Weight', 'Price','Total_Price','Total_Weight','image' ,'added_by']
