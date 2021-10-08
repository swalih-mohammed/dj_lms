from django.shortcuts import render

from rest_framework import generics
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Course
from .serializers import CourseSerializer, CourseDetailSerializer


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
