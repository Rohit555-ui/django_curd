from django.db import models
from django.db.models.signals import post_save, pre_save
from .signals import *
from simple_history.models import HistoricalRecords


class Model1(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    name1 = models.CharField(max_length=100, null=False, blank=False)
    name2 = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        db_table = 'model1'

class Model111(models.Model):
    name = models.CharField(max_length=100)


class Model555(models.Model):
    name = models.CharField(max_length=100)

class Model2(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'model2'


class Model3(models.Model):
    name = models.CharField(max_length=100, unique=True)
    model1 = models.ForeignKey(Model1, on_delete=models.CASCADE, null=True)
    model2 = models.ForeignKey(Model2, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'model3'


class Model4(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'model4'

class Model6(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'model6'


class Model5(models.Model):
    fload_number = models.FloatField(max_length=50)
    decimal_number = models.DecimalField(max_digits=50, decimal_places=2)

    class Meta:
        db_table = 'model5'


class ModelData(models.Model):
    name = models.CharField(max_length=100)
    model4 = models.ForeignKey(Model4, on_delete=models.CASCADE)

    class Meta:
        db_table = 'model_data'


class Check1(models.Model):
    name1 = models.CharField(max_length=100)

    class Meta:
        db_table = 'check1'


class Check2(models.Model):
    name2 = models.CharField(max_length=100)
    check1 = models.OneToOneField(Check1, on_delete=models.CASCADE)

    class Meta:
        db_table = 'check2'


class Courses(models.Model):
    name = models.CharField(max_length=100, unique=True)
    course_fee = models.IntegerField(null=False)

    class Meta:
        db_table = 'courses'


class Student(models.Model):
    # first entry of tuple in choises is to set value, seconds is for description of setting value
    category_values = (
        ('c1', 'c1'),
        ('c2', 'c2'),
        ('c3', 'c3'),
        ('c4', 'c4')
    )
    name = models.CharField(max_length=100, null=False, blank=False)
    course = models.ManyToManyField(Courses)
    address = models.CharField(max_length=100, null=False, blank=False)
    history = HistoricalRecords()
    class Meta:
        db_table = 'student'


class Language(models.Model):
    name = models.CharField(max_length=10, unique=True)

    class Meta:
        db_table = 'language'

    def get_all_language(self):
        return Language.objects.all()


class Framework(models.Model):
    name = models.CharField(max_length=10)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='lan_frame')

    class Meta:
        db_table = 'framework'


class LanguageMaker(models.Model):
    name = models.CharField(max_length=100)
    framework = models.ForeignKey(Framework, on_delete=models.CASCADE, default=None)
    address = models.CharField(max_length=100)

    class Meta:
        db_table = 'languagemaker'


class District(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    district_id = models.CharField(max_length=100, blank=False, unique=True)
    time_stamp = models.DateTimeField()
    state = models.ForeignKey('states.States', on_delete=models.CASCADE)

    class Meta:
        db_table = 'district'


class DistrictHistory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    district_id = models.CharField(max_length=100, blank=False)
    time_stamp = models.DateTimeField()
    status = models.CharField(max_length=200)

    class Meta:
        db_table = 'district_history'


class TestModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=100, blank=False)
    image = models.ImageField(blank=False, null=False, upload_to='static/country/images/')

    class Meta:
        db_table = 'test_model'


class TestModel1(models.Model):
    testmodel = models.OneToOneField(TestModel, on_delete=models.CASCADE, primary_key=True)
    name1 = models.CharField(max_length=100)

    class Meta:
        db_table = 'test_model1'


class Testing(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'testing'


class Testing1(models.Model):
    name = models.CharField(max_length=100)
    dhuhdu = models.ForeignKey(Testing, on_delete=models.CASCADE)

    class Meta:
        db_table = 'testing1'


class SelfExample(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'self_example'


def b_save(sender, instance, **kwargs):
    print("b save is calling")


def a_save(sender, instance, **kwargs):
    print("a save is calling")


post_save.connect(receiver=a_save, sender=District)
pre_save.connect(receiver=b_save, sender=District)
