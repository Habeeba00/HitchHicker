

from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny 
from .serializers import MyTokenObtainPairSerializer,SignUpSerializer
from .models import CustomUser
from rest_framework_simplejwt.views import TokenObtainPairView

#Login User
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

#Register User
class SignUpView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]
    serializer_class = SignUpSerializer



    def create(self, request, *args, **kwargs):
        # Call the parent class to create the user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        print(user.is_active)
        # You can add any custom data to the response here if needed
        response_data = {
            'user': serializer.data,  # This will return the serialized data of the created user
            'message': 'User registered successfully'
        }

        return Response(response_data, status=status.HTTP_201_CREATED)
    



    