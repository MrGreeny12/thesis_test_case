from django_filters import rest_framework as filters

from organization.models import Employee


class EmployeesFilter(filters.FilterSet):
    city = filters.CharFilter(field_name='city', lookup_expr='icontains')

    class Meta:
        model = Employee
        fields = ('last_name', 'department')
