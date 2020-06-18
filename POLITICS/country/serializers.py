from abc import ABC

from rest_framework import serializers
from .models import Country, PMs
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


class PmsPostSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=100, required=True)
    age = serializers.IntegerField(required=True, min_value=35)
    party = serializers.CharField(max_length=100, required=True)
    country_id = serializers.CharField(max_length=100, required=True)

    def validate(self, attrs):
        country_id = attrs['country_id']
        name = attrs['name']
        try:
            country_data = Country.objects.get(country_id=country_id)
        except Exception as e:
            raise serializers.ValidationError('This Country does not exists in this world')

        country_mapping_data = PMs.objects.filter(country_id=country_data.id)
        if country_mapping_data.exists():
            raise serializers.ValidationError('This country has already pm, '+str(country_mapping_data[0].name))

        attrs['country_table_id'] = country_data.id
        return attrs
