# Generated by Django 3.2.16 on 2022-10-19 11:58

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helsings_school', '0006_auto_20221019_1450'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='registered',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
