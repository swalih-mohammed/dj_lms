from rest_framework import viewsets
from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status


from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)

from courses.models import CourseCategory
from .models import User, Student, Teacher
from .serializers import UserSerializer, StudentSerializer, StudentDetailSerializer, UpdateStudentDetailsSerializer

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


# class StudentDetailView(RetrieveAPIView):
#     permission_classes = (AllowAny,)
#     serializer_class = StudentDetailSerializer
#     queryset = Student.objects.all()


# class UpdateStudentDetails(CreateAPIView):
#     permission_classes = (AllowAny,)
#     serializer_class = UpdateStudentDetailsSerializer
#     queryset = Student.objects.all()

#     def post(self, request):
#         serializer = UpdateStudentDetailsSerializer(data=request.data)
#         serializer.is_valid()
#         serializer.create(request)
#         return Response(status=HTTP_201_CREATED)

class StudentDetailView(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = (AllowAny,)

    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    # def put(self, request, pk, format=None):
    #     student = self.get_object(pk)
    #     serializer = StudentSerializer(student, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class StudentCurrentCourseChangeView(CreateAPIView):
#     permission_classes = (AllowAny,)
#     serializer_class = UpdateStudentDetailsSerializer
#     queryset = Student.objects.all()

#     def post(self, request):
#         serializer = Student(data=request.data)
#         serializer.is_valid()
#         serializer.create(request)
#         return Response(status=HTTP_201_CREATED)

class StudentCurrentCourseChangeView(GenericAPIView, UpdateModelMixin):
    '''
    You just need to provide the field which is to be modified.
    '''
    queryset = Student.objects.all()
    serializer_class = UpdateStudentDetailsSerializer
    permission_classes = (AllowAny,)

    def put(self, request, *args, **kwargs):
        print("putting in curren tchange")
        return self.partial_update(request, *args, **kwargs)
