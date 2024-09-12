from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import Shipments
from .serializers import ShipmentsSerializer
from rest_framework.permissions import IsAuthenticated
from CustomUser.models import CustomUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from .filters import ShipmentsFilter
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
        

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data

        # Modify the 'username' field to return only the username string
        if isinstance(data['username'], dict):
            data['username'] = data['username']['username']

        return Response(data)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        # Modify the 'username' field for each trip in the list
        for shipment in data:
            if isinstance(trip['username'], dict):
                shipment['username'] = shipment['username']['username']

        return Response(data)


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance_id = instance.id
        instance.delete()
        return Response({"message": f"Shipment with id {instance_id} deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    



    
