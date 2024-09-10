from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny 
from .serializers import MyTokenObtainPairSerializer,SignUpSerializer,RequestPasswordRequestSerializer,OTPRequestSerializer,ResetPasswordWithOTPSerializer
from .models import CustomUser,PasswordReset,OTP
from rest_framework_simplejwt.views import TokenObtainPairView
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .utils import send_email



class RequestPassword(generics.GenericAPIView):
    permission_classes=[AllowAny]
    serializer_class=RequestPasswordRequestSerializer

    def post(self,request):
        email=request.data['email']
        user=CustomUser.objects.filter(email__iexact=email).first()

        if user:
            token_generator=PasswordResetTokenGenerator()
            token=token_generator.make_token(user)
            expiration_date=timezone.now()+timedelta(hours=24)

            reset=PasswordReset(email=email,token=token,expiration_date=expiration_date)
            reset.save()
            reset_url=f"http://localhost:8000/CustomUser/reset-password?token={token}&email={email}"
            email_message=\
                f"you are receving this email because you requested"\
                f"a password reset for your acount. \n\n"\
                f"to reset your password, please click the following link \n "\
                f"{reset_url}\n\n" f"this link will expire in {48} hours"
            
            send_email(email,'passord reset requested',email_message)
            return Response({'success': "Email sent successfully!"},status=status.HTTP_200_OK)
        else:
            return Response({"error":"User with this email address not found"},
                            status=status.HTTP_404_NOT_FOUND)
        


        
class OTPRequestView(generics.GenericAPIView):
    serializer_class = OTPRequestSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        email = serializer.validated_data['email']
        user = CustomUser.objects.filter(email=email).first()

        otp_instance, created = OTP.objects.get_or_create(user=user)
        if not created:
            otp_instance.save()

        return Response({"otp": otp_instance.otp}, status=status.HTTP_200_OK)


class ResetPasswordWithOTPView(generics.GenericAPIView):
    serializer_class = ResetPasswordWithOTPSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        new_password = serializer.validated_data['new_password']

        # Get the user instance
        user = CustomUser.objects.get(email=email)

        # Reset the password
        user.set_password(new_password)
        user.save()

        # Optionally delete the OTP after use
        OTP.objects.filter(user=user).delete()

        return Response({'message': 'Password reset successfully.'}, status=status.HTTP_200_OK)



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





        
