from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import RetrieveAPIView, CreateAPIView


from .models import Quiz, QuizCompleted
from .serializers import QuizDetailSerializer, QuizCompletedSerializer

from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)
# Create your views here.


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
