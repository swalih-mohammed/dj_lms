from django.shortcuts import render

from rest_framework import generics
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated


from .models import Section
from .serializers import SectionSerializer


class SectionListView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SectionSerializer
    # serializer_class = RoadSerializer

    def get_queryset(self):
        id = self.kwargs['pk']
        return Section.objects.filter(course=id)

    # def get_queryset(self):
    #     qs = Section.objects.all()
    #     return qs


class SectionDetailView(RetrieveAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
