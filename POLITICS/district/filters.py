from django_filters import rest_framework as filters
from district.models import Student


class StudentFilter(filters.FilterSet):

    class Meta:
        model = Student
        fields = ['name', 'address']