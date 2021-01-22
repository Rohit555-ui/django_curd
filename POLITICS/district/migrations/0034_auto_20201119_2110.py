# Generated by Django 3.1.1 on 2020-11-19 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('district', '0033_auto_20201119_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ManyToManyField(null=True, related_name='student_course', to='district.Courses'),
        ),
    ]
