from Trips.models import Trips
from Trips.serializers import TripSerializers
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from CustomUser.models import CustomUser

class TripsViewset(viewsets.ModelViewSet):
    queryset = Trips.objects.all()
    serializer_class = TripSerializers
    permission_classes=[IsAuthenticated]



    # def create(self, request, *args, **kwargs):
    #     if request.method == "POST":
    #         try:
    #             adding_user = request.user    
    #             username = adding_user.username
    #             serializer = self.get_serializer(data=request.data)
    #             serializer.is_valid(raise_exception=True)
    #             instance_trips=serializer.save(added_by=adding_user)
    #             data = TripSerializers(instance_trips).data
    #             data['username'] = username


    #             return Response(data ,status=status.HTTP_201_CREATED)
    #         except CustomUser.DoesNotExist:
    #             return Response({'error': 'CustomUser with given id not found'}, status=status.HTTP_404_NOT_FOUND)
            

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance_id = instance.id
    #     instance.delete()
    #     return Response({"message": f"Trip with id {instance_id} deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    

    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
        
    #     # instance_Name = instance.Shipment_Name
    #     instance_id = instance.id

    #     serializer.save()

    #     return Response(
    #         {"message": f"The Trip {instance_id} has been updated successfully.", "data": serializer.data},
    #         status=status.HTTP_200_OK
    #     )
    
