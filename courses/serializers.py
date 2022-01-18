from rest_framework import serializers
from .models import Course, Section, Unit, UnitCompleted
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
    total_units = serializers.SerializerMethodField()
    completed_units = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_units(self, obj):
        request = self.context['request']
        username = request.parser_context['kwargs']['username']
        units = UnitSerializer(
            obj.Units.all(), many=True, context={'username': username}).data
        return units

    def get_completed_units(self, obj):
        try:
            request = self.context['request']
            username = request.parser_context['kwargs']['username']
            user = User.objects.get(username=username)
            print(obj.title)

            # units_in_course = obj.Units.all()
            completed_units = UnitCompleted.objects.filter(
                student=user.id, is_completed=True, unit__course=obj.id).distinct()
            # if len(completed_units) == 0 or len(units_in_course) == 0:
            #     return 0
            # print("total units", len(completed_units))
            # completed = completed_units
            return len(completed_units)

        except:
            print("error in finding progress")
            return 0

    def get_total_units(self, obj):
        units_in_course = obj.Units.all()
        return len(units_in_course)


class UnitSerializer(serializers.ModelSerializer):
    progress = serializers.SerializerMethodField()

    class Meta:
        model = Unit
        fields = '__all__'

    def get_progress(self, obj):
        try:
            username = self.context['username']
            user = User.objects.get(username=username)
            # print(obj.title)
            lessons_in_unit = obj.Lessons.all()
            completed_lessons = LessonCompleted.objects.filter(
                student=user.id, is_completed=True, lesson__unit=obj.id).distinct()
            quizzes_in_unit = obj.unitQuizzes.all()
            completed_quizzes = QuizCompleted.objects.filter(
                student=user.id, is_completed=True, quiz__unit=obj.id).distinct()

            total_itmes = len(lessons_in_unit)+len(quizzes_in_unit)
            total_completed_items = len(
                completed_lessons)+len(completed_quizzes)

            if total_itmes == 0 or total_completed_items == 0:
                return 0
            progress = total_completed_items/total_itmes
            return progress

        except:
            print("error in finding progress")
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
