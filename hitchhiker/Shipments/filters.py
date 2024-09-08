import django_filters
from django_filters import rest_framework as filters
from .models import Shipments



class ShipmentsFilter(filters.FilterSet):
    From=django_filters.CharFilter(field_name="From",lookup_expr="icontains")
    To=django_filters.CharFilter(field_name="To",lookup_expr="icontains")
    Date_Befor=django_filters.DateFilter(field_name="Date_Befor",lookup_expr="lte")
    Weight=django_filters.NumberFilter(field_name='Weight',lookup_expr='lte')


    class Meta:
        model=Shipments
        fields =['From','To','Date_Befor','Weight']
