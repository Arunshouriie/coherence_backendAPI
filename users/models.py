from datetime import datetime
from email.policy import default
from operator import truediv
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
import uuid
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail 


GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
class User(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
    
    def __unicode__(self):
        return self.user_name

class user_info(models.Model):
    patient_id = models.ForeignKey('User',blank=True, null=True, on_delete=models.CASCADE)
    # uuid = models.ForeignKey('User', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    dob = models.DateField(max_length=8, blank=True, null=True)
    trial_enrollment_date = models.DateField(max_length=8, blank=True, null=True)
    age = models.IntegerField()
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.CharField(max_length=250, blank=True, null=True)
    contact_no = PhoneNumberField(blank=True, help_text='Contact phone number')
    email = models.CharField(max_length=50, blank=True, null=True)
    nominee_name = models.CharField(max_length=50, blank=True, null=True)
    nominee_mobile = PhoneNumberField(blank=True, help_text='nominee phone number')
    postal_code = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True, default= "")
    country = models.CharField(max_length=50, blank=True, null=True, default= "")
    current_clinician = models.CharField(max_length=50, blank=True, null=True, default= "")
    clinician_pic = models.ImageField(upload_to = 'images/', blank=True, default= "")
    diagnosis = models.CharField(max_length=250, blank=True, null=True, default= "")
    allergies = models.CharField(max_length=50, blank=True, null=True, default= "")
    medicine_name = models.CharField(max_length=50, blank=True, null=True, default= "")
    medicine_pic = models.ImageField(upload_to = 'images/', default= "", blank=True)
    dose_duration = models.IntegerField(default=-1)
    dose_per_day = models.IntegerField(default=-1)
    dosage_time1 = models.DateTimeField(default=datetime.now, blank=True)
    dosage_time2 = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    device_id = models.AutoField(primary_key=True, blank=True)

    class Meta:
        verbose_name = "User_profile"
        verbose_name_plural = "User_profiles"
    
    def __unicode__(self):
        return self.name


class provisioning(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    mac_id = models.CharField(max_length=25)
    public_ip = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = "device"
        verbose_name_plural = "devices"

class reminder_schedule_groups(models.Model):
    duration_in_mins = models.IntegerField(default=-1)
    recurring = models.IntegerField(default=-1)
    No_of_alarms_before_dispense = models.IntegerField(default=-1)
    No_of_alarms_after_dispense = models.IntegerField(default=-1)
    time_range_between_alarms = models.CharField(max_length=50)
    class Meta:
        verbose_name = "Reminder_schedule"
        verbose_name_plural = "Reminders"
    
    def __unicode__(self):
        return self.duration_in_mins

class dispense(models.Model):
    # # uuid = models.ForeignKey('User', on_delete=models.CASCADE)
    # dispense_medicine = models.BooleanField(default = False)
    # time_stamp = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    schedule_id = models.IntegerField(default=-1)
    dispense_time = models.DateTimeField(default=datetime.now)
    alarms_start_time = models.DateTimeField(default=datetime.now)
    alarms_end_time = models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = "Dispense"
        verbose_name_plural = "Dispense"

class reminder_schedule_audit(models.Model):
    id = models.AutoField(primary_key=True)
    dispense_id = models.IntegerField(default=-1)
    dispense_consumed = models.BooleanField(default=False)
    date_of_alarms = models.DateTimeField(default=datetime.now)
    alarm_count = models.IntegerField(default=-1)

    class Meta:
        verbose_name = "Reminder_Audit_schedule"
        verbose_name_plural = "Reminder_Audits"

class alarm_audit(models.Model):
    id = models.AutoField(primary_key=True)
    schedule_audit_id = models.IntegerField()
    alarm_number = models.IntegerField(default=-1)
    sent_time = models.IntegerField(default=-1)
    actual_time = models.IntegerField(default=-1)

    class Meta:
        verbose_name = "Alarm_Audit"
        verbose_name_plural = "Audits_Alarm"



class medicine_dispense_information(models.Model):
    dispense_id = models.AutoField(primary_key=True)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    dispense = models.BooleanField()
    dispense_time = models.DateTimeField(default=datetime.now)
    video_review = models.BooleanField(default=False)
    points = models.DecimalField(blank=True, null=True, max_digits=12, decimal_places=3)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    class Meta:
        verbose_name = "medicine_dispense"
        verbose_name_plural = "medicines"




@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )