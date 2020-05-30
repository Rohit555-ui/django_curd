from django.db import models
from django.db.models.signals import post_save, pre_save
from .signals import *


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


def b_save(sender, instance, **kwargs):
    print("b save is calling")


def a_save(sender, instance, **kwargs):
    print("a save is calling")


post_save.connect(receiver=a_save, sender=District)
pre_save.connect(receiver=b_save, sender=District)




