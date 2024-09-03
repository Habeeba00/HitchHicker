from .views import SignUpView
from django.urls import path
from .views import MyTokenObtainPairView

urlpatterns = [
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('SignUp/', SignUpView.as_view(), name='sign-up'),

]
