from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)

from rest_framework.response import Response
from .models import Bug
from .serializers import BugSerializer


class ReportBugView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = BugSerializer
    queryset = Bug.objects.all()

    def post(self, request):
        print(request.data)
        serializer = BugSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
