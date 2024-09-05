from rest_framework import serializers
from location.models import locationModel
class locationSerializer(serializers.ModelSerializer):

    class Meta:
        model=locationModel
        fields="__all__"