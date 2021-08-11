from django.db.models.fields import CharField
from rest_framework import serializers
from django.apps import apps
# from typing_extensions import Required
from .models import *

states_model = apps.get_model('states', 'States')
country_model = apps.get_model('country', 'Country')


class Model1Serializer(serializers.ModelSerializer):
    name3 = serializers.CharField(max_length=100)
    class Meta:
        model = Model1
        fields = '__all__'

    def create(self, validated_data):
        # it will return instance of model
        return Model1.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     validated_data['name1'] = int(validated_data['name1']) * 2
    #     model1_obj = Model1.objects.filter(id=instance.id).update(**validated_data)
    #     return instance


class FrameworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Framework
        fields = '__all__'


class StudentSerializerMS(serializers.ModelSerializer):
    class Meta:
        model = Student
        # it fetches all keys from request and matches to model fields
        fields = ('name', 'address', 'roll_no', 'student_category', 'student_weight', 'student_height')

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ["id"]

class DynamicFieldSerializerMixin(object):
    dynamic_fields: dict = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, context_key in self.dynamic_fields.items():
            if not self.context.get(context_key):
                self.fields.pop(field_name)


class StudentSerializerS(DynamicFieldSerializerMixin, serializers.ModelSerializer):
    # name = serializers.CharField(max_length=100, required=True)
    # address = serializers.CharField(max_length=100, required=True)
    # # student_category = serializers.CharField(max_length=100, required=True)
    # course_name = serializers.SerializerMethodField('rohit')
    # above example of one of this example
    courses = CourseSerializer(read_only=True, many=True)
    dynamic_fields = {
        "name": "with_name",
        "address": "with_address"
    }

    no_of_course = serializers.SerializerMethodField()
    def get_no_of_course(self, obj):
        if self.context.get('course_count'):
            return obj.course.all().count()
        else:
            return None

    class Meta:
        model = Student
        fields = ["name", "address", "no_of_course", "courses", "value"]

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

class Allm(serializers.ModelSerializer):
    class Meta:
        model = Model1
        fields = ('name', 'name1', 'name2')


class TestSerializers(serializers.ModelSerializer):

    def create(self, validated_data):
        print("coming in create method")
        return Testing.objects.create(**validated_data)

    def get(self):
        queryset = Testing.objects.all()
        return queryset


    class Meta:
        model = Testing
        fields = ['name']

class StudentSerEx(serializers.ModelSerializer):
    address = serializers.CharField(required=False)
    course = serializers.IntegerField(required=False)

    def validate(self, data):
        print(data)
        return data
    class Meta:
        model = Student
        fields = '__all__'


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
