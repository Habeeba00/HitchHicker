from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import Shipments
from .serializers import ShipmentsSerializer
from rest_framework.permissions import IsAuthenticated
from CustomUser.models import CustomUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from .filters import ShipmentsFilter



class ShipmentsView(viewsets.ModelViewSet):
    queryset=Shipments.objects.all()
    serializer_class=ShipmentsSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    search_fields=["From","To",'Date_Befor','Weight']
    ordering_fields=['Date_Befor',"Shipment_Name"]
    ordering = ['Date_Befor']
    filterset_class = ShipmentsFilter



    def create(self, request, *args, **kwargs):
        if request.method == "POST":
            try:
                adding_user = request.user    
                username = adding_user.username
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                instance_shipment=serializer.save(added_by=adding_user)
                data = ShipmentsSerializer(instance_shipment).data
                data['username'] = username


                return Response(data ,status=status.HTTP_201_CREATED)
            except CustomUser.DoesNotExist:
                return Response({'error': 'CustomUser with given id not found'}, status=status.HTTP_404_NOT_FOUND)
            

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
        
        instance_Name = instance.Shipment_Name
        serializer.save()

        return Response(
            {"message": f"The shipment {instance_Name} has been updated successfully.", "data": serializer.data},
            status=status.HTTP_200_OK
        )
    
