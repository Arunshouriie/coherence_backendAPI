from rest_framework import generics, permissions
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import  reminder_schedule_groups, dispense, reminder_schedule_audit, alarm_audit, provisioning, medicine_dispense_information, user_info, Capture_event

# User Serializer
# class UserSerializer(serializers.ModelSerializer):
    # class Meta:
        # model = User
        # fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

# User Serializer
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'email')

# Change Password
from rest_framework import serializers
from django.contrib.auth.models import User

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

# class user_profile_serializer(serializers.Serializer):
#     user_profile = serializers.ModelSerializer
#     class Meta:
#         model = user_profile
#         fields = '__all__'

class medicine_schedule_serializer(serializers.ModelSerializer):

    class Meta:
        model = reminder_schedule_groups
        fields = '__all__'

class provisionserializer(serializers.ModelSerializer):
    class Meta:
        model = provisioning
        fields = ('user_id', 'mac_id', 'public_ip')

class dispense_serializer(serializers.ModelSerializer):

    class Meta:
        model = dispense
        fields = '__all__'

class schedule_audit_serializer(serializers.ModelSerializer):

    class Meta:
        model = reminder_schedule_audit
        fields = '__all__'

class alarm_audit_serializer(serializers.ModelSerializer):

    class Meta:
        model = alarm_audit
        fields = '__all__'

class medicine_dispense_serializer(serializers.ModelSerializer):
    class Meta:
        model = medicine_dispense_information
        fields = '__all__'

class Capture_event_serializer(serializers.ModelSerializer):
    class Meta:
        model = Capture_event
        fields = '__all__'

class user_info_serializer(serializers.ModelSerializer):

    class Meta:

        model = user_info

        fields = "__all__"

    # def create(self, validated_data):

        # user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        # return user