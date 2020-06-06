from django.db import models


class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    country_id = models.CharField(max_length=100, blank=False)
    time_stamp = models.DateTimeField()

    class Meta:
        db_table = 'country'


class PMs(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    pm_id = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(max_length=5, blank=False)
    party = models.CharField(max_length=100, blank=False)
    country = models.ForeignKey('country.Country', default=None, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField()

    class Meta:
        db_table = 'pms'


