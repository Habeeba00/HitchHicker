import django_filters
from django_filters import rest_framework as filters
from Trips.models import Trips


class TripsFilter(filters.FilterSet): 
    depart_Date = django_filters.DateFilter(field_name="depart_Date", lookup_expr="lte") 
    Weight = django_filters.NumberFilter(field_name='FreeWeight', lookup_expr='gte')  
    From=django_filters.CharFilter(method='filter_from')
    To=django_filters.CharFilter(method='filter_to')
    
    class Meta:
        model = Trips
        fields = ['From', 'To', 'depart_Date', 'Weight']
        
    def filter_from(self, queryset, name, value):
        return queryset.filter(From__city__icontains=value)
    
    
    def filter_to(self, queryset, name, value):
        return queryset.filter(To__city__icontains=value)
