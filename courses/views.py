from django.shortcuts import render

from rest_framework import generics
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status

from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)
from users.models import Student

from users.models import User
from .models import Course, CourseCategory, EnrolledCourse, Unit, UnitCompleted
from .serializers import CourseSerializer, CourseCategorySerializer, CourseDetailSerializer, EnrolledCourseSerializer, UnitSerializer, UnitDetailSerializer


class CourseCategoryView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CourseCategorySerializer

    def get_queryset(self):
        qs = CourseCategory.objects.all()
        return qs


class CourseListView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CourseSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        student = Student.objects.get(user=user_id)
        qs = Course.objects.filter(
            category=student.current_course)
        return qs


class EnrolledCourseListView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = EnrolledCourseSerializer

    def get_queryset(self):
        print("course enrolled list")
        username = self.kwargs['username']
        category = self.kwargs['category']
        user = User.objects.get(username=username)
        student = Student.objects.get(user=user)
        category = CourseCategory.objects.filter(order=category).first()
        courses = EnrolledCourse.objects.filter(
            student=student, is_enrolled=True, course__category=category,  course__is_active=True)
        return courses


class CourseEnrollView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = EnrolledCourseSerializer
    queryset = EnrolledCourse.objects.all()

    def post(self, request):
        serializer = EnrolledCourseSerializer(data=request.data)
        serializer.is_valid()
        serializer.create(request)
        return Response(status=HTTP_201_CREATED)


# class CourseDetailView(RetrieveAPIView):
#     permission_classes = (AllowAny,)
#     serializer_class = CourseDetailSerializer
#     queryset = Course.objects.all()


class CurrentCourseDetailView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CourseDetailSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        student = Student.objects.get(user=user_id)
        qs = Course.objects.filter(
            is_active=True, category=student.current_course, order=student.level)
        return qs


class UnitDetailView(generics.ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = UnitDetailSerializer

    def get_queryset(self):
        # user_id = self.kwargs['user_id']
        unit_id = self.kwargs['unit_id']
        qs = Unit.objects.filter(pk=unit_id)
        return qs
