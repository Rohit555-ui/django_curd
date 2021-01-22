from django.db import models


class States(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    state_id = models.CharField(max_length=100, blank=False)
    time_stamp = models.DateTimeField()
    country = models.ForeignKey('country.Country', on_delete=models.CASCADE)

    class Meta:
        db_table = 'states'
