from rest_framework import serializers
from .models import States
from django.apps import apps
country_model = apps.get_model('country', 'Country')


class StatesUpdateSerializers(serializers.Serializer):
    state_name = serializers.CharField(required=True)
    time_stamp = serializers.DateTimeField(required=True)
    state_id = serializers.CharField(required=True)
    country_id = serializers.CharField(required=True)

    def validate(self, attrs):
        state_id = attrs.get('state_id', None)
        country_id = attrs.get('country_id', None)
        try:
            check_state_data = States.objects.get(state_id=state_id)
        except Exception as e:
            raise serializers.ValidationError("No state exist of this state id")
        state_table_id = check_state_data.id

        try:
            check_country_data = country_model.objects.get(country_id=country_id)
        except Exception as e:
            raise serializers.ValidationError("No country exist of this country id")
        country_table_id = check_country_data.id

        try:
            check_state_mapping = States.objects.get(id=state_table_id, country_id=country_table_id)
        except Exception as e:
            raise serializers.ValidationError("Country, State mapping is incorrect")

        attrs['state_table_id'] = state_table_id

        return attrs


class StatesSerializers(serializers.Serializer):
    name = serializers.CharField(required=True)
    time_stamp = serializers.DateTimeField(required=True)
    country_name = serializers.CharField(required=True)

    def validate(self, attrs):
        country_name = attrs.get('country_name', None)
        state_name = attrs.get('name', None)
        try:
            check_country_data = country_model.objects.get(name=country_name)
        except Exception as e:
            raise serializers.ValidationError("Incorrect country name passed")
        check_state = States.objects.filter(name=state_name, country_id=check_country_data.id)
        if check_state.exists():
            raise serializers.ValidationError("This State already exists in this country")
        attrs['country'] = check_country_data

        return attrs

# we add meta class in serializer(ser..Modelser..) so it checks fields only for model which is passed

