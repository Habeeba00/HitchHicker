from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Trips.views import TripsViewset

router = DefaultRouter()
router.register(r'Trips', TripsViewset)

urlpatterns = [
    path('',include(router.urls))
]