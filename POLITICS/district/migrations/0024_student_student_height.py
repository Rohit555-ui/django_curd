# Generated by Django 3.0.5 on 2020-09-17 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('district', '0023_auto_20200917_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_height',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
