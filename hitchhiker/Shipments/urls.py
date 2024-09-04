from django.urls import path
from .views import ShipmentsView

urlpatterns=[
    path('Shipments/', ShipmentsView.as_view(), name='Shipments'),

]
