# Generated by Django 3.1.1 on 2020-11-26 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('district', '0038_auto_20201126_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='framework',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lan_frame', to='district.language'),
        ),
    ]