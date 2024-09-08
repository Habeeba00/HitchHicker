from django.urls import path, include
from rest_framework.routers import DefaultRouter
from location.views import loctaionViewset

router = DefaultRouter()
router.register(r'Location', loctaionViewset)

urlpatterns = [
    path('',include(router.urls))
]