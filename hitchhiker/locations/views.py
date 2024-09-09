from locations.models import locationModel
from locations.serializers import locationSerializer
from rest_framework import viewsets

class locationViewset(viewsets.ModelViewSet):
    queryset = locationModel.objects.all()
    serializer_class = locationSerializer