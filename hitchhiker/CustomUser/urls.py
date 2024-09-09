from .views import SignUpView
from django.urls import path
from .views import MyTokenObtainPairView,RequestPassword,OTPRequestView


urlpatterns = [
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('SignUp/', SignUpView.as_view(), name='sign-up'),
    path('request-password/', RequestPassword.as_view(), name='request-password'),
    path('reset-password/', OTPRequestView.as_view(), name='reset-password'),
    

]
