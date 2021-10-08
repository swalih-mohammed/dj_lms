from django.shortcuts import render

from rest_framework import generics
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)

from .models import UnitTest, GradedUnitTest
from .serializers import UnitTestSerializer, GradedUnitTestSerializer


class UnitTestListView(generics.ListAPIView):
    serializer_class = UnitTestSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        id = self.kwargs['unitID']
        return UnitTest.objects.filter(unit=id)


class unitTestDetailView(RetrieveAPIView):
    serializer_class = UnitTestSerializer
    queryset = UnitTest.objects.all()


class GradedUnitTestCreateView(CreateAPIView):
    serializer_class = GradedUnitTestSerializer
    queryset = GradedUnitTest.objects.all()

    def post(self, request):
        print(request.data)
        serializer = GradedUnitTestSerializer(data=request.data)
        serializer.is_valid()
        graded_assignment = serializer.create(request)
        if graded_assignment:
            return Response(status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)
