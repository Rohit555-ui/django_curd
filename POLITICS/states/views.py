from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import StatesSerializers, StatesUpdateSerializers
from rest_framework.response import Response
from .models import States
import random
import string
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from django.apps import apps
country_model = apps.get_model('country', 'Country')


class StatesAction(APIView):
    def delete(self, request):
        try:
            request_data = request.data
            state_id = request_data.get('state_id', None)
            if state_id is not None:
                check_states = States.objects.filter(state_id=state_id)
                if check_states.exists():
                    check_states.delete()
                    response_data = {
                        'message': 'States Deleted Successfully',
                        'error': 'No error'
                    }
                    return Response(response_data, status.HTTP_200_OK)
                else:
                    response_data = {
                        'message': 'States Not Deleted',
                        'error': 'No state of this state id'
                    }
                    return Response(response_data, status.HTTP_400_BAD_REQUEST)
            else:
                response_data = {
                    'message': 'States Not Deleted',
                    'error': 'State_id is required'
                }
                return Response(response_data, status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response_data = {
                'message': 'States Not Deleted',
                'error': str(e)
            }
            return Response(response_data, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        try:
            request_data = request.data
            serialized = StatesUpdateSerializers(data=request_data)
            if serialized.is_valid():
                random_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
                state_name = serialized.data['state_name']
                time_stamp = serialized.data['time_stamp']
                new_state_id = state_name + "_" + str(random_id)
                state_table_id = serialized.validated_data['state_table_id']
                get_state_data = States.objects.filter(id=state_table_id)
                get_state_data.update(name=state_name, state_id=new_state_id, time_stamp=time_stamp)
                # update will work for data filterd by filter method not by get
                response_data = {
                    'message': 'State Details Updated Successfully',
                    'data': request_data
                }
                return Response(response_data, status.HTTP_200_OK)
            else:
                return Response(serialized.errors, status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response_data = {
                'message': 'State Details Not Updated',
                'error': str(e)
            }
            return Response(response_data, status.HTTP_200_OK)

    def get(self, request):
        # all_states_data = States.objects.values(id=1)
        # this values method converts query set into dictionary and send it directly
        final_data = []
        all_states = States.objects.all().order_by('-time_stamp')
        print(str(all_states.query))
        for state_obj in all_states:
            current_dict_obj = {
                'state_name': state_obj.name,
                'state_creation_time': state_obj.time_stamp,
                'country_name': state_obj.country.name
            }
            final_data.append(current_dict_obj)

        return Response(final_data, status.HTTP_200_OK)

    def post(self, request):
        request_data = request.data
        serialized = StatesSerializers(data=request_data)
        if serialized.is_valid():
            validated_country_data_dict = serialized.validated_data['country']
            country_id = int(validated_country_data_dict.id)
            random_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            state_name = request_data['name']
            time_stamp = request_data['time_stamp']
            state_id = str(state_name) + "_" + str(random_id)
            new_state = States.objects.create(
                name=state_name,
                state_id=state_id,
                country_id=country_id,
                time_stamp=time_stamp
            )
            new_state.save()
            response_data = {
                'message': 'New State Created Successfully',
                'data': request_data
            }
            return Response(response_data, status.HTTP_201_CREATED)
        else:
            return Response(serialized.errors, status.HTTP_400_BAD_REQUEST)