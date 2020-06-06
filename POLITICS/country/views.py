from django.shortcuts import render
from rest_framework.response import Response
import random
from django.db.models import Q
import string
from datetime import datetime as dt
from rest_framework import status
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Country, PMs
import datetime


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated, ))
def pm_action(request):
    if request.method == 'POST':
        requested_data = request.data
        post_serializers = PmsPostSerializers(data=requested_data)
        if post_serializers.is_valid():
            current_time = datetime.datetime.now()
            validated_dict = post_serializers.validated_data
            country_table_id = validated_dict['country_table_id']
            name = validated_dict['name']
            age = validated_dict['age']
            party = validated_dict['party']
            random_country_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            pm_id = str(name) + '_' + str(random_country_id)
            pm_object = PMs.objects.create(
                name=name,
                pm_id=pm_id,
                age=age,
                party=party,
                time_stamp=current_time,
                country_id=country_table_id
            )
            pm_object.save()
            return_data = {
                'message': 'New Pm Added Successfully',
                'data': requested_data
            }
            return Response(return_data, status.HTTP_201_CREATED)

        else:
            return Response(post_serializers.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated, ))
def country_action(request):
    if request.method == 'PUT':
        requested_data = request.data
        current_time = datetime.datetime.now()
        country_id = requested_data.get('country_id', None)
        name = requested_data.get('name', None)
        if country_id and name:
            country_data = Country.objects.filter(country_id=country_id)
            # second method to update
            # country_data = Country.objects.get(country_id=country_id)
            # country_data.name = name
            # country_data.save()
            # but it generates error if mathching country_id data not found
            if country_data.exists():
                country_data.update(name=name, time_stamp=current_time)
                response_data = {
                    'message': 'Country Details Updated Successfully',
                    'data': requested_data
                }
                return Response(response_data, status.HTTP_200_OK)
            else:
                response_data = {
                    'message': 'Country_id is incorrect',
                    'data': requested_data
                }
                return Response(response_data, status.HTTP_400_BAD_REQUEST)
        else:
            response_data = {
                'message': 'Country_id and name are required',
                'data': requested_data
            }
            return Response(response_data, status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        requested_data = request.query_params
        country_id = requested_data.get('country_id', None)
        if country_id:
            all_data = Country.objects.filter(Q(country_id=country_id))
        else:
            all_data = Country.objects.all()
        serialized_data = CountryGetDataSerializers(all_data, many=True)

        response_data = {
            'data': serialized_data.data
        }
        return Response(response_data, status.HTTP_200_OK)

    elif request.method == 'DELETE':
        requested_data = request.data
        country_id = requested_data.get('country_id')
        if country_id:
            get_country_data = Country.objects.filter(country_id=country_id)
            if get_country_data.exists():
                delete_result = get_country_data.delete()
                response_data = {
                    'message': 'Deleted Successfully',
                    'Country_id': country_id
                }
                return Response(response_data, status.HTTP_200_OK)
            else:
                response_data = {
                    'message': 'Incorrect Country_id Passed'
                }
                return Response(response_data, status.HTTP_400_BAD_REQUEST)
        else:
            response_data = {
                'message': 'Country_id is required'
            }
            return Response(response_data, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        request_data = request.data
        # Instance of CountrySerializers
        country_instance = CountrySerializers(data=request_data)
        if country_instance.is_valid():
            country_name = request_data['name']
            time_stamp = request_data['time_stamp']
            check_country_entry = Country.objects.filter(name=country_name)
            if not check_country_entry.exists():
                random_country_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
                new_country_id = str(country_name) + "_" + str(random_country_id)
                new_country = Country.objects.create(
                    name=country_name,
                    country_id=new_country_id,
                    time_stamp=time_stamp
                )
                new_country.save()
                response_data = {
                    'message': 'Country Added Successfully',
                    'data': request_data
                }
                return Response(response_data, status.HTTP_201_CREATED)
            else:
                response_data = {
                    'message': 'Country Already Exists',
                    'data': request_data
                }
                return Response(response_data, status.HTTP_400_BAD_REQUEST)

        else:
            return Response(country_instance.errors, status.HTTP_400_BAD_REQUEST)

