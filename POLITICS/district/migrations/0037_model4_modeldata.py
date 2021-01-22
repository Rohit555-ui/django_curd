# Generated by Django 3.1.1 on 2020-11-26 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('district', '0036_auto_20201120_1233'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'model4',
            },
        ),
        migrations.CreateModel(
            name='ModelData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('model4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='district.model4')),
            ],
            options={
                'db_table': 'model_data',
            },
        ),
    ]
