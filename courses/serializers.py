from rest_framework import serializers
from .models import Course, Section, Unit
from lessons.models import Lesson, LessonCompleted
from quizzes.models import Quiz, QuizCompleted
from users.models import User


from lessons.serializers import LessonSerializer, LessonCompletedSerializer
from quizzes.serializers import QuizSerializer, QuizCompletedSerializer
# from .serializers import UnitSerializer, UnitDetailSerializer, SectionSerializer


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'


class UnitDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Unit
        fields = '__all__'


class SectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Section
        fields = '__all__'


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

    # def get_units(self, obj):
    #     units = UnitSerializer(obj.Units.all(), many=True).data
    #     return units

    def get_units(self, obj):
        request = self.context['request']
        username = request.parser_context['kwargs']['username']
        units = UnitSerializer(
            obj.Units.all(), many=True, context={'username': username}).data
        return units


class UnitSerializer(serializers.ModelSerializer):
    progress = serializers.SerializerMethodField()

    class Meta:
        model = Unit
        fields = '__all__'

    def get_progress(self, obj):
        try:
            username = self.context['username']
            user = User.objects.get(username=username)

            lessons = Lesson.objects.filter(unit=obj.id)
            completed_lessons = LessonCompleted.objects.filter(
                student=user.id, is_completed=True)

            quizzes = Quiz.objects.filter(unit=obj.id)
            completed_quizzes = QuizCompleted.objects.filter(
                student=user.id, is_completed=True)

            total_items = len(lessons) + len(quizzes)
            total_completed_items = len(
                completed_lessons) + len(completed_quizzes)

            if(total_items == total_completed_items):
                # print("same")
                return 0
            else:
                # print("not same")
                progress = total_completed_items/total_items
                if progress > 1:
                    return 0
                return progress
        except:
            return 0


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
        request = self.context['request']
        username = request.parser_context['kwargs']['username']
        quizzes = QuizSerializer(obj.unitQuizzes.all(), many=True, context={
                                 'username': username}).data
        return quizzes
