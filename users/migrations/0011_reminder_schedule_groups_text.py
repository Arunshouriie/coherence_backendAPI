# Generated by Django 4.1.7 on 2023-06-22 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_user_info_dosage_time1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reminder_schedule_groups',
            name='text',
            field=models.BooleanField(default=False),
        ),
    ]
