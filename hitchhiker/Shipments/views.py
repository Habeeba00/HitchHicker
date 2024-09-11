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
    search_fields=["From","To",'Date_Befor','Weight']
    ordering_fields=['Date_Befor',"Shipment_Name"]
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
    
   
    
def update(self, request, *args, **kwargs):
    partial = kwargs.pop('partial', False)
    instance = self.get_object()
    serializer = self.get_serializer(instance, data=request.data, partial=partial)
    serializer.is_valid(raise_exception=True)
    
    # Store the shipment name before updating
    instance_Name = instance.Shipment_Name
    
    # Save the shipment update
    serializer.save()

    # Handle Trip Data if provided in the request
    trip_data = request.data.get('trip')  # Assuming the trip data comes in 'trip' key
    if trip_data:
        # Validate and process trip data
        trip_serializer = tripSerializers(data=trip_data)
        if trip_serializer.is_valid():
            trip_instance = trip_serializer.save()
            # Add the trip to the shipment instance
            instance.trip = trip_instance
            instance.save()
        else:
            return Response(trip_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(
        {"message": f"The shipment {instance_Name} has been updated successfully with the trip.", "data": serializer.data},
        status=status.HTTP_200_OK
    )


    
