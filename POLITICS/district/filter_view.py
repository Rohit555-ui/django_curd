from django.shortcuts import render
from django.views.generic import ListView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView
from django.db.models import Avg, Max, Min, Sum, Count
from rest_framework import viewsets, mixins
from .serializers import *
import random, logging
from .decorator import decor, DecorClass
from drf_yasg.utils import get_serializer_class, swagger_auto_schema
from rest_framework.exceptions import ParseError
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ParseError, AuthenticationFailed, APIException, NotFound
import string
from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework import generics
from django.db.models import Subquery
from django.db.models import Q
from .models import *
from django.db import connection
from django.views.decorators.csrf import csrf_protect
from django.apps import apps
import pandas as pd
from django.http import HttpResponse
from django.views.generic.base import TemplateView, RedirectView
from district.filters import StudentFilter

# Link for refrence is https://www.django-rest-framework.org/api-guide/filtering/

# http://localhost:8001/district/FilterByUrl/s1
class FilterByUrlParam(ListAPIView):
    serializer_class = StudentSerializerS

    def get_queryset(self):
        return Student.objects.filter(name=self.kwargs['name'])

# http://localhost:8001/district/FilterByQueryParams?name=s1
class FilterByQueryParams(ListAPIView):
    serializer_class = StudentSerializerS

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        return Student.objects.filter(name=name)

# http://localhost:8001/district/GenericFilter?name=s1&address=a1
class GenericFilter(ListAPIView):
    serializer_class = StudentSerializerS
    filter_backends = [DjangoFilterBackend]
    filter_class = StudentFilter

    def get_queryset(self):
        return Student.objects.all()


















































