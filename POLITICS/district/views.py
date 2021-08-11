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

states_model = apps.get_model('states', 'States')
country_model = apps.get_model('country', 'Country')

from rest_framework import viewsets, mixins
from .permmissions import IsCrudAdmin, IsNameRohit
from rest_framework import generics

from django.views import View

class CeleryClassView(APIView):
    def get(self, request):
        from .tasks import add
        add.delay(x=5, y=10)
        return Response("success")

    def post(self, request):
        from .tasks import post_add
        post_add.delay(a=5, b=10)
        return Response("success")


class DjangoBaseView(View):
    def get(self, request):
        context = {
            'aa': 'rohit'
        }
        return HttpResponse(context)
        # return render(request, 'country/allCountry.html', context)


class DjangoTemplateViewWithParameters(TemplateView):
    template_name = 'TemplateViews/template_view_param.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'rohit kumar'
        return context


class DjangoRedirectView(RedirectView):
    # url = 'DTVWP'
    pattern_name = 'DTVWOP'
    # either it should be redireted acc. to given url or pattern_name(given name in url mapping)

class ApiViewExample(APIView):
    def get(self, request, id, *args, **kwargs):
        print(args)
        print(kwargs)
        print(id)
        return Response(request.query_params)
    def post(self, request, *args, **kwargs):
        print(args)
        print(kwargs)
        return Response(request.data)
    def put(self, request, id, *args, **kwargs):
        print(args)
        print(kwargs)
        print(id)
        return Response(request.data)
    def delete(self, request, id, *args, **kwargs):
        print(args)
        print(kwargs)
        print(id)
        return Response(request.data)

class CreateApiViewExample(CreateAPIView):
    # As CreateAPIView is used for creating model instance but get, post, put, delete method may be used inside this bcoz it extends APIView class and that class has all methods
    def post(self, request, *args, **kwargs):
        return Response(request.data)
    def get(self, request, *args, **kwargs):
        return Response(request.query_params)

class ListApiViewExample(APIView):
    serializer_class = StudentSerializerS
    # queryset = Student.objects.all()

    def get(self, request, *args, **kwargs):
        s = Student.objects.all()
        context={
            'with_name': False,
            'with_address': True
        }
        return Response(StudentSerializerS(s, many=True, context=context).data)
        print(kwargs)
        if 'id' in kwargs:
            return StudentSerializerS(self.queryset.filter(id=kwargs['id'])).data
        return self.list(request, *args, **kwargs)
        

class DjangoListView(ListView):
    # it will search by default modelname_list.html file in app_name directory in templates folder
    model = Language
    # we can change by default html file name
    template_name = 'district/language.html'

    # if we want to pass list of model object after filtering
    def get_queryset(self):
        query_set = Framework.objects.filter()
        return query_set


class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountryViewSetSerializer
    queryset = country_model.objects.all()
    lookup_field = 'country_id'

    def list(self, request, *args, **kwargs):
        return Response("hefuufddhfusd")

    def create(self, request, *args, **kwargs):
        return Response("create method is called")

class all_m(generics.ListAPIView):
    queryset = Model1.objects.all()
    serializer_class = Allm
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'name1']

class Hexample(APIView):
    # serilizer_class = TestSerializers
    # queryset = Testing.objects.all()

    def post(self, request, *args, **kwargs):
        # return Response("inside")
        request_data = request.data
        serialized_data = TestSerializers(data=request_data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response("success")
        else:
            return Response(serialized_data.errors)

class StudentExSerView(APIView):
    def post(self, request):
        from .serializers import StudentSerEx
        ser  = StudentSerEx(data=request.data)

        if ser.is_valid(raise_exception=True):
            # print(ser.validated_data)
            ser.save()
            # print(ser.data)
            return Response("Success")

class StudentHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        s = Student.objects.create(name='student1122', address='address1122')
        return Response("saved")



class TestModelViewSet(viewsets.ModelViewSet):
    try:
        queryset = Student.objects.all()
        serializer_class = StudentSerializerMS
        lookup_field = 'roll_no'

        def list(self, request, *args, **kwargs):
            return Response(self.lookup_field)

        def create(self, request, *args, **kwargs):
            return Response("create method is called")

    except Exception as e:
        print(str(e))


# @permission_classes((IsAuthenticated,))
class TestViewSet(viewsets.ViewSet):
    # logger = logging.getLogger(__name__)

    def create(self, request):
        request_data = request.data
        language_obj = Language.objects.get(id=13)
        request_data['language'] = {
            'id': language_obj.id, 'name': language_obj.name
        }
        framework_serilized = FrameworkSerializer(data=request_data)
        if framework_serilized.is_valid(raise_exception=True):
            framework_serilized.save()
            return Response("Saved Successfully")

    # calling class object so __init__ and __call__  are getting called
    @DecorClass
    def list(self, request):
        try:
            check1_m = Check1.objects.filter(id=1).first()
            # check1_m.name1 = "check1_name"
            # check1_m.save()

            check2_m = Check2()
            check2_m.name2 = "check2_name"
            check2_m.check1 = check1_m
            check2_m.save()
            m5 = Model5()
            m5.fload_number = 100.7878
            m5.decimal_number = 120.21212
            m5.save()
            query_set1 = District.objects.filter(state__name='UP').select_related('state__country')
            # for i in query_set1:
            #     print("country name is = "+str(i.state.country.name)+" and state name is = "+str(i.state.name)+" and district is = "+str(i.name))
            # query_set1 = Language.objects.filter(id=12)
            # query_set1 = Framework.objects.filter(language__name='PHP', name='CakePHP')
            # for i in query_set1:
            #     print(i.language.name)
            # query_set1 = Model4.objects.filter(modeldata__isnull=True)
            # query_set1 = Language.objects.prefetch_related('lan_frame')
            # for i in query_set1:
            #     cc = i.lan_frame.all()
            #     for j in cc:
            #         print(j.name)
            # query_set1 = Framework.objects.all()
            # for i in query_set1:
            #     print("language is = "+str(i.name))
            #     print("framework is = "+str(i.language.name))
            print(connection.queries)
            return Response(str(query_set1.query))
            # query_set = Model3.objects.select_related('model1', 'model2')
            # return Response(str(query_set.query))
            # result = []
            # all_language_data = Language.objects.prefetch_related('lan_frame')
            # for lang_obj in all_language_data:
            #     current_lang_data = {}
            #     related_frameworks_queryset = lang_obj.lan_frame.all()
            #     current_lang_data['language_name'] = lang_obj.name
            #     current_lang_frames = []
            #     if related_frameworks_queryset.exists():
            #         for rel_frame_obj in related_frameworks_queryset:
            #             current_lang_frames.append(rel_frame_obj.name)
            #         current_lang_data['frameworks'] = current_lang_frames
            #     else:
            #         current_lang_data['frameworks'] = current_lang_frames
            #     result.append(current_lang_data)
            # return Response(result, status.HTTP_200_OK)
        except NotFound as e:
            raise NotFound("not found catched")
        except Exception as e:
            # self.logger.error("Exception occured is = " + str(e))
            raise APIException(e)


class CountryViewSetOnly(viewsets.ViewSet):
    queryset = country_model.objects.all()
    # permission_classes = [IsAuthenticated & IsCrudAdmin]
    permission_classes = [IsNameRohit]

    # lookup_field = 'country_id'

    def list(self, request):
        query_set = country_model.objects.all()
        # query_set = get_object_or_404(query_set, id=1)
        serialized_data = CountryViewSetSerializer(query_set, many=True)
        return Response(serialized_data.data)

    @swagger_auto_schema(
        operation_description='Add New Country',
        request_body=CountryViewSetSerializer,
        responses={
            status.HTTP_200_OK: 'OK',
            status.HTTP_401_UNAUTHORIZED: 'Unauthorized',
            status.HTTP_403_FORBIDDEN: 'Forbidden',
        }
    )
    def create(self, request):
        # CountrySerializer
        request_data = request.data
        serialized = CountryViewSetSerializer(data=request_data)
        if serialized.is_valid():
            country_name = serialized.data['name']
            country_id = serialized.data['country_id']
            print(country_name, country_id)
            return Response("success")
        else:
            # return Response(serialized.errors)
            raise serializers.ValidationError("authentication failed", status.HTTP_401_UNAUTHORIZED)

    def update(self, request, pk=None):
        return Response(str(pk))

    def destroy(self, request, pk=None):
        return Response(str(pk))

    def retrieve(self, request, pk=None):
        return Response("retrieve")


class test_action(mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  generics.GenericAPIView):
    serializer_class = TestSerializers
    queryset = TestModel.objects.all()
    lookup_field = 'name'

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


@api_view(['POST', 'GET', 'DELETE'])
def many_to_many(request):
    if request.method == 'POST':
        try:
            request_data = request.data
            student_name = request_data['student_name']
            course_name = request_data['course_name']

            check_student_entry = Student.objects.filter(name=student_name)
            if check_student_entry.exists():
                print("Student already present = " + str(student_name))
                student_obj = check_student_entry[0]
            else:
                print("Student created = " + str(student_name))
                student_obj = Student(name=student_name)
                student_obj.save()

            check_course_entry = Courses.objects.filter(name=course_name)
            if check_course_entry.exists():
                print("Course already present = " + str(course_name))
                course_obj = check_course_entry[0]
            else:
                print("Course created = " + str(course_name))
                course_obj = Courses(name=course_name)
                course_obj.save()

            course_obj.student.add(student_obj)

            return Response("saved successfully")
        except Exception as e:
            return Response(str(e))
    elif request.method == 'GET':
        try:
            test_query = Framework.objects.filter(language_id=11).first()
            # if test_query:
            #     print(test_query.query)
            # student_obj = Student.objects.get(id=27)
            # query_set1 = Courses.objects.prefetch_related('student')
            query_set1 = Courses.objects.prefetch_related("student")
            # for qs in query_set1:
            #     print("----------------")
            #     print(qs.name)
            #     all_students = qs.student.all()
            #     for student_obj in all_students:
            #         print(student_obj.name)
            # print(str(connection.queries))

            # test_query_set = Framework.objects.filter(language__name='PHP')
            # test_query_set = Framework.objects.filter(language__isnull=False).select_related('language')
            test_query_set = Language.objects.filter(framework__isnull=False)
            # print(test_query_set.language.name)
            # for i in test_query_set:
            #     print(i.language.name)
            print(str(connection.queries))
            return Response(str(test_query_set.query))
            return Response(str(connection.queries))
        except Exception as e:
            return Response(str(e))
    elif request.method == 'DELETE':
        try:
            all_student = Student.objects.all()
            all_student.delete()

            all_course = Courses.objects.all()
            all_course.delete()
            return Response("Delete Successfully")
        except Exception as e:
            return Response(str(e))

def test():
    l = 0
    from django.db import connection
    s = Student.objects.filter()
    for so in s:
        c = so.course.all()
        print(c)
    print(connection.queries)
    l = len(connection.queries)
    print(l)


class StudentDetailsMixin(mixins.CreateModelMixin,
                          mixins.DestroyModelMixin,
                          mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializerMS
    lookup_field = 'roll_no'

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class Model1Post(APIView):
    def post(self, request):
        ser = Model1Serializer(data=request.data)

        if ser.is_valid():
            print(ser.validated_data)
            print(ser.data)
            # ser.save()
            print(ser.validated_data)
            return Response("saved")
        else:
            return Response(ser.errors)

    def put(self, request):
        ins = Model1.objects.filter(name=request.data.get('name')).first()
        ser = Model1Serializer(ins,data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            print(ser.validated_data)
            print(ser.data)
            return Response("saved")
        else:
            return Response(ser.errors)

class StudentDetails(APIView):
    def get(self, request):
        all_student = Student.objects.all()
        if all_student.exists():
            serialized_students = StudentSerializerS(all_student, many=True, context={'course_count': False})
            return Response(serialized_students.data, status.HTTP_200_OK)
        else:
            return Response({'message': 'Student Data Not Available'}, status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        request_data = request.data
        serialized = StudentSerializerS(data=request_data)

        if serialized.is_valid():
            print(serialized.validated_data)
            student_object = Student()
            student_object.name = request_data['name']
            student_object.address = request_data['address']
            student_object.roll_no = request_data['roll_no']
            student_object.student_category = request_data['student_category']

            student_object.save()
            return Response(request_data, status.HTTP_201_CREATED)

        else:
            return Response(serialized.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
def one_to_many(request):
    if request.method == 'POST':
        try:
            python = Language()
            python.name = 'PHP'
            python.save()

            frame_work_obj = Framework()
            frame_work_obj.name = 'CakePHP'
            frame_work_obj.language = python
            frame_work_obj.save()

            frame_work_obj = Framework()
            frame_work_obj.name = 'yii'
            frame_work_obj.language = python
            frame_work_obj.save()

            frame_work_obj = Framework()
            frame_work_obj.name = 'Codignitor'
            frame_work_obj.language = python
            frame_work_obj.save()
            return Response("Language and Framework have been created")
        except Exception as e:
            return Response(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'DELETE':
        all_language = Courses.objects.all()
        all_language.delete()
        return Response("deleted successfully")
    elif request.method == 'GET':
        custom = 0
        if custom == 0:
            test_list = []
            # refer link
            # https://books.agiliq.com/projects/django-orm-cookbook/en/latest/truncate.html
            all_data_no_condition = Framework.objects.all()
            # or all_data_no_condition = Framework.objects.filter()
            or_condition = Framework.objects.filter(Q(name__startswith='C') | Q(name__endswith='o'))

            # or_condition = Framework.objects.filter(Q(name__startswith='C') | Q(name__endswith='o'))
            and_condition = Framework.objects.filter(Q(name__startswith='D') & Q(language_id=11))
            not_condition_first = Framework.objects.filter(~Q(name__startswith='D'))
            not_condition_second = Framework.objects.filter(id=10).exclude(Q(name__startswith='D'))

            query_set_1 = Framework.objects.filter(Q(id=3))
            query_set_2 = Framework.objects.filter(Q(id=4))
            union_condition = query_set_1.union(query_set_2)

            values_some_field_without_cond = Framework.objects.values("name")
            values_some_field_fetch_cond = Framework.objects.filter(id=4).values("name")
            only_some_field_fetch_cond = Framework.objects.filter(id=4).only("name")

            language_filter_cond = Language.objects.filter(name="PHP")
            # subquery_condition = Framework.objects.filter(
            #     Q(language_id__in=Subquery(language_filter_cond.values("id"))))

            greater_than_condition = Framework.objects.filter(id__gt=5)
            greater_than_equal_condition = Framework.objects.filter(id__gte=5)

            less_than_condition = Framework.objects.filter(id__lt=5)
            less_than_equal_condition = Framework.objects.filter(id__lte=5)

            inner_join_select_related = Framework.objects.select_related("language")
            inner_join_filter = Framework.objects.filter(language__name='PHP')

            inner_join_condition = Framework.objects.prefetch_related('name').all()
            inner_join_condition_extra = Framework.objects.filter(language_id=11).select_related('language')

            test_query = Framework.objects.select_related('language')
            test_query1 = Framework.objects.all()

            order_by_all = Framework.objects.order_by('-id')
            order_by_filter = Framework.objects.filter(language_id=11).order_by('-id')

            seconds_largest_id = Framework.objects.order_by('-id')[1]

            # distinct_language_id = Framework.objects.distinct('language_id').all()

            # aggregate functions returns dictionary
            max_id_dict = Framework.objects.aggregate(Max('id'))
            min_id_dict = Framework.objects.aggregate(Min('id'))
            avg_id_dict = Framework.objects.aggregate(Avg('id'))
            sum_id_dict = Framework.objects.aggregate(Sum('id'))
            # print(sum_id_dict)

            # Between two values queryset and null example
            between_queryset = Framework.objects.filter(~Q(name__isnull=True) & Q(id__range=(1, 9)))

            # for i in inner_join_filter:
            #     language_dict = {
            #         'frame_work_name': i.name,
            #         'language_name': i.language.name
            #     }
            #     test_list.append(language_dict)
            # print(connection.queries)
            # return Response(sum_id_dict)
            test_query_set = LanguageMaker.objects.select_related('framework__language').order_by('-id')
            group_by_set = Framework.objects.aggregate(Sum('id'))
            annotate_query_set = Framework.objects.values('language').annotate(sum=Count('language'), max=Max('id'))
            tt = Framework.objects.values('name', 'language')
            print(tt)
            # for i in test_query_set:
            #     print(i.name)
            #     print(i.framework.name)
            #     print(i.framework.language.name)
            q2 = Language.objects.order_by('-id')[:3]
            return Response(str(q2.query))
            # return Response(or_condition)
        elif custom == 1:
            l1 = Language()
            q1 = l1.get_all_language()
            return Response(str(q1.query))
            # curr_obj = connection.cursor()
            # query = """SELECT * FROM framework AS T1 INNER JOIN language AS T2 ON T1.language_id=T2.id"""
            # df = pd.read_sql(query, con=connection)
            # print(df)
            # return Response(df)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def test_model(request):
    if request.method == 'POST':
        self_obj = SelfExample()
        self_obj.name = 'A'
        self_obj.address = 'a'
        self_obj.parent = None
        self_obj.save()
        return Response("Inserted")
    elif request.method == 'GET':
        logger = logging.getLogger(__name__)
        try:
            a = 1 / 0
        except Exception as e:
            logger.error("error logging in except field!!!!")
        return Response("Logging Testing")
        result = []
        #
        # self_query = SelfExample.objects.select_related('parent')
        # test_query_query = Testing1.objects.select_related('dhuhdu')
        # left_join_query = Testing.objects.filter(testing1__isnull=True)
        # # for i in test_query_query:
        # #     print(i.dhuhdu.name)
        # # print(str(connection.queries))
        # return Response(str(left_join_query.query))
        # query_set = Framework.objects.select_related('language')
        # serialized_data = FrameworkSerializer(query_set, many=True)
        # return Response({
        #     'data': serialized_data.data
        # })


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def uploadFile(request):
    if request.method == 'GET':
        query_set = TestModel.objects.all().values('image.url')
        return Response(query_set, content_type='*/*')
    if request.method == 'POST':
        requested_data = request.data
        serialized_data = uploadFileSerializer(data=requested_data)
        if serialized_data.is_valid():
            test_model_obj = TestModel()
            test_model_obj.name = requested_data['name']
            test_model_obj.address = requested_data['address']
            test_model_obj.image = requested_data['image']
            serialized_data.save()
            return Response({'data': serialized_data.data}, status.HTTP_200_OK)
        else:
            return Response({'error': serialized_data.errors}, status.HTTP_201_CREATED)


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
            return Response(str(request_data['image']))
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

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def query_testing(request):
    from django.db import connection
    # for forward fourign key
    # f = Framework.objects.all().select_related("language")

    # for reverse fourign key
    l = Language.objects.all().prefetch_related("framework_set")
    for i in l:
        print(i.name, i.framework_set.all())

    print(connection.queries)
    l=len(connection.queries)
    print(f"nof of queries: {l}")
    return Response({"status": "success"}, status.HTTP_200_OK)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def query_many_to_many(request):
    from django.db import connection
    # s = Student.objects.all().prefetch_related("course")
    s = Courses.objects.all().prefetch_related("student_set")
    for i in s:
        print(i.student_set.all())
    # from IPython.core.debugger import Tracer
    # Tracer()()

    print(connection.queries)
    l=len(connection.queries)
    print(f"nof of queries: {l}")
    return Response({"status": "success"}, status.HTTP_200_OK)


class Dview(ListView):
    model = Student
    template_name = 
    def get(self, request):
        data_dict = {
            "name": "rohit",
            "age": "24"
        }
        return render(request, 'country/allCountry.html', data_dict)





















































