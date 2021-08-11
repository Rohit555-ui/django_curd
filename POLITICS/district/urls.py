# """config URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/3.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
from django.contrib import admin
from django.urls import path, include
from .views import *
from .filter_view import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'VS', CountryViewSet)
router.register(r'VSS', CountryViewSetOnly)
router.register(r'Language', CountryViewSetOnly)
router.register(r'TVS', TestViewSet, basename='testViewSet')
# router.register(r'hexam', Hexample, basename='Hexample')

urlpatterns = [
    path('View_Set/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('action', DistrictAction.as_view()),
    path('test', test_action.as_view()),
    path('uploadFile', uploadFile),
    path('query_testing', query_testing),
    path('query_many_to_many', query_many_to_many),
    path('testm', test_model),
    path('oneToMany', one_to_many),
    path('manyToMany', many_to_many),
    path('student', StudentDetails.as_view()),
    path('model1', Model1Post.as_view()),
    path('hexam/', Hexample.as_view()),
    path('all_m/', all_m.as_view()),
    path('all_m/<int:pk>', all_m.as_view()),
    path('studentm', StudentDetailsMixin.as_view()),
    path('DCBV/', DjangoBaseView.as_view()),
    # either we can pass template name here or we define template name in view class like DTVWOP
    path('DTVWOP', TemplateView.as_view(template_name='TemplateViews/template_view.html'), name='DTVWOP'),
    path('DTVWP', DjangoTemplateViewWithParameters.as_view(), name='DTVWP'),
    path('DRV', DjangoRedirectView.as_view()),
    path('DLV', DjangoListView.as_view()),
    path('ApiViewExample', ApiViewExample.as_view()),
    path('ApiViewExample/<int:id>', ApiViewExample.as_view()),
    path('CreateApiViewExample', CreateApiViewExample.as_view()),
    path('ListApiViewExample', ListApiViewExample.as_view()),
    path('ListApiViewExample/<int:id>', ListApiViewExample.as_view()),
    path('FilterByUrl/<str:name>', FilterByUrlParam.as_view()),
    path('FilterByQueryParams', FilterByQueryParams.as_view()),
    path('GenericFilter', GenericFilter.as_view()),
    path('StudentExSerView', StudentExSerView.as_view()),
    path('StudentHistoryView', StudentHistoryView.as_view()),
    path('celery_exam', CeleryClassView.as_view()),
    path('celery_exam', CeleryClassView.as_view()),
    path('Dview', Dview.as_view()),
]
