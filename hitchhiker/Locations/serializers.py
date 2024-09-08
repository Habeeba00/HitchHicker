from rest_framework import serializers
from Locations.models import locationModel
class locationSerializer(serializers.ModelSerializer):

    class Meta:
        model=locationModel
        fields="__all__"