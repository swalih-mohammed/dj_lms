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
        # try:
        username = self.context['username']
        user = User.objects.get(username=username)
        print(obj.title)
        lessons_in_unit = obj.Lessons.all()
        # print("lessons in unit:", len(lessons_in_unit))
        completed_lessons = LessonCompleted.objects.filter(
            student=user.id, is_completed=True, lesson__unit=obj.id).distinct()
        # print("completed lessons:", len(completed_lessons))

        # finding quiz
        quizzes_in_unit = obj.unitQuizzes.all()
        # print("quizz in unit:", len(quizzes_in_unit))
        completed_quizzes = QuizCompleted.objects.filter(
            student=user.id, is_completed=True, quiz__unit=obj.id).distinct()
        # print("completed quizz:", len(completed_quizzes))
        #  calculating total items
        total_itmes = len(lessons_in_unit)+len(quizzes_in_unit)
        total_completed_items = len(completed_lessons)+len(completed_quizzes)

        if total_itmes == 0 or total_completed_items == 0:
            return 0
        progress = total_completed_items/total_itmes
        return progress
        # lessons = LessonCompletedSerializer(
        #     obj.Lessons.filter(student=user.id, is_completed=True), many=True).data

        # print(obj.title)
        # print(len(lessons))
        # lessons = Lesson.objects.filter(unit=obj.id)
        #     completed_lessons = LessonCompleted.objects.filter(unit=obj.id,
        #                                                        student=user.id, is_completed=True)

        # #     quizzes = Quiz.objects.filter(unit=obj.id)
        # #     completed_quizzes = QuizCompleted.objects.filter(unit=obj.id,
        # #                                                      student=user.id, is_completed=True)

        # #     total_items = len(lessons) + len(quizzes)
        # #     total_completed_items = len(
        # #         completed_lessons) + len(completed_quizzes)

        # #     if(total_items == total_completed_items):
        # #         print("same")
        # #         return 0
        # #     else:
        # #         print("not same", total_completed_items, total_items)
        # #         progress = total_completed_items/total_items
        # #         if progress > 1:
        # #             print("progress more than one")
        # #             return 0
        # #         return progress
        # except:
        #     print("error")
        #     return 0


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
