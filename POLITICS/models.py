# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class Country(models.Model):
    name = models.CharField(max_length=100)
    country_id = models.CharField(max_length=100)
    time_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class CountryHistory(models.Model):
    name = models.CharField(max_length=100)
    country_id = models.CharField(max_length=100)
    country_status = models.CharField(max_length=100)
    time_stamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'country_history'


class Courses(models.Model):
    name = models.CharField(unique=True, max_length=100)
    course_fee = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'courses'


class CoursesStudent(models.Model):
    courses = models.ForeignKey(Courses, models.DO_NOTHING)
    student = models.ForeignKey('Student', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'courses_student'
        unique_together = (('courses', 'student'),)


class District(models.Model):
    name = models.CharField(max_length=100)
    district_id = models.CharField(unique=True, max_length=100)
    time_stamp = models.DateTimeField()
    state = models.ForeignKey('States', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'district'


class DistrictHistory(models.Model):
    name = models.CharField(max_length=100)
    district_id = models.CharField(max_length=100)
    time_stamp = models.DateTimeField()
    status = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'district_history'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoCeleryResultsTaskresult(models.Model):
    task_id = models.CharField(unique=True, max_length=255)
    status = models.CharField(max_length=50)
    content_type = models.CharField(max_length=128)
    content_encoding = models.CharField(max_length=64)
    result = models.TextField(blank=True, null=True)
    date_done = models.DateTimeField()
    traceback = models.TextField(blank=True, null=True)
    meta = models.TextField(blank=True, null=True)
    task_args = models.TextField(blank=True, null=True)
    task_kwargs = models.TextField(blank=True, null=True)
    task_name = models.CharField(max_length=255, blank=True, null=True)
    worker = models.CharField(max_length=100, blank=True, null=True)
    date_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_celery_results_taskresult'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Framework(models.Model):
    name = models.CharField(max_length=10)
    language = models.ForeignKey('Language', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'framework'


class Language(models.Model):
    name = models.CharField(unique=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'language'


class Languagemaker(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    framework = models.ForeignKey(Framework, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'languagemaker'


class Pms(models.Model):
    name = models.CharField(max_length=100)
    pm_id = models.CharField(max_length=100)
    age = models.IntegerField()
    party = models.CharField(max_length=100)
    time_stamp = models.DateTimeField()
    country = models.ForeignKey(Country, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pms'


class PmsHistory(models.Model):
    name = models.CharField(max_length=100)
    pm_id = models.CharField(max_length=100)
    age = models.IntegerField()
    party = models.CharField(max_length=100)
    country_id = models.IntegerField()
    time_stamp = models.DateTimeField()
    status = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'pms_history'


class ReGenerate(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 're_generate'


class States(models.Model):
    name = models.CharField(max_length=100)
    state_id = models.CharField(max_length=100)
    time_stamp = models.DateTimeField()
    country = models.ForeignKey(Country, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'states'


class Student(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    roll_no = models.CharField(unique=True, max_length=100)
    student_category = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'student'


class TestModel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'test_model'


class TestModel1(models.Model):
    testmodel = models.OneToOneField(TestModel, models.DO_NOTHING, primary_key=True)
    name1 = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'test_model1'
