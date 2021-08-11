# from django_filters import rest_framework as filters
from district.models import Student
import django_filters


class StudentFilter(django_filters.rest_framework.FilterSet):
    # filter name condition with icontains
    # https://django-filter.readthedocs.io/en/stable/guide/usage.html
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    value = django_filters.CharFilter(field_name='value', lookup_expr='lt')

    class Meta:
        model = Student
        fields = ['name', 'address']