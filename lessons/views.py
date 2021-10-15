from django.shortcuts import render

from rest_framework import generics
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)


from .models import Lesson, LessonCompleted
from .serializers import LessonDetailSerializer, LessonCompletedSerializer


class LessonListView(APIView):
    permission_classes = (AllowAny, )
    serializer_class = LessonDetailSerializer

    # def get(self, request, *args, **kwargs):
    #     print(equest)


class LessonDetailView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LessonDetailSerializer
    queryset = Lesson.objects.all()


# class LessonTestView(generics.ListAPIView):
#     permission_classes = (AllowAny, )
#     serializer_class = LessonQuestionSerializer

#     def get_queryset(self):
#         lesson_id = self.kwargs['pk']
#         return LessonQuestion.objects.filter(lesson=lesson_id)


class LessonCompletedCreateView(CreateAPIView):
    serializer_class = LessonCompletedSerializer
    queryset = LessonCompleted.objects.all()

    def post(self, request):
        # print(request.data)

        serializer = LessonCompletedSerializer(data=request.data)
        serializer.is_valid()
        lessonCompleted = serializer.create(request)
        if lessonCompleted:
            return Response(status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)
