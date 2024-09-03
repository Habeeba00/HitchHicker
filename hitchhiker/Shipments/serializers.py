from rest_framework import serializers
from .models import Shipments
from CustomUser.models import CustomUser



class ShipmentsSerializer(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(
    queryset=CustomUser.objects.all(),  # Adjust the queryset as needed
    slug_field='username',
    required=True
)


    class Meta:
        model=Shipments
        fields="__all__"
        # fields = [
        #     'From',
        #     'To',
        #     'Date_Befor',
        #     'Shipment_Name',
        #     'Quantity',
        #     'Weight',
        #     'Price',
        #     'Total_Price',
        #     'Total_Weight',
        #     'added_by'
        # ]
        