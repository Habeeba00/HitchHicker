from rest_framework import generics,status
from rest_framework.response import Response
from .models import Shipments
from .serializers import ShipmentsSerializer
from rest_framework.permissions import IsAuthenticated
from CustomUser.models import CustomUser



class ShipmentsView(generics.ListCreateAPIView):
    queryset=Shipments.objects.all()
    serializer_class=ShipmentsSerializer
    permission_classes = [IsAuthenticated]

      
    # def create(self, request, *args, **kwargs):
    #   if request.method == "POST":
    #     print("Entered")
    #     try:
    #         adding_user = request.user
    #         print(adding_user)
    #         print(f"Authenticated User ID: {adding_user.id}")
            
    #         serializer = self.get_serializer(data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         instance_shipment=serializer.save(added_by=adding_user)
    #         data = ShipmentsSerializer(instance_shipment).data

    #         return Response(data.data, status=status.HTTP_201_CREATED)
    #     except CustomUser.DoesNotExist:
    #         return Response({'error': 'CustomUser with given id not found'}, status=status.HTTP_404_NOT_FOUND)

            