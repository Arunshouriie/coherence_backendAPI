# Generated by Django 4.1.7 on 2023-06-21 12:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_medicine_dispense_information_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine_dispense_information',
            name='dispense_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]