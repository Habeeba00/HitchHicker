from Locations.models import locationModel
from Locations.serializers import locationSerializer
from rest_framework import viewsets

class locationViewset(viewsets.ModelViewSet):
    queryset = locationModel.objects.all()
    serializer_class = locationSerializer