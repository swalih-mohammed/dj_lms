from rest_framework import serializers

from .models import Unit
from users.models import User
from lessons.serializers import LessonSerializer
from unitTests.serializers import UnitTestSerializer


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'


class UnitDetailSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()

    class Meta:
        model = Unit
        fields = '__all__'

    def get_lessons(self, obj):
        request = self.context['request']
        username = request.parser_context['kwargs']['username']
        lessons = LessonSerializer(
            obj.unitLessons.all(), many=True, context={'username': username}).data
        return lessons
