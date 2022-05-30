from allauth.account.adapter import get_adapter
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings
from django.utils.translation import gettext as _
from dj_rest_auth.registration.serializers import RegisterSerializer

from courses.models import CourseCategory
from .models import User, Student, Teacher


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'is_student', 'is_teacher')


class CustomRegisterSerializer(RegisterSerializer):
    is_student = serializers.BooleanField()
    is_teacher = serializers.BooleanField()

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'is_student', 'is_teacher')

    def get_cleaned_data(self):
        # print(self.validated_data)
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'is_student': self.validated_data.get('is_student', ''),
            'is_teacher': self.validated_data.get('is_teacher', '')
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.is_student = self.cleaned_data.get('is_student')
        user.is_teacher = self.cleaned_data.get('is_teacher')
        user.save()
        adapter.save_user(request, user, self)
        return user


class TokenSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()

    class Meta:
        model = Token
        fields = ('key', 'user', 'email', 'name')

    def get_email(self, obj):
        serializer_data = UserSerializer(
            obj.user
        ).data
        email = serializer_data.get('email')
        return email

    def get_name(self, obj):
        serializer_data = UserSerializer(
            obj.user
        ).data
        name = serializer_data.get('username')
        return name


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password_reset_form_class = PasswordResetForm

    def validate_email(self, value):
        self.reset_form = self.password_reset_form_class(
            data=self.initial_data)
        if not self.reset_form.is_valid():
            raise serializers.ValidationError(_('Error'))

        ###### FILTER YOUR USER MODEL ######
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError(_('Invalid e-mail address'))
        return value

    def save(self):
        request = self.context.get('request')
        opts = {
            'use_https': request.is_secure(),
            'from_email': getattr(settings, 'DEFAULT_FROM_EMAIL'),
            ###### USE YOUR HTML FILE ######
            'html_email_template_name': 'example_message.html',
            'request': request,
        }
        self.reset_form.save(**opts)


class StudentDetailSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        source="user.username", read_only=True)

    class Meta:
        model = Student
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(
        source="user.username", read_only=True)
    current_course = serializers.CharField(
        source="current_course.title", read_only=True)
    current_course_language = serializers.CharField(
        source="current_course.language", read_only=True)
    current_course_id = serializers.CharField(
        source="current_course.id", read_only=True)
    current_course_level = serializers.CharField(
        source="level", read_only=True)

    class Meta:
        model = Student
        fields = ['student_name', 'id', 'user', 'current_course',
                  'current_course_id', 'current_course_language', 'current_course_level']


class UpdateStudentDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'
