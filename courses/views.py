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
from .models import Course, EnrolledCourse, Section, Unit
from .serializers import CourseSerializer, CourseDetailSerializer, EnrolledCourseSerializer, SectionSerializer, SectionDetailSerializer, UnitSerializer, UnitDetailSerializer


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
        username = self.kwargs['username']
        category = self.kwargs['category']
        user = User.objects.get(username=username)
        courses = EnrolledCourse.objects.filter(
            student=user, is_enrolled=True, course__category=category)
        return courses


class CourseEnrollView(CreateAPIView):
    # print("course enrolll view")
    permission_classes = (AllowAny,)
    serializer_class = EnrolledCourseSerializer
    queryset = EnrolledCourse.objects.all()

    def post(self, request):
        serializer = EnrolledCourseSerializer(data=request.data)
        serializer.is_valid()
        serializer.create(request)
        return Response(status=HTTP_201_CREATED)
        # courseEnrolled = serializer.create(request)
        # if courseEnrolled:
        #     return Response(status=HTTP_201_CREATED)
        # return Response(status=HTTP_400_BAD_REQUEST)


class CourseDetailView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.all()


class SectionListView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SectionSerializer

    def get_queryset(self):
        id = self.kwargs['pk']
        return Lesson.objects.filter(section=id)


class SectionDetailView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SectionDetailSerializer
    queryset = Section.objects.all()


class UnitListView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UnitSerializer

    def get_queryset(self):
        id = self.kwargs['pk']
        return Lesson.objects.filter(section=id)


class UnitDetailView(generics.ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = UnitDetailSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        unitId = self.kwargs['unitId']
        qs = Unit.objects.filter(pk=unitId)
        return qs
