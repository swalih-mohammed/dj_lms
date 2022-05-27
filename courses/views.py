from django.shortcuts import render

from rest_framework import generics
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)

from users.models import User
from .models import Course, EnrolledCourse, Unit, UnitCompleted
from .serializers import CourseSerializer, CourseDetailSerializer, EnrolledCourseSerializer, UnitSerializer, UnitDetailSerializer


class CourseListView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CourseSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        qs = Course.objects.filter(is_active=True, category=category)
        return qs


class EnrolledCourseListView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = EnrolledCourseSerializer

    def get_queryset(self):
        print("course enrolled list")
        username = self.kwargs['username']
        category = self.kwargs['category']
        user = User.objects.get(username=username)
        courses = EnrolledCourse.objects.filter(
            student=user, is_enrolled=True, course__category=category, course__is_active=True)
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
        username = self.kwargs['username']
        category = self.kwargs['category']
        order = self.kwargs['order']
        user = User.objects.get(username=username)
        if str(order) == str(0):
            courses = Course.objects.filter(
                category=category).order_by('order')
            level = 1
            for course in courses:
                total_units_in_course = course.Units.all()
                total_completed_units = UnitCompleted.objects.filter(
                    student=user.id, is_completed=True, unit__course=course.id)
                if len(total_units_in_course) == len(total_completed_units):
                    level = level + 1
                else:
                    break
            qs = Course.objects.filter(
                category=category, order=level)
        else:
            qs = Course.objects.filter(
                category=category, order=order)
        return qs


class UnitDetailView(generics.ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = UnitDetailSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        unitId = self.kwargs['unitId']
        qs = Unit.objects.filter(pk=unitId)
        return qs
