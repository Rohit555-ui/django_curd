# Generated by Django 3.1.1 on 2020-11-19 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('district', '0032_auto_20201118_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='student',
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_course', to='district.courses'),
        ),
    ]
