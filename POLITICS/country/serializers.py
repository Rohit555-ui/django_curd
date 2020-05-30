from rest_framework import serializers
from .models import Country
from datetime import datetime as dt
import logging
from django.contrib.auth.models import User


class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('name', 'time_stamp')


class CountryGetDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('name', 'country_id', 'time_stamp')

