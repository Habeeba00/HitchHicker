
from location.models import locationModel
from location.serializers import locationSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

class loctaionViewset(viewsets.ModelViewSet):
    queryset = locationModel.objects.all()
    serializer_class = locationSerializer
    # filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
    # filterset_fields=['country']
  
    