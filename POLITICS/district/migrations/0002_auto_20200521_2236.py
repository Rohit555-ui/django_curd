# Generated by Django 3.0.5 on 2020-05-21 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('district', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='district',
            old_name='state_id',
            new_name='state',
        ),
    ]
