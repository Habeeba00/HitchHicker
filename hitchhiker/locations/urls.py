from django.urls import path, include
from rest_framework.routers import DefaultRouter
from locations.views import locationViewset

router = DefaultRouter()
router.register(r'locations', locationViewset)

urlpatterns = [
    path('',include(router.urls))
]