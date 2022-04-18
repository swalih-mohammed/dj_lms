from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from .models import Quiz, QuizCompleted
from .serializers import GeneralQuizListSerializer, QuizDetailSerializer, QuizCompletedSerializer, GeneralQuizListSerializer
from users.models import User

from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)


class GeneralQuizListView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = GeneralQuizListSerializer

    def get_queryset(self):
        # username = self.kwargs['username']
        category = self.kwargs['category']
        # user = User.objects.get(username=username)
        quizzes = Quiz.objects.filter(
            category=category)
        return quizzes


class QizDetailView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = QuizDetailSerializer
    queryset = Quiz.objects.all()


class QuizCompletedCreateView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = QuizCompletedSerializer
    queryset = QuizCompleted.objects.all()

    def post(self, request):
        serializer = QuizCompletedSerializer(data=request.data)
        serializer.is_valid()
        QuizCompleted = serializer.create(request)
        if QuizCompleted:
            return Response(status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)
