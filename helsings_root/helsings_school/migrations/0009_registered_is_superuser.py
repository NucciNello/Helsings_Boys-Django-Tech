# Generated by Django 3.2.16 on 2022-10-19 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helsings_school', '0008_rename_user_name_registered_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='registered',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
