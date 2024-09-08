from Trips.models import Trips
from Trips.serializers import tripSerializers
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter,OrderingFilter
from Trips.filters import TripsFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from CustomUser.models import CustomUser
from django.shortcuts import get_object_or_404

class TripsViewset(viewsets.ModelViewSet):
    queryset = Trips.objects.all()
    serializer_class = tripSerializers
    # permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    search_fields=["From","To",'depart_Date','FreeWeight']
    ordering_fields=['depart_Date',"Shipment_Name"]
    ordering = ['depart_Date']
    filterset_class = TripsFilter
    
    
    def create(self, request, *args, **kwargs):
        if request.method=="POST":
            try:
                adding_user = request.user  
                username = adding_user.username
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                instance_Trip=serializer.save(username=adding_user)
                data=tripSerializers(instance_Trip).data
                data['username']=username
                return Response(data ,status=status.HTTP_201_CREATED)
            except CustomUser.DoesNotExist:
                return Response({'error': 'CustomUser with given id not found'}, status=status.HTTP_404_NOT_FOUND)
   
   
    def update(self, request, pk):
        shipment = get_object_or_404(Trips, pk=pk)
        
        serializer = tripSerializers(shipment, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()  

        return Response(serializer.data)     
    
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance_id = instance.id
        instance.delete()
        return Response({"message": f"Trip with id {instance_id} deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    
