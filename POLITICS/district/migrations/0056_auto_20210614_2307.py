# Generated by Django 3.1.7 on 2021-06-14 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('district', '0055_auto_20210528_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='framework',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='district.language'),
        ),
    ]
