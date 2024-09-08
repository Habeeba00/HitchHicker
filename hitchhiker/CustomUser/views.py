from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny 
from .serializers import MyTokenObtainPairSerializer,SignUpSerializer
from .models import CustomUser
from rest_framework_simplejwt.views import TokenObtainPairView
from django.core.mail import send_mail
from rest_framework.decorators import api_view


@api_view(['POST'])
def reset_request(request):
    data = request.data
    email = data['email']
    user = CustomUser.objects.get(email=email)
    if CustomUser.objects.filter(email=email).exists():
        send_mail(
        'Subject here',
        f'Here is the message with {user.otp}.',
        'from@example.com',
        [user.email],
        fail_silently=False,
        )
        message = {
            'detail': 'Success Message'}
        return Response(message, status=status.HTTP_200_OK)
    else:
        message = {
            'detail': 'Some Error Message'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
def reset_password(request):
    """Reset password with email, OTP, and new password"""
    data = request.data

    try:
        user = CustomUser.objects.get(email=data['email'])
    except CustomUser.DoesNotExist:
        return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    if user.is_active:
        if data['otp'] == user.otp:  # Ensure 'otp' is the correct field name
            new_password = data.get('password', '')
            if new_password:
                user.set_password(new_password)
                user.save()  # Save changes
                return Response({'detail': 'Password updated successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Password cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'OTP did not match'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'detail': 'User account is not active'}, status=status.HTTP_400_BAD_REQUEST)


#Login User
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

#Register User
class SignUpView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]
    serializer_class = SignUpSerializer




    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        print(user.is_active)
        response_data = {
            'user': serializer.data,
            'message': 'User registered successfully'
        }

        return Response(response_data, status=status.HTTP_201_CREATED)





        
