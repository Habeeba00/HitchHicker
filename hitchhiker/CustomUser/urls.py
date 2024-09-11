from .views import SignUpView
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import MyTokenObtainPairView,RequestPassword,OTPRequestView,ResetPasswordWithOTPView,LogoutView


urlpatterns = [
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('SignUp/', SignUpView.as_view(), name='sign-up'),
    path('request-password/', RequestPassword.as_view(), name='request-password'),
    path('reset-password/', OTPRequestView.as_view(), name='reset-password'),
    path('reset-password-otp/', ResetPasswordWithOTPView.as_view(), name='reset-password-otp'),
    path('api/logout/', LogoutView.as_view(), name='logout'),


    

]
