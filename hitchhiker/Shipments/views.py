from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import Shipments
from .serializers import ShipmentsSerializer
from rest_framework.permissions import IsAuthenticated
from CustomUser.models import CustomUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from .filters import ShipmentsFilter
from django.shortcuts import get_object_or_404
from Trips.serializers import tripSerializers
from .permissions import IsOwnerUser




class ShipmentsView(viewsets.ModelViewSet):
    queryset=Shipments.objects.all()
    serializer_class=ShipmentsSerializer
    permission_classes = [IsAuthenticated,IsOwnerUser]
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    
    search_fields=["From__name","To__name",'Date_Befor','Weight']
    
    ordering_fields=['Date_Befor',"From__name","To__name"]
    
    ordering = ['Date_Befor']
    
    filterset_class = ShipmentsFilter


    def create(self, request, *args, **kwargs):
        try:
            serializer = ShipmentsSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            print(request.user)
            shipment = serializer.save(added_by=request.user)
            
            data = serializer.data
            from_location = shipment.From 
            print(from_location)
            to_location = shipment.To  
            data['added_by'] = request.user.username
            data['From'] = from_location.city 
            data['To'] = to_location.city
            
            return Response(data, status=status.HTTP_201_CREATED)
        except CustomUser.DoesNotExist:
            return Response({'error': 'CustomUser with given id not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance_id = instance.id
        instance.delete()
        return Response({"message": f"Shipment with id {instance_id} deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    
   
    