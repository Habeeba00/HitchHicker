import django_filters
from django_filters import rest_framework as filters
from .models import Shipments



class ShipmentsFilter(filters.FilterSet):
    Date_Befor=django_filters.DateFilter(field_name="Date_Befor",lookup_expr="lte")
    Weight=django_filters.NumberFilter(field_name='Weight',lookup_expr='gte')
    From=django_filters.CharFilter(method='filter_from')
    To=django_filters.CharFilter(method='filter_to')
    
    
    
    class Meta:
        model=Shipments
        fields =['From','To','Date_Befor','Weight']
    
    
    def filter_from(self, queryset, name, value):
        return queryset.filter(From__city__icontains=value)
    
    
    def filter_to(self, queryset, name, value):
        return queryset.filter(To__city__icontains=value)
