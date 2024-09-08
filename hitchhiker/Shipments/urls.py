from django.urls import path,include
from .views import ShipmentsView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'Shipments',ShipmentsView)

urlpatterns=[
    path('', include(router.urls)),

]
