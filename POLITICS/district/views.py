from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
import random
import string
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Subquery
from django.apps import apps
states_model = apps.get_model('states', 'States')
country_model = apps.get_model('country', 'Country')


# Create your views here.
class DistrictAction(APIView):
    def get(self, request):
        try:
            all_data = []
            all_country_list = []
            all_state_list = []
            all_district_list = []

            request_data = request.query_params
            district_id = request_data.get('district_id', None)
            state_id = request_data.get('state_id', None)
            country_id = request_data.get('country_id', None)
            if district_id:
                district_data = District.objects.filter(district_id=district_id)
            elif state_id:
                district_data = District.objects.filter(
                    state_id__in=Subquery(states_model.objects.filter(state_id=state_id).values('id'))
                )
            elif country_id:
                district_data = District.objects.filter(
                    state_id__in=Subquery(
                        states_model.objects.filter(country_id__in=Subquery(
                                country_model.objects.filter(country_id=country_id).values('id')
                            )
                        ).values('id')
                    )
                )
            else:
                district_data = District.objects.filter()

            for district_obj in district_data:
                district_name = district_obj.name
                district_id = district_obj.district_id
                state_name = district_obj.state.name
                state_id = district_obj.state.state_id
                country_name = district_obj.state.country.name
                country_id = district_obj.state.country.country_id
                if not country_id in all_country_list:
                    temp_country_data = {}
                    temp_country_data['country_name'] = country_name
                    temp_country_data['country_id'] = country_id
                    temp_country_data['states'] = []
                    all_data.append(temp_country_data)
                    all_country_list.append(country_id)

                if not state_id in all_state_list:
                    temp_state_data = {}
                    temp_state_data['state_name'] = state_name
                    temp_state_data['state_id'] = state_id
                    temp_state_data['districts'] = []
                    for all_data_obj in all_data:
                        if country_name == all_data_obj['country_name']:
                            all_data_obj['states'].append(temp_state_data)
                            all_state_list.append(state_id)

                if not district_id in all_district_list:
                    temp_district_data = {}
                    temp_district_data['district_name'] = district_name
                    temp_district_data['district_id'] = district_id
                    for all_data_obj in all_data:
                        # print(all_data_obj['country_name'])
                        if country_name == all_data_obj['country_name']:
                            for all_states_obj in all_data_obj['states']:
                                if state_name == all_states_obj['state_name']:
                                    all_states_obj['districts'].append(temp_district_data)
                                    all_district_list.append(district_id)

            response_data = {
                'status': 'success',
                'data': all_data
            }
            return Response(response_data, status.HTTP_200_OK)
        except Exception as e:
            response_data = {
                'status': 'failed',
                'error': str(e)
            }
            return Response(response_data, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            request_data = request.data
            serialized = DistrictPostSerializers(data=request_data)
            if serialized.is_valid():
                random_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
                name = request_data.get('name', None)
                district_id = name + "_" + str(random_id)
                time_stamp = request_data.get('time_stamp', None)
                state_id = serialized.validated_data['state_table_id']
                new_district = District.objects.create(
                    name=name,
                    district_id=district_id,
                    state_id=state_id,
                    time_stamp=time_stamp
                )
                new_district.save()
                response_data = {
                    'status': 'success',
                    'message': 'District Saved Successfully'
                }
                return Response(response_data, status.HTTP_201_CREATED)
            else:
                response_data = {
                    'status': 'failed',
                    'error': serialized.errors
                }
                return Response(response_data, status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response_data = {
                'status': 'failed',
                'error': str(e)
            }
            return Response(response_data, status.HTTP_500_INTERNAL_SERVER_ERROR)


