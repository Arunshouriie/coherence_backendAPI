# Generated by Django 4.1.7 on 2023-06-21 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_medicine_dispense_information_reviewed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicine_dispense_information',
            old_name='reviewed',
            new_name='video_review',
        ),
        migrations.AddField(
            model_name='medicine_dispense_information',
            name='points',
            field=models.IntegerField(default=-1),
        ),
    ]
