from locations.models import locationModel
from locations.serializers import locationSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class locationViewset(viewsets.ModelViewSet):
    queryset = locationModel.objects.all()
    serializer_class = locationSerializer
    permission_classes=[IsAuthenticated]