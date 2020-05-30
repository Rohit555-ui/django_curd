from rest_framework import serializers
from django.apps import apps
from .models import *
states_model = apps.get_model('states', 'States')


class DistrictPostSerializers(serializers.Serializer):
    name = serializers.CharField(required=True)
    state_id = serializers.CharField(required=True)
    time_stamp = serializers.DateTimeField(required=True)

    def validate(self, attrs):
        name = attrs.get('name', None)
        state_id = attrs.get('state_id', None)

        try:
            check_state_data = states_model.objects.get(state_id=state_id)
        except Exception as e:
            raise serializers.ValidationError('This State does not exist')

        check_district_state_mapping = District.objects.filter(name=name, state_id=check_state_data.id)
        if check_district_state_mapping.exists():
            raise serializers.ValidationError('This district already exists in this state')

        attrs['state_table_id'] = check_state_data.id

        return attrs


