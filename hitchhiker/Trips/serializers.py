from rest_framework import status
from Shipments.models import Shipments
from Shipments.serializers import ShipmentsSerializer
from rest_framework.response import Response
from CustomUser.models import CustomUser
from rest_framework import serializers

from Trips.models import Trips
class tripSerializers(serializers.ModelSerializer):
    shipments = ShipmentsSerializer(many=True, read_only=True)  # Add shipments to trip serializer

    class Meta:
        model=Trips
        fields = '__all__'
