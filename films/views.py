from django.shortcuts import render

from rest_framework import generics
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated


from .models import Film
from .serializers import FilmSerializer


class UnitFilmListView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = FilmSerializer

    def get_queryset(self):
        id = self.kwargs['unitID']
        return Film.objects.filter(unit=id)


class unitFilmDetailView(RetrieveAPIView):
    serializer_class = FilmSerializer
    queryset = Film.objects.all()
