# Generated by Django 3.0.5 on 2020-05-03 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('state_id', models.CharField(max_length=100)),
                ('state_id2', models.CharField(max_length=100)),
                ('time_stamp', models.DateTimeField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='country.Country')),
            ],
            options={
                'db_table': 'states',
            },
        ),
    ]