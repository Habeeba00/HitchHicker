import django_filters
from django_filters import rest_framework as filters
from Trips.models import Trips


class TripsFilter(filters.FilterSet):
    From=django_filters.CharFilter(field_name="From",lookup_expr="icontains")
    To=django_filters.CharFilter(field_name="To",lookup_expr="icontains")
    depart_Date=django_filters.DateFilter(field_name="depart_Date",lookup_expr="lte")
    Weight=django_filters.NumberFilter(field_name='FreeWeight',lookup_expr='gte')
    
    class Meta:
        model=Trips
        fields =['From','To','depart_Date','Weight']
