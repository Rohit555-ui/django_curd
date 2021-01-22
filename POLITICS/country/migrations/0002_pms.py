# Generated by Django 3.0.5 on 2020-06-03 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PMs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('pm_id', models.CharField(max_length=100)),
                ('age', models.IntegerField(max_length=5)),
                ('party', models.CharField(max_length=100)),
                ('time_stamp', models.DateTimeField()),
            ],
            options={
                'db_table': 'pms',
            },
        ),
    ]
