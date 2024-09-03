from rest_framework.routers import DefaultRouter
from django.urls import path,include
# from .views import SignInView ,SignUpView


router=DefaultRouter()
# router.register(r'SignUp',SignUpView,basename='SignUp'),
# router.register(r'SignIn',SignInView,basename='SignIn')


urlpatterns=[
    path('',include(router.urls))
]