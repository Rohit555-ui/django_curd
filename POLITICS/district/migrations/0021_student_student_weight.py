# Generated by Django 3.0.5 on 2020-09-17 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('district', '0020_auto_20200906_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_weight',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
