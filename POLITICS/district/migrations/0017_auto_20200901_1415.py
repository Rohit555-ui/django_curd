# Generated by Django 3.0.5 on 2020-09-01 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('district', '0016_auto_20200901_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(max_length=100),
        ),
    ]
