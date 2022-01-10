from rest_framework import serializers
from .models import Course, Section, Unit
from lessons.serializers import LessonSerializer
from quizzes.serializers import QuizSerializer
# from .serializers import UnitSerializer, UnitDetailSerializer, SectionSerializer


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'


class UnitDetailSerializer(serializers.ModelSerializer):
    # lessons = serializers.SerializerMethodField()

    class Meta:
        model = Unit
        fields = '__all__'

    # def get_lessons(self, obj):
    #     request = self.context['request']
    #     username = request.parser_context['kwargs']['username']
    #     lessons = LessonSerializer(
    #         obj.unitLessons.all(), many=True, context={'username': username}).data
    #     return lessons


class SectionSerializer(serializers.ModelSerializer):
    # units = serializers.SerializerMethodField()

    class Meta:
        model = Section
        fields = '__all__'

    # def get_units(self, obj):
    #     units = UnitSerializer(obj.units.all(), many=True).data
    #     return units


class SectionDetailSerializer(serializers.ModelSerializer):
    units = serializers.SerializerMethodField()
    lessons = serializers.SerializerMethodField()

    class Meta:
        model = Section
        fields = '__all__'

    def get_units(self, obj):
        units = UnitSerializer(obj.Units.all(), many=True).data
        return units

    def get_lessons(self, obj):
        lessons = LessonSerializer(obj.Sections.all(), many=True).data
        return lessons


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    units = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_units(self, obj):
        units = UnitSerializer(obj.Units.all(), many=True).data
        return units


class UnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Unit
        fields = '__all__'


class UnitDetailSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()
    quizzes = serializers.SerializerMethodField()

    class Meta:
        model = Unit
        fields = '__all__'

    def get_lessons(self, obj):
        request = self.context['request']
        username = request.parser_context['kwargs']['username']
        lessons = LessonSerializer(
            obj.Lessons.all(), many=True, context={'username': username}).data
        return lessons

    def get_quizzes(self, obj):
        quizzes = UnitSerializer(obj.QuizSerializer.all(), many=True).data
        return quizzes
