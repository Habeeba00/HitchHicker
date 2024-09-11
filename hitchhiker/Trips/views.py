from Trips.models import Trips
from Trips.serializers import tripSerializers
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter,OrderingFilter
from Trips.filters import TripsFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from CustomUser.models import CustomUser
from Shipments.filters import ShipmentsFilter


class TripsViewset(viewsets.ModelViewSet):
    queryset = Trips.objects.all()
    serializer_class = tripSerializers
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    
    search_fields=["From__name","To__name", "depart_Date", "FreeWeight"]
    
    ordering_fields = ['depart_Date', 'From__name', 'To__name']
    
    ordering = ['depart_Date']
    filterset_class = TripsFilter
    
    def retrieve(self, request, *args, **kwargs):
        trip = self.get_object()

        shipments = trip.shipments.all()  
        
        shipment_names = [shipment.Shipment_Name for shipment in shipments]

        serializer = self.get_serializer(trip)

        data = serializer.data
        data['shipments']=shipment_names

        return Response(data)
    
    
    
    
    
    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())

    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)

    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # trips = self.get_queryset()

        serializer = self.get_serializer(queryset, many=True)

        data = serializer.data

        for trip_data in data:
            trip = queryset.get(id=trip_data['id'])

            shipments = trip.shipments.all() 
            shipment_names = [shipment.Shipment_Name for shipment in shipments]
            
            trip_data['shipments'] = shipment_names

        return Response(data)
    
    def create(self, request, *args, **kwargs):
        if request.method=="POST":
            try:
                serializer=tripSerializers(data=request.data)
                serializer.is_valid(raise_exception=True)
                trip=serializer.save(username=request.user)
                data = serializer.data
                fromLocation=trip.From
                ToLocation=trip.To
                data['username'] = request.user.username
                data['From'] = fromLocation.country 
                data['To'] = ToLocation.country 
                return Response(data, status=status.HTTP_201_CREATED)
            except CustomUser.DoesNotExist:
                return Response({'error': 'CustomUser with given id not found'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
              
    # def update(self, request, pk):
    #     shipment = get_object_or_404(Trips, pk=pk)
        
    #     serializer = tripSerializers(shipment, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()  

    #     return Response(serializer.data)     
    
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance_id = instance.id
        instance.delete()
        return Response({"message": f"Trip with id {instance_id} deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    
