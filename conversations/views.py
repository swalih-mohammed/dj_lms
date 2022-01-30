from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import RetrieveAPIView, CreateAPIView


from .models import Conversation
from .serializers import ConversationDetailSerializer

from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)
# Create your views here.


class ConversationDetailView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ConversationDetailSerializer
    queryset = Conversation.objects.all()


# class ConversationCompletedCreateView(CreateAPIView):
#     permission_classes = (AllowAny,)
#     serializer_class = ConversationCompletedSerializer
#     queryset = ConversationCompleted.objects.all()

    # def post(self, request):
    #     serializer = ConversationCompletedSerializer(data=request.data)
    #     serializer.is_valid()
    #     ConversationCompleted = serializer.create(request)
    #     if ConversationCompleted:
    #         return Response(status=HTTP_201_CREATED)
    #     return Response(status=HTTP_400_BAD_REQUEST)
