from rest_framework import serializers
from django.apps import apps
from .models import *

states_model = apps.get_model('states', 'States')
country_model = apps.get_model('country', 'Country')


class VedioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class FrameworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Framework
        fields = '__all__'


class StudentSerializerMS(serializers.ModelSerializer):
    class Meta:
        model = Student
        # it fetches all keys from request and matches to model fields
        fields = ('name', 'address', 'roll_no', 'student_category', 'student_weight', 'student_height')


class StudentSerializerS(serializers.Serializer):
    name = serializers.CharField(max_length=100, required=True)
    address = serializers.CharField(max_length=100, required=True)
    roll_no = serializers.CharField(max_length=100, required=True)
    student_category = serializers.CharField(max_length=100, required=True)


class CountryViewSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = country_model
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'name']


class FrameworkSerializer(serializers.ModelSerializer):
    language = LanguageSerializer()

    class Meta:
        model = Framework
        fields = ['id', 'name', 'language']


class CountrySerializer(serializers.Serializer):
    name = serializers.CharField(required=True, allow_null=False)
    country_id = serializers.CharField(required=True, allow_null=False)


# class CountryViewSetSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=2)
#     country_id = serializers.CharField(max_length=5)


class uploadFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = ('name', 'address', 'image')


class TestSerializers(serializers.Serializer):
    name = serializers.CharField(required=True)
    address = serializers.CharField(required=True)


class TestingSerializer(serializers.Serializer):
    value = serializers.FloatField(required=True)
    date_time = serializers.DateTimeField()


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
