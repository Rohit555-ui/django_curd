# Generated by Django 3.0.8 on 2021-02-16 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('district', '0044_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='videofile',
            field=models.FileField(null=True, upload_to='media/video/', verbose_name=''),
        ),
    ]
