# Generated by Django 3.2.16 on 2022-10-19 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helsings_school', '0005_auto_20221019_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='registered',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='registered',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
