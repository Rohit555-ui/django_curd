from django.db import models
from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
from .signals import (
    process_after_pm_insert, process_before_pm_delete, process_after_country_insert, process_after_country_delete
)


class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    country_id = models.CharField(max_length=100, blank=False)
    time_stamp = models.DateTimeField(null=True)

    class Meta:
        db_table = 'country'


class CountryHistory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    country_id = models.CharField(max_length=100, blank=False)
    country_status = models.CharField(max_length=100, blank=False)
    time_stamp = models.DateTimeField()

    class Meta:
        db_table = 'country_history'


class PMs(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    pm_id = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(blank=False)
    party = models.CharField(max_length=100, blank=False)
    country = models.ForeignKey('country.Country', default=None, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField()

    class Meta:
        db_table = 'pms'


class PMsHistory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    pm_id = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(blank=False)
    party = models.CharField(max_length=100, blank=False)
    country_id = models.IntegerField(blank=False)
    time_stamp = models.DateTimeField()
    status = models.CharField(max_length=100, blank=False)

    class Meta:
        db_table = 'pms_history'


pre_delete.connect(receiver=process_before_pm_delete, sender=PMs)
post_save.connect(receiver=process_after_pm_insert, sender=PMs)
post_save.connect(receiver=process_after_country_insert, sender=Country)
post_delete.connect(receiver=process_after_country_delete, sender=Country)
