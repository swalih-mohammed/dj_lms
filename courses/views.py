from django.shortcuts import render

from rest_framework import generics
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Course, Section, Unit
from .serializers import CourseSerializer, CourseDetailSerializer, SectionSerializer, SectionDetailSerializer, UnitSerializer, UnitDetailSerializer


class CourseListView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CourseSerializer

    def get_queryset(self):
        qs = Course.objects.all()
        return qs


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
