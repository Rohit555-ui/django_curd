from django.db import models


class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    country_id = models.CharField(max_length=100, blank=False)
    time_stamp = models.DateTimeField()

    class Meta:
        db_table = 'country'






