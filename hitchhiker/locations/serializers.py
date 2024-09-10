from rest_framework import serializers
from locations.models import locationModel


class locationSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)

    class Meta:
        model=locationModel
        fields="__all__"