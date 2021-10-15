from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import RetrieveAPIView


from .models import Quiz
from .serializers import QuizDetailSerializer

# Create your views here.


class QizDetailView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = QuizDetailSerializer
    queryset = Quiz.objects.all()
