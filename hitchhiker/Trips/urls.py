from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Trips.views import tripViewset

router = DefaultRouter()
router.register(r'Trips', tripViewset)

urlpatterns = router.urls