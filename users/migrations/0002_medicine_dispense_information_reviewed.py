# Generated by Django 4.1.7 on 2023-06-21 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine_dispense_information',
            name='reviewed',
            field=models.BooleanField(default=False),
        ),
    ]
