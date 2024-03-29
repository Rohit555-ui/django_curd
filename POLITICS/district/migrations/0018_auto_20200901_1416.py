# Generated by Django 3.0.5 on 2020-09-01 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('district', '0017_auto_20200901_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_fee',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_category',
            field=models.CharField(choices=[('General', 'Upper Caste'), ('Obc', 'Other Backword Class'), ('Sc', 'Scheduled Castes'), ('St', 'Scheduled Tribes')], max_length=100),
        ),
    ]
