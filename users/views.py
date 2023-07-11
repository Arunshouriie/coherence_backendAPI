import http
from django.contrib.auth import login

from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework import status, viewsets

from rest_framework import generics, permissions
from rest_framework.response import Response
# from .models import AuthToken
from .serializers import UserSerializer,provisionserializer,user_info_serializer, RegisterSerializer, ChangePasswordSerializer, medicine_schedule_serializer, dispense_serializer, schedule_audit_serializer, alarm_audit_serializer, medicine_dispense_serializer, Capture_event_serializer
from django.views.decorators.debug import sensitive_post_parameters
from rest_framework.views import APIView
from rest_framework import generics, permissions
from .models import  reminder_schedule_groups,user_info, dispense, reminder_schedule_audit, alarm_audit, provisioning, medicine_dispense_information, Capture_event

# Change Password
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated   

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        # "token": AuthToken.objects.create(user)[1]
        })

# Login API
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

# Get User API
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny,]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class UserinfoView(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = user_info.objects.all()
    serializer_class = user_info_serializer

class medicinescheduleView(viewsets.ModelViewSet):
    """
    """
    serializer_class = medicine_schedule_serializer
    permission_classes = [permissions.AllowAny]
    queryset = reminder_schedule_groups.objects.all()


class DispenseView(viewsets.ModelViewSet):
    """
    """
    serializer_class = dispense_serializer
    permission_classes = [permissions.AllowAny]
    queryset = dispense.objects.all()

class ScheduleAuditView(viewsets.ModelViewSet):
    """
    """
    serializer_class = schedule_audit_serializer
    permission_classes = [permissions.AllowAny]
    queryset = reminder_schedule_audit.objects.all()

class AlarmAuditView(viewsets.ModelViewSet):
    """
    """
    serializer_class = alarm_audit_serializer
    permission_classes = [permissions.AllowAny]
    queryset = alarm_audit.objects.all()

class provisionView(viewsets.ModelViewSet):
    """
    """
    serializer_class = provisionserializer
    permission_classes = [permissions.AllowAny]
    queryset = provisioning.objects.all()

class MedicinedispenseView(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = medicine_dispense_information.objects.all()
    serializer_class = medicine_dispense_serializer

class CaptureEventView(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Capture_event.objects.all()
    serializer_class = Capture_event_serializer


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)