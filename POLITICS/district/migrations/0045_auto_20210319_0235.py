# Generated by Django 3.1.7 on 2021-03-19 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('district', '0044_auto_20210319_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.ManyToManyField(to='district.Courses'),
        ),
    ]